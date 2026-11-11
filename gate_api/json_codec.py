# coding: utf-8
"""Exact opt-in JSON numbers at the generated SDK's single JSON boundary.

Ordinary payloads retain the standard library encoder and decoder. Decimal
payloads never pass through a binary float, and the same encoder is used by
request signing and the REST transport. This module has no SDK/model imports.
"""
from __future__ import absolute_import

from decimal import Decimal
import json

import simplejson
import six


def decimal_value(value):
    """Accept finite exact values; reject floats rather than blessing lost digits."""
    if isinstance(value, bool) or not isinstance(value, (Decimal,) + six.integer_types):
        raise ValueError("Exact JSON number requires a finite Decimal or integer")
    value = value if isinstance(value, Decimal) else Decimal(value)
    if not value.is_finite():
        raise ValueError("Exact JSON number must be finite")
    return value


def container_item_type(type_name):
    """Unwrap only the pinned generator's existing list/map type notation."""
    if not isinstance(type_name, six.string_types):
        return None
    if type_name.startswith('list[') and type_name.endswith(']'):
        return type_name[5:-1]
    if type_name.startswith('dict(') and type_name.endswith(')') and ',' in type_name:
        return type_name.split(',', 1)[1][:-1].strip()
    return None


def coerce_decimal(value, type_name):
    """Validate exact leaves when users construct DTOs, including containers."""
    if value is None:
        return None
    if type_name == 'Decimal':
        return decimal_value(value)
    inner = container_item_type(type_name)
    if inner is None:
        raise ValueError("Unsupported exact JSON number type")
    if type_name.startswith('list['):
        if not isinstance(value, (list, tuple)):
            raise ValueError("Exact JSON number array requires a list")
        return [coerce_decimal(item, inner) for item in value]
    if not isinstance(value, dict):
        raise ValueError("Exact JSON number map requires an object")
    return {key: coerce_decimal(item, inner) for key, item in six.iteritems(value)}


def uses_decimal(response_type, models):
    """Follow finite generated type metadata without a shared mutable cache.

    A per-call visited set handles model cycles correctly. Caching an unfinished
    recursive false could miss a Decimal reachable through another cycle edge.
    """
    pending, visited = [response_type], set()
    while pending:
        candidate = pending.pop()
        if candidate is Decimal or candidate == 'Decimal':
            return True
        inner = container_item_type(candidate)
        if inner is not None:
            pending.append(inner)
            continue
        if isinstance(candidate, six.string_types):
            candidate = getattr(models, candidate, None)
        if candidate is None or id(candidate) in visited:
            continue
        visited.add(id(candidate))
        fields = getattr(candidate, 'openapi_types', None)
        if isinstance(fields, dict):
            pending.extend(fields.values())
    return False


def _invalid_constant(_value):
    # NaN/Infinity are Python extensions, not valid exact JSON monetary values.
    raise ValueError("Non-finite JSON number")


def loads(payload, exact=False):
    """Select precision before parsing, retaining normal float behavior otherwise."""
    if exact:
        return json.loads(payload, parse_float=Decimal, parse_constant=_invalid_constant)
    return json.loads(payload)


def _contains_decimal(value):
    """Walk request-owned containers iteratively and terminate on circular input."""
    pending, seen, found = [value], set(), False
    while pending:
        item = pending.pop()
        if isinstance(item, Decimal):
            decimal_value(item)
            found = True
        elif isinstance(item, (dict, list, tuple)) and id(item) not in seen:
            seen.add(id(item))
            if isinstance(item, dict):
                # Standard json rejects Decimal keys; never let an alternative
                # encoder coerce them or create a different signing payload.
                if any(isinstance(key, Decimal) for key in item):
                    raise TypeError("Decimal JSON object keys are not supported")
                pending.extend(item.values())
            else:
                pending.extend(item)
    return found


def dumps(value):
    """Encode Decimal as an unquoted JSON number using the pinned exact codec."""
    if _contains_decimal(value):
        # Ordinary floats in a mixed payload retain stdlib's legacy options.
        # All Decimal leaves were checked finite above, independent of allow_nan.
        return simplejson.dumps(value, use_decimal=True, allow_nan=True)
    return json.dumps(value)


def legacy_numbers(value):
    """Restore ordinary unknown-object number types after exact response parsing.

    Only declared Decimal leaves retain their precise representation. Iterative
    copying avoids adding a recursive depth limit to legacy object payloads.
    """
    if not _contains_decimal(value):
        return value
    root, copies, pending = [None], {}, [(value, None, 0)]
    while pending:
        item, owner, key = pending.pop()
        target = root if owner is None else owner
        if isinstance(item, Decimal):
            target[key] = float(item)
        elif isinstance(item, (dict, list)):
            identity = id(item)
            if identity in copies:
                target[key] = copies[identity]
                continue
            clone = {} if isinstance(item, dict) else [None] * len(item)
            copies[identity] = clone
            target[key] = clone
            iterator = six.iteritems(item) if isinstance(item, dict) else enumerate(item)
            pending.extend((child, clone, child_key) for child_key, child in iterator)
        else:
            target[key] = item
    return root[0]
