# gate_api.P2PApi

All URIs are relative to *https://api.gateio.ws/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**p2p_merchant_account_get_user_info**](P2PApi.md#p2p_merchant_account_get_user_info) | **POST** /p2p/merchant/account/get_user_info | Get account information
[**p2p_merchant_account_get_counterparty_user_info**](P2PApi.md#p2p_merchant_account_get_counterparty_user_info) | **POST** /p2p/merchant/account/get_counterparty_user_info | Get counterparty information
[**p2p_merchant_account_get_myself_payment**](P2PApi.md#p2p_merchant_account_get_myself_payment) | **POST** /p2p/merchant/account/get_myself_payment | Get payment method list
[**p2p_merchant_transaction_get_pending_transaction_list**](P2PApi.md#p2p_merchant_transaction_get_pending_transaction_list) | **POST** /p2p/merchant/transaction/get_pending_transaction_list | Get pending orders
[**p2p_merchant_transaction_get_completed_transaction_list**](P2PApi.md#p2p_merchant_transaction_get_completed_transaction_list) | **POST** /p2p/merchant/transaction/get_completed_transaction_list | Get all/historical orders
[**p2p_merchant_transaction_get_transaction_details**](P2PApi.md#p2p_merchant_transaction_get_transaction_details) | **POST** /p2p/merchant/transaction/get_transaction_details | Query order details
[**p2p_merchant_transaction_confirm_payment**](P2PApi.md#p2p_merchant_transaction_confirm_payment) | **POST** /p2p/merchant/transaction/confirm-payment | Confirm payment
[**p2p_merchant_transaction_confirm_receipt**](P2PApi.md#p2p_merchant_transaction_confirm_receipt) | **POST** /p2p/merchant/transaction/confirm-receipt | Confirm receipt
[**p2p_merchant_transaction_cancel**](P2PApi.md#p2p_merchant_transaction_cancel) | **POST** /p2p/merchant/transaction/cancel | Cancel order
[**p2p_merchant_books_place_biz_push_order**](P2PApi.md#p2p_merchant_books_place_biz_push_order) | **POST** /p2p/merchant/books/place_biz_push_order | Publish ad order
[**p2p_merchant_books_ads_update_status**](P2PApi.md#p2p_merchant_books_ads_update_status) | **POST** /p2p/merchant/books/ads_update_status | Update ad status
[**p2p_merchant_books_ads_detail**](P2PApi.md#p2p_merchant_books_ads_detail) | **POST** /p2p/merchant/books/ads_detail | Query ad details
[**p2p_merchant_books_my_ads_list**](P2PApi.md#p2p_merchant_books_my_ads_list) | **POST** /p2p/merchant/books/my_ads_list | Get my ad list
[**p2p_merchant_chat_get_chats_list**](P2PApi.md#p2p_merchant_chat_get_chats_list) | **POST** /p2p/merchant/chat/get_chats_list | Get chat history
[**p2p_merchant_chat_send_chat_message**](P2PApi.md#p2p_merchant_chat_send_chat_message) | **POST** /p2p/merchant/chat/send_chat_message | Send text message
[**p2p_merchant_chat_upload_chat_file**](P2PApi.md#p2p_merchant_chat_upload_chat_file) | **POST** /p2p/merchant/chat/upload_chat_file | Upload chat file


# **p2p_merchant_account_get_user_info**
> InlineResponse20014 p2p_merchant_account_get_user_info()

Get account information

### Example

```python
from __future__ import print_function
import gate_api
from gate_api.exceptions import ApiException, GateApiException
# Defining the host is optional and defaults to https://api.gateio.ws/api/v4
# See configuration.py for a list of all supported configuration parameters.
configuration = gate_api.Configuration(
    host = "https://api.gateio.ws/api/v4"
)

api_client = gate_api.ApiClient(configuration)
# Create an instance of the API class
api_instance = gate_api.P2PApi(api_client)

try:
    # Get account information
    api_response = api_instance.p2p_merchant_account_get_user_info()
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling P2PApi->p2p_merchant_account_get_user_info: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project-Id-Version: GateApiTools 1.0.0 Report-Msgid-Bugs-To: EMAIL@ADDRESS POT-Creation-Date: 2025-11-12 18:14+0800 PO-Revision-Date: 2019-01-02 17:30+0800 Last-Translator: FULL NAME &lt;EMAIL@ADDRESS&gt; Language: en Language-Team: en &lt;L@li.org&gt; Plural-Forms: nplurals&#x3D;2; plural&#x3D;(n !&#x3D;1) MIME-Version: 1.0 Content-Type: text/plain; charset&#x3D;utf-8 Content-Transfer-Encoding: 8bit Generated-By: Babel 2.8.0  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p2p_merchant_account_get_counterparty_user_info**
> InlineResponse20015 p2p_merchant_account_get_counterparty_user_info(biz_uid)

Get counterparty information

### Example

```python
from __future__ import print_function
import gate_api
from gate_api.exceptions import ApiException, GateApiException
# Defining the host is optional and defaults to https://api.gateio.ws/api/v4
# See configuration.py for a list of all supported configuration parameters.
configuration = gate_api.Configuration(
    host = "https://api.gateio.ws/api/v4"
)

api_client = gate_api.ApiClient(configuration)
# Create an instance of the API class
api_instance = gate_api.P2PApi(api_client)
biz_uid = 'biz_uid_example' # str | Counterparty UID (encrypted)

try:
    # Get counterparty information
    api_response = api_instance.p2p_merchant_account_get_counterparty_user_info(biz_uid)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling P2PApi->p2p_merchant_account_get_counterparty_user_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **biz_uid** | **str**| Counterparty UID (encrypted) | 

### Return type

[**InlineResponse20015**](InlineResponse20015.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project-Id-Version: GateApiTools 1.0.0 Report-Msgid-Bugs-To: EMAIL@ADDRESS POT-Creation-Date: 2025-11-12 18:14+0800 PO-Revision-Date: 2019-01-02 17:30+0800 Last-Translator: FULL NAME &lt;EMAIL@ADDRESS&gt; Language: en Language-Team: en &lt;L@li.org&gt; Plural-Forms: nplurals&#x3D;2; plural&#x3D;(n !&#x3D;1) MIME-Version: 1.0 Content-Type: text/plain; charset&#x3D;utf-8 Content-Transfer-Encoding: 8bit Generated-By: Babel 2.8.0  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p2p_merchant_account_get_myself_payment**
> InlineResponse20016 p2p_merchant_account_get_myself_payment(fiat=fiat)

Get payment method list

### Example

```python
from __future__ import print_function
import gate_api
from gate_api.exceptions import ApiException, GateApiException
# Defining the host is optional and defaults to https://api.gateio.ws/api/v4
# See configuration.py for a list of all supported configuration parameters.
configuration = gate_api.Configuration(
    host = "https://api.gateio.ws/api/v4"
)

api_client = gate_api.ApiClient(configuration)
# Create an instance of the API class
api_instance = gate_api.P2PApi(api_client)
fiat = 'fiat_example' # str | Fiat currency (optional)

try:
    # Get payment method list
    api_response = api_instance.p2p_merchant_account_get_myself_payment(fiat=fiat)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling P2PApi->p2p_merchant_account_get_myself_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fiat** | **str**| Fiat currency | [optional] 

### Return type

[**InlineResponse20016**](InlineResponse20016.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project-Id-Version: GateApiTools 1.0.0 Report-Msgid-Bugs-To: EMAIL@ADDRESS POT-Creation-Date: 2025-11-12 18:14+0800 PO-Revision-Date: 2019-01-02 17:30+0800 Last-Translator: FULL NAME &lt;EMAIL@ADDRESS&gt; Language: en Language-Team: en &lt;L@li.org&gt; Plural-Forms: nplurals&#x3D;2; plural&#x3D;(n !&#x3D;1) MIME-Version: 1.0 Content-Type: text/plain; charset&#x3D;utf-8 Content-Transfer-Encoding: 8bit Generated-By: Babel 2.8.0  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p2p_merchant_transaction_get_pending_transaction_list**
> InlineResponse20017 p2p_merchant_transaction_get_pending_transaction_list(crypto_currency, fiat_currency, order_tab=order_tab, select_type=select_type, status=status, txid=txid, start_time=start_time, end_time=end_time)

Get pending orders

### Example

```python
from __future__ import print_function
import gate_api
from gate_api.exceptions import ApiException, GateApiException
# Defining the host is optional and defaults to https://api.gateio.ws/api/v4
# See configuration.py for a list of all supported configuration parameters.
configuration = gate_api.Configuration(
    host = "https://api.gateio.ws/api/v4"
)

api_client = gate_api.ApiClient(configuration)
# Create an instance of the API class
api_instance = gate_api.P2PApi(api_client)
crypto_currency = 'crypto_currency_example' # str | Cryptocurrency
fiat_currency = 'fiat_currency_example' # str | Fiat currency
order_tab = 'order_tab_example' # str | 订单标签页，默认pending（pending：处理中（pending:  AND status in ('OPEN', 'PAID', 'LOCKED', 'TEMP')）；dispute：申诉中（status in ('ACCEPT', 'BCLOSED', 'CANCEL', 'BECANCEL', 'SCLOSED', 'SCANCEL'))) (optional)
select_type = 'select_type_example' # str | Buy/Sell (sell=Sell, buy=Buy, others=All) (optional)
status = 'status_example' # str | Order Status (dispute: Disputed Order; closed: ACCEPT, BCLOSED; cancel: CANCEL, BECANCEL, SCLOSED, SCANCEL; locked: LOCKED; open: OPEN; paid: PAID; completed: CANCEL, BECANCEL, SCLOSED, SCANCEL, ACCEPT, BCLOSED) (optional)
txid = 56 # int | Order ID (optional)
start_time = 56 # int | Start timestamp, default is 00:00 89 days ago (optional)
end_time = 56 # int | End timestamp, default is 23:59:59 today (optional)

try:
    # Get pending orders
    api_response = api_instance.p2p_merchant_transaction_get_pending_transaction_list(crypto_currency, fiat_currency, order_tab=order_tab, select_type=select_type, status=status, txid=txid, start_time=start_time, end_time=end_time)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling P2PApi->p2p_merchant_transaction_get_pending_transaction_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crypto_currency** | **str**| Cryptocurrency | 
 **fiat_currency** | **str**| Fiat currency | 
 **order_tab** | **str**| 订单标签页，默认pending（pending：处理中（pending:  AND status in (&#39;OPEN&#39;, &#39;PAID&#39;, &#39;LOCKED&#39;, &#39;TEMP&#39;)）；dispute：申诉中（status in (&#39;ACCEPT&#39;, &#39;BCLOSED&#39;, &#39;CANCEL&#39;, &#39;BECANCEL&#39;, &#39;SCLOSED&#39;, &#39;SCANCEL&#39;))) | [optional] 
 **select_type** | **str**| Buy/Sell (sell&#x3D;Sell, buy&#x3D;Buy, others&#x3D;All) | [optional] 
 **status** | **str**| Order Status (dispute: Disputed Order; closed: ACCEPT, BCLOSED; cancel: CANCEL, BECANCEL, SCLOSED, SCANCEL; locked: LOCKED; open: OPEN; paid: PAID; completed: CANCEL, BECANCEL, SCLOSED, SCANCEL, ACCEPT, BCLOSED) | [optional] 
 **txid** | **int**| Order ID | [optional] 
 **start_time** | **int**| Start timestamp, default is 00:00 89 days ago | [optional] 
 **end_time** | **int**| End timestamp, default is 23:59:59 today | [optional] 

### Return type

[**InlineResponse20017**](InlineResponse20017.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project-Id-Version: GateApiTools 1.0.0 Report-Msgid-Bugs-To: EMAIL@ADDRESS POT-Creation-Date: 2025-11-12 18:14+0800 PO-Revision-Date: 2019-01-02 17:30+0800 Last-Translator: FULL NAME &lt;EMAIL@ADDRESS&gt; Language: en Language-Team: en &lt;L@li.org&gt; Plural-Forms: nplurals&#x3D;2; plural&#x3D;(n !&#x3D;1) MIME-Version: 1.0 Content-Type: text/plain; charset&#x3D;utf-8 Content-Transfer-Encoding: 8bit Generated-By: Babel 2.8.0  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p2p_merchant_transaction_get_completed_transaction_list**
> InlineResponse20017 p2p_merchant_transaction_get_completed_transaction_list(crypto_currency, fiat_currency, select_type=select_type, status=status, txid=txid, start_time=start_time, end_time=end_time, query_dispute=query_dispute, page=page, per_page=per_page)

Get all/historical orders

### Example

```python
from __future__ import print_function
import gate_api
from gate_api.exceptions import ApiException, GateApiException
# Defining the host is optional and defaults to https://api.gateio.ws/api/v4
# See configuration.py for a list of all supported configuration parameters.
configuration = gate_api.Configuration(
    host = "https://api.gateio.ws/api/v4"
)

api_client = gate_api.ApiClient(configuration)
# Create an instance of the API class
api_instance = gate_api.P2PApi(api_client)
crypto_currency = 'crypto_currency_example' # str | Cryptocurrency
fiat_currency = 'fiat_currency_example' # str | Fiat currency
select_type = 'select_type_example' # str | Buy/Sell (sell=Sell, buy=Buy, others=All) (optional)
status = 'status_example' # str | Order Status (dispute: Disputed Order; closed: ACCEPT, BCLOSED; cancel: CANCEL, BECANCEL, SCLOSED, SCANCEL; locked: LOCKED; open: OPEN; paid: PAID; completed: CANCEL, BECANCEL, SCLOSED, SCANCEL, ACCEPT, BCLOSED) (optional)
txid = 56 # int | Order ID (optional)
start_time = 56 # int | Start timestamp, default is 00:00 89 days ago (optional)
end_time = 56 # int | End timestamp, default is 23:59:59 today (optional)
query_dispute = 56 # int | 1: Include appeal status, 0: None (optional)
page = 56 # int | page number (optional)
per_page = 56 # int | Number of orders per page (optional)

try:
    # Get all/historical orders
    api_response = api_instance.p2p_merchant_transaction_get_completed_transaction_list(crypto_currency, fiat_currency, select_type=select_type, status=status, txid=txid, start_time=start_time, end_time=end_time, query_dispute=query_dispute, page=page, per_page=per_page)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling P2PApi->p2p_merchant_transaction_get_completed_transaction_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crypto_currency** | **str**| Cryptocurrency | 
 **fiat_currency** | **str**| Fiat currency | 
 **select_type** | **str**| Buy/Sell (sell&#x3D;Sell, buy&#x3D;Buy, others&#x3D;All) | [optional] 
 **status** | **str**| Order Status (dispute: Disputed Order; closed: ACCEPT, BCLOSED; cancel: CANCEL, BECANCEL, SCLOSED, SCANCEL; locked: LOCKED; open: OPEN; paid: PAID; completed: CANCEL, BECANCEL, SCLOSED, SCANCEL, ACCEPT, BCLOSED) | [optional] 
 **txid** | **int**| Order ID | [optional] 
 **start_time** | **int**| Start timestamp, default is 00:00 89 days ago | [optional] 
 **end_time** | **int**| End timestamp, default is 23:59:59 today | [optional] 
 **query_dispute** | **int**| 1: Include appeal status, 0: None | [optional] 
 **page** | **int**| page number | [optional] 
 **per_page** | **int**| Number of orders per page | [optional] 

### Return type

[**InlineResponse20017**](InlineResponse20017.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project-Id-Version: GateApiTools 1.0.0 Report-Msgid-Bugs-To: EMAIL@ADDRESS POT-Creation-Date: 2025-11-12 18:14+0800 PO-Revision-Date: 2019-01-02 17:30+0800 Last-Translator: FULL NAME &lt;EMAIL@ADDRESS&gt; Language: en Language-Team: en &lt;L@li.org&gt; Plural-Forms: nplurals&#x3D;2; plural&#x3D;(n !&#x3D;1) MIME-Version: 1.0 Content-Type: text/plain; charset&#x3D;utf-8 Content-Transfer-Encoding: 8bit Generated-By: Babel 2.8.0  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p2p_merchant_transaction_get_transaction_details**
> InlineResponse20018 p2p_merchant_transaction_get_transaction_details(txid, channel=channel)

Query order details

### Example

```python
from __future__ import print_function
import gate_api
from gate_api.exceptions import ApiException, GateApiException
# Defining the host is optional and defaults to https://api.gateio.ws/api/v4
# See configuration.py for a list of all supported configuration parameters.
configuration = gate_api.Configuration(
    host = "https://api.gateio.ws/api/v4"
)

api_client = gate_api.ApiClient(configuration)
# Create an instance of the API class
api_instance = gate_api.P2PApi(api_client)
txid = 56 # int | Order ID
channel = 'channel_example' # str | Empty or web3 (optional)

try:
    # Query order details
    api_response = api_instance.p2p_merchant_transaction_get_transaction_details(txid, channel=channel)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling P2PApi->p2p_merchant_transaction_get_transaction_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **txid** | **int**| Order ID | 
 **channel** | **str**| Empty or web3 | [optional] 

### Return type

[**InlineResponse20018**](InlineResponse20018.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project-Id-Version: GateApiTools 1.0.0 Report-Msgid-Bugs-To: EMAIL@ADDRESS POT-Creation-Date: 2025-11-12 18:14+0800 PO-Revision-Date: 2019-01-02 17:30+0800 Last-Translator: FULL NAME &lt;EMAIL@ADDRESS&gt; Language: en Language-Team: en &lt;L@li.org&gt; Plural-Forms: nplurals&#x3D;2; plural&#x3D;(n !&#x3D;1) MIME-Version: 1.0 Content-Type: text/plain; charset&#x3D;utf-8 Content-Transfer-Encoding: 8bit Generated-By: Babel 2.8.0  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p2p_merchant_transaction_confirm_payment**
> InlineResponse2007 p2p_merchant_transaction_confirm_payment(inline_object10=inline_object10)

Confirm payment

### Example

```python
from __future__ import print_function
import gate_api
from gate_api.exceptions import ApiException, GateApiException
# Defining the host is optional and defaults to https://api.gateio.ws/api/v4
# See configuration.py for a list of all supported configuration parameters.
configuration = gate_api.Configuration(
    host = "https://api.gateio.ws/api/v4"
)

api_client = gate_api.ApiClient(configuration)
# Create an instance of the API class
api_instance = gate_api.P2PApi(api_client)
inline_object10 = gate_api.InlineObject10() # InlineObject10 |  (optional)

try:
    # Confirm payment
    api_response = api_instance.p2p_merchant_transaction_confirm_payment(inline_object10=inline_object10)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling P2PApi->p2p_merchant_transaction_confirm_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object10** | [**InlineObject10**](InlineObject10.md)|  | [optional] 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project-Id-Version: GateApiTools 1.0.0 Report-Msgid-Bugs-To: EMAIL@ADDRESS POT-Creation-Date: 2025-11-12 18:14+0800 PO-Revision-Date: 2019-01-02 17:30+0800 Last-Translator: FULL NAME &lt;EMAIL@ADDRESS&gt; Language: en Language-Team: en &lt;L@li.org&gt; Plural-Forms: nplurals&#x3D;2; plural&#x3D;(n !&#x3D;1) MIME-Version: 1.0 Content-Type: text/plain; charset&#x3D;utf-8 Content-Transfer-Encoding: 8bit Generated-By: Babel 2.8.0  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p2p_merchant_transaction_confirm_receipt**
> InlineResponse2007 p2p_merchant_transaction_confirm_receipt(inline_object11=inline_object11)

Confirm receipt

### Example

```python
from __future__ import print_function
import gate_api
from gate_api.exceptions import ApiException, GateApiException
# Defining the host is optional and defaults to https://api.gateio.ws/api/v4
# See configuration.py for a list of all supported configuration parameters.
configuration = gate_api.Configuration(
    host = "https://api.gateio.ws/api/v4"
)

api_client = gate_api.ApiClient(configuration)
# Create an instance of the API class
api_instance = gate_api.P2PApi(api_client)
inline_object11 = gate_api.InlineObject11() # InlineObject11 |  (optional)

try:
    # Confirm receipt
    api_response = api_instance.p2p_merchant_transaction_confirm_receipt(inline_object11=inline_object11)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling P2PApi->p2p_merchant_transaction_confirm_receipt: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object11** | [**InlineObject11**](InlineObject11.md)|  | [optional] 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project-Id-Version: GateApiTools 1.0.0 Report-Msgid-Bugs-To: EMAIL@ADDRESS POT-Creation-Date: 2025-11-12 18:14+0800 PO-Revision-Date: 2019-01-02 17:30+0800 Last-Translator: FULL NAME &lt;EMAIL@ADDRESS&gt; Language: en Language-Team: en &lt;L@li.org&gt; Plural-Forms: nplurals&#x3D;2; plural&#x3D;(n !&#x3D;1) MIME-Version: 1.0 Content-Type: text/plain; charset&#x3D;utf-8 Content-Transfer-Encoding: 8bit Generated-By: Babel 2.8.0  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p2p_merchant_transaction_cancel**
> InlineResponse2007 p2p_merchant_transaction_cancel(inline_object12=inline_object12)

Cancel order

### Example

```python
from __future__ import print_function
import gate_api
from gate_api.exceptions import ApiException, GateApiException
# Defining the host is optional and defaults to https://api.gateio.ws/api/v4
# See configuration.py for a list of all supported configuration parameters.
configuration = gate_api.Configuration(
    host = "https://api.gateio.ws/api/v4"
)

api_client = gate_api.ApiClient(configuration)
# Create an instance of the API class
api_instance = gate_api.P2PApi(api_client)
inline_object12 = gate_api.InlineObject12() # InlineObject12 |  (optional)

try:
    # Cancel order
    api_response = api_instance.p2p_merchant_transaction_cancel(inline_object12=inline_object12)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling P2PApi->p2p_merchant_transaction_cancel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object12** | [**InlineObject12**](InlineObject12.md)|  | [optional] 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project-Id-Version: GateApiTools 1.0.0 Report-Msgid-Bugs-To: EMAIL@ADDRESS POT-Creation-Date: 2025-11-12 18:14+0800 PO-Revision-Date: 2019-01-02 17:30+0800 Last-Translator: FULL NAME &lt;EMAIL@ADDRESS&gt; Language: en Language-Team: en &lt;L@li.org&gt; Plural-Forms: nplurals&#x3D;2; plural&#x3D;(n !&#x3D;1) MIME-Version: 1.0 Content-Type: text/plain; charset&#x3D;utf-8 Content-Transfer-Encoding: 8bit Generated-By: Babel 2.8.0  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p2p_merchant_books_place_biz_push_order**
> object p2p_merchant_books_place_biz_push_order(currency_type, exchange_type, type, unit_price, number, min_amount, max_amount, pay_type=pay_type, pay_type_json=pay_type_json, rate_fixed=rate_fixed, oid=oid, tier_limit=tier_limit, verified_limit=verified_limit, reg_time_limit=reg_time_limit, advertisers_limit=advertisers_limit, hide_payment=hide_payment, expire_min=expire_min, trade_tips=trade_tips, auto_reply=auto_reply, min_completed_limit=min_completed_limit, max_completed_limit=max_completed_limit, completed_rate_limit=completed_rate_limit, user_country_limit=user_country_limit, user_order_limit=user_order_limit, rate_reference_id=rate_reference_id, rate_offset=rate_offset, float_trend=float_trend)

Publish ad order

### Example

```python
from __future__ import print_function
import gate_api
from gate_api.exceptions import ApiException, GateApiException
# Defining the host is optional and defaults to https://api.gateio.ws/api/v4
# See configuration.py for a list of all supported configuration parameters.
configuration = gate_api.Configuration(
    host = "https://api.gateio.ws/api/v4"
)

api_client = gate_api.ApiClient(configuration)
# Create an instance of the API class
api_instance = gate_api.P2PApi(api_client)
currency_type = 'currency_type_example' # str | Cryptocurrency
exchange_type = 'exchange_type_example' # str | Fiat currency
type = 'type_example' # str | Ad type: 0=Sell, 1=Buy, 2=Edit sell, 3=Edit buy
unit_price = 'unit_price_example' # str | Unit price
number = 'number_example' # str | Size
min_amount = 'min_amount_example' # str | Minimum transaction amount per order
max_amount = 'max_amount_example' # str | Maximum transaction amount per order
pay_type = 'pay_type_example' # str | Payment method (optional)
pay_type_json = 'pay_type_json_example' # str | Payment method JSON string (optional)
rate_fixed = 'rate_fixed_example' # str | Price type: 0-Floating price, 1-Fixed price (optional)
oid = 'oid_example' # str | Ad ID when editing (optional)
tier_limit = 'tier_limit_example' # str | Order tier limit (optional)
verified_limit = 'verified_limit_example' # str | Verification level limit (optional)
reg_time_limit = 'reg_time_limit_example' # str | Registration time limit (optional)
advertisers_limit = 'advertisers_limit_example' # str | Advertiser restriction (optional)
hide_payment = 'hide_payment_example' # str | Whether to hide payment method: 1=Yes, 0=No (optional)
expire_min = 'expire_min_example' # str | Ad expiration time (minutes) (optional)
trade_tips = 'trade_tips_example' # str | Trading terms (optional)
auto_reply = 'auto_reply_example' # str | Auto reply (optional)
min_completed_limit = 'min_completed_limit_example' # str | Minimum limit of completed orders (optional)
max_completed_limit = 'max_completed_limit_example' # str | Maximum limit of completed orders (optional)
completed_rate_limit = 'completed_rate_limit_example' # str | 30-day completion rate limit (optional)
user_country_limit = 'user_country_limit_example' # str | KYC nationality restriction (optional)
user_order_limit = 'user_order_limit_example' # str | Order count limit (optional)
rate_reference_id = 'rate_reference_id_example' # str | Reference exchange rate ID (optional)
rate_offset = 'rate_offset_example' # str | Reference exchange rate offset (optional)
float_trend = 'float_trend_example' # str | 444 (optional)

try:
    # Publish ad order
    api_response = api_instance.p2p_merchant_books_place_biz_push_order(currency_type, exchange_type, type, unit_price, number, min_amount, max_amount, pay_type=pay_type, pay_type_json=pay_type_json, rate_fixed=rate_fixed, oid=oid, tier_limit=tier_limit, verified_limit=verified_limit, reg_time_limit=reg_time_limit, advertisers_limit=advertisers_limit, hide_payment=hide_payment, expire_min=expire_min, trade_tips=trade_tips, auto_reply=auto_reply, min_completed_limit=min_completed_limit, max_completed_limit=max_completed_limit, completed_rate_limit=completed_rate_limit, user_country_limit=user_country_limit, user_order_limit=user_order_limit, rate_reference_id=rate_reference_id, rate_offset=rate_offset, float_trend=float_trend)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling P2PApi->p2p_merchant_books_place_biz_push_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency_type** | **str**| Cryptocurrency | 
 **exchange_type** | **str**| Fiat currency | 
 **type** | **str**| Ad type: 0&#x3D;Sell, 1&#x3D;Buy, 2&#x3D;Edit sell, 3&#x3D;Edit buy | 
 **unit_price** | **str**| Unit price | 
 **number** | **str**| Size | 
 **min_amount** | **str**| Minimum transaction amount per order | 
 **max_amount** | **str**| Maximum transaction amount per order | 
 **pay_type** | **str**| Payment method | [optional] 
 **pay_type_json** | **str**| Payment method JSON string | [optional] 
 **rate_fixed** | **str**| Price type: 0-Floating price, 1-Fixed price | [optional] 
 **oid** | **str**| Ad ID when editing | [optional] 
 **tier_limit** | **str**| Order tier limit | [optional] 
 **verified_limit** | **str**| Verification level limit | [optional] 
 **reg_time_limit** | **str**| Registration time limit | [optional] 
 **advertisers_limit** | **str**| Advertiser restriction | [optional] 
 **hide_payment** | **str**| Whether to hide payment method: 1&#x3D;Yes, 0&#x3D;No | [optional] 
 **expire_min** | **str**| Ad expiration time (minutes) | [optional] 
 **trade_tips** | **str**| Trading terms | [optional] 
 **auto_reply** | **str**| Auto reply | [optional] 
 **min_completed_limit** | **str**| Minimum limit of completed orders | [optional] 
 **max_completed_limit** | **str**| Maximum limit of completed orders | [optional] 
 **completed_rate_limit** | **str**| 30-day completion rate limit | [optional] 
 **user_country_limit** | **str**| KYC nationality restriction | [optional] 
 **user_order_limit** | **str**| Order count limit | [optional] 
 **rate_reference_id** | **str**| Reference exchange rate ID | [optional] 
 **rate_offset** | **str**| Reference exchange rate offset | [optional] 
 **float_trend** | **str**| 444 | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project-Id-Version: GateApiTools 1.0.0 Report-Msgid-Bugs-To: EMAIL@ADDRESS POT-Creation-Date: 2025-11-12 18:14+0800 PO-Revision-Date: 2019-01-02 17:30+0800 Last-Translator: FULL NAME &lt;EMAIL@ADDRESS&gt; Language: en Language-Team: en &lt;L@li.org&gt; Plural-Forms: nplurals&#x3D;2; plural&#x3D;(n !&#x3D;1) MIME-Version: 1.0 Content-Type: text/plain; charset&#x3D;utf-8 Content-Transfer-Encoding: 8bit Generated-By: Babel 2.8.0  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p2p_merchant_books_ads_update_status**
> InlineResponse20019 p2p_merchant_books_ads_update_status(adv_no, adv_status, trade_type=trade_type)

Update ad status

### Example

```python
from __future__ import print_function
import gate_api
from gate_api.exceptions import ApiException, GateApiException
# Defining the host is optional and defaults to https://api.gateio.ws/api/v4
# See configuration.py for a list of all supported configuration parameters.
configuration = gate_api.Configuration(
    host = "https://api.gateio.ws/api/v4"
)

api_client = gate_api.ApiClient(configuration)
# Create an instance of the API class
api_instance = gate_api.P2PApi(api_client)
adv_no = 56 # int | Ad ID
adv_status = 56 # int | Ad status: 1=Active, 3=Inactive, 4=Closed
trade_type = 'sell' # str | Project-Id-Version: GateApiTools 1.0.0 Report-Msgid-Bugs-To: EMAIL@ADDRESS POT-Creation-Date: 2025-11-12 18:14+0800 PO-Revision-Date: 2019-01-02 17:30+0800 Last-Translator: FULL NAME <EMAIL@ADDRESS> Language: en Language-Team: en <L@li.org> Plural-Forms: nplurals=2; plural=(n !=1) MIME-Version: 1.0 Content-Type: text/plain; charset=utf-8 Content-Transfer-Encoding: 8bit Generated-By: Babel 2.8.0  (optional)

try:
    # Update ad status
    api_response = api_instance.p2p_merchant_books_ads_update_status(adv_no, adv_status, trade_type=trade_type)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling P2PApi->p2p_merchant_books_ads_update_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **adv_no** | **int**| Ad ID | 
 **adv_status** | **int**| Ad status: 1&#x3D;Active, 3&#x3D;Inactive, 4&#x3D;Closed | 
 **trade_type** | **str**| Project-Id-Version: GateApiTools 1.0.0 Report-Msgid-Bugs-To: EMAIL@ADDRESS POT-Creation-Date: 2025-11-12 18:14+0800 PO-Revision-Date: 2019-01-02 17:30+0800 Last-Translator: FULL NAME &lt;EMAIL@ADDRESS&gt; Language: en Language-Team: en &lt;L@li.org&gt; Plural-Forms: nplurals&#x3D;2; plural&#x3D;(n !&#x3D;1) MIME-Version: 1.0 Content-Type: text/plain; charset&#x3D;utf-8 Content-Transfer-Encoding: 8bit Generated-By: Babel 2.8.0  | [optional] 

### Return type

[**InlineResponse20019**](InlineResponse20019.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project-Id-Version: GateApiTools 1.0.0 Report-Msgid-Bugs-To: EMAIL@ADDRESS POT-Creation-Date: 2025-11-12 18:14+0800 PO-Revision-Date: 2019-01-02 17:30+0800 Last-Translator: FULL NAME &lt;EMAIL@ADDRESS&gt; Language: en Language-Team: en &lt;L@li.org&gt; Plural-Forms: nplurals&#x3D;2; plural&#x3D;(n !&#x3D;1) MIME-Version: 1.0 Content-Type: text/plain; charset&#x3D;utf-8 Content-Transfer-Encoding: 8bit Generated-By: Babel 2.8.0  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p2p_merchant_books_ads_detail**
> InlineResponse20020 p2p_merchant_books_ads_detail(adv_no)

Query ad details

### Example

```python
from __future__ import print_function
import gate_api
from gate_api.exceptions import ApiException, GateApiException
# Defining the host is optional and defaults to https://api.gateio.ws/api/v4
# See configuration.py for a list of all supported configuration parameters.
configuration = gate_api.Configuration(
    host = "https://api.gateio.ws/api/v4"
)

api_client = gate_api.ApiClient(configuration)
# Create an instance of the API class
api_instance = gate_api.P2PApi(api_client)
adv_no = 'adv_no_example' # str | 

try:
    # Query ad details
    api_response = api_instance.p2p_merchant_books_ads_detail(adv_no)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling P2PApi->p2p_merchant_books_ads_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **adv_no** | **str**|  | 

### Return type

[**InlineResponse20020**](InlineResponse20020.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project-Id-Version: GateApiTools 1.0.0 Report-Msgid-Bugs-To: EMAIL@ADDRESS POT-Creation-Date: 2025-11-12 18:14+0800 PO-Revision-Date: 2019-01-02 17:30+0800 Last-Translator: FULL NAME &lt;EMAIL@ADDRESS&gt; Language: en Language-Team: en &lt;L@li.org&gt; Plural-Forms: nplurals&#x3D;2; plural&#x3D;(n !&#x3D;1) MIME-Version: 1.0 Content-Type: text/plain; charset&#x3D;utf-8 Content-Transfer-Encoding: 8bit Generated-By: Babel 2.8.0  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p2p_merchant_books_my_ads_list**
> InlineResponse20021 p2p_merchant_books_my_ads_list(asset=asset, fiat_unit=fiat_unit, trade_type=trade_type)

Get my ad list

### Example

```python
from __future__ import print_function
import gate_api
from gate_api.exceptions import ApiException, GateApiException
# Defining the host is optional and defaults to https://api.gateio.ws/api/v4
# See configuration.py for a list of all supported configuration parameters.
configuration = gate_api.Configuration(
    host = "https://api.gateio.ws/api/v4"
)

api_client = gate_api.ApiClient(configuration)
# Create an instance of the API class
api_instance = gate_api.P2PApi(api_client)
asset = 'asset_example' # str | Cryptocurrency (optional)
fiat_unit = 'fiat_unit_example' # str | Fiat currency (optional)
trade_type = 'trade_type_example' # str | Buy/Sell (optional)

try:
    # Get my ad list
    api_response = api_instance.p2p_merchant_books_my_ads_list(asset=asset, fiat_unit=fiat_unit, trade_type=trade_type)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling P2PApi->p2p_merchant_books_my_ads_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**| Cryptocurrency | [optional] 
 **fiat_unit** | **str**| Fiat currency | [optional] 
 **trade_type** | **str**| Buy/Sell | [optional] 

### Return type

[**InlineResponse20021**](InlineResponse20021.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project-Id-Version: GateApiTools 1.0.0 Report-Msgid-Bugs-To: EMAIL@ADDRESS POT-Creation-Date: 2025-11-12 18:14+0800 PO-Revision-Date: 2019-01-02 17:30+0800 Last-Translator: FULL NAME &lt;EMAIL@ADDRESS&gt; Language: en Language-Team: en &lt;L@li.org&gt; Plural-Forms: nplurals&#x3D;2; plural&#x3D;(n !&#x3D;1) MIME-Version: 1.0 Content-Type: text/plain; charset&#x3D;utf-8 Content-Transfer-Encoding: 8bit Generated-By: Babel 2.8.0  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p2p_merchant_chat_get_chats_list**
> InlineResponse20022 p2p_merchant_chat_get_chats_list(txid, lastreceived=lastreceived, firstreceived=firstreceived)

Get chat history

### Example

```python
from __future__ import print_function
import gate_api
from gate_api.exceptions import ApiException, GateApiException
# Defining the host is optional and defaults to https://api.gateio.ws/api/v4
# See configuration.py for a list of all supported configuration parameters.
configuration = gate_api.Configuration(
    host = "https://api.gateio.ws/api/v4"
)

api_client = gate_api.ApiClient(configuration)
# Create an instance of the API class
api_instance = gate_api.P2PApi(api_client)
txid = 56 # int | Order ID
lastreceived = 56 # int | Pagination timestamp (forward) (optional)
firstreceived = 56 # int | Pagination timestamp (backward) (optional)

try:
    # Get chat history
    api_response = api_instance.p2p_merchant_chat_get_chats_list(txid, lastreceived=lastreceived, firstreceived=firstreceived)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling P2PApi->p2p_merchant_chat_get_chats_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **txid** | **int**| Order ID | 
 **lastreceived** | **int**| Pagination timestamp (forward) | [optional] 
 **firstreceived** | **int**| Pagination timestamp (backward) | [optional] 

### Return type

[**InlineResponse20022**](InlineResponse20022.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project-Id-Version: GateApiTools 1.0.0 Report-Msgid-Bugs-To: EMAIL@ADDRESS POT-Creation-Date: 2025-11-12 18:14+0800 PO-Revision-Date: 2019-01-02 17:30+0800 Last-Translator: FULL NAME &lt;EMAIL@ADDRESS&gt; Language: en Language-Team: en &lt;L@li.org&gt; Plural-Forms: nplurals&#x3D;2; plural&#x3D;(n !&#x3D;1) MIME-Version: 1.0 Content-Type: text/plain; charset&#x3D;utf-8 Content-Transfer-Encoding: 8bit Generated-By: Babel 2.8.0  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p2p_merchant_chat_send_chat_message**
> InlineResponse20023 p2p_merchant_chat_send_chat_message(txid, message, type=type)

Send text message

### Example

```python
from __future__ import print_function
import gate_api
from gate_api.exceptions import ApiException, GateApiException
# Defining the host is optional and defaults to https://api.gateio.ws/api/v4
# See configuration.py for a list of all supported configuration parameters.
configuration = gate_api.Configuration(
    host = "https://api.gateio.ws/api/v4"
)

api_client = gate_api.ApiClient(configuration)
# Create an instance of the API class
api_instance = gate_api.P2PApi(api_client)
txid = 56 # int | Order ID
message = 'message_example' # str | Message content
type = 56 # int | 0=Text, 1=File (video or image), default is 0 if not provided (optional)

try:
    # Send text message
    api_response = api_instance.p2p_merchant_chat_send_chat_message(txid, message, type=type)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling P2PApi->p2p_merchant_chat_send_chat_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **txid** | **int**| Order ID | 
 **message** | **str**| Message content | 
 **type** | **int**| 0&#x3D;Text, 1&#x3D;File (video or image), default is 0 if not provided | [optional] 

### Return type

[**InlineResponse20023**](InlineResponse20023.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project-Id-Version: GateApiTools 1.0.0 Report-Msgid-Bugs-To: EMAIL@ADDRESS POT-Creation-Date: 2025-11-12 18:14+0800 PO-Revision-Date: 2019-01-02 17:30+0800 Last-Translator: FULL NAME &lt;EMAIL@ADDRESS&gt; Language: en Language-Team: en &lt;L@li.org&gt; Plural-Forms: nplurals&#x3D;2; plural&#x3D;(n !&#x3D;1) MIME-Version: 1.0 Content-Type: text/plain; charset&#x3D;utf-8 Content-Transfer-Encoding: 8bit Generated-By: Babel 2.8.0  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p2p_merchant_chat_upload_chat_file**
> InlineResponse20024 p2p_merchant_chat_upload_chat_file(image_content_type, base64_img)

Upload chat file

### Example

```python
from __future__ import print_function
import gate_api
from gate_api.exceptions import ApiException, GateApiException
# Defining the host is optional and defaults to https://api.gateio.ws/api/v4
# See configuration.py for a list of all supported configuration parameters.
configuration = gate_api.Configuration(
    host = "https://api.gateio.ws/api/v4"
)

api_client = gate_api.ApiClient(configuration)
# Create an instance of the API class
api_instance = gate_api.P2PApi(api_client)
image_content_type = 'image_content_type_example' # str | File type, currently only images and videos are supported
base64_img = 'base64_img_example' # str | File content (base64 encoded)

try:
    # Upload chat file
    api_response = api_instance.p2p_merchant_chat_upload_chat_file(image_content_type, base64_img)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling P2PApi->p2p_merchant_chat_upload_chat_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_content_type** | **str**| File type, currently only images and videos are supported | 
 **base64_img** | **str**| File content (base64 encoded) | 

### Return type

[**InlineResponse20024**](InlineResponse20024.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project-Id-Version: GateApiTools 1.0.0 Report-Msgid-Bugs-To: EMAIL@ADDRESS POT-Creation-Date: 2025-11-12 18:14+0800 PO-Revision-Date: 2019-01-02 17:30+0800 Last-Translator: FULL NAME &lt;EMAIL@ADDRESS&gt; Language: en Language-Team: en &lt;L@li.org&gt; Plural-Forms: nplurals&#x3D;2; plural&#x3D;(n !&#x3D;1) MIME-Version: 1.0 Content-Type: text/plain; charset&#x3D;utf-8 Content-Transfer-Encoding: 8bit Generated-By: Babel 2.8.0  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

