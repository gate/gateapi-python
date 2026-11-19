# gate_api.StockOptionsApi

All URIs are relative to *https://api.gateio.ws/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**query_option_fee_rate**](StockOptionsApi.md#query_option_fee_rate) | **GET** /stock_options/fee-rate | Get option trading fee rates
[**query_option_symbols**](StockOptionsApi.md#query_option_symbols) | **GET** /stock_options/underlyings | List option underlyings
[**query_option_contracts**](StockOptionsApi.md#query_option_contracts) | **GET** /stock_options/contracts | List option contracts
[**query_option_expirations**](StockOptionsApi.md#query_option_expirations) | **GET** /stock_options/market/expirations | List option expiration dates
[**query_option_chain**](StockOptionsApi.md#query_option_chain) | **GET** /stock_options/market/chain | Get the option chain
[**query_option_order_book**](StockOptionsApi.md#query_option_order_book) | **GET** /stock_options/market/{symbol}/orderbook | Get the option order book
[**query_option_positions**](StockOptionsApi.md#query_option_positions) | **GET** /stock_options/positions | List current option positions
[**close_option_position**](StockOptionsApi.md#close_option_position) | **POST** /stock_options/positions/close | Close an option position
[**query_option_order_list**](StockOptionsApi.md#query_option_order_list) | **GET** /stock_options/orders | List current option orders
[**create_option_order**](StockOptionsApi.md#create_option_order) | **POST** /stock_options/orders | Create an option order
[**cancel_all_option_orders**](StockOptionsApi.md#cancel_all_option_orders) | **DELETE** /stock_options/orders | Cancel all option limit orders
[**query_option_order_detail**](StockOptionsApi.md#query_option_order_detail) | **GET** /stock_options/orders/{order_id} | Get option order details
[**update_option_order**](StockOptionsApi.md#update_option_order) | **PUT** /stock_options/orders/{order_id} | Amend an option limit order
[**cancel_option_order**](StockOptionsApi.md#cancel_option_order) | **DELETE** /stock_options/orders/{order_id} | Cancel an option limit order
[**query_option_order_history**](StockOptionsApi.md#query_option_order_history) | **GET** /stock_options/orders/history | List historical option orders


# **query_option_fee_rate**
> StockOptionConfigResponse query_option_fee_rate()

Get option trading fee rates

Query the fee configuration for options trading before placing an order. Returns the rates and applicable minimum and maximum fees for SEC, TAF, OCC, ORF and CAT charges.

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
api_instance = gate_api.StockOptionsApi(api_client)

try:
    # Get option trading fee rates
    api_response = api_instance.query_option_fee_rate()
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling StockOptionsApi->query_option_fee_rate: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**StockOptionConfigResponse**](StockOptionConfigResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Option trading fee configuration |  -  |
**400** | Request failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_option_symbols**
> StockOptionSymbolListResponse query_option_symbols(underlyings=underlyings)

List option underlyings

Query available option underlyings before looking up contracts, expiration dates and option chains. Returns underlying symbols, names, multilingual descriptions, icons, price precision and order quantity limits. `underlyings` accepts multiple comma-separated symbols; omit it to query all available underlyings.

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
api_instance = gate_api.StockOptionsApi(api_client)
underlyings = 'AAPL,TSLA' # str | Comma-separated option underlying symbols, for example AAPL,TSLA. Omit to query all available underlyings. (optional)

try:
    # List option underlyings
    api_response = api_instance.query_option_symbols(underlyings=underlyings)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling StockOptionsApi->query_option_symbols: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **underlyings** | **str**| Comma-separated option underlying symbols, for example AAPL,TSLA. Omit to query all available underlyings. | [optional] 

### Return type

[**StockOptionSymbolListResponse**](StockOptionSymbolListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Option underlying list |  -  |
**400** | Request failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_option_contracts**
> StockOptionContractListResponse query_option_contracts(underlying, exchange=exchange, expiration_date=expiration_date, option_type=option_type, page=page, page_size=page_size)

List option contracts

Query option contracts for an underlying, including contract symbols, strike prices, expiration dates and trading rules. `underlying` is required. Filter by expiration date and call or put type; only US market (`us`) contracts are currently available. Results are paginated in ascending contract symbol order, with total records, total pages and the current page. The default and maximum `page_size` are both 1000. Use price precision and minimum and maximum order quantities to check an order before submission.

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
api_instance = gate_api.StockOptionsApi(api_client)
underlying = 'AAPL' # str | Option underlying symbol, for example AAPL. This is one underlying symbol, not an option contract symbol.
exchange = 'us' # str | Trading market filter. Only US market (us) contracts are currently available. Omitted or empty values use us. - us: US market. (optional)
expiration_date = '2026-08-14' # date | Option expiration date in YYYY-MM-DD format. Omit to disable expiration date filtering. (optional)
option_type = gate_api.StockOptionOptionType() # StockOptionOptionType | Option type filter for the contract list. Omit for both types. - call: Call option. - put: Put option. (optional)
page = 1 # int | Page number, starting from 1. Defaults to 1 when omitted. (optional) (default to 1)
page_size = 1000 # int | Contracts per page. Defaults to 1000 when omitted; values above 1000 are capped at 1000. (optional) (default to 1000)

try:
    # List option contracts
    api_response = api_instance.query_option_contracts(underlying, exchange=exchange, expiration_date=expiration_date, option_type=option_type, page=page, page_size=page_size)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling StockOptionsApi->query_option_contracts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **underlying** | **str**| Option underlying symbol, for example AAPL. This is one underlying symbol, not an option contract symbol. | 
 **exchange** | **str**| Trading market filter. Only US market (us) contracts are currently available. Omitted or empty values use us. - us: US market. | [optional] 
 **expiration_date** | **date**| Option expiration date in YYYY-MM-DD format. Omit to disable expiration date filtering. | [optional] 
 **option_type** | [**StockOptionOptionType**](.md)| Option type filter for the contract list. Omit for both types. - call: Call option. - put: Put option. | [optional] 
 **page** | **int**| Page number, starting from 1. Defaults to 1 when omitted. | [optional] [default to 1]
 **page_size** | **int**| Contracts per page. Defaults to 1000 when omitted; values above 1000 are capped at 1000. | [optional] [default to 1000]

### Return type

[**StockOptionContractListResponse**](StockOptionContractListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Option contract list |  -  |
**400** | Request failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_option_expirations**
> StockOptionExpirationListResponse query_option_expirations(underlying)

List option expiration dates

Query expiration dates for an option underlying before selecting a contract expiration. `underlying` is required. Returns dates and their Unix timestamps; use the selected date to query the option chain.

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
api_instance = gate_api.StockOptionsApi(api_client)
underlying = 'AAPL' # str | Option underlying symbol, for example AAPL. This is one underlying symbol, not an option contract symbol.

try:
    # List option expiration dates
    api_response = api_instance.query_option_expirations(underlying)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling StockOptionsApi->query_option_expirations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **underlying** | **str**| Option underlying symbol, for example AAPL. This is one underlying symbol, not an option contract symbol. | 

### Return type

[**StockOptionExpirationListResponse**](StockOptionExpirationListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Option expiration date list |  -  |
**400** | Request failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_option_chain**
> StockOptionOptionChainResponse query_option_chain(underlying, expiration_date, option_type=option_type)

Get the option chain

Query option quotes at different strike prices for the same underlying and expiration date to compare call and put contracts. `underlying` and `expiration_date` are required. Set `option_type` to `call` or `put` to filter; omit it or use `all` for both types. Returns contract symbols, strike prices, bid and ask quotes, last prices, mark prices, implied volatility and Greeks.

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
api_instance = gate_api.StockOptionsApi(api_client)
underlying = 'AAPL' # str | Option underlying symbol, for example AAPL. This is one underlying symbol, not an option contract symbol.
expiration_date = '2026-08-14' # date | Required option expiration date in YYYY-MM-DD format, obtained from the expiration date list.
option_type = 'option_type_example' # str | Option type filter for the option chain. - call: Call options only. - put: Put options only. - all: Both types, equivalent to omitting this parameter. (optional)

try:
    # Get the option chain
    api_response = api_instance.query_option_chain(underlying, expiration_date, option_type=option_type)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling StockOptionsApi->query_option_chain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **underlying** | **str**| Option underlying symbol, for example AAPL. This is one underlying symbol, not an option contract symbol. | 
 **expiration_date** | **date**| Required option expiration date in YYYY-MM-DD format, obtained from the expiration date list. | 
 **option_type** | **str**| Option type filter for the option chain. - call: Call options only. - put: Put options only. - all: Both types, equivalent to omitting this parameter. | [optional] 

### Return type

[**StockOptionOptionChainResponse**](StockOptionOptionChainResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Option chain |  -  |
**400** | Request failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_option_order_book**
> StockOptionOrderBookResponse query_option_order_book(symbol)

Get the option order book

Query the best bid and ask for an option contract. `symbol` is the option contract symbol. Each of `bids` and `asks` contains at most one price level, without order quantities. A side without an available quote is an empty array. Both sides are empty arrays when the contract is not found.

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
api_instance = gate_api.StockOptionsApi(api_client)
symbol = 'AAPL260814P00130000' # str | Option contract symbol

try:
    # Get the option order book
    api_response = api_instance.query_option_order_book(symbol)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling StockOptionsApi->query_option_order_book: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Option contract symbol | 

### Return type

[**StockOptionOrderBookResponse**](StockOptionOrderBookResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Option order book |  -  |
**400** | Request failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_option_positions**
> StockOptionPositionListResponse query_option_positions(underlying=underlying, symbol=symbol, price_type=price_type)

List current option positions

Query the current user's option positions, market values and profit and loss. Filter by `underlying` or `symbol`. A specified `symbol` must identify an existing option contract; no position returns an empty list. `price_type` selects the price for market value, unrealized PnL and today's PnL: `latest` (default) uses the last traded price; `mark` uses the mark price. Aggregate `today_pnl` includes current positions and contracts fully closed today. Results are sorted by `open_time` descending, then `symbol` ascending.

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
api_instance = gate_api.StockOptionsApi(api_client)
underlying = 'AAPL' # str | Option underlying symbol, for example AAPL. Omit to disable underlying filtering. Current orders support only one underlying. (optional)
symbol = 'AAPL260814P00130000' # str | Full option contract symbol, for example AAPL260814P00130000. Omit to disable contract filtering. (optional)
price_type = gate_api.StockOptionPositionPnlPriceType() # StockOptionPositionPnlPriceType | Valuation price type for position market value, unrealized PnL, and daily PnL. Options: `latest` (last traded price) or `mark` (mark price). Defaults to `latest` when omitted or empty. (optional)

try:
    # List current option positions
    api_response = api_instance.query_option_positions(underlying=underlying, symbol=symbol, price_type=price_type)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling StockOptionsApi->query_option_positions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **underlying** | **str**| Option underlying symbol, for example AAPL. Omit to disable underlying filtering. Current orders support only one underlying. | [optional] 
 **symbol** | **str**| Full option contract symbol, for example AAPL260814P00130000. Omit to disable contract filtering. | [optional] 
 **price_type** | [**StockOptionPositionPnlPriceType**](.md)| Valuation price type for position market value, unrealized PnL, and daily PnL. Options: &#x60;latest&#x60; (last traded price) or &#x60;mark&#x60; (mark price). Defaults to &#x60;latest&#x60; when omitted or empty. | [optional] 

### Return type

[**StockOptionPositionListResponse**](StockOptionPositionListResponse.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Current option position list |  -  |
**400** | Request failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **close_option_position**
> StockOptionClosePositionResponse close_option_position(stock_option_close_position_request)

Close an option position

Submit a closing order for part or all of an option position. `symbol` and `quantity` are required. The positive quantity must not exceed the available position and must satisfy the contract's minimum, maximum and quantity increment rules. Omit `order_type` or pass an empty value for a `market` order. A `limit` order requires a positive `price`; a market order ignores `price`. The closing side is derived from the position and time in force is fixed to `day`. The response returns the closing `order_id`; query the order for its subsequent status.

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
api_instance = gate_api.StockOptionsApi(api_client)
stock_option_close_position_request = gate_api.StockOptionClosePositionRequest() # StockOptionClosePositionRequest | 

try:
    # Close an option position
    api_response = api_instance.close_option_position(stock_option_close_position_request)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling StockOptionsApi->close_option_position: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stock_option_close_position_request** | [**StockOptionClosePositionRequest**](StockOptionClosePositionRequest.md)|  | 

### Return type

[**StockOptionClosePositionResponse**](StockOptionClosePositionResponse.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Position closing response |  -  |
**400** | Request failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_option_order_list**
> StockOptionOrderListResponse query_option_order_list(underlying=underlying, symbol=symbol, side=side)

List current option orders

Query the current user's unfinished option orders, including open and partially filled orders. Filter by `underlying`, `symbol` or `side`. `underlying` accepts only one symbol, not a comma-separated list. `status` includes only 1 (new) and 2 (partially filled). Query order history for terminal orders. Matching orders are sorted by creation time `time_setup` descending. This endpoint has no pagination parameters.

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
api_instance = gate_api.StockOptionsApi(api_client)
underlying = 'AAPL' # str | Option underlying symbol, for example AAPL. Omit to disable underlying filtering. Current orders support only one underlying. (optional)
symbol = 'AAPL260814P00130000' # str | Full option contract symbol, for example AAPL260814P00130000. Omit to disable contract filtering. (optional)
side = gate_api.StockOptionOrderListSide() # StockOptionOrderListSide | Order side filter. Omit to query both sides. - 1: Sell orders only. - 2: Buy orders only. (optional)

try:
    # List current option orders
    api_response = api_instance.query_option_order_list(underlying=underlying, symbol=symbol, side=side)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling StockOptionsApi->query_option_order_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **underlying** | **str**| Option underlying symbol, for example AAPL. Omit to disable underlying filtering. Current orders support only one underlying. | [optional] 
 **symbol** | **str**| Full option contract symbol, for example AAPL260814P00130000. Omit to disable contract filtering. | [optional] 
 **side** | [**StockOptionOrderListSide**](.md)| Order side filter. Omit to query both sides. - 1: Sell orders only. - 2: Buy orders only. | [optional] 

### Return type

[**StockOptionOrderListResponse**](StockOptionOrderListResponse.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Current option order list |  -  |
**400** | Request failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_option_order**
> StockOptionPutOrderResponse create_option_order(stock_option_put_order_request)

Create an option order

Submit a buy or sell order for an option contract and return the order ID on success. `symbol`, `side`, `order_type`, `time_in_force` and `quantity` are required. `side` is 1 (sell) or 2 (buy). Limit orders require a positive `price` and support `day` or `gtc`. Market orders ignore `price` and support only `day`. Quantity is a positive decimal string within the contract's minimum and maximum order quantities. Sell orders require sufficient available long positions. `client_order_id` is optional and is generated automatically when omitted or whitespace-only. Query current orders or order details to track the returned order ID.

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
api_instance = gate_api.StockOptionsApi(api_client)
stock_option_put_order_request = gate_api.StockOptionPutOrderRequest() # StockOptionPutOrderRequest | 

try:
    # Create an option order
    api_response = api_instance.create_option_order(stock_option_put_order_request)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling StockOptionsApi->create_option_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stock_option_put_order_request** | [**StockOptionPutOrderRequest**](StockOptionPutOrderRequest.md)|  | 

### Return type

[**StockOptionPutOrderResponse**](StockOptionPutOrderResponse.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Order creation response |  -  |
**400** | Request failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_all_option_orders**
> StockOptionCancelAllOrdersResponse cancel_all_option_orders(stock_option_cancel_all_orders_request=stock_option_cancel_all_orders_request)

Cancel all option limit orders

Cancel all or a filtered set of the current user's option limit orders. The request body may be omitted or an empty object. Without filters, all limit orders are cancelled. Filter by `underlying`, `symbol` or `side`. `side` supports 1 (sell) and 2 (buy); omit it to include both sides. The response reports the cancellation request result. Query the orders to confirm their subsequent status.

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
api_instance = gate_api.StockOptionsApi(api_client)
stock_option_cancel_all_orders_request = gate_api.StockOptionCancelAllOrdersRequest() # StockOptionCancelAllOrdersRequest |  (optional)

try:
    # Cancel all option limit orders
    api_response = api_instance.cancel_all_option_orders(stock_option_cancel_all_orders_request=stock_option_cancel_all_orders_request)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling StockOptionsApi->cancel_all_option_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stock_option_cancel_all_orders_request** | [**StockOptionCancelAllOrdersRequest**](StockOptionCancelAllOrdersRequest.md)|  | [optional] 

### Return type

[**StockOptionCancelAllOrdersResponse**](StockOptionCancelAllOrdersResponse.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Bulk order cancellation response |  -  |
**400** | Request failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_option_order_detail**
> StockOptionOrderDetailResponse query_option_order_detail(order_id)

Get option order details

Query one of the current user's orders by ID to track its status, filled quantity and average fill price. `order_id` is required and must be a positive integer represented as a string. Both current and finished orders can be queried, without filtering by terminal status. Returns price, quantity, filled quantity, status description, average fill price, fees and timestamps.

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
api_instance = gate_api.StockOptionsApi(api_client)
order_id = '8000000001' # str | Option order ID as a positive integer string, obtained from order submission or query results.

try:
    # Get option order details
    api_response = api_instance.query_option_order_detail(order_id)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling StockOptionsApi->query_option_order_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| Option order ID as a positive integer string, obtained from order submission or query results. | 

### Return type

[**StockOptionOrderDetailResponse**](StockOptionOrderDetailResponse.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Option order details |  -  |
**400** | Request failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_option_order**
> StockOptionUpdateOrderResponse update_option_order(order_id, stock_option_update_order_request)

Amend an option limit order

Update the price and total quantity of one of the current user's option limit orders. The path `order_id` and body `price` and `quantity` are required. Market orders cannot be amended. `quantity` is the new total order quantity, not the remaining unfilled quantity, and must be at least `filled_quantity`. Amending a sell order also requires sufficient available positions for the new unfilled quantity. Returns the order ID; query the order for its subsequent status.

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
api_instance = gate_api.StockOptionsApi(api_client)
order_id = '72057594037983901' # str | Option order ID as a positive integer string, obtained from order submission or query results.
stock_option_update_order_request = gate_api.StockOptionUpdateOrderRequest() # StockOptionUpdateOrderRequest | 

try:
    # Amend an option limit order
    api_response = api_instance.update_option_order(order_id, stock_option_update_order_request)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling StockOptionsApi->update_option_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| Option order ID as a positive integer string, obtained from order submission or query results. | 
 **stock_option_update_order_request** | [**StockOptionUpdateOrderRequest**](StockOptionUpdateOrderRequest.md)|  | 

### Return type

[**StockOptionUpdateOrderResponse**](StockOptionUpdateOrderResponse.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Order amendment response |  -  |
**400** | Request failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_option_order**
> StockOptionCancelOrderResponse cancel_option_order(order_id)

Cancel an option limit order

Cancel one of the current user's option limit orders by ID. `order_id` is required. Only limit orders can be cancelled; already filled quantities are unaffected. Returns the order ID. Query order details or order history for the final status.

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
api_instance = gate_api.StockOptionsApi(api_client)
order_id = '72057594037983901' # str | Option order ID as a positive integer string, obtained from order submission or query results.

try:
    # Cancel an option limit order
    api_response = api_instance.cancel_option_order(order_id)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling StockOptionsApi->cancel_option_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| Option order ID as a positive integer string, obtained from order submission or query results. | 

### Return type

[**StockOptionCancelOrderResponse**](StockOptionCancelOrderResponse.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Order cancellation response |  -  |
**400** | Request failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_option_order_history**
> StockOptionOrderHistoryResponse query_option_order_history(underlying=underlying, symbol=symbol, begin_time=begin_time, end_time=end_time, side=side, page=page, page_size=page_size)

List historical option orders

Query the current user's finished option orders with pagination to check orders, fills and fees. `status` includes only 3 (filled), 4 (cancelled) and 5 (rejected). Filter by underlying, contract, side or order creation time. `begin_time` and `end_time` are Unix timestamps in seconds; when both are provided, the start must not be later than the end. Returns total records, total pages and the current page. The default and maximum `page_size` are both 100.

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
api_instance = gate_api.StockOptionsApi(api_client)
underlying = 'AAPL' # str | Option underlying symbol, for example AAPL. Omit to disable underlying filtering. Current orders support only one underlying. (optional)
symbol = 'AAPL260814P00130000' # str | Full option contract symbol, for example AAPL260814P00130000. Omit to disable contract filtering. (optional)
begin_time = 56 # int | Order creation time filter start, as a Unix timestamp in seconds. Omit for no lower bound; must not exceed end_time when both are provided. (optional)
end_time = 56 # int | Order creation time filter end, as a Unix timestamp in seconds. Omit for no upper bound; must not precede begin_time when both are provided. (optional)
side = gate_api.StockOptionOrderListSide() # StockOptionOrderListSide | Order side filter. Omit to query both sides. - 1: Sell orders only. - 2: Buy orders only. (optional)
page = 1 # int | Page number, starting from 1. Defaults to 1 when omitted. (optional) (default to 1)
page_size = 100 # int | Number of items per page, up to 100. Defaults to 100 when omitted; values above 100 are capped at 100. (optional) (default to 100)

try:
    # List historical option orders
    api_response = api_instance.query_option_order_history(underlying=underlying, symbol=symbol, begin_time=begin_time, end_time=end_time, side=side, page=page, page_size=page_size)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling StockOptionsApi->query_option_order_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **underlying** | **str**| Option underlying symbol, for example AAPL. Omit to disable underlying filtering. Current orders support only one underlying. | [optional] 
 **symbol** | **str**| Full option contract symbol, for example AAPL260814P00130000. Omit to disable contract filtering. | [optional] 
 **begin_time** | **int**| Order creation time filter start, as a Unix timestamp in seconds. Omit for no lower bound; must not exceed end_time when both are provided. | [optional] 
 **end_time** | **int**| Order creation time filter end, as a Unix timestamp in seconds. Omit for no upper bound; must not precede begin_time when both are provided. | [optional] 
 **side** | [**StockOptionOrderListSide**](.md)| Order side filter. Omit to query both sides. - 1: Sell orders only. - 2: Buy orders only. | [optional] 
 **page** | **int**| Page number, starting from 1. Defaults to 1 when omitted. | [optional] [default to 1]
 **page_size** | **int**| Number of items per page, up to 100. Defaults to 100 when omitted; values above 100 are capped at 100. | [optional] [default to 100]

### Return type

[**StockOptionOrderHistoryResponse**](StockOptionOrderHistoryResponse.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Historical option order list |  -  |
**400** | Request failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

