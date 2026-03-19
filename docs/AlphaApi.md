# gate_api.AlphaApi

All URIs are relative to *https://api.gateio.ws/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_alpha_accounts**](AlphaApi.md#list_alpha_accounts) | **GET** /alpha/accounts | Alpha Account API
[**list_alpha_account_book**](AlphaApi.md#list_alpha_account_book) | **GET** /alpha/account_book | Alpha Account Transaction History API
[**quote_alpha_order**](AlphaApi.md#quote_alpha_order) | **POST** /alpha/quote | Alpha Quote API
[**list_alpha_order**](AlphaApi.md#list_alpha_order) | **GET** /alpha/orders | Alpha Order List API
[**place_alpha_order**](AlphaApi.md#place_alpha_order) | **POST** /alpha/orders | Alpha Order API
[**get_alpha_order**](AlphaApi.md#get_alpha_order) | **GET** /alpha/order | Alpha Single Order Query API
[**list_alpha_currencies**](AlphaApi.md#list_alpha_currencies) | **GET** /alpha/currencies | Query currency information
[**list_alpha_tickers**](AlphaApi.md#list_alpha_tickers) | **GET** /alpha/tickers | Query currency ticker
[**list_alpha_tokens**](AlphaApi.md#list_alpha_tokens) | **GET** /alpha/tokens | Query Token Information


# **list_alpha_accounts**
> list[AccountsResponse] list_alpha_accounts()

Alpha Account API

Query position assets

### Example

* Api Key Authentication (apiv4):
```python
from __future__ import print_function
import gate_api
from gate_api.exceptions import ApiException, GateApiException
# Defining the host is optional and defaults to https://api.gateio.ws/api/v4
# See configuration.py for a list of all supported configuration parameters.
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure APIv4 key authorization
configuration = gate_api.Configuration(
    host = "https://api.gateio.ws/api/v4",
    key = "YOU_API_KEY",
    secret = "YOUR_API_SECRET"
)

api_client = gate_api.ApiClient(configuration)
# Create an instance of the API class
api_instance = gate_api.AlphaApi(api_client)

try:
    # Alpha Account API
    api_response = api_instance.list_alpha_accounts()
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling AlphaApi->list_alpha_accounts: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[AccountsResponse]**](AccountsResponse.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positions queried successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_alpha_account_book**
> list[AccountBookResponse] list_alpha_account_book(_from, to=to, page=page, limit=limit)

Alpha Account Transaction History API

Query asset transactions

### Example

* Api Key Authentication (apiv4):
```python
from __future__ import print_function
import gate_api
from gate_api.exceptions import ApiException, GateApiException
# Defining the host is optional and defaults to https://api.gateio.ws/api/v4
# See configuration.py for a list of all supported configuration parameters.
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure APIv4 key authorization
configuration = gate_api.Configuration(
    host = "https://api.gateio.ws/api/v4",
    key = "YOU_API_KEY",
    secret = "YOUR_API_SECRET"
)

api_client = gate_api.ApiClient(configuration)
# Create an instance of the API class
api_instance = gate_api.AlphaApi(api_client)
_from = 56 # int | Start timestamp for the query
to = 56 # int | End timestamp for the query, defaults to current time if not specified (optional)
page = 56 # int | Page number (optional)
limit = 56 # int | Maximum 100 items per page (optional)

try:
    # Alpha Account Transaction History API
    api_response = api_instance.list_alpha_account_book(_from, to=to, page=page, limit=limit)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling AlphaApi->list_alpha_account_book: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **int**| Start timestamp for the query | 
 **to** | **int**| End timestamp for the query, defaults to current time if not specified | [optional] 
 **page** | **int**| Page number | [optional] 
 **limit** | **int**| Maximum 100 items per page | [optional] 

### Return type

[**list[AccountBookResponse]**](AccountBookResponse.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Transaction history retrieved successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quote_alpha_order**
> QuoteResponse quote_alpha_order(quote_request)

Alpha Quote API

The quote_id returned by the price inquiry interface is valid for one minute; an order must be placed within this minute. If it times out, a new price inquiry is required. Rate-limited at 10 requests per second per user.

### Example

* Api Key Authentication (apiv4):
```python
from __future__ import print_function
import gate_api
from gate_api.exceptions import ApiException, GateApiException
# Defining the host is optional and defaults to https://api.gateio.ws/api/v4
# See configuration.py for a list of all supported configuration parameters.
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure APIv4 key authorization
configuration = gate_api.Configuration(
    host = "https://api.gateio.ws/api/v4",
    key = "YOU_API_KEY",
    secret = "YOUR_API_SECRET"
)

api_client = gate_api.ApiClient(configuration)
# Create an instance of the API class
api_instance = gate_api.AlphaApi(api_client)
quote_request = gate_api.QuoteRequest() # QuoteRequest | 

try:
    # Alpha Quote API
    api_response = api_instance.quote_alpha_order(quote_request)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling AlphaApi->quote_alpha_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quote_request** | [**QuoteRequest**](QuoteRequest.md)|  | 

### Return type

[**QuoteResponse**](QuoteResponse.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Quote retrieved successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_alpha_order**
> list[OrderResponse] list_alpha_order(currency=currency, side=side, status=status, _from=_from, to=to, limit=limit, page=page)

Alpha Order List API

### Example

* Api Key Authentication (apiv4):
```python
from __future__ import print_function
import gate_api
from gate_api.exceptions import ApiException, GateApiException
# Defining the host is optional and defaults to https://api.gateio.ws/api/v4
# See configuration.py for a list of all supported configuration parameters.
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure APIv4 key authorization
configuration = gate_api.Configuration(
    host = "https://api.gateio.ws/api/v4",
    key = "YOU_API_KEY",
    secret = "YOUR_API_SECRET"
)

api_client = gate_api.ApiClient(configuration)
# Create an instance of the API class
api_instance = gate_api.AlphaApi(api_client)
currency = 'memeboxsst' # str | Trading symbol (optional)
side = 'buy' # str | Buy or sell orders - buy - sell (optional)
status = 2 # int | Order Status - `0` : All - `1` : Processing - `2` : Successful - `3` : Failed - `4` : Cancelled - `5` : Buy order placed but transfer not completed - `6` : Order cancelled but transfer not completed (optional)
_from = 1627706330 # int | Start time for order query (optional)
to = 1635329650 # int | End time for order query, defaults to current time if not specified (optional)
limit = 100 # int | Maximum number of items returned. Default: 100, minimum: 1, maximum: 100 (optional) (default to 100)
page = 1 # int | Page number (optional) (default to 1)

try:
    # Alpha Order List API
    api_response = api_instance.list_alpha_order(currency=currency, side=side, status=status, _from=_from, to=to, limit=limit, page=page)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling AlphaApi->list_alpha_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| Trading symbol | [optional] 
 **side** | **str**| Buy or sell orders - buy - sell | [optional] 
 **status** | **int**| Order Status - &#x60;0&#x60; : All - &#x60;1&#x60; : Processing - &#x60;2&#x60; : Successful - &#x60;3&#x60; : Failed - &#x60;4&#x60; : Cancelled - &#x60;5&#x60; : Buy order placed but transfer not completed - &#x60;6&#x60; : Order cancelled but transfer not completed | [optional] 
 **_from** | **int**| Start time for order query | [optional] 
 **to** | **int**| End time for order query, defaults to current time if not specified | [optional] 
 **limit** | **int**| Maximum number of items returned. Default: 100, minimum: 1, maximum: 100 | [optional] [default to 100]
 **page** | **int**| Page number | [optional] [default to 1]

### Return type

[**list[OrderResponse]**](OrderResponse.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List retrieved successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **place_alpha_order**
> PlaceOrderResponse place_alpha_order(place_order_request)

Alpha Order API

Order placement interface, rate-limited at 5 requests per second per user.

### Example

* Api Key Authentication (apiv4):
```python
from __future__ import print_function
import gate_api
from gate_api.exceptions import ApiException, GateApiException
# Defining the host is optional and defaults to https://api.gateio.ws/api/v4
# See configuration.py for a list of all supported configuration parameters.
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure APIv4 key authorization
configuration = gate_api.Configuration(
    host = "https://api.gateio.ws/api/v4",
    key = "YOU_API_KEY",
    secret = "YOUR_API_SECRET"
)

api_client = gate_api.ApiClient(configuration)
# Create an instance of the API class
api_instance = gate_api.AlphaApi(api_client)
place_order_request = gate_api.PlaceOrderRequest() # PlaceOrderRequest | 

try:
    # Alpha Order API
    api_response = api_instance.place_alpha_order(place_order_request)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling AlphaApi->place_alpha_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **place_order_request** | [**PlaceOrderRequest**](PlaceOrderRequest.md)|  | 

### Return type

[**PlaceOrderResponse**](PlaceOrderResponse.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Order placed successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alpha_order**
> OrderResponse get_alpha_order(order_id)

Alpha Single Order Query API

### Example

* Api Key Authentication (apiv4):
```python
from __future__ import print_function
import gate_api
from gate_api.exceptions import ApiException, GateApiException
# Defining the host is optional and defaults to https://api.gateio.ws/api/v4
# See configuration.py for a list of all supported configuration parameters.
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure APIv4 key authorization
configuration = gate_api.Configuration(
    host = "https://api.gateio.ws/api/v4",
    key = "YOU_API_KEY",
    secret = "YOUR_API_SECRET"
)

api_client = gate_api.ApiClient(configuration)
# Create an instance of the API class
api_instance = gate_api.AlphaApi(api_client)
order_id = 'fdaf12321' # str | Order ID

try:
    # Alpha Single Order Query API
    api_response = api_instance.get_alpha_order(order_id)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling AlphaApi->get_alpha_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| Order ID | 

### Return type

[**OrderResponse**](OrderResponse.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Order queried successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_alpha_currencies**
> list[AlphaCurrency] list_alpha_currencies(currency=currency, limit=limit, page=page)

Query currency information

When currency is provided, query and return specified currency information; when currency is not provided, return paginated currency list

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
api_instance = gate_api.AlphaApi(api_client)
currency = 'memeboxtrump' # str | Query currency information by currency symbol (optional)
limit = 100 # int | Maximum number of records returned in a single list (optional) (default to 100)
page = 1 # int | Page number (optional) (default to 1)

try:
    # Query currency information
    api_response = api_instance.list_alpha_currencies(currency=currency, limit=limit, page=page)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling AlphaApi->list_alpha_currencies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| Query currency information by currency symbol | [optional] 
 **limit** | **int**| Maximum number of records returned in a single list | [optional] [default to 100]
 **page** | **int**| Page number | [optional] [default to 1]

### Return type

[**list[AlphaCurrency]**](AlphaCurrency.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Query successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_alpha_tickers**
> list[AlphaTicker] list_alpha_tickers(currency=currency, limit=limit, page=page)

Query currency ticker

When currency is provided, returns ticker information for the specified currency. When currency is not provided, returns paginated ticker list

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
api_instance = gate_api.AlphaApi(api_client)
currency = 'memeboxtrump' # str | Query by specified currency name (optional)
limit = 100 # int | Maximum number of records returned in a single list (optional) (default to 100)
page = 1 # int | Page number (optional) (default to 1)

try:
    # Query currency ticker
    api_response = api_instance.list_alpha_tickers(currency=currency, limit=limit, page=page)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling AlphaApi->list_alpha_tickers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| Query by specified currency name | [optional] 
 **limit** | **int**| Maximum number of records returned in a single list | [optional] [default to 100]
 **page** | **int**| Page number | [optional] [default to 1]

### Return type

[**list[AlphaTicker]**](AlphaTicker.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Query successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_alpha_tokens**
> list[Tokens] list_alpha_tokens(chain=chain, launch_platform=launch_platform, address=address, page=page)

Query Token Information

Supports passing chain, platform, and address

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
api_instance = gate_api.AlphaApi(api_client)
chain = 'solana' # str | Query Token List by Chain  - solana - eth - bsc - base - world - sui - arbitrum - avalanche - polygon - linea - optimism - zksync - gatelayer (optional)
launch_platform = 'pump' # str | Query Token List by Launch Platform  - meteora_dbc - fourmeme - moonshot - pump - raydium_launchlab - letsbonk - gatefun - virtuals (optional)
address = '0x1234p' # str | Query Token List by Contract Address (optional)
page = 1 # int | Page number (optional) (default to 1)

try:
    # Query Token Information
    api_response = api_instance.list_alpha_tokens(chain=chain, launch_platform=launch_platform, address=address, page=page)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling AlphaApi->list_alpha_tokens: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chain** | **str**| Query Token List by Chain  - solana - eth - bsc - base - world - sui - arbitrum - avalanche - polygon - linea - optimism - zksync - gatelayer | [optional] 
 **launch_platform** | **str**| Query Token List by Launch Platform  - meteora_dbc - fourmeme - moonshot - pump - raydium_launchlab - letsbonk - gatefun - virtuals | [optional] 
 **address** | **str**| Query Token List by Contract Address | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]

### Return type

[**list[Tokens]**](Tokens.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Query successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

