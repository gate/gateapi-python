# gate_api.StockApi

All URIs are relative to *https://api.gateio.ws/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**query_stock_user_assets**](StockApi.md#query_stock_user_assets) | **GET** /stock/users/assets | Query user assets
[**query_stock_symbols**](StockApi.md#query_stock_symbols) | **GET** /stock/symbols | Query symbol list
[**query_stock_symbol_detail**](StockApi.md#query_stock_symbol_detail) | **GET** /stock/symbols/detail | Query symbol details
[**query_stock_order_book**](StockApi.md#query_stock_order_book) | **GET** /stock/market/{symbol}/orderbook | Query market order book
[**query_stock_order_list**](StockApi.md#query_stock_order_list) | **GET** /stock/orders | Query open order list
[**create_stock_order**](StockApi.md#create_stock_order) | **POST** /stock/orders | Create order
[**delete_all_stock_orders**](StockApi.md#delete_all_stock_orders) | **DELETE** /stock/orders | Cancel all open orders
[**query_stock_order_history**](StockApi.md#query_stock_order_history) | **GET** /stock/orders/history | Query historical order list
[**update_stock_order**](StockApi.md#update_stock_order) | **PUT** /stock/orders/{order_id} | Modify order
[**delete_stock_order**](StockApi.md#delete_stock_order) | **DELETE** /stock/orders/{order_id} | Cancel order
[**query_stock_positions**](StockApi.md#query_stock_positions) | **GET** /stock/positions | Query current position list
[**close_stock_position**](StockApi.md#close_stock_position) | **POST** /stock/positions/close | Close position
[**query_stock_transactions**](StockApi.md#query_stock_transactions) | **GET** /stock/transactions | Query transaction records
[**create_stock_transaction**](StockApi.md#create_stock_transaction) | **POST** /stock/transactions | Fund transfer
[**query_stock_exchanges**](StockApi.md#query_stock_exchanges) | **GET** /stock/exchanges | Query supported exchanges
[**query_stock_fee_rate**](StockApi.md#query_stock_fee_rate) | **GET** /stock/fee-rate | Query fee rates for Japanese and Korean stocks


# **query_stock_user_assets**
> UserAssetResp2 query_stock_user_assets(pnl_calc_type=pnl_calc_type, pnl_calc_price=pnl_calc_price)

Query user assets

Rate limit: 5 qps.

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
api_instance = gate_api.StockApi(api_client)
pnl_calc_type = 1 # int | PnL calculation cost type. Defaults to average cost price when omitted (1 = average cost price, 2 = diluted cost price) (optional)
pnl_calc_price = 1 # int | PnL calculation price type. Defaults to intraday price when omitted (1 = intraday price, 2 = latest extended-hours price) (optional)

try:
    # Query user assets
    api_response = api_instance.query_stock_user_assets(pnl_calc_type=pnl_calc_type, pnl_calc_price=pnl_calc_price)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling StockApi->query_stock_user_assets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pnl_calc_type** | **int**| PnL calculation cost type. Defaults to average cost price when omitted (1 &#x3D; average cost price, 2 &#x3D; diluted cost price) | [optional] 
 **pnl_calc_price** | **int**| PnL calculation price type. Defaults to intraday price when omitted (1 &#x3D; intraday price, 2 &#x3D; latest extended-hours price) | [optional] 

### Return type

[**UserAssetResp2**](UserAssetResp2.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request success |  -  |
**400** | Request failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_stock_symbols**
> Symbols2 query_stock_symbols(symbols=symbols, exchange=exchange, with_desc_i18n=with_desc_i18n, page=page, page_size=page_size)

Query symbol list

Rate limit: 5 qps.

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
api_instance = gate_api.StockApi(api_client)
symbols = 'AAPL,TSLA' # str | Symbol list, multiple separated by commas (optional)
exchange = 'us' # str | Exchange, supports us, hk, and kr (optional)
with_desc_i18n = true # bool | Whether to return multilingual symbol description (optional)
page = 1 # int | Page number, defaults to 1 (optional)
page_size = 100 # int | Page size, defaults to 10, max 500; server caps at 500 (optional)

try:
    # Query symbol list
    api_response = api_instance.query_stock_symbols(symbols=symbols, exchange=exchange, with_desc_i18n=with_desc_i18n, page=page, page_size=page_size)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling StockApi->query_stock_symbols: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbols** | **str**| Symbol list, multiple separated by commas | [optional] 
 **exchange** | **str**| Exchange, supports us, hk, and kr | [optional] 
 **with_desc_i18n** | **bool**| Whether to return multilingual symbol description | [optional] 
 **page** | **int**| Page number, defaults to 1 | [optional] 
 **page_size** | **int**| Page size, defaults to 10, max 500; server caps at 500 | [optional] 

### Return type

[**Symbols2**](Symbols2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request success |  -  |
**400** | Request failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_stock_symbol_detail**
> SymbolDetail query_stock_symbol_detail(symbols=symbols, exchange=exchange, page=page, page_size=page_size)

Query symbol details

Rate limit: 5 qps.

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
api_instance = gate_api.StockApi(api_client)
symbols = 'AAPL,TSLA' # str | Symbol list, multiple separated by commas (optional)
exchange = 'us' # str | Exchange, supports us, hk, and kr (optional)
page = 1 # int | Page number, defaults to 1 (optional)
page_size = 100 # int | Page size, defaults to 10, max 500; server caps at 500 (optional)

try:
    # Query symbol details
    api_response = api_instance.query_stock_symbol_detail(symbols=symbols, exchange=exchange, page=page, page_size=page_size)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling StockApi->query_stock_symbol_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbols** | **str**| Symbol list, multiple separated by commas | [optional] 
 **exchange** | **str**| Exchange, supports us, hk, and kr | [optional] 
 **page** | **int**| Page number, defaults to 1 | [optional] 
 **page_size** | **int**| Page size, defaults to 10, max 500; server caps at 500 | [optional] 

### Return type

[**SymbolDetail**](SymbolDetail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request success |  -  |
**400** | Request failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_stock_order_book**
> OrderBook2 query_stock_order_book(symbol)

Query market order book

Rate limit: 5 qps.

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
api_instance = gate_api.StockApi(api_client)
symbol = 'AAPL' # str | Symbol

try:
    # Query market order book
    api_response = api_instance.query_stock_order_book(symbol)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling StockApi->query_stock_order_book: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Symbol | 

### Return type

[**OrderBook2**](OrderBook2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request success |  -  |
**400** | Request failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_stock_order_list**
> OrderList2 query_stock_order_list(symbol=symbol)

Query open order list

Rate limit: 5 qps.

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
api_instance = gate_api.StockApi(api_client)
symbol = 'AAPL' # str | Symbol (optional)

try:
    # Query open order list
    api_response = api_instance.query_stock_order_list(symbol=symbol)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling StockApi->query_stock_order_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Symbol | [optional] 

### Return type

[**OrderList2**](OrderList2.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request success |  -  |
**400** | Request failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_stock_order**
> CreateOrder2 create_stock_order(trad_fi_spot_order_request)

Create order

Rate limit: 5 qps.

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
api_instance = gate_api.StockApi(api_client)
trad_fi_spot_order_request = gate_api.TradFiSpotOrderRequest() # TradFiSpotOrderRequest | 

try:
    # Create order
    api_response = api_instance.create_stock_order(trad_fi_spot_order_request)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling StockApi->create_stock_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trad_fi_spot_order_request** | [**TradFiSpotOrderRequest**](TradFiSpotOrderRequest.md)|  | 

### Return type

[**CreateOrder2**](CreateOrder2.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Order placed successfully |  -  |
**400** | Request failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_all_stock_orders**
> DeleteOrder delete_all_stock_orders()

Cancel all open orders

Rate limit: 5 qps.

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
api_instance = gate_api.StockApi(api_client)

try:
    # Cancel all open orders
    api_response = api_instance.delete_all_stock_orders()
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling StockApi->delete_all_stock_orders: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DeleteOrder**](DeleteOrder.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request success |  -  |
**400** | Request failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_stock_order_history**
> OrderHistoryList2 query_stock_order_history(symbol=symbol, order_ids=order_ids, begin_time=begin_time, end_time=end_time, side=side, page=page, page_size=page_size)

Query historical order list

Rate limit: 5 qps.

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
api_instance = gate_api.StockApi(api_client)
symbol = 'AAPL' # str | Symbol (optional)
order_ids = '123456,123457' # str | Order ID list, multiple separated by commas; max 20, each must be a positive integer (optional)
begin_time = 1769378400 # int | Start time (Unix timestamp, seconds). When both begin_time and end_time are provided, end_time must be >= begin_time, query range must not exceed 3 months. (optional)
end_time = 1769464800 # int | End time (Unix timestamp, seconds). When both begin_time and end_time are provided, end_time must be >= begin_time, query range must not exceed 3 months. (optional)
side = 2 # int | Side (1=sell, 2=buy) (optional)
page = 1 # int | Page number, defaults to 1 (optional)
page_size = 100 # int | Page size, defaults to 10, max 500; server caps at 500 (optional)

try:
    # Query historical order list
    api_response = api_instance.query_stock_order_history(symbol=symbol, order_ids=order_ids, begin_time=begin_time, end_time=end_time, side=side, page=page, page_size=page_size)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling StockApi->query_stock_order_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Symbol | [optional] 
 **order_ids** | **str**| Order ID list, multiple separated by commas; max 20, each must be a positive integer | [optional] 
 **begin_time** | **int**| Start time (Unix timestamp, seconds). When both begin_time and end_time are provided, end_time must be &gt;&#x3D; begin_time, query range must not exceed 3 months. | [optional] 
 **end_time** | **int**| End time (Unix timestamp, seconds). When both begin_time and end_time are provided, end_time must be &gt;&#x3D; begin_time, query range must not exceed 3 months. | [optional] 
 **side** | **int**| Side (1&#x3D;sell, 2&#x3D;buy) | [optional] 
 **page** | **int**| Page number, defaults to 1 | [optional] 
 **page_size** | **int**| Page size, defaults to 10, max 500; server caps at 500 | [optional] 

### Return type

[**OrderHistoryList2**](OrderHistoryList2.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request success |  -  |
**400** | Request failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_stock_order**
> UpdateOrder2 update_stock_order(order_id, trad_fi_spot_order_update_request)

Modify order

Rate limit: 5 qps.

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
api_instance = gate_api.StockApi(api_client)
order_id = 123456 # int | Order ID
trad_fi_spot_order_update_request = gate_api.TradFiSpotOrderUpdateRequest() # TradFiSpotOrderUpdateRequest | 

try:
    # Modify order
    api_response = api_instance.update_stock_order(order_id, trad_fi_spot_order_update_request)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling StockApi->update_stock_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **int**| Order ID | 
 **trad_fi_spot_order_update_request** | [**TradFiSpotOrderUpdateRequest**](TradFiSpotOrderUpdateRequest.md)|  | 

### Return type

[**UpdateOrder2**](UpdateOrder2.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request success |  -  |
**400** | Request failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_stock_order**
> DeleteOrder delete_stock_order(order_id)

Cancel order

Rate limit: 5 qps.

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
api_instance = gate_api.StockApi(api_client)
order_id = 123456 # int | Order ID

try:
    # Cancel order
    api_response = api_instance.delete_stock_order(order_id)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling StockApi->delete_stock_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **int**| Order ID | 

### Return type

[**DeleteOrder**](DeleteOrder.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request success |  -  |
**400** | Request failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_stock_positions**
> PositionList2 query_stock_positions(pnl_calc_type=pnl_calc_type, pnl_calc_price=pnl_calc_price, symbol=symbol, exchange=exchange)

Query current position list

Rate limit: 5 qps.

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
api_instance = gate_api.StockApi(api_client)
pnl_calc_type = 1 # int | PnL calculation cost type. Defaults to average cost price when omitted (1 = average cost price, 2 = diluted cost price) (optional)
pnl_calc_price = 1 # int | PnL calculation price type. Defaults to intraday price when omitted (1 = intraday price, 2 = latest extended-hours price) (optional)
symbol = 'AAPL' # str | Symbol (optional)
exchange = 'us' # str | Exchange, supports us, hk, and kr (optional)

try:
    # Query current position list
    api_response = api_instance.query_stock_positions(pnl_calc_type=pnl_calc_type, pnl_calc_price=pnl_calc_price, symbol=symbol, exchange=exchange)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling StockApi->query_stock_positions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pnl_calc_type** | **int**| PnL calculation cost type. Defaults to average cost price when omitted (1 &#x3D; average cost price, 2 &#x3D; diluted cost price) | [optional] 
 **pnl_calc_price** | **int**| PnL calculation price type. Defaults to intraday price when omitted (1 &#x3D; intraday price, 2 &#x3D; latest extended-hours price) | [optional] 
 **symbol** | **str**| Symbol | [optional] 
 **exchange** | **str**| Exchange, supports us, hk, and kr | [optional] 

### Return type

[**PositionList2**](PositionList2.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request success |  -  |
**400** | Request failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **close_stock_position**
> ClosePosition close_stock_position(trad_fi_spot_close_position_request)

Close position

Rate limit: 5 qps.

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
api_instance = gate_api.StockApi(api_client)
trad_fi_spot_close_position_request = gate_api.TradFiSpotClosePositionRequest() # TradFiSpotClosePositionRequest | 

try:
    # Close position
    api_response = api_instance.close_stock_position(trad_fi_spot_close_position_request)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling StockApi->close_stock_position: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trad_fi_spot_close_position_request** | [**TradFiSpotClosePositionRequest**](TradFiSpotClosePositionRequest.md)|  | 

### Return type

[**ClosePosition**](ClosePosition.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request success |  -  |
**400** | Request failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_stock_transactions**
> TransactionList2 query_stock_transactions(begin_time=begin_time, end_time=end_time, ref_id=ref_id, type=type, page=page, page_size=page_size)

Query transaction records

Rate limit: 5 qps.

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
api_instance = gate_api.StockApi(api_client)
begin_time = 1769378400 # int | Start time (Unix timestamp, seconds). When both begin_time and end_time are provided, end_time must be >= begin_time, query range must not exceed 3 months. (optional)
end_time = 1769464800 # int | End time (Unix timestamp, seconds). When both begin_time and end_time are provided, end_time must be >= begin_time, query range must not exceed 3 months. (optional)
ref_id = 'transfer-202607070001' # str | Business idempotent ID. When ref_id is provided, the server queries by ref_id, ignoring other parameters such as begin_time, end_time, type, page, page_size (optional)
type = 'deposit' # str | Transaction type (optional)
page = 1 # int | Page number, defaults to 1 (optional)
page_size = 100 # int | Page size, defaults to 10, max 500; server caps at 500 (optional)

try:
    # Query transaction records
    api_response = api_instance.query_stock_transactions(begin_time=begin_time, end_time=end_time, ref_id=ref_id, type=type, page=page, page_size=page_size)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling StockApi->query_stock_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **begin_time** | **int**| Start time (Unix timestamp, seconds). When both begin_time and end_time are provided, end_time must be &gt;&#x3D; begin_time, query range must not exceed 3 months. | [optional] 
 **end_time** | **int**| End time (Unix timestamp, seconds). When both begin_time and end_time are provided, end_time must be &gt;&#x3D; begin_time, query range must not exceed 3 months. | [optional] 
 **ref_id** | **str**| Business idempotent ID. When ref_id is provided, the server queries by ref_id, ignoring other parameters such as begin_time, end_time, type, page, page_size | [optional] 
 **type** | **str**| Transaction type | [optional] 
 **page** | **int**| Page number, defaults to 1 | [optional] 
 **page_size** | **int**| Page size, defaults to 10, max 500; server caps at 500 | [optional] 

### Return type

[**TransactionList2**](TransactionList2.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request success |  -  |
**400** | Request failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_stock_transaction**
> CreateTransaction2 create_stock_transaction(trad_fi_spot_transaction_request)

Fund transfer

Rate limit: 5 qps.

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
api_instance = gate_api.StockApi(api_client)
trad_fi_spot_transaction_request = gate_api.TradFiSpotTransactionRequest() # TradFiSpotTransactionRequest | 

try:
    # Fund transfer
    api_response = api_instance.create_stock_transaction(trad_fi_spot_transaction_request)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling StockApi->create_stock_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trad_fi_spot_transaction_request** | [**TradFiSpotTransactionRequest**](TradFiSpotTransactionRequest.md)|  | 

### Return type

[**CreateTransaction2**](CreateTransaction2.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request success |  -  |
**400** | Request failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_stock_exchanges**
> Exchanges query_stock_exchanges()

Query supported exchanges

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
api_instance = gate_api.StockApi(api_client)

try:
    # Query supported exchanges
    api_response = api_instance.query_stock_exchanges()
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling StockApi->query_stock_exchanges: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Exchanges**](Exchanges.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request success |  -  |
**400** | Request failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_stock_fee_rate**
> FeeRate query_stock_fee_rate()

Query fee rates for Japanese and Korean stocks

Query fee rates for Japanese and Korean stocks. Rate limit: 5 qps.

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
api_instance = gate_api.StockApi(api_client)

try:
    # Query fee rates for Japanese and Korean stocks
    api_response = api_instance.query_stock_fee_rate()
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling StockApi->query_stock_fee_rate: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**FeeRate**](FeeRate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request success |  -  |
**400** | Request failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

