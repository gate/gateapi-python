# gate_api.CrossExApi

All URIs are relative to *https://api.gateio.ws/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_crossex_rule_symbols**](CrossExApi.md#list_crossex_rule_symbols) | **GET** /crossex/rule/symbols | Query symbol information
[**list_crossex_rule_risk_limits**](CrossExApi.md#list_crossex_rule_risk_limits) | **GET** /crossex/rule/risk_limits | Query risk limit information
[**list_crossex_transfer_coins**](CrossExApi.md#list_crossex_transfer_coins) | **GET** /crossex/transfers/coin | Query supported transfer currencies
[**list_crossex_transfers**](CrossExApi.md#list_crossex_transfers) | **GET** /crossex/transfers | Query Fund Transfer History
[**create_crossex_transfer**](CrossExApi.md#create_crossex_transfer) | **POST** /crossex/transfers | Fund Transfer
[**create_crossex_order**](CrossExApi.md#create_crossex_order) | **POST** /crossex/orders | Create order
[**cancel_batch_crossex_orders**](CrossExApi.md#cancel_batch_crossex_orders) | **POST** /crossex/batch_cancel_orders | Batch cancel orders
[**get_crossex_order**](CrossExApi.md#get_crossex_order) | **GET** /crossex/orders/{order_id} | Query order details
[**update_crossex_order**](CrossExApi.md#update_crossex_order) | **PUT** /crossex/orders/{order_id} | Modify Order
[**cancel_crossex_order**](CrossExApi.md#cancel_crossex_order) | **DELETE** /crossex/orders/{order_id} | Cancel Order
[**create_crossex_convert_quote**](CrossExApi.md#create_crossex_convert_quote) | **POST** /crossex/convert/quote | Flash Swap Inquiry
[**create_crossex_convert_order**](CrossExApi.md#create_crossex_convert_order) | **POST** /crossex/convert/orders | Flash Swap Transaction
[**get_crossex_account**](CrossExApi.md#get_crossex_account) | **GET** /crossex/accounts | Query Account Assets
[**update_crossex_account**](CrossExApi.md#update_crossex_account) | **PUT** /crossex/accounts | Modify Account Contract Position Mode and Account Mode
[**get_crossex_positions_leverage**](CrossExApi.md#get_crossex_positions_leverage) | **GET** /crossex/positions/leverage | Query Contract Trading Pair Leverage Multiplier
[**update_crossex_positions_leverage**](CrossExApi.md#update_crossex_positions_leverage) | **POST** /crossex/positions/leverage | Modify Contract Trading Pair Leverage Multiplier
[**get_crossex_margin_positions_leverage**](CrossExApi.md#get_crossex_margin_positions_leverage) | **GET** /crossex/margin_positions/leverage | Query Leveraged Trading Pair Leverage Multiplier
[**update_crossex_margin_positions_leverage**](CrossExApi.md#update_crossex_margin_positions_leverage) | **POST** /crossex/margin_positions/leverage | Modify Leveraged Trading Pair Leverage Multiplier
[**close_crossex_position**](CrossExApi.md#close_crossex_position) | **POST** /crossex/position | Full Close Position
[**get_crossex_positions_margin_mode**](CrossExApi.md#get_crossex_positions_margin_mode) | **GET** /crossex/positions/margin_mode | Get futures position margin mode
[**update_crossex_positions_margin_mode**](CrossExApi.md#update_crossex_positions_margin_mode) | **POST** /crossex/positions/margin_mode | Update futures position margin mode
[**update_crossex_positions_margin**](CrossExApi.md#update_crossex_positions_margin) | **POST** /crossex/positions/margin | Increase or decrease isolated margin
[**get_crossex_interest_rate**](CrossExApi.md#get_crossex_interest_rate) | **GET** /crossex/interest_rate | Query margin asset interest rates
[**get_crossex_fee**](CrossExApi.md#get_crossex_fee) | **GET** /crossex/fee | Query User Fee Rates
[**list_crossex_positions**](CrossExApi.md#list_crossex_positions) | **GET** /crossex/positions | Query Contract Positions
[**list_crossex_margin_positions**](CrossExApi.md#list_crossex_margin_positions) | **GET** /crossex/margin_positions | Query Leveraged Positions
[**list_crossex_adl_rank**](CrossExApi.md#list_crossex_adl_rank) | **GET** /crossex/adl_rank | Query ADL Position Reduction Ranking
[**list_crossex_open_orders**](CrossExApi.md#list_crossex_open_orders) | **GET** /crossex/open_orders | Query All Current Open Orders
[**list_crossex_history_orders**](CrossExApi.md#list_crossex_history_orders) | **GET** /crossex/history_orders | Query order history
[**list_crossex_history_positions**](CrossExApi.md#list_crossex_history_positions) | **GET** /crossex/history_positions | Query Contract Position History
[**list_crossex_history_margin_positions**](CrossExApi.md#list_crossex_history_margin_positions) | **GET** /crossex/history_margin_positions | Query Leveraged Position History
[**list_crossex_history_margin_interests**](CrossExApi.md#list_crossex_history_margin_interests) | **GET** /crossex/history_margin_interests | Query Leveraged Interest Deduction History
[**list_crossex_history_trades**](CrossExApi.md#list_crossex_history_trades) | **GET** /crossex/history_trades | Query filled history
[**list_crossex_account_book**](CrossExApi.md#list_crossex_account_book) | **GET** /crossex/account_book | Query Account Asset Change History
[**list_crossex_coin_discount_rate**](CrossExApi.md#list_crossex_coin_discount_rate) | **GET** /crossex/coin_discount_rate | Query Currency Discount Rate
[**list_crossex_market_tickers**](CrossExApi.md#list_crossex_market_tickers) | **GET** /crossex/market/tickers | Get exchange tickers
[**list_crossex_market_funding_info**](CrossExApi.md#list_crossex_market_funding_info) | **GET** /crossex/market/funding_info | Get exchange futures funding rate information


# **list_crossex_rule_symbols**
> list[Symbol] list_crossex_rule_symbols(symbols=symbols)

Query symbol information

Query Trading Pair Information

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
api_instance = gate_api.CrossExApi(api_client)
symbols = 'symbols_example' # str | List of trading pairs, comma-separated. Example: BINANCE_FUTURE_ADA_USDT,OKX_FUTURE_ADA_USDT (optional)

try:
    # Query symbol information
    api_response = api_instance.list_crossex_rule_symbols(symbols=symbols)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling CrossExApi->list_crossex_rule_symbols: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbols** | **str**| List of trading pairs, comma-separated. Example: BINANCE_FUTURE_ADA_USDT,OKX_FUTURE_ADA_USDT | [optional] 

### Return type

[**list[Symbol]**](Symbol.md)

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

# **list_crossex_rule_risk_limits**
> list[CrossexRiskLimit] list_crossex_rule_risk_limits(symbols)

Query risk limit information

Query risk limit information for futures/margin trading pairs

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
api_instance = gate_api.CrossExApi(api_client)
symbols = 'BINANCE_FUTURE_AAVE_USDT' # str | Trading Pair List, multiple separated by commas Example values: BINANCE_FUTURE_ADA_USDT,GATE_MARGIN_ADA_USDT

try:
    # Query risk limit information
    api_response = api_instance.list_crossex_rule_risk_limits(symbols)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling CrossExApi->list_crossex_rule_risk_limits: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbols** | **str**| Trading Pair List, multiple separated by commas Example values: BINANCE_FUTURE_ADA_USDT,GATE_MARGIN_ADA_USDT | 

### Return type

[**list[CrossexRiskLimit]**](CrossexRiskLimit.md)

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

# **list_crossex_transfer_coins**
> list[CrossexTransferCoin] list_crossex_transfer_coins(coin=coin)

Query supported transfer currencies

`est_fee`: Estimated fee. When a fund transfer involves an on-chain withdrawal, the exchange charges this fee. This value is for reference only; the actual fee charged by the exchange applies

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
api_instance = gate_api.CrossExApi(api_client)
coin = 'BTC' # str | Query by specified currency name (optional)

try:
    # Query supported transfer currencies
    api_response = api_instance.list_crossex_transfer_coins(coin=coin)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling CrossExApi->list_crossex_transfer_coins: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coin** | **str**| Query by specified currency name | [optional] 

### Return type

[**list[CrossexTransferCoin]**](CrossexTransferCoin.md)

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

# **list_crossex_transfers**
> list[CrossexTransferRecord] list_crossex_transfers(coin=coin, order_id=order_id, _from=_from, to=to, page=page, limit=limit)

Query Fund Transfer History

Rate Limit: 200 requests per 10 seconds

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
api_instance = gate_api.CrossExApi(api_client)
coin = 'USDT, BTC, ETH' # str | Query by specified currency name (optional)
order_id = '38083797492939266' # str | Supports querying by the order ID returned when creating an order (tx_id), as well as a user-defined custom ID specified at creation (text) (optional)
_from = 1750681141933 # int | Start timestamp for the query (optional)
to = 1750681141933 # int | End timestamp for the query, defaults to current time if not specified (optional)
page = 1 # int | Page number (optional)
limit = 100 # int | Maximum number returned by list, max 1000 (optional)

try:
    # Query Fund Transfer History
    api_response = api_instance.list_crossex_transfers(coin=coin, order_id=order_id, _from=_from, to=to, page=page, limit=limit)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling CrossExApi->list_crossex_transfers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coin** | **str**| Query by specified currency name | [optional] 
 **order_id** | **str**| Supports querying by the order ID returned when creating an order (tx_id), as well as a user-defined custom ID specified at creation (text) | [optional] 
 **_from** | **int**| Start timestamp for the query | [optional] 
 **to** | **int**| End timestamp for the query, defaults to current time if not specified | [optional] 
 **page** | **int**| Page number | [optional] 
 **limit** | **int**| Maximum number returned by list, max 1000 | [optional] 

### Return type

[**list[CrossexTransferRecord]**](CrossexTransferRecord.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project-Id-Version: GateApiTools 1.0.0 Report-Msgid-Bugs-To: EMAIL@ADDRESS POT-Creation-Date: 2025-11-12 18:14+0800 PO-Revision-Date: 2019-01-02 17:30+0800 Last-Translator: FULL NAME &lt;EMAIL@ADDRESS&gt; Language: en Language-Team: en &lt;L@li.org&gt; Plural-Forms: nplurals&#x3D;2; plural&#x3D;(n !&#x3D;1) MIME-Version: 1.0 Content-Type: text/plain; charset&#x3D;utf-8 Content-Transfer-Encoding: 8bit Generated-By: Babel 2.8.0  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_crossex_transfer**
> CrossexTransferResponse create_crossex_transfer(crossex_transfer_request=crossex_transfer_request)

Fund Transfer

Rate limit: 10 requests per 10 seconds - In cross-exchange mode, when transferring USDT, either `from` or `to` must be `SPOT`, and the other side must be `CROSSEX`.   If `CROSSEX_${exchange_type}` (e.g. `CROSSEX_GATE`) is provided, it will be automatically treated as `CROSSEX`. - In isolated exchange mode, when transferring USDT, either `from` or `to` must be `CROSSEX_${exchange_type}`, and the other side must be `SPOT` or `CROSSEX_${exchange_type}`.   If `CROSSEX` is provided, it will be automatically treated as `CROSSEX_GATE`. - When transferring non-USDT assets to or from CrossEx, neither `from` nor `to` can be `CROSSEX`; `CROSSEX_${exchange_type}` must be explicitly specified. - When transferring non-USDT assets, transfers between `CROSSEX_{exchange_type}` accounts are supported, for example: from = `CROSSEX_BINANCE`, to = `CROSSEX_GATE` - When either side of the transfer is `CROSSEX_KRAKEN`, only USDT is supported for now. - When either side of the transfer is `CROSSEX_HYPERLIQUID`, the other side must be `SPOT`, and only USDC is supported.

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
api_instance = gate_api.CrossExApi(api_client)
crossex_transfer_request = gate_api.CrossexTransferRequest() # CrossexTransferRequest |  (optional)

try:
    # Fund Transfer
    api_response = api_instance.create_crossex_transfer(crossex_transfer_request=crossex_transfer_request)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling CrossExApi->create_crossex_transfer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crossex_transfer_request** | [**CrossexTransferRequest**](CrossexTransferRequest.md)|  | [optional] 

### Return type

[**CrossexTransferResponse**](CrossexTransferResponse.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project-Id-Version: GateApiTools 1.0.0 Report-Msgid-Bugs-To: EMAIL@ADDRESS POT-Creation-Date: 2025-11-12 18:14+0800 PO-Revision-Date: 2019-01-02 17:30+0800 Last-Translator: FULL NAME &lt;EMAIL@ADDRESS&gt; Language: en Language-Team: en &lt;L@li.org&gt; Plural-Forms: nplurals&#x3D;2; plural&#x3D;(n !&#x3D;1) MIME-Version: 1.0 Content-Type: text/plain; charset&#x3D;utf-8 Content-Transfer-Encoding: 8bit Generated-By: Babel 2.8.0  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_crossex_order**
> CrossexOrderActionResponse create_crossex_order(crossex_order_request=crossex_order_request)

Create order

Rate Limit: 100 requests per 10 seconds, maximum 1,000 open orders per user

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
api_instance = gate_api.CrossExApi(api_client)
crossex_order_request = gate_api.CrossexOrderRequest() # CrossexOrderRequest |  (optional)

try:
    # Create order
    api_response = api_instance.create_crossex_order(crossex_order_request=crossex_order_request)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling CrossExApi->create_crossex_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crossex_order_request** | [**CrossexOrderRequest**](CrossexOrderRequest.md)|  | [optional] 

### Return type

[**CrossexOrderActionResponse**](CrossexOrderActionResponse.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project-Id-Version: GateApiTools 1.0.0 Report-Msgid-Bugs-To: EMAIL@ADDRESS POT-Creation-Date: 2025-11-12 18:14+0800 PO-Revision-Date: 2019-01-02 17:30+0800 Last-Translator: FULL NAME &lt;EMAIL@ADDRESS&gt; Language: en Language-Team: en &lt;L@li.org&gt; Plural-Forms: nplurals&#x3D;2; plural&#x3D;(n !&#x3D;1) MIME-Version: 1.0 Content-Type: text/plain; charset&#x3D;utf-8 Content-Transfer-Encoding: 8bit Generated-By: Babel 2.8.0  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_batch_crossex_orders**
> list[CrossexBatchCancelOrderResponse] cancel_batch_crossex_orders(crossex_batch_cancel_order_request)

Batch cancel orders

Cancel multiple specified orders. Either order_id or text is required; if both are provided, order_id takes precedence. Rate limit: 100 requests per 10 seconds

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
api_instance = gate_api.CrossExApi(api_client)
crossex_batch_cancel_order_request = [gate_api.CrossexBatchCancelOrderRequest()] # list[CrossexBatchCancelOrderRequest] | 

try:
    # Batch cancel orders
    api_response = api_instance.cancel_batch_crossex_orders(crossex_batch_cancel_order_request)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling CrossExApi->cancel_batch_crossex_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crossex_batch_cancel_order_request** | [**list[CrossexBatchCancelOrderRequest]**](CrossexBatchCancelOrderRequest.md)|  | 

### Return type

[**list[CrossexBatchCancelOrderResponse]**](CrossexBatchCancelOrderResponse.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Batch order cancellation request results |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_crossex_order**
> CrossexOrder get_crossex_order(order_id)

Query order details

Rate Limit: 200 requests per 10 seconds

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
api_instance = gate_api.CrossExApi(api_client)
order_id = '2048522992198912' # str | 1. Supports querying order IDs returned when creating orders 2. Supports custom IDs specified by users when creating orders (i.e., the text field)

try:
    # Query order details
    api_response = api_instance.get_crossex_order(order_id)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling CrossExApi->get_crossex_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| 1. Supports querying order IDs returned when creating orders 2. Supports custom IDs specified by users when creating orders (i.e., the text field) | 

### Return type

[**CrossexOrder**](CrossexOrder.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project-Id-Version: GateApiTools 1.0.0 Report-Msgid-Bugs-To: EMAIL@ADDRESS POT-Creation-Date: 2025-11-12 18:14+0800 PO-Revision-Date: 2019-01-02 17:30+0800 Last-Translator: FULL NAME &lt;EMAIL@ADDRESS&gt; Language: en Language-Team: en &lt;L@li.org&gt; Plural-Forms: nplurals&#x3D;2; plural&#x3D;(n !&#x3D;1) MIME-Version: 1.0 Content-Type: text/plain; charset&#x3D;utf-8 Content-Transfer-Encoding: 8bit Generated-By: Babel 2.8.0  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_crossex_order**
> CrossexOrderActionResponse update_crossex_order(order_id, crossex_order_update_request=crossex_order_update_request)

Modify Order

Rate Limit: 100 requests per 10 seconds

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
api_instance = gate_api.CrossExApi(api_client)
order_id = 'order_id_example' # str | Support Order ID or Text for Modify Order
crossex_order_update_request = gate_api.CrossexOrderUpdateRequest() # CrossexOrderUpdateRequest |  (optional)

try:
    # Modify Order
    api_response = api_instance.update_crossex_order(order_id, crossex_order_update_request=crossex_order_update_request)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling CrossExApi->update_crossex_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| Support Order ID or Text for Modify Order | 
 **crossex_order_update_request** | [**CrossexOrderUpdateRequest**](CrossexOrderUpdateRequest.md)|  | [optional] 

### Return type

[**CrossexOrderActionResponse**](CrossexOrderActionResponse.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project-Id-Version: GateApiTools 1.0.0 Report-Msgid-Bugs-To: EMAIL@ADDRESS POT-Creation-Date: 2025-11-12 18:14+0800 PO-Revision-Date: 2019-01-02 17:30+0800 Last-Translator: FULL NAME &lt;EMAIL@ADDRESS&gt; Language: en Language-Team: en &lt;L@li.org&gt; Plural-Forms: nplurals&#x3D;2; plural&#x3D;(n !&#x3D;1) MIME-Version: 1.0 Content-Type: text/plain; charset&#x3D;utf-8 Content-Transfer-Encoding: 8bit Generated-By: Babel 2.8.0  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_crossex_order**
> CrossexOrderActionResponse cancel_crossex_order(order_id)

Cancel Order

Rate Limit: 100 requests per 10 seconds

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
api_instance = gate_api.CrossExApi(api_client)
order_id = 'order_id_example' # str | Support Order ID or Text for Cancel Order

try:
    # Cancel Order
    api_response = api_instance.cancel_crossex_order(order_id)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling CrossExApi->cancel_crossex_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| Support Order ID or Text for Cancel Order | 

### Return type

[**CrossexOrderActionResponse**](CrossexOrderActionResponse.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project-Id-Version: GateApiTools 1.0.0 Report-Msgid-Bugs-To: EMAIL@ADDRESS POT-Creation-Date: 2025-11-12 18:14+0800 PO-Revision-Date: 2019-01-02 17:30+0800 Last-Translator: FULL NAME &lt;EMAIL@ADDRESS&gt; Language: en Language-Team: en &lt;L@li.org&gt; Plural-Forms: nplurals&#x3D;2; plural&#x3D;(n !&#x3D;1) MIME-Version: 1.0 Content-Type: text/plain; charset&#x3D;utf-8 Content-Transfer-Encoding: 8bit Generated-By: Babel 2.8.0  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_crossex_convert_quote**
> CrossexConvertQuoteResponse create_crossex_convert_quote(crossex_convert_quote_request=crossex_convert_quote_request)

Flash Swap Inquiry

Rate limit: 100 requests per day For HYPERLIQUID, swaps between `HYPERLIQUID_USDC` and `CROSSEX_USDT` are supported. Flash Swap in isolated exchange mode is not currently supported for HYPERLIQUID. For KRAKEN, only conversion from `KRAKEN_USD` to `CROSSEX_USDT` is supported. Flash Swap in isolated exchange mode is not currently supported for KRAKEN.

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
api_instance = gate_api.CrossExApi(api_client)
crossex_convert_quote_request = gate_api.CrossexConvertQuoteRequest() # CrossexConvertQuoteRequest |  (optional)

try:
    # Flash Swap Inquiry
    api_response = api_instance.create_crossex_convert_quote(crossex_convert_quote_request=crossex_convert_quote_request)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling CrossExApi->create_crossex_convert_quote: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crossex_convert_quote_request** | [**CrossexConvertQuoteRequest**](CrossexConvertQuoteRequest.md)|  | [optional] 

### Return type

[**CrossexConvertQuoteResponse**](CrossexConvertQuoteResponse.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project-Id-Version: GateApiTools 1.0.0 Report-Msgid-Bugs-To: EMAIL@ADDRESS POT-Creation-Date: 2025-11-12 18:14+0800 PO-Revision-Date: 2019-01-02 17:30+0800 Last-Translator: FULL NAME &lt;EMAIL@ADDRESS&gt; Language: en Language-Team: en &lt;L@li.org&gt; Plural-Forms: nplurals&#x3D;2; plural&#x3D;(n !&#x3D;1) MIME-Version: 1.0 Content-Type: text/plain; charset&#x3D;utf-8 Content-Transfer-Encoding: 8bit Generated-By: Babel 2.8.0  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_crossex_convert_order**
> CrossexConvertOrderResponse create_crossex_convert_order(crossex_convert_order_request=crossex_convert_order_request)

Flash Swap Transaction

Rate limit: 10 requests per 10 seconds

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
api_instance = gate_api.CrossExApi(api_client)
crossex_convert_order_request = gate_api.CrossexConvertOrderRequest() # CrossexConvertOrderRequest |  (optional)

try:
    # Flash Swap Transaction
    api_response = api_instance.create_crossex_convert_order(crossex_convert_order_request=crossex_convert_order_request)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling CrossExApi->create_crossex_convert_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crossex_convert_order_request** | [**CrossexConvertOrderRequest**](CrossexConvertOrderRequest.md)|  | [optional] 

### Return type

[**CrossexConvertOrderResponse**](CrossexConvertOrderResponse.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project-Id-Version: GateApiTools 1.0.0 Report-Msgid-Bugs-To: EMAIL@ADDRESS POT-Creation-Date: 2025-11-12 18:14+0800 PO-Revision-Date: 2019-01-02 17:30+0800 Last-Translator: FULL NAME &lt;EMAIL@ADDRESS&gt; Language: en Language-Team: en &lt;L@li.org&gt; Plural-Forms: nplurals&#x3D;2; plural&#x3D;(n !&#x3D;1) MIME-Version: 1.0 Content-Type: text/plain; charset&#x3D;utf-8 Content-Transfer-Encoding: 8bit Generated-By: Babel 2.8.0  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_crossex_account**
> CrossexAccount get_crossex_account(exchange_type=exchange_type)

Query Account Assets

Rate limit: 200 requests per 10 seconds If 100% <= initial_margin_rate < 110%, transferring out the margin currency is prohibited. If initial_margin_rate < 100%, the system automatically cancels orders; only closing positions is allowed, not opening new ones. If maintenance_margin_rate <= 100%, the system forces liquidation.

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
api_instance = gate_api.CrossExApi(api_client)
exchange_type = 'BINANCE,OKX,GATE,BYBIT,KRAKEN,HYPERLIQUID,DERIBIT' # str | Trading venue identifier. Omit in cross-exchange mode; required in isolated-per-venue mode (`BINANCE` / `OKX` / `GATE` / `BYBIT` / `KRAKEN` / `HYPERLIQUID` / `DERIBIT`). (optional)

try:
    # Query Account Assets
    api_response = api_instance.get_crossex_account(exchange_type=exchange_type)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling CrossExApi->get_crossex_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exchange_type** | **str**| Trading venue identifier. Omit in cross-exchange mode; required in isolated-per-venue mode (&#x60;BINANCE&#x60; / &#x60;OKX&#x60; / &#x60;GATE&#x60; / &#x60;BYBIT&#x60; / &#x60;KRAKEN&#x60; / &#x60;HYPERLIQUID&#x60; / &#x60;DERIBIT&#x60;). | [optional] 

### Return type

[**CrossexAccount**](CrossexAccount.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project-Id-Version: GateApiTools 1.0.0 Report-Msgid-Bugs-To: EMAIL@ADDRESS POT-Creation-Date: 2025-11-12 18:14+0800 PO-Revision-Date: 2019-01-02 17:30+0800 Last-Translator: FULL NAME &lt;EMAIL@ADDRESS&gt; Language: en Language-Team: en &lt;L@li.org&gt; Plural-Forms: nplurals&#x3D;2; plural&#x3D;(n !&#x3D;1) MIME-Version: 1.0 Content-Type: text/plain; charset&#x3D;utf-8 Content-Transfer-Encoding: 8bit Generated-By: Babel 2.8.0  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_crossex_account**
> CrossexAccountUpdateResponse update_crossex_account(crossex_account_update_request=crossex_account_update_request)

Modify Account Contract Position Mode and Account Mode

Rate Limit: 100 requests per 60 seconds. position_mode+exchange_type modifies contract position mode (exchange_type is required when the user's account mode is split exchange); account_mode modifies the user's account mode.

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
api_instance = gate_api.CrossExApi(api_client)
crossex_account_update_request = gate_api.CrossexAccountUpdateRequest() # CrossexAccountUpdateRequest |  (optional)

try:
    # Modify Account Contract Position Mode and Account Mode
    api_response = api_instance.update_crossex_account(crossex_account_update_request=crossex_account_update_request)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling CrossExApi->update_crossex_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crossex_account_update_request** | [**CrossexAccountUpdateRequest**](CrossexAccountUpdateRequest.md)|  | [optional] 

### Return type

[**CrossexAccountUpdateResponse**](CrossexAccountUpdateResponse.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Project-Id-Version: GateApiTools 1.0.0 Report-Msgid-Bugs-To: EMAIL@ADDRESS POT-Creation-Date: 2025-11-12 18:14+0800 PO-Revision-Date: 2019-01-02 17:30+0800 Last-Translator: FULL NAME &lt;EMAIL@ADDRESS&gt; Language: en Language-Team: en &lt;L@li.org&gt; Plural-Forms: nplurals&#x3D;2; plural&#x3D;(n !&#x3D;1) MIME-Version: 1.0 Content-Type: text/plain; charset&#x3D;utf-8 Content-Transfer-Encoding: 8bit Generated-By: Babel 2.8.0  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_crossex_positions_leverage**
> dict(str, str) get_crossex_positions_leverage(symbols=symbols)

Query Contract Trading Pair Leverage Multiplier

Rate Limit: 200 requests per 10 seconds

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
api_instance = gate_api.CrossExApi(api_client)
symbols = 'BINANCE_FUTURE_BTC_USDT,OKX_FUTURE_BTC_USDT,GATE_FUTURE_BTC_USDT' # str | Trading Pair List, multiple separated by commas (optional)

try:
    # Query Contract Trading Pair Leverage Multiplier
    api_response = api_instance.get_crossex_positions_leverage(symbols=symbols)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling CrossExApi->get_crossex_positions_leverage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbols** | **str**| Trading Pair List, multiple separated by commas | [optional] 

### Return type

**dict(str, str)**

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project-Id-Version: GateApiTools 1.0.0 Report-Msgid-Bugs-To: EMAIL@ADDRESS POT-Creation-Date: 2025-11-12 18:14+0800 PO-Revision-Date: 2019-01-02 17:30+0800 Last-Translator: FULL NAME &lt;EMAIL@ADDRESS&gt; Language: en Language-Team: en &lt;L@li.org&gt; Plural-Forms: nplurals&#x3D;2; plural&#x3D;(n !&#x3D;1) MIME-Version: 1.0 Content-Type: text/plain; charset&#x3D;utf-8 Content-Transfer-Encoding: 8bit Generated-By: Babel 2.8.0  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_crossex_positions_leverage**
> CrossexLeverageResponse update_crossex_positions_leverage(crossex_leverage_request=crossex_leverage_request)

Modify Contract Trading Pair Leverage Multiplier

Rate Limit: 100 requests per 10 seconds

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
api_instance = gate_api.CrossExApi(api_client)
crossex_leverage_request = gate_api.CrossexLeverageRequest() # CrossexLeverageRequest |  (optional)

try:
    # Modify Contract Trading Pair Leverage Multiplier
    api_response = api_instance.update_crossex_positions_leverage(crossex_leverage_request=crossex_leverage_request)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling CrossExApi->update_crossex_positions_leverage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crossex_leverage_request** | [**CrossexLeverageRequest**](CrossexLeverageRequest.md)|  | [optional] 

### Return type

[**CrossexLeverageResponse**](CrossexLeverageResponse.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Project-Id-Version: GateApiTools 1.0.0 Report-Msgid-Bugs-To: EMAIL@ADDRESS POT-Creation-Date: 2025-11-12 18:14+0800 PO-Revision-Date: 2019-01-02 17:30+0800 Last-Translator: FULL NAME &lt;EMAIL@ADDRESS&gt; Language: en Language-Team: en &lt;L@li.org&gt; Plural-Forms: nplurals&#x3D;2; plural&#x3D;(n !&#x3D;1) MIME-Version: 1.0 Content-Type: text/plain; charset&#x3D;utf-8 Content-Transfer-Encoding: 8bit Generated-By: Babel 2.8.0  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_crossex_margin_positions_leverage**
> dict(str, str) get_crossex_margin_positions_leverage(symbols=symbols)

Query Leveraged Trading Pair Leverage Multiplier

Rate Limit: 200 requests per 10 seconds

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
api_instance = gate_api.CrossExApi(api_client)
symbols = 'BINANCE_MARGIN_BTC_USDT,OKX_MARGIN_BTC_USDT,GATE_MARGIN_BTC_USDT' # str | Trading Pair List, multiple separated by commas (optional)

try:
    # Query Leveraged Trading Pair Leverage Multiplier
    api_response = api_instance.get_crossex_margin_positions_leverage(symbols=symbols)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling CrossExApi->get_crossex_margin_positions_leverage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbols** | **str**| Trading Pair List, multiple separated by commas | [optional] 

### Return type

**dict(str, str)**

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project-Id-Version: GateApiTools 1.0.0 Report-Msgid-Bugs-To: EMAIL@ADDRESS POT-Creation-Date: 2025-11-12 18:14+0800 PO-Revision-Date: 2019-01-02 17:30+0800 Last-Translator: FULL NAME &lt;EMAIL@ADDRESS&gt; Language: en Language-Team: en &lt;L@li.org&gt; Plural-Forms: nplurals&#x3D;2; plural&#x3D;(n !&#x3D;1) MIME-Version: 1.0 Content-Type: text/plain; charset&#x3D;utf-8 Content-Transfer-Encoding: 8bit Generated-By: Babel 2.8.0  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_crossex_margin_positions_leverage**
> CrossexLeverageResponse update_crossex_margin_positions_leverage(crossex_leverage_request=crossex_leverage_request)

Modify Leveraged Trading Pair Leverage Multiplier

Rate Limit: 100 requests per 10 seconds

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
api_instance = gate_api.CrossExApi(api_client)
crossex_leverage_request = gate_api.CrossexLeverageRequest() # CrossexLeverageRequest |  (optional)

try:
    # Modify Leveraged Trading Pair Leverage Multiplier
    api_response = api_instance.update_crossex_margin_positions_leverage(crossex_leverage_request=crossex_leverage_request)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling CrossExApi->update_crossex_margin_positions_leverage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crossex_leverage_request** | [**CrossexLeverageRequest**](CrossexLeverageRequest.md)|  | [optional] 

### Return type

[**CrossexLeverageResponse**](CrossexLeverageResponse.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Project-Id-Version: GateApiTools 1.0.0 Report-Msgid-Bugs-To: EMAIL@ADDRESS POT-Creation-Date: 2025-11-12 18:14+0800 PO-Revision-Date: 2019-01-02 17:30+0800 Last-Translator: FULL NAME &lt;EMAIL@ADDRESS&gt; Language: en Language-Team: en &lt;L@li.org&gt; Plural-Forms: nplurals&#x3D;2; plural&#x3D;(n !&#x3D;1) MIME-Version: 1.0 Content-Type: text/plain; charset&#x3D;utf-8 Content-Transfer-Encoding: 8bit Generated-By: Babel 2.8.0  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **close_crossex_position**
> CrossexOrderActionResponse close_crossex_position(crossex_close_position_request=crossex_close_position_request)

Full Close Position

Rate limit: 100 requests per day. Automatic position-closing rules. FUTURE and MARGIN positions are supported.  Before using this endpoint, ensure that the following prerequisite is met: - There are no open orders for the symbol in the current account. - Once the prerequisite is met, the system checks whether the position meets either of the following conditions: - Less than the minimum notional amount (minNotional) - Less than the minimum order size (minSize)  When either condition is met, the system automatically creates a closing order and immediately closes the entire position. This endpoint prevents positions that are too small to be submitted to an exchange from becoming stranded and ensures that small positions can be closed when they fall below the threshold.

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
api_instance = gate_api.CrossExApi(api_client)
crossex_close_position_request = gate_api.CrossexClosePositionRequest() # CrossexClosePositionRequest |  (optional)

try:
    # Full Close Position
    api_response = api_instance.close_crossex_position(crossex_close_position_request=crossex_close_position_request)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling CrossExApi->close_crossex_position: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crossex_close_position_request** | [**CrossexClosePositionRequest**](CrossexClosePositionRequest.md)|  | [optional] 

### Return type

[**CrossexOrderActionResponse**](CrossexOrderActionResponse.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Project-Id-Version: GateApiTools 1.0.0 Report-Msgid-Bugs-To: EMAIL@ADDRESS POT-Creation-Date: 2025-11-12 18:14+0800 PO-Revision-Date: 2019-01-02 17:30+0800 Last-Translator: FULL NAME &lt;EMAIL@ADDRESS&gt; Language: en Language-Team: en &lt;L@li.org&gt; Plural-Forms: nplurals&#x3D;2; plural&#x3D;(n !&#x3D;1) MIME-Version: 1.0 Content-Type: text/plain; charset&#x3D;utf-8 Content-Transfer-Encoding: 8bit Generated-By: Babel 2.8.0  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_crossex_positions_margin_mode**
> CrossexMarginModeResponse get_crossex_positions_margin_mode(symbol)

Get futures position margin mode

Rate Limit: 200 requests per 10 seconds

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
api_instance = gate_api.CrossExApi(api_client)
symbol = 'HYPERLIQUID_FUTURE_CXMT_USDC' # str | Futures trading pair

try:
    # Get futures position margin mode
    api_response = api_instance.get_crossex_positions_margin_mode(symbol)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling CrossExApi->get_crossex_positions_margin_mode: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Futures trading pair | 

### Return type

[**CrossexMarginModeResponse**](CrossexMarginModeResponse.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project-Id-Version: GateApiTools 1.0.0 Report-Msgid-Bugs-To: EMAIL@ADDRESS POT-Creation-Date: 2025-11-12 18:14+0800 PO-Revision-Date: 2019-01-02 17:30+0800 Last-Translator: FULL NAME &lt;EMAIL@ADDRESS&gt; Language: en Language-Team: en &lt;L@li.org&gt; Plural-Forms: nplurals&#x3D;2; plural&#x3D;(n !&#x3D;1) MIME-Version: 1.0 Content-Type: text/plain; charset&#x3D;utf-8 Content-Transfer-Encoding: 8bit Generated-By: Babel 2.8.0  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_crossex_positions_margin_mode**
> CrossexMarginModeResponse update_crossex_positions_margin_mode(crossex_margin_mode_request=crossex_margin_mode_request)

Update futures position margin mode

Rate limit: 100 requests per 10 seconds. Only Hyperliquid futures trading pairs are supported. The margin mode cannot be changed while open orders or positions exist

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
api_instance = gate_api.CrossExApi(api_client)
crossex_margin_mode_request = gate_api.CrossexMarginModeRequest() # CrossexMarginModeRequest |  (optional)

try:
    # Update futures position margin mode
    api_response = api_instance.update_crossex_positions_margin_mode(crossex_margin_mode_request=crossex_margin_mode_request)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling CrossExApi->update_crossex_positions_margin_mode: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crossex_margin_mode_request** | [**CrossexMarginModeRequest**](CrossexMarginModeRequest.md)|  | [optional] 

### Return type

[**CrossexMarginModeResponse**](CrossexMarginModeResponse.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Project-Id-Version: GateApiTools 1.0.0 Report-Msgid-Bugs-To: EMAIL@ADDRESS POT-Creation-Date: 2025-11-12 18:14+0800 PO-Revision-Date: 2019-01-02 17:30+0800 Last-Translator: FULL NAME &lt;EMAIL@ADDRESS&gt; Language: en Language-Team: en &lt;L@li.org&gt; Plural-Forms: nplurals&#x3D;2; plural&#x3D;(n !&#x3D;1) MIME-Version: 1.0 Content-Type: text/plain; charset&#x3D;utf-8 Content-Transfer-Encoding: 8bit Generated-By: Babel 2.8.0  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_crossex_positions_margin**
> CrossexIsolatedMarginResponse update_crossex_positions_margin(crossex_isolated_margin_request=crossex_isolated_margin_request)

Increase or decrease isolated margin

Rate limit: 100 requests per 10 seconds. Only Hyperliquid isolated futures positions are supported. Positive values increase margin, while negative values decrease margin

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
api_instance = gate_api.CrossExApi(api_client)
crossex_isolated_margin_request = gate_api.CrossexIsolatedMarginRequest() # CrossexIsolatedMarginRequest |  (optional)

try:
    # Increase or decrease isolated margin
    api_response = api_instance.update_crossex_positions_margin(crossex_isolated_margin_request=crossex_isolated_margin_request)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling CrossExApi->update_crossex_positions_margin: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crossex_isolated_margin_request** | [**CrossexIsolatedMarginRequest**](CrossexIsolatedMarginRequest.md)|  | [optional] 

### Return type

[**CrossexIsolatedMarginResponse**](CrossexIsolatedMarginResponse.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Project-Id-Version: GateApiTools 1.0.0 Report-Msgid-Bugs-To: EMAIL@ADDRESS POT-Creation-Date: 2025-11-12 18:14+0800 PO-Revision-Date: 2019-01-02 17:30+0800 Last-Translator: FULL NAME &lt;EMAIL@ADDRESS&gt; Language: en Language-Team: en &lt;L@li.org&gt; Plural-Forms: nplurals&#x3D;2; plural&#x3D;(n !&#x3D;1) MIME-Version: 1.0 Content-Type: text/plain; charset&#x3D;utf-8 Content-Transfer-Encoding: 8bit Generated-By: Babel 2.8.0  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_crossex_interest_rate**
> list[CrossexInterestRate] get_crossex_interest_rate(coin=coin, exchange_type=exchange_type)

Query margin asset interest rates

Rate Limit: 200 requests per 10 seconds

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
api_instance = gate_api.CrossExApi(api_client)
coin = 'SOL' # str | Query by specified currency name (optional)
exchange_type = 'BINANCE,OKX,GATE,BYBIT,KRAKEN,HYPERLIQUID,DERIBIT' # str | Exchange (optional)

try:
    # Query margin asset interest rates
    api_response = api_instance.get_crossex_interest_rate(coin=coin, exchange_type=exchange_type)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling CrossExApi->get_crossex_interest_rate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coin** | **str**| Query by specified currency name | [optional] 
 **exchange_type** | **str**| Exchange | [optional] 

### Return type

[**list[CrossexInterestRate]**](CrossexInterestRate.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project-Id-Version: GateApiTools 1.0.0 Report-Msgid-Bugs-To: EMAIL@ADDRESS POT-Creation-Date: 2025-11-12 18:14+0800 PO-Revision-Date: 2019-01-02 17:30+0800 Last-Translator: FULL NAME &lt;EMAIL@ADDRESS&gt; Language: en Language-Team: en &lt;L@li.org&gt; Plural-Forms: nplurals&#x3D;2; plural&#x3D;(n !&#x3D;1) MIME-Version: 1.0 Content-Type: text/plain; charset&#x3D;utf-8 Content-Transfer-Encoding: 8bit Generated-By: Babel 2.8.0  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_crossex_fee**
> list[InlineResponse200] get_crossex_fee()

Query User Fee Rates

Rate Limit: 200 requests per 10 seconds

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
api_instance = gate_api.CrossExApi(api_client)

try:
    # Query User Fee Rates
    api_response = api_instance.get_crossex_fee()
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling CrossExApi->get_crossex_fee: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[InlineResponse200]**](InlineResponse200.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project-Id-Version: GateApiTools 1.0.0 Report-Msgid-Bugs-To: EMAIL@ADDRESS POT-Creation-Date: 2025-11-12 18:14+0800 PO-Revision-Date: 2019-01-02 17:30+0800 Last-Translator: FULL NAME &lt;EMAIL@ADDRESS&gt; Language: en Language-Team: en &lt;L@li.org&gt; Plural-Forms: nplurals&#x3D;2; plural&#x3D;(n !&#x3D;1) MIME-Version: 1.0 Content-Type: text/plain; charset&#x3D;utf-8 Content-Transfer-Encoding: 8bit Generated-By: Babel 2.8.0  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_crossex_positions**
> list[CrossexPosition] list_crossex_positions(symbol=symbol, exchange_type=exchange_type)

Query Contract Positions

Rate Limit: 200 requests per 10 seconds

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
api_instance = gate_api.CrossExApi(api_client)
symbol = 'BINANCE_FUTURE_ADA_USDT' # str | Trading Pair (optional)
exchange_type = 'BINANCE,OKX,GATE,BYBIT,KRAKEN,HYPERLIQUID,DERIBIT' # str | Exchange (optional)

try:
    # Query Contract Positions
    api_response = api_instance.list_crossex_positions(symbol=symbol, exchange_type=exchange_type)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling CrossExApi->list_crossex_positions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Trading Pair | [optional] 
 **exchange_type** | **str**| Exchange | [optional] 

### Return type

[**list[CrossexPosition]**](CrossexPosition.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project-Id-Version: GateApiTools 1.0.0 Report-Msgid-Bugs-To: EMAIL@ADDRESS POT-Creation-Date: 2025-11-12 18:14+0800 PO-Revision-Date: 2019-01-02 17:30+0800 Last-Translator: FULL NAME &lt;EMAIL@ADDRESS&gt; Language: en Language-Team: en &lt;L@li.org&gt; Plural-Forms: nplurals&#x3D;2; plural&#x3D;(n !&#x3D;1) MIME-Version: 1.0 Content-Type: text/plain; charset&#x3D;utf-8 Content-Transfer-Encoding: 8bit Generated-By: Babel 2.8.0  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_crossex_margin_positions**
> list[CrossexMarginPosition] list_crossex_margin_positions(symbol=symbol, exchange_type=exchange_type)

Query Leveraged Positions

Rate Limit: 200 requests per 10 seconds

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
api_instance = gate_api.CrossExApi(api_client)
symbol = 'BINANCE_MARGIN_ADA_USDT' # str | Currency pair (optional)
exchange_type = 'BINANCE' # str | Exchange (optional)

try:
    # Query Leveraged Positions
    api_response = api_instance.list_crossex_margin_positions(symbol=symbol, exchange_type=exchange_type)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling CrossExApi->list_crossex_margin_positions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Currency pair | [optional] 
 **exchange_type** | **str**| Exchange | [optional] 

### Return type

[**list[CrossexMarginPosition]**](CrossexMarginPosition.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project-Id-Version: GateApiTools 1.0.0 Report-Msgid-Bugs-To: EMAIL@ADDRESS POT-Creation-Date: 2025-11-12 18:14+0800 PO-Revision-Date: 2019-01-02 17:30+0800 Last-Translator: FULL NAME &lt;EMAIL@ADDRESS&gt; Language: en Language-Team: en &lt;L@li.org&gt; Plural-Forms: nplurals&#x3D;2; plural&#x3D;(n !&#x3D;1) MIME-Version: 1.0 Content-Type: text/plain; charset&#x3D;utf-8 Content-Transfer-Encoding: 8bit Generated-By: Babel 2.8.0  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_crossex_adl_rank**
> CrossexAdlRank list_crossex_adl_rank(symbol)

Query ADL Position Reduction Ranking

Rate Limit: 200 requests per 10 seconds

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
api_instance = gate_api.CrossExApi(api_client)
symbol = 'BINANCE_FUTURE_ADA_USDT' # str | Trading Pair

try:
    # Query ADL Position Reduction Ranking
    api_response = api_instance.list_crossex_adl_rank(symbol)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling CrossExApi->list_crossex_adl_rank: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Trading Pair | 

### Return type

[**CrossexAdlRank**](CrossexAdlRank.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project-Id-Version: GateApiTools 1.0.0 Report-Msgid-Bugs-To: EMAIL@ADDRESS POT-Creation-Date: 2025-11-12 18:14+0800 PO-Revision-Date: 2019-01-02 17:30+0800 Last-Translator: FULL NAME &lt;EMAIL@ADDRESS&gt; Language: en Language-Team: en &lt;L@li.org&gt; Plural-Forms: nplurals&#x3D;2; plural&#x3D;(n !&#x3D;1) MIME-Version: 1.0 Content-Type: text/plain; charset&#x3D;utf-8 Content-Transfer-Encoding: 8bit Generated-By: Babel 2.8.0  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_crossex_open_orders**
> list[CrossexOrder] list_crossex_open_orders(symbol=symbol, exchange_type=exchange_type, business_type=business_type)

Query All Current Open Orders

Rate Limit: 200 requests per 10 seconds

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
api_instance = gate_api.CrossExApi(api_client)
symbol = 'BINANCE_FUTURE_ADA_USDT' # str | Trading Pair (optional)
exchange_type = 'BINANCE' # str | Exchange (optional)
business_type = 'FUTURE' # str | Business Type (optional)

try:
    # Query All Current Open Orders
    api_response = api_instance.list_crossex_open_orders(symbol=symbol, exchange_type=exchange_type, business_type=business_type)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling CrossExApi->list_crossex_open_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Trading Pair | [optional] 
 **exchange_type** | **str**| Exchange | [optional] 
 **business_type** | **str**| Business Type | [optional] 

### Return type

[**list[CrossexOrder]**](CrossexOrder.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project-Id-Version: GateApiTools 1.0.0 Report-Msgid-Bugs-To: EMAIL@ADDRESS POT-Creation-Date: 2025-11-12 18:14+0800 PO-Revision-Date: 2019-01-02 17:30+0800 Last-Translator: FULL NAME &lt;EMAIL@ADDRESS&gt; Language: en Language-Team: en &lt;L@li.org&gt; Plural-Forms: nplurals&#x3D;2; plural&#x3D;(n !&#x3D;1) MIME-Version: 1.0 Content-Type: text/plain; charset&#x3D;utf-8 Content-Transfer-Encoding: 8bit Generated-By: Babel 2.8.0  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_crossex_history_orders**
> list[CrossexOrder] list_crossex_history_orders(page=page, limit=limit, symbol=symbol, _from=_from, to=to, attributes=attributes)

Query order history

Rate Limit: 200 requests per 10 seconds

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
api_instance = gate_api.CrossExApi(api_client)
page = 56 # int | Page number (optional)
limit = 56 # int | Maximum number of records returned in a single list (optional)
symbol = 'symbol_example' # str | Currency pair (optional)
_from = 56 # int | Start Millisecond Timestamp (optional)
to = 56 # int | End Millisecond Timestamp (optional)
attributes = 'attributes_example' # str | Order attributes (`COMMON` normal / `LIQ` liquidation takeover / `REDUCE` liquidation reduction / `ADL` auto-deleverage / `SETTLEMENT` delisting settlement). Multiple values, comma-separated. (optional)

try:
    # Query order history
    api_response = api_instance.list_crossex_history_orders(page=page, limit=limit, symbol=symbol, _from=_from, to=to, attributes=attributes)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling CrossExApi->list_crossex_history_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number | [optional] 
 **limit** | **int**| Maximum number of records returned in a single list | [optional] 
 **symbol** | **str**| Currency pair | [optional] 
 **_from** | **int**| Start Millisecond Timestamp | [optional] 
 **to** | **int**| End Millisecond Timestamp | [optional] 
 **attributes** | **str**| Order attributes (&#x60;COMMON&#x60; normal / &#x60;LIQ&#x60; liquidation takeover / &#x60;REDUCE&#x60; liquidation reduction / &#x60;ADL&#x60; auto-deleverage / &#x60;SETTLEMENT&#x60; delisting settlement). Multiple values, comma-separated. | [optional] 

### Return type

[**list[CrossexOrder]**](CrossexOrder.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project-Id-Version: GateApiTools 1.0.0 Report-Msgid-Bugs-To: EMAIL@ADDRESS POT-Creation-Date: 2025-11-12 18:14+0800 PO-Revision-Date: 2019-01-02 17:30+0800 Last-Translator: FULL NAME &lt;EMAIL@ADDRESS&gt; Language: en Language-Team: en &lt;L@li.org&gt; Plural-Forms: nplurals&#x3D;2; plural&#x3D;(n !&#x3D;1) MIME-Version: 1.0 Content-Type: text/plain; charset&#x3D;utf-8 Content-Transfer-Encoding: 8bit Generated-By: Babel 2.8.0  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_crossex_history_positions**
> list[CrossexHistoricalPosition] list_crossex_history_positions(page=page, limit=limit, symbol=symbol, _from=_from, to=to)

Query Contract Position History

Rate Limit: 200 requests per 10 seconds

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
api_instance = gate_api.CrossExApi(api_client)
page = 56 # int | Page number (optional)
limit = 56 # int | Maximum number returned by list, max 1000 (optional)
symbol = 'symbol_example' # str | Currency pair (optional)
_from = 56 # int | Start Millisecond Timestamp (optional)
to = 56 # int | End Millisecond Timestamp (optional)

try:
    # Query Contract Position History
    api_response = api_instance.list_crossex_history_positions(page=page, limit=limit, symbol=symbol, _from=_from, to=to)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling CrossExApi->list_crossex_history_positions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number | [optional] 
 **limit** | **int**| Maximum number returned by list, max 1000 | [optional] 
 **symbol** | **str**| Currency pair | [optional] 
 **_from** | **int**| Start Millisecond Timestamp | [optional] 
 **to** | **int**| End Millisecond Timestamp | [optional] 

### Return type

[**list[CrossexHistoricalPosition]**](CrossexHistoricalPosition.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project-Id-Version: GateApiTools 1.0.0 Report-Msgid-Bugs-To: EMAIL@ADDRESS POT-Creation-Date: 2025-11-12 18:14+0800 PO-Revision-Date: 2019-01-02 17:30+0800 Last-Translator: FULL NAME &lt;EMAIL@ADDRESS&gt; Language: en Language-Team: en &lt;L@li.org&gt; Plural-Forms: nplurals&#x3D;2; plural&#x3D;(n !&#x3D;1) MIME-Version: 1.0 Content-Type: text/plain; charset&#x3D;utf-8 Content-Transfer-Encoding: 8bit Generated-By: Babel 2.8.0  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_crossex_history_margin_positions**
> list[CrossexHistoricalMarginPosition] list_crossex_history_margin_positions(page=page, limit=limit, symbol=symbol, _from=_from, to=to)

Query Leveraged Position History

Rate Limit: 200 requests per 10 seconds

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
api_instance = gate_api.CrossExApi(api_client)
page = 56 # int | Page number (optional)
limit = 56 # int | Maximum number returned by list, max 1000 (optional)
symbol = 'symbol_example' # str | Currency pair (optional)
_from = 56 # int | Start Millisecond Timestamp (optional)
to = 56 # int | End Millisecond Timestamp (optional)

try:
    # Query Leveraged Position History
    api_response = api_instance.list_crossex_history_margin_positions(page=page, limit=limit, symbol=symbol, _from=_from, to=to)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling CrossExApi->list_crossex_history_margin_positions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number | [optional] 
 **limit** | **int**| Maximum number returned by list, max 1000 | [optional] 
 **symbol** | **str**| Currency pair | [optional] 
 **_from** | **int**| Start Millisecond Timestamp | [optional] 
 **to** | **int**| End Millisecond Timestamp | [optional] 

### Return type

[**list[CrossexHistoricalMarginPosition]**](CrossexHistoricalMarginPosition.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project-Id-Version: GateApiTools 1.0.0 Report-Msgid-Bugs-To: EMAIL@ADDRESS POT-Creation-Date: 2025-11-12 18:14+0800 PO-Revision-Date: 2019-01-02 17:30+0800 Last-Translator: FULL NAME &lt;EMAIL@ADDRESS&gt; Language: en Language-Team: en &lt;L@li.org&gt; Plural-Forms: nplurals&#x3D;2; plural&#x3D;(n !&#x3D;1) MIME-Version: 1.0 Content-Type: text/plain; charset&#x3D;utf-8 Content-Transfer-Encoding: 8bit Generated-By: Babel 2.8.0  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_crossex_history_margin_interests**
> list[CrossexMarginInterestRecord] list_crossex_history_margin_interests(symbol=symbol, _from=_from, to=to, page=page, limit=limit, exchange_type=exchange_type)

Query Leveraged Interest Deduction History

Rate Limit: 200 requests per 10 seconds

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
api_instance = gate_api.CrossExApi(api_client)
symbol = 'symbol_example' # str | Currency pair (optional)
_from = 56 # int | Start Millisecond Timestamp (optional)
to = 56 # int | End Millisecond Timestamp (optional)
page = 56 # int | Page number (optional)
limit = 56 # int | Maximum number returned by list, max 1000 (optional)
exchange_type = 'exchange_type_example' # str | Exchange (optional)

try:
    # Query Leveraged Interest Deduction History
    api_response = api_instance.list_crossex_history_margin_interests(symbol=symbol, _from=_from, to=to, page=page, limit=limit, exchange_type=exchange_type)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling CrossExApi->list_crossex_history_margin_interests: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | **str**| Currency pair | [optional] 
 **_from** | **int**| Start Millisecond Timestamp | [optional] 
 **to** | **int**| End Millisecond Timestamp | [optional] 
 **page** | **int**| Page number | [optional] 
 **limit** | **int**| Maximum number returned by list, max 1000 | [optional] 
 **exchange_type** | **str**| Exchange | [optional] 

### Return type

[**list[CrossexMarginInterestRecord]**](CrossexMarginInterestRecord.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project-Id-Version: GateApiTools 1.0.0 Report-Msgid-Bugs-To: EMAIL@ADDRESS POT-Creation-Date: 2025-11-12 18:14+0800 PO-Revision-Date: 2019-01-02 17:30+0800 Last-Translator: FULL NAME &lt;EMAIL@ADDRESS&gt; Language: en Language-Team: en &lt;L@li.org&gt; Plural-Forms: nplurals&#x3D;2; plural&#x3D;(n !&#x3D;1) MIME-Version: 1.0 Content-Type: text/plain; charset&#x3D;utf-8 Content-Transfer-Encoding: 8bit Generated-By: Babel 2.8.0  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_crossex_history_trades**
> list[CrossexTrade] list_crossex_history_trades(page=page, limit=limit, symbol=symbol, _from=_from, to=to)

Query filled history

Rate Limit: 200 requests per 10 seconds

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
api_instance = gate_api.CrossExApi(api_client)
page = 56 # int | Page number (optional)
limit = 56 # int | Maximum number returned by list, max 1000 (optional)
symbol = 'symbol_example' # str | Currency pair (optional)
_from = 56 # int | Start Millisecond Timestamp (optional)
to = 56 # int | End Millisecond Timestamp (optional)

try:
    # Query filled history
    api_response = api_instance.list_crossex_history_trades(page=page, limit=limit, symbol=symbol, _from=_from, to=to)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling CrossExApi->list_crossex_history_trades: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number | [optional] 
 **limit** | **int**| Maximum number returned by list, max 1000 | [optional] 
 **symbol** | **str**| Currency pair | [optional] 
 **_from** | **int**| Start Millisecond Timestamp | [optional] 
 **to** | **int**| End Millisecond Timestamp | [optional] 

### Return type

[**list[CrossexTrade]**](CrossexTrade.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project-Id-Version: GateApiTools 1.0.0 Report-Msgid-Bugs-To: EMAIL@ADDRESS POT-Creation-Date: 2025-11-12 18:14+0800 PO-Revision-Date: 2019-01-02 17:30+0800 Last-Translator: FULL NAME &lt;EMAIL@ADDRESS&gt; Language: en Language-Team: en &lt;L@li.org&gt; Plural-Forms: nplurals&#x3D;2; plural&#x3D;(n !&#x3D;1) MIME-Version: 1.0 Content-Type: text/plain; charset&#x3D;utf-8 Content-Transfer-Encoding: 8bit Generated-By: Babel 2.8.0  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_crossex_account_book**
> list[CrossexAccountBookRecord] list_crossex_account_book(page=page, limit=limit, coin=coin, statement_type=statement_type, _from=_from, to=to)

Query Account Asset Change History

Rate Limit: 200 requests per 10 seconds

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
api_instance = gate_api.CrossExApi(api_client)
page = 56 # int | Page number (optional)
limit = 56 # int | Maximum number returned by list, max 1000 (optional)
coin = 'coin_example' # str | Query by specified currency name (optional)
statement_type = 'statement_type_example' # str | Bill entry type. The filter accepts the same values returned in the response. (optional)
_from = 56 # int | Start Millisecond Timestamp (optional)
to = 56 # int | End Millisecond Timestamp (optional)

try:
    # Query Account Asset Change History
    api_response = api_instance.list_crossex_account_book(page=page, limit=limit, coin=coin, statement_type=statement_type, _from=_from, to=to)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling CrossExApi->list_crossex_account_book: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number | [optional] 
 **limit** | **int**| Maximum number returned by list, max 1000 | [optional] 
 **coin** | **str**| Query by specified currency name | [optional] 
 **statement_type** | **str**| Bill entry type. The filter accepts the same values returned in the response. | [optional] 
 **_from** | **int**| Start Millisecond Timestamp | [optional] 
 **to** | **int**| End Millisecond Timestamp | [optional] 

### Return type

[**list[CrossexAccountBookRecord]**](CrossexAccountBookRecord.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project-Id-Version: GateApiTools 1.0.0 Report-Msgid-Bugs-To: EMAIL@ADDRESS POT-Creation-Date: 2025-11-12 18:14+0800 PO-Revision-Date: 2019-01-02 17:30+0800 Last-Translator: FULL NAME &lt;EMAIL@ADDRESS&gt; Language: en Language-Team: en &lt;L@li.org&gt; Plural-Forms: nplurals&#x3D;2; plural&#x3D;(n !&#x3D;1) MIME-Version: 1.0 Content-Type: text/plain; charset&#x3D;utf-8 Content-Transfer-Encoding: 8bit Generated-By: Babel 2.8.0  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_crossex_coin_discount_rate**
> list[CrossexCoinDiscountRate] list_crossex_coin_discount_rate(coin=coin, exchange_type=exchange_type)

Query Currency Discount Rate

Rate Limit: 200 requests per 10 seconds

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
api_instance = gate_api.CrossExApi(api_client)
coin = 'SOL' # str | Query by specified currency name (optional)
exchange_type = 'OKX' # str | OKX/GATE/BINANCE/BYBIT/KRAKEN/HYPERLIQUID/DERIBIT (optional)

try:
    # Query Currency Discount Rate
    api_response = api_instance.list_crossex_coin_discount_rate(coin=coin, exchange_type=exchange_type)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling CrossExApi->list_crossex_coin_discount_rate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coin** | **str**| Query by specified currency name | [optional] 
 **exchange_type** | **str**| OKX/GATE/BINANCE/BYBIT/KRAKEN/HYPERLIQUID/DERIBIT | [optional] 

### Return type

[**list[CrossexCoinDiscountRate]**](CrossexCoinDiscountRate.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project-Id-Version: GateApiTools 1.0.0 Report-Msgid-Bugs-To: EMAIL@ADDRESS POT-Creation-Date: 2025-11-12 18:14+0800 PO-Revision-Date: 2019-01-02 17:30+0800 Last-Translator: FULL NAME &lt;EMAIL@ADDRESS&gt; Language: en Language-Team: en &lt;L@li.org&gt; Plural-Forms: nplurals&#x3D;2; plural&#x3D;(n !&#x3D;1) MIME-Version: 1.0 Content-Type: text/plain; charset&#x3D;utf-8 Content-Transfer-Encoding: 8bit Generated-By: Babel 2.8.0  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_crossex_market_tickers**
> list[InlineResponse2001] list_crossex_market_tickers(symbols=symbols)

Get exchange tickers

Rate limit: 1 request per second - Margin trading pairs cannot be passed directly as parameters. For example, `GATE_MARGIN_BTC_USDT` is invalid.

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
api_instance = gate_api.CrossExApi(api_client)
symbols = 'GATE_SPOT_BTC_USDT,GATE_FUTURE_BTC_USDT' # str | Trading Pair List, multiple separated by commas (optional)

try:
    # Get exchange tickers
    api_response = api_instance.list_crossex_market_tickers(symbols=symbols)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling CrossExApi->list_crossex_market_tickers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbols** | **str**| Trading Pair List, multiple separated by commas | [optional] 

### Return type

[**list[InlineResponse2001]**](InlineResponse2001.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project-Id-Version: GateApiTools 1.0.0 Report-Msgid-Bugs-To: EMAIL@ADDRESS POT-Creation-Date: 2025-11-12 18:14+0800 PO-Revision-Date: 2019-01-02 17:30+0800 Last-Translator: FULL NAME &lt;EMAIL@ADDRESS&gt; Language: en Language-Team: en &lt;L@li.org&gt; Plural-Forms: nplurals&#x3D;2; plural&#x3D;(n !&#x3D;1) MIME-Version: 1.0 Content-Type: text/plain; charset&#x3D;utf-8 Content-Transfer-Encoding: 8bit Generated-By: Babel 2.8.0  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_crossex_market_funding_info**
> list[InlineResponse2002] list_crossex_market_funding_info(symbols=symbols)

Get exchange futures funding rate information

Rate limit: 1 request per second - For `Deribit`, `funding_rate` is the current real-time rate calculated over an 8-hour period.

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
api_instance = gate_api.CrossExApi(api_client)
symbols = 'symbols_example' # str | Trading Pair List, multiple separated by commas (optional)

try:
    # Get exchange futures funding rate information
    api_response = api_instance.list_crossex_market_funding_info(symbols=symbols)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling CrossExApi->list_crossex_market_funding_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbols** | **str**| Trading Pair List, multiple separated by commas | [optional] 

### Return type

[**list[InlineResponse2002]**](InlineResponse2002.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project-Id-Version: GateApiTools 1.0.0 Report-Msgid-Bugs-To: EMAIL@ADDRESS POT-Creation-Date: 2025-11-12 18:14+0800 PO-Revision-Date: 2019-01-02 17:30+0800 Last-Translator: FULL NAME &lt;EMAIL@ADDRESS&gt; Language: en Language-Team: en &lt;L@li.org&gt; Plural-Forms: nplurals&#x3D;2; plural&#x3D;(n !&#x3D;1) MIME-Version: 1.0 Content-Type: text/plain; charset&#x3D;utf-8 Content-Transfer-Encoding: 8bit Generated-By: Babel 2.8.0  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

