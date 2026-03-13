# gate_api.TradFiApi

All URIs are relative to *https://api.gateio.ws/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**query_mt5_account_info**](TradFiApi.md#query_mt5_account_info) | **GET** /tradfi/users/mt5-account | Query MT5 account information
[**query_categories**](TradFiApi.md#query_categories) | **GET** /tradfi/symbols/categories | Query trading symbol categories
[**query_symbols**](TradFiApi.md#query_symbols) | **GET** /tradfi/symbols | Query trading symbol list
[**query_symbol_detail**](TradFiApi.md#query_symbol_detail) | **GET** /tradfi/symbols/detail | Query trading symbol details
[**query_symbol_kline**](TradFiApi.md#query_symbol_kline) | **GET** /tradfi/symbols/{symbol}/klines | Query trading symbol klines
[**query_symbol_ticker**](TradFiApi.md#query_symbol_ticker) | **GET** /tradfi/symbols/{symbol}/tickers | Query trading symbol ticker
[**create_trad_fi_user**](TradFiApi.md#create_trad_fi_user) | **POST** /tradfi/users | Create TradFi user
[**query_user_assets**](TradFiApi.md#query_user_assets) | **GET** /tradfi/users/assets | Query account assets
[**query_transaction**](TradFiApi.md#query_transaction) | **GET** /tradfi/transactions | Query Fund Transfer In/Out Records
[**create_transaction**](TradFiApi.md#create_transaction) | **POST** /tradfi/transactions | Fund Deposit and Withdrawal
[**query_order_list**](TradFiApi.md#query_order_list) | **GET** /tradfi/orders | Query active order list
[**create_trad_fi_order**](TradFiApi.md#create_trad_fi_order) | **POST** /tradfi/orders | Create an order
[**update_order**](TradFiApi.md#update_order) | **PUT** /tradfi/orders/{order_id} | Modify order
[**delete_order**](TradFiApi.md#delete_order) | **DELETE** /tradfi/orders/{order_id} | Cancel order
[**query_order_history_list**](TradFiApi.md#query_order_history_list) | **GET** /tradfi/orders/history | Query historical order list
[**query_position_list**](TradFiApi.md#query_position_list) | **GET** /tradfi/positions | Query active position list
[**update_position**](TradFiApi.md#update_position) | **PUT** /tradfi/positions/{position_id} | Modify position
[**close_position**](TradFiApi.md#close_position) | **POST** /tradfi/positions/{position_id}/close | Close position
[**query_position_history_list**](TradFiApi.md#query_position_history_list) | **GET** /tradfi/positions/history | Query historical position list


# **query_mt5_account_info**
> Mt5Account query_mt5_account_info()

Query MT5 account information

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
api_instance = gate_api.TradFiApi(api_client)

try:
    # Query MT5 account information
    api_response = api_instance.query_mt5_account_info()
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling TradFiApi->query_mt5_account_info: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Mt5Account**](Mt5Account.md)

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

# **query_categories**
> Categories query_categories()

Query trading symbol categories

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
api_instance = gate_api.TradFiApi(api_client)

try:
    # Query trading symbol categories
    api_response = api_instance.query_categories()
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling TradFiApi->query_categories: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Categories**](Categories.md)

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

# **query_symbols**
> Symbols query_symbols()

Query trading symbol list

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
api_instance = gate_api.TradFiApi(api_client)

try:
    # Query trading symbol list
    api_response = api_instance.query_symbols()
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling TradFiApi->query_symbols: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Symbols**](Symbols.md)

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

# **query_symbol_detail**
> ContractDetail query_symbol_detail(symbols)

Query trading symbol details

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
api_instance = gate_api.TradFiApi(api_client)
symbols = 'EURUSD,XAGUSD' # str | Trading symbol code list (comma-separated, max 10 symbols)

try:
    # Query trading symbol details
    api_response = api_instance.query_symbol_detail(symbols)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling TradFiApi->query_symbol_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbols** | **str**| Trading symbol code list (comma-separated, max 10 symbols) | 

### Return type

[**ContractDetail**](ContractDetail.md)

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

# **query_symbol_kline**
> Klines query_symbol_kline(symbol, kline_type, begin_time=begin_time, end_time=end_time, limit=limit)

Query trading symbol klines

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
api_instance = gate_api.TradFiApi(api_client)
symbol = 'EURUSD' # str | Trading symbol code
kline_type = '1m' # str | Kline type (time period)
begin_time = 1769378400 # int | Start time (Unix timestamp in seconds) (optional)
end_time = 1769464800 # int | End time (Unix timestamp in seconds) (optional)
limit = 100 # int | Kline limit (max 500, error if exceeded) (optional)

try:
    # Query trading symbol klines
    api_response = api_instance.query_symbol_kline(symbol, kline_type, begin_time=begin_time, end_time=end_time, limit=limit)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling TradFiApi->query_symbol_kline: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Trading symbol code | 
 **kline_type** | **str**| Kline type (time period) | 
 **begin_time** | **int**| Start time (Unix timestamp in seconds) | [optional] 
 **end_time** | **int**| End time (Unix timestamp in seconds) | [optional] 
 **limit** | **int**| Kline limit (max 500, error if exceeded) | [optional] 

### Return type

[**Klines**](Klines.md)

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

# **query_symbol_ticker**
> Ticker2 query_symbol_ticker(symbol)

Query trading symbol ticker

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
api_instance = gate_api.TradFiApi(api_client)
symbol = 'EURUSD' # str | Trading symbol code

try:
    # Query trading symbol ticker
    api_response = api_instance.query_symbol_ticker(symbol)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling TradFiApi->query_symbol_ticker: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Trading symbol code | 

### Return type

[**Ticker2**](Ticker2.md)

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

# **create_trad_fi_user**
> CreateUserResp create_trad_fi_user()

Create TradFi user

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
api_instance = gate_api.TradFiApi(api_client)

try:
    # Create TradFi user
    api_response = api_instance.create_trad_fi_user()
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling TradFiApi->create_trad_fi_user: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CreateUserResp**](CreateUserResp.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Account opened successfully |  -  |
**400** | Request failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_user_assets**
> UserAssetResp query_user_assets()

Query account assets

Query account assets

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
api_instance = gate_api.TradFiApi(api_client)

try:
    # Query account assets
    api_response = api_instance.query_user_assets()
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling TradFiApi->query_user_assets: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UserAssetResp**](UserAssetResp.md)

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

# **query_transaction**
> TransactionList query_transaction(begin_time=begin_time, end_time=end_time, type=type, page=page, page_size=page_size)

Query Fund Transfer In/Out Records

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
api_instance = gate_api.TradFiApi(api_client)
begin_time = 1704067200 # int | Start Time (Second-level Timestamp) (optional)
end_time = 1706745599 # int | End Time (Second-level Timestamp) (optional)
type = 'withdraw' # str | Transaction Type (deposit - transfer in, withdraw - transfer out, dividend - dividend payment, fill_negative - cover negative balance) (optional)
page = 1 # int | page number (optional)
page_size = 20 # int | Number per page, default 10, maximum 50 (optional)

try:
    # Query Fund Transfer In/Out Records
    api_response = api_instance.query_transaction(begin_time=begin_time, end_time=end_time, type=type, page=page, page_size=page_size)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling TradFiApi->query_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **begin_time** | **int**| Start Time (Second-level Timestamp) | [optional] 
 **end_time** | **int**| End Time (Second-level Timestamp) | [optional] 
 **type** | **str**| Transaction Type (deposit - transfer in, withdraw - transfer out, dividend - dividend payment, fill_negative - cover negative balance) | [optional] 
 **page** | **int**| page number | [optional] 
 **page_size** | **int**| Number per page, default 10, maximum 50 | [optional] 

### Return type

[**TransactionList**](TransactionList.md)

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

# **create_transaction**
> CreateTransaction create_transaction(trad_fi_transaction_request)

Fund Deposit and Withdrawal

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
api_instance = gate_api.TradFiApi(api_client)
trad_fi_transaction_request = gate_api.TradFiTransactionRequest() # TradFiTransactionRequest | 

try:
    # Fund Deposit and Withdrawal
    api_response = api_instance.create_transaction(trad_fi_transaction_request)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling TradFiApi->create_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trad_fi_transaction_request** | [**TradFiTransactionRequest**](TradFiTransactionRequest.md)|  | 

### Return type

[**CreateTransaction**](CreateTransaction.md)

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

# **query_order_list**
> OrderList query_order_list()

Query active order list

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
api_instance = gate_api.TradFiApi(api_client)

try:
    # Query active order list
    api_response = api_instance.query_order_list()
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling TradFiApi->query_order_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**OrderList**](OrderList.md)

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

# **create_trad_fi_order**
> CreateOrder create_trad_fi_order(trad_fi_order_request)

Create an order

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
api_instance = gate_api.TradFiApi(api_client)
trad_fi_order_request = gate_api.TradFiOrderRequest() # TradFiOrderRequest | 

try:
    # Create an order
    api_response = api_instance.create_trad_fi_order(trad_fi_order_request)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling TradFiApi->create_trad_fi_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trad_fi_order_request** | [**TradFiOrderRequest**](TradFiOrderRequest.md)|  | 

### Return type

[**CreateOrder**](CreateOrder.md)

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

# **update_order**
> UpdateOrder update_order(order_id, trad_fi_order_update_request)

Modify order

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
api_instance = gate_api.TradFiApi(api_client)
order_id = 1223 # int | Order ID
trad_fi_order_update_request = gate_api.TradFiOrderUpdateRequest() # TradFiOrderUpdateRequest | 

try:
    # Modify order
    api_response = api_instance.update_order(order_id, trad_fi_order_update_request)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling TradFiApi->update_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **int**| Order ID | 
 **trad_fi_order_update_request** | [**TradFiOrderUpdateRequest**](TradFiOrderUpdateRequest.md)|  | 

### Return type

[**UpdateOrder**](UpdateOrder.md)

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

# **delete_order**
> object delete_order(order_id)

Cancel order

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
api_instance = gate_api.TradFiApi(api_client)
order_id = 1223 # int | Order ID

try:
    # Cancel order
    api_response = api_instance.delete_order(order_id)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling TradFiApi->delete_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **int**| Order ID | 

### Return type

**object**

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Deleted successfully |  -  |
**400** | Request failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_order_history_list**
> OrderHistoryList query_order_history_list(begin_time=begin_time, end_time=end_time, symbol=symbol, side=side)

Query historical order list

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
api_instance = gate_api.TradFiApi(api_client)
begin_time = 1769397000 # int | Start time (Unix timestamp in seconds), earliest query is one month ago (optional)
end_time = 1769398000 # int | End time (Unix timestamp in seconds) (optional)
symbol = 'USDCAD' # str | Currency pair (optional)
side = 2 # int | Order side (1=sell, 2=buy) (optional)

try:
    # Query historical order list
    api_response = api_instance.query_order_history_list(begin_time=begin_time, end_time=end_time, symbol=symbol, side=side)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling TradFiApi->query_order_history_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **begin_time** | **int**| Start time (Unix timestamp in seconds), earliest query is one month ago | [optional] 
 **end_time** | **int**| End time (Unix timestamp in seconds) | [optional] 
 **symbol** | **str**| Currency pair | [optional] 
 **side** | **int**| Order side (1&#x3D;sell, 2&#x3D;buy) | [optional] 

### Return type

[**OrderHistoryList**](OrderHistoryList.md)

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

# **query_position_list**
> PositionList query_position_list()

Query active position list

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
api_instance = gate_api.TradFiApi(api_client)

try:
    # Query active position list
    api_response = api_instance.query_position_list()
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling TradFiApi->query_position_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PositionList**](PositionList.md)

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

# **update_position**
> UpdatePosition update_position(position_id, trad_fi_position_update_request)

Modify position

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
api_instance = gate_api.TradFiApi(api_client)
position_id = 1223 # int | Position ID
trad_fi_position_update_request = gate_api.TradFiPositionUpdateRequest() # TradFiPositionUpdateRequest | 

try:
    # Modify position
    api_response = api_instance.update_position(position_id, trad_fi_position_update_request)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling TradFiApi->update_position: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **position_id** | **int**| Position ID | 
 **trad_fi_position_update_request** | [**TradFiPositionUpdateRequest**](TradFiPositionUpdateRequest.md)|  | 

### Return type

[**UpdatePosition**](UpdatePosition.md)

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

# **close_position**
> DeletePosition close_position(position_id, trad_fi_close_position_request)

Close position

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
api_instance = gate_api.TradFiApi(api_client)
position_id = 1223 # int | Position ID
trad_fi_close_position_request = gate_api.TradFiClosePositionRequest() # TradFiClosePositionRequest | 

try:
    # Close position
    api_response = api_instance.close_position(position_id, trad_fi_close_position_request)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling TradFiApi->close_position: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **position_id** | **int**| Position ID | 
 **trad_fi_close_position_request** | [**TradFiClosePositionRequest**](TradFiClosePositionRequest.md)|  | 

### Return type

[**DeletePosition**](DeletePosition.md)

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

# **query_position_history_list**
> PositionHistoryList query_position_history_list(begin_time=begin_time, end_time=end_time, symbol=symbol, position_dir=position_dir)

Query historical position list

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
api_instance = gate_api.TradFiApi(api_client)
begin_time = 56 # int | Start Time (Unix Timestamp, seconds). The earliest queryable time is one month ago (optional)
end_time = 56 # int | End time (timestamp in seconds) (optional)
symbol = 'symbol_example' # str | Trading symbol (e.g., EURUSD) (optional)
position_dir = 'position_dir_example' # str | Position direction (Long=long position, Short=short position) (optional)

try:
    # Query historical position list
    api_response = api_instance.query_position_history_list(begin_time=begin_time, end_time=end_time, symbol=symbol, position_dir=position_dir)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling TradFiApi->query_position_history_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **begin_time** | **int**| Start Time (Unix Timestamp, seconds). The earliest queryable time is one month ago | [optional] 
 **end_time** | **int**| End time (timestamp in seconds) | [optional] 
 **symbol** | **str**| Trading symbol (e.g., EURUSD) | [optional] 
 **position_dir** | **str**| Position direction (Long&#x3D;long position, Short&#x3D;short position) | [optional] 

### Return type

[**PositionHistoryList**](PositionHistoryList.md)

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

