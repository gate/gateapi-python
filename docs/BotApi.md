# gate_api.BotApi

All URIs are relative to *https://api.gateio.ws/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_ai_hub_strategy_recommend**](BotApi.md#get_ai_hub_strategy_recommend) | **GET** /bot/strategy/recommend | Get AIHub strategy recommendations
[**post_ai_hub_spot_grid_create**](BotApi.md#post_ai_hub_spot_grid_create) | **POST** /bot/spot-grid/create | Create spot grid
[**post_ai_hub_margin_grid_create**](BotApi.md#post_ai_hub_margin_grid_create) | **POST** /bot/margin-grid/create | Create a lever grid
[**post_ai_hub_infinite_grid_create**](BotApi.md#post_ai_hub_infinite_grid_create) | **POST** /bot/infinite-grid/create | Create infinite grid
[**post_ai_hub_futures_grid_create**](BotApi.md#post_ai_hub_futures_grid_create) | **POST** /bot/futures-grid/create | Create a contract grid
[**post_ai_hub_spot_martingale_create**](BotApi.md#post_ai_hub_spot_martingale_create) | **POST** /bot/spot-martingale/create | Create Spot Martin
[**post_ai_hub_contract_martingale_create**](BotApi.md#post_ai_hub_contract_martingale_create) | **POST** /bot/contract-martingale/create | Create contract martin
[**get_ai_hub_portfolio_running**](BotApi.md#get_ai_hub_portfolio_running) | **GET** /bot/portfolio/running | Query the list of running policies
[**get_ai_hub_portfolio_detail**](BotApi.md#get_ai_hub_portfolio_detail) | **GET** /bot/portfolio/detail | Query order policy details
[**post_ai_hub_portfolio_stop**](BotApi.md#post_ai_hub_portfolio_stop) | **POST** /bot/portfolio/stop | Terminate a single running policy


# **get_ai_hub_strategy_recommend**
> AIHubDiscoverSuccessResponse get_ai_hub_strategy_recommend(market=market, strategy_type=strategy_type, direction=direction, invest_amount=invest_amount, scene=scene, refresh_recommendation_id=refresh_recommendation_id, limit=limit, max_drawdown_lte=max_drawdown_lte, backtest_apr_gte=backtest_apr_gte, x_gate_service_id=x_gate_service_id, x_gate_app_lang=x_gate_app_lang, x_request_id=x_request_id, x_trace_id=x_trace_id)

Get AIHub strategy recommendations

The only formal interface for the discover domain. Support scenarios: - `top1` - `bundle` - `filter` - `refresh` Constraints: - The active recommendation pool only contains `spot_grid`, `futures_grid`, `spot_martingale` - Can return but do not actively recommend `infinite_grid`, `margin_grid` - `contract_martingale`, `smart-position`, `spot-future-arbitrage` must not be returned - When `scene=filter` is used, only filtering by `market`, `backtest_apr_gte`, `max_drawdown_lte` is allowed - `scene=refresh` inherits the refresh context through `refresh_recommendation_id`; the official minimum format only requires `strategy_type|market` - If the upstream directly transmits the previous recommendation `recommendation_id`, the third paragraph `backtest_id` will currently be ignored.

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
api_instance = gate_api.BotApi(api_client)
market = 'market_example' # str | Trading pair, such as `BTC_USDT` (optional)
strategy_type = 'strategy_type_example' # str | Recommended target policy type; `contract_martingale` not allowed (optional)
direction = 'direction_example' # str | Market direction (optional)
invest_amount = 'invest_amount_example' # str | Investment amount, string transparent transmission (optional)
scene = 'scene_example' # str | Recommended scenario; when empty, bot-service can automatically infer according to the implementation logic. (optional)
refresh_recommendation_id = 'refresh_recommendation_id_example' # str | It is recommended to refresh the context. Used when `scene=refresh` is used; when `scene` is empty but the field exists, bot-service will also automatically determine as `refresh`. The official minimum format is `strategy_type|market`; if the `recommendation_id` of the previous recommendation is directly passed through, the third paragraph `backtest_id` will be ignored. (optional)
limit = 56 # int | Return quantity; when `scene=filter` is used, the actual results are up to 10 (optional)
max_drawdown_lte = 'max_drawdown_lte_example' # str | Maximum drawdown limit (optional)
backtest_apr_gte = 'backtest_apr_gte_example' # str | Backtest annualized lower limit (optional)
x_gate_service_id = 'x_gate_service_id_example' # str | Call source identifier; injected by APIv4 if necessary (optional)
x_gate_app_lang = 'x_gate_app_lang_example' # str | Language context, such as `zh-CN` / `en-US` (optional)
x_request_id = 'x_request_id_example' # str | Request link ID; caller can transmit transparently (optional)
x_trace_id = 'x_trace_id_example' # str | trace header; can be generated uniformly by APIv4 (optional)

try:
    # Get AIHub strategy recommendations
    api_response = api_instance.get_ai_hub_strategy_recommend(market=market, strategy_type=strategy_type, direction=direction, invest_amount=invest_amount, scene=scene, refresh_recommendation_id=refresh_recommendation_id, limit=limit, max_drawdown_lte=max_drawdown_lte, backtest_apr_gte=backtest_apr_gte, x_gate_service_id=x_gate_service_id, x_gate_app_lang=x_gate_app_lang, x_request_id=x_request_id, x_trace_id=x_trace_id)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling BotApi->get_ai_hub_strategy_recommend: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **market** | **str**| Trading pair, such as &#x60;BTC_USDT&#x60; | [optional] 
 **strategy_type** | **str**| Recommended target policy type; &#x60;contract_martingale&#x60; not allowed | [optional] 
 **direction** | **str**| Market direction | [optional] 
 **invest_amount** | **str**| Investment amount, string transparent transmission | [optional] 
 **scene** | **str**| Recommended scenario; when empty, bot-service can automatically infer according to the implementation logic. | [optional] 
 **refresh_recommendation_id** | **str**| It is recommended to refresh the context. Used when &#x60;scene&#x3D;refresh&#x60; is used; when &#x60;scene&#x60; is empty but the field exists, bot-service will also automatically determine as &#x60;refresh&#x60;. The official minimum format is &#x60;strategy_type|market&#x60;; if the &#x60;recommendation_id&#x60; of the previous recommendation is directly passed through, the third paragraph &#x60;backtest_id&#x60; will be ignored. | [optional] 
 **limit** | **int**| Return quantity; when &#x60;scene&#x3D;filter&#x60; is used, the actual results are up to 10 | [optional] 
 **max_drawdown_lte** | **str**| Maximum drawdown limit | [optional] 
 **backtest_apr_gte** | **str**| Backtest annualized lower limit | [optional] 
 **x_gate_service_id** | **str**| Call source identifier; injected by APIv4 if necessary | [optional] 
 **x_gate_app_lang** | **str**| Language context, such as &#x60;zh-CN&#x60; / &#x60;en-US&#x60; | [optional] 
 **x_request_id** | **str**| Request link ID; caller can transmit transparently | [optional] 
 **x_trace_id** | **str**| trace header; can be generated uniformly by APIv4 | [optional] 

### Return type

[**AIHubDiscoverSuccessResponse**](AIHubDiscoverSuccessResponse.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Unified business response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_ai_hub_spot_grid_create**
> AIHubCreateSuccessResponse post_ai_hub_spot_grid_create(spot_grid_create_request, x_gate_service_id=x_gate_service_id, x_gate_app_lang=x_gate_app_lang, x_request_id=x_request_id, x_trace_id=x_trace_id)

Create spot grid

Create a spot grid strategy based on the incoming parameters.

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
api_instance = gate_api.BotApi(api_client)
spot_grid_create_request = gate_api.SpotGridCreateRequest() # SpotGridCreateRequest | 
x_gate_service_id = 'x_gate_service_id_example' # str | Call source identifier; injected by APIv4 if necessary (optional)
x_gate_app_lang = 'x_gate_app_lang_example' # str | Language context, such as `zh-CN` / `en-US` (optional)
x_request_id = 'x_request_id_example' # str | Request link ID; caller can transmit transparently (optional)
x_trace_id = 'x_trace_id_example' # str | trace header; can be generated uniformly by APIv4 (optional)

try:
    # Create spot grid
    api_response = api_instance.post_ai_hub_spot_grid_create(spot_grid_create_request, x_gate_service_id=x_gate_service_id, x_gate_app_lang=x_gate_app_lang, x_request_id=x_request_id, x_trace_id=x_trace_id)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling BotApi->post_ai_hub_spot_grid_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spot_grid_create_request** | [**SpotGridCreateRequest**](SpotGridCreateRequest.md)|  | 
 **x_gate_service_id** | **str**| Call source identifier; injected by APIv4 if necessary | [optional] 
 **x_gate_app_lang** | **str**| Language context, such as &#x60;zh-CN&#x60; / &#x60;en-US&#x60; | [optional] 
 **x_request_id** | **str**| Request link ID; caller can transmit transparently | [optional] 
 **x_trace_id** | **str**| trace header; can be generated uniformly by APIv4 | [optional] 

### Return type

[**AIHubCreateSuccessResponse**](AIHubCreateSuccessResponse.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Unified business response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_ai_hub_margin_grid_create**
> AIHubCreateSuccessResponse post_ai_hub_margin_grid_create(margin_grid_create_request, x_gate_service_id=x_gate_service_id, x_gate_app_lang=x_gate_app_lang, x_request_id=x_request_id, x_trace_id=x_trace_id)

Create a lever grid

Create a leverage grid strategy based on the passed parameters.

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
api_instance = gate_api.BotApi(api_client)
margin_grid_create_request = gate_api.MarginGridCreateRequest() # MarginGridCreateRequest | 
x_gate_service_id = 'x_gate_service_id_example' # str | Call source identifier; injected by APIv4 if necessary (optional)
x_gate_app_lang = 'x_gate_app_lang_example' # str | Language context, such as `zh-CN` / `en-US` (optional)
x_request_id = 'x_request_id_example' # str | Request link ID; caller can transmit transparently (optional)
x_trace_id = 'x_trace_id_example' # str | trace header; can be generated uniformly by APIv4 (optional)

try:
    # Create a lever grid
    api_response = api_instance.post_ai_hub_margin_grid_create(margin_grid_create_request, x_gate_service_id=x_gate_service_id, x_gate_app_lang=x_gate_app_lang, x_request_id=x_request_id, x_trace_id=x_trace_id)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling BotApi->post_ai_hub_margin_grid_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **margin_grid_create_request** | [**MarginGridCreateRequest**](MarginGridCreateRequest.md)|  | 
 **x_gate_service_id** | **str**| Call source identifier; injected by APIv4 if necessary | [optional] 
 **x_gate_app_lang** | **str**| Language context, such as &#x60;zh-CN&#x60; / &#x60;en-US&#x60; | [optional] 
 **x_request_id** | **str**| Request link ID; caller can transmit transparently | [optional] 
 **x_trace_id** | **str**| trace header; can be generated uniformly by APIv4 | [optional] 

### Return type

[**AIHubCreateSuccessResponse**](AIHubCreateSuccessResponse.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Unified business response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_ai_hub_infinite_grid_create**
> AIHubCreateSuccessResponse post_ai_hub_infinite_grid_create(infinite_grid_create_request, x_gate_service_id=x_gate_service_id, x_gate_app_lang=x_gate_app_lang, x_request_id=x_request_id, x_trace_id=x_trace_id)

Create infinite grid

Create an infinite grid strategy based on passed parameters.

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
api_instance = gate_api.BotApi(api_client)
infinite_grid_create_request = gate_api.InfiniteGridCreateRequest() # InfiniteGridCreateRequest | 
x_gate_service_id = 'x_gate_service_id_example' # str | Call source identifier; injected by APIv4 if necessary (optional)
x_gate_app_lang = 'x_gate_app_lang_example' # str | Language context, such as `zh-CN` / `en-US` (optional)
x_request_id = 'x_request_id_example' # str | Request link ID; caller can transmit transparently (optional)
x_trace_id = 'x_trace_id_example' # str | trace header; can be generated uniformly by APIv4 (optional)

try:
    # Create infinite grid
    api_response = api_instance.post_ai_hub_infinite_grid_create(infinite_grid_create_request, x_gate_service_id=x_gate_service_id, x_gate_app_lang=x_gate_app_lang, x_request_id=x_request_id, x_trace_id=x_trace_id)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling BotApi->post_ai_hub_infinite_grid_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **infinite_grid_create_request** | [**InfiniteGridCreateRequest**](InfiniteGridCreateRequest.md)|  | 
 **x_gate_service_id** | **str**| Call source identifier; injected by APIv4 if necessary | [optional] 
 **x_gate_app_lang** | **str**| Language context, such as &#x60;zh-CN&#x60; / &#x60;en-US&#x60; | [optional] 
 **x_request_id** | **str**| Request link ID; caller can transmit transparently | [optional] 
 **x_trace_id** | **str**| trace header; can be generated uniformly by APIv4 | [optional] 

### Return type

[**AIHubCreateSuccessResponse**](AIHubCreateSuccessResponse.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Unified business response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_ai_hub_futures_grid_create**
> AIHubCreateSuccessResponse post_ai_hub_futures_grid_create(futures_grid_create_request, x_gate_service_id=x_gate_service_id, x_gate_app_lang=x_gate_app_lang, x_request_id=x_request_id, x_trace_id=x_trace_id)

Create a contract grid

Create a contract grid strategy based on the incoming parameters.

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
api_instance = gate_api.BotApi(api_client)
futures_grid_create_request = gate_api.FuturesGridCreateRequest() # FuturesGridCreateRequest | 
x_gate_service_id = 'x_gate_service_id_example' # str | Call source identifier; injected by APIv4 if necessary (optional)
x_gate_app_lang = 'x_gate_app_lang_example' # str | Language context, such as `zh-CN` / `en-US` (optional)
x_request_id = 'x_request_id_example' # str | Request link ID; caller can transmit transparently (optional)
x_trace_id = 'x_trace_id_example' # str | trace header; can be generated uniformly by APIv4 (optional)

try:
    # Create a contract grid
    api_response = api_instance.post_ai_hub_futures_grid_create(futures_grid_create_request, x_gate_service_id=x_gate_service_id, x_gate_app_lang=x_gate_app_lang, x_request_id=x_request_id, x_trace_id=x_trace_id)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling BotApi->post_ai_hub_futures_grid_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **futures_grid_create_request** | [**FuturesGridCreateRequest**](FuturesGridCreateRequest.md)|  | 
 **x_gate_service_id** | **str**| Call source identifier; injected by APIv4 if necessary | [optional] 
 **x_gate_app_lang** | **str**| Language context, such as &#x60;zh-CN&#x60; / &#x60;en-US&#x60; | [optional] 
 **x_request_id** | **str**| Request link ID; caller can transmit transparently | [optional] 
 **x_trace_id** | **str**| trace header; can be generated uniformly by APIv4 | [optional] 

### Return type

[**AIHubCreateSuccessResponse**](AIHubCreateSuccessResponse.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Unified business response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_ai_hub_spot_martingale_create**
> AIHubCreateSuccessResponse post_ai_hub_spot_martingale_create(spot_martingale_create_request, x_gate_service_id=x_gate_service_id, x_gate_app_lang=x_gate_app_lang, x_request_id=x_request_id, x_trace_id=x_trace_id)

Create Spot Martin

Create a spot martingale strategy from the given parameters. Stop-loss semantics match the app / `MartingaleBot`: - Use **`create_params.stop_loss_per_cycle`** (ratio per round as a decimal string) for creation-side stop-loss; **do not** use `stop_loss_price` for creation logic. - Stop-loss prices shown on detail pages are computed per round by the engine; creation accepts optional **`create_params.trigger_price`** (trigger price).

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
api_instance = gate_api.BotApi(api_client)
spot_martingale_create_request = gate_api.SpotMartingaleCreateRequest() # SpotMartingaleCreateRequest | 
x_gate_service_id = 'x_gate_service_id_example' # str | Call source identifier; injected by APIv4 if necessary (optional)
x_gate_app_lang = 'x_gate_app_lang_example' # str | Language context, such as `zh-CN` / `en-US` (optional)
x_request_id = 'x_request_id_example' # str | Request link ID; caller can transmit transparently (optional)
x_trace_id = 'x_trace_id_example' # str | trace header; can be generated uniformly by APIv4 (optional)

try:
    # Create Spot Martin
    api_response = api_instance.post_ai_hub_spot_martingale_create(spot_martingale_create_request, x_gate_service_id=x_gate_service_id, x_gate_app_lang=x_gate_app_lang, x_request_id=x_request_id, x_trace_id=x_trace_id)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling BotApi->post_ai_hub_spot_martingale_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spot_martingale_create_request** | [**SpotMartingaleCreateRequest**](SpotMartingaleCreateRequest.md)|  | 
 **x_gate_service_id** | **str**| Call source identifier; injected by APIv4 if necessary | [optional] 
 **x_gate_app_lang** | **str**| Language context, such as &#x60;zh-CN&#x60; / &#x60;en-US&#x60; | [optional] 
 **x_request_id** | **str**| Request link ID; caller can transmit transparently | [optional] 
 **x_trace_id** | **str**| trace header; can be generated uniformly by APIv4 | [optional] 

### Return type

[**AIHubCreateSuccessResponse**](AIHubCreateSuccessResponse.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Unified business response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_ai_hub_contract_martingale_create**
> AIHubCreateSuccessResponse post_ai_hub_contract_martingale_create(contract_martingale_create_request, x_gate_service_id=x_gate_service_id, x_gate_app_lang=x_gate_app_lang, x_request_id=x_request_id, x_trace_id=x_trace_id)

Create contract martin

Create a contract Martin strategy based on the input parameters.

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
api_instance = gate_api.BotApi(api_client)
contract_martingale_create_request = gate_api.ContractMartingaleCreateRequest() # ContractMartingaleCreateRequest | 
x_gate_service_id = 'x_gate_service_id_example' # str | Call source identifier; injected by APIv4 if necessary (optional)
x_gate_app_lang = 'x_gate_app_lang_example' # str | Language context, such as `zh-CN` / `en-US` (optional)
x_request_id = 'x_request_id_example' # str | Request link ID; caller can transmit transparently (optional)
x_trace_id = 'x_trace_id_example' # str | trace header; can be generated uniformly by APIv4 (optional)

try:
    # Create contract martin
    api_response = api_instance.post_ai_hub_contract_martingale_create(contract_martingale_create_request, x_gate_service_id=x_gate_service_id, x_gate_app_lang=x_gate_app_lang, x_request_id=x_request_id, x_trace_id=x_trace_id)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling BotApi->post_ai_hub_contract_martingale_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_martingale_create_request** | [**ContractMartingaleCreateRequest**](ContractMartingaleCreateRequest.md)|  | 
 **x_gate_service_id** | **str**| Call source identifier; injected by APIv4 if necessary | [optional] 
 **x_gate_app_lang** | **str**| Language context, such as &#x60;zh-CN&#x60; / &#x60;en-US&#x60; | [optional] 
 **x_request_id** | **str**| Request link ID; caller can transmit transparently | [optional] 
 **x_trace_id** | **str**| trace header; can be generated uniformly by APIv4 | [optional] 

### Return type

[**AIHubCreateSuccessResponse**](AIHubCreateSuccessResponse.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Unified business response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ai_hub_portfolio_running**
> AIHubPortfolioRunningSuccessResponse get_ai_hub_portfolio_running(strategy_type=strategy_type, market=market, page=page, page_size=page_size, x_gate_service_id=x_gate_service_id, x_gate_app_lang=x_gate_app_lang, x_request_id=x_request_id, x_trace_id=x_trace_id)

Query the list of running policies

Query the list of AIHub strategies currently running by the user, and support filtering by strategy type, trading pair and paging conditions.

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
api_instance = gate_api.BotApi(api_client)
strategy_type = 'strategy_type_example' # str | Filter by policy type (optional)
market = 'market_example' # str | Filter by trading pair (optional)
page = 1 # int | Page number, default 1 (optional) (default to 1)
page_size = 20 # int | Paging size, default 20, maximum 50 (optional) (default to 20)
x_gate_service_id = 'x_gate_service_id_example' # str | Call source identifier; injected by APIv4 if necessary (optional)
x_gate_app_lang = 'x_gate_app_lang_example' # str | Language context, such as `zh-CN` / `en-US` (optional)
x_request_id = 'x_request_id_example' # str | Request link ID; caller can transmit transparently (optional)
x_trace_id = 'x_trace_id_example' # str | trace header; can be generated uniformly by APIv4 (optional)

try:
    # Query the list of running policies
    api_response = api_instance.get_ai_hub_portfolio_running(strategy_type=strategy_type, market=market, page=page, page_size=page_size, x_gate_service_id=x_gate_service_id, x_gate_app_lang=x_gate_app_lang, x_request_id=x_request_id, x_trace_id=x_trace_id)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling BotApi->get_ai_hub_portfolio_running: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **strategy_type** | **str**| Filter by policy type | [optional] 
 **market** | **str**| Filter by trading pair | [optional] 
 **page** | **int**| Page number, default 1 | [optional] [default to 1]
 **page_size** | **int**| Paging size, default 20, maximum 50 | [optional] [default to 20]
 **x_gate_service_id** | **str**| Call source identifier; injected by APIv4 if necessary | [optional] 
 **x_gate_app_lang** | **str**| Language context, such as &#x60;zh-CN&#x60; / &#x60;en-US&#x60; | [optional] 
 **x_request_id** | **str**| Request link ID; caller can transmit transparently | [optional] 
 **x_trace_id** | **str**| trace header; can be generated uniformly by APIv4 | [optional] 

### Return type

[**AIHubPortfolioRunningSuccessResponse**](AIHubPortfolioRunningSuccessResponse.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Unified business response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ai_hub_portfolio_detail**
> AIHubPortfolioDetailSuccessResponse get_ai_hub_portfolio_detail(strategy_id, strategy_type, x_gate_service_id=x_gate_service_id, x_gate_app_lang=x_gate_app_lang, x_request_id=x_request_id, x_trace_id=x_trace_id)

Query order policy details

Both `strategy_id` and `strategy_type` must be passed in the request, where `strategy_type` is used to distribute to the underlying detailed implementation by strategy type.

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
api_instance = gate_api.BotApi(api_client)
strategy_id = 'strategy_id_example' # str | Policy ID
strategy_type = 'strategy_type_example' # str | Policy type; used for underlying detail distribution
x_gate_service_id = 'x_gate_service_id_example' # str | Call source identifier; injected by APIv4 if necessary (optional)
x_gate_app_lang = 'x_gate_app_lang_example' # str | Language context, such as `zh-CN` / `en-US` (optional)
x_request_id = 'x_request_id_example' # str | Request link ID; caller can transmit transparently (optional)
x_trace_id = 'x_trace_id_example' # str | trace header; can be generated uniformly by APIv4 (optional)

try:
    # Query order policy details
    api_response = api_instance.get_ai_hub_portfolio_detail(strategy_id, strategy_type, x_gate_service_id=x_gate_service_id, x_gate_app_lang=x_gate_app_lang, x_request_id=x_request_id, x_trace_id=x_trace_id)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling BotApi->get_ai_hub_portfolio_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **strategy_id** | **str**| Policy ID | 
 **strategy_type** | **str**| Policy type; used for underlying detail distribution | 
 **x_gate_service_id** | **str**| Call source identifier; injected by APIv4 if necessary | [optional] 
 **x_gate_app_lang** | **str**| Language context, such as &#x60;zh-CN&#x60; / &#x60;en-US&#x60; | [optional] 
 **x_request_id** | **str**| Request link ID; caller can transmit transparently | [optional] 
 **x_trace_id** | **str**| trace header; can be generated uniformly by APIv4 | [optional] 

### Return type

[**AIHubPortfolioDetailSuccessResponse**](AIHubPortfolioDetailSuccessResponse.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Unified business response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_ai_hub_portfolio_stop**
> AIHubPortfolioStopSuccessResponse post_ai_hub_portfolio_stop(ai_hub_portfolio_stop_request, x_gate_service_id=x_gate_service_id, x_gate_app_lang=x_gate_app_lang, x_request_id=x_request_id, x_trace_id=x_trace_id)

Terminate a single running policy

Only one policy is allowed to be terminated per request. Risk warning and secondary confirmation are borne by the upper layer of OpenClaw; this interface is only responsible for executing stop.

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
api_instance = gate_api.BotApi(api_client)
ai_hub_portfolio_stop_request = gate_api.AIHubPortfolioStopRequest() # AIHubPortfolioStopRequest | 
x_gate_service_id = 'x_gate_service_id_example' # str | Call source identifier; injected by APIv4 if necessary (optional)
x_gate_app_lang = 'x_gate_app_lang_example' # str | Language context, such as `zh-CN` / `en-US` (optional)
x_request_id = 'x_request_id_example' # str | Request link ID; caller can transmit transparently (optional)
x_trace_id = 'x_trace_id_example' # str | trace header; can be generated uniformly by APIv4 (optional)

try:
    # Terminate a single running policy
    api_response = api_instance.post_ai_hub_portfolio_stop(ai_hub_portfolio_stop_request, x_gate_service_id=x_gate_service_id, x_gate_app_lang=x_gate_app_lang, x_request_id=x_request_id, x_trace_id=x_trace_id)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling BotApi->post_ai_hub_portfolio_stop: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ai_hub_portfolio_stop_request** | [**AIHubPortfolioStopRequest**](AIHubPortfolioStopRequest.md)|  | 
 **x_gate_service_id** | **str**| Call source identifier; injected by APIv4 if necessary | [optional] 
 **x_gate_app_lang** | **str**| Language context, such as &#x60;zh-CN&#x60; / &#x60;en-US&#x60; | [optional] 
 **x_request_id** | **str**| Request link ID; caller can transmit transparently | [optional] 
 **x_trace_id** | **str**| trace header; can be generated uniformly by APIv4 | [optional] 

### Return type

[**AIHubPortfolioStopSuccessResponse**](AIHubPortfolioStopSuccessResponse.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Unified business response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

