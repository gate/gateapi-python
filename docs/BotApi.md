# gate_api.BotApi

All URIs are relative to *https://api.gateio.ws/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_ai_hub_strategy_recommend**](BotApi.md#get_ai_hub_strategy_recommend) | **GET** /bot/strategy/recommend | 获取 AIHub 策略推荐
[**post_ai_hub_spot_grid_create**](BotApi.md#post_ai_hub_spot_grid_create) | **POST** /bot/spot-grid/create | 创建现货网格
[**post_ai_hub_margin_grid_create**](BotApi.md#post_ai_hub_margin_grid_create) | **POST** /bot/margin-grid/create | 创建杠杆网格
[**post_ai_hub_infinite_grid_create**](BotApi.md#post_ai_hub_infinite_grid_create) | **POST** /bot/infinite-grid/create | 创建无限网格
[**post_ai_hub_futures_grid_create**](BotApi.md#post_ai_hub_futures_grid_create) | **POST** /bot/futures-grid/create | 创建合约网格
[**post_ai_hub_spot_martingale_create**](BotApi.md#post_ai_hub_spot_martingale_create) | **POST** /bot/spot-martingale/create | 创建现货马丁
[**post_ai_hub_contract_martingale_create**](BotApi.md#post_ai_hub_contract_martingale_create) | **POST** /bot/contract-martingale/create | 创建合约马丁
[**get_ai_hub_portfolio_running**](BotApi.md#get_ai_hub_portfolio_running) | **GET** /bot/portfolio/running | 查询运行中策略列表
[**get_ai_hub_portfolio_detail**](BotApi.md#get_ai_hub_portfolio_detail) | **GET** /bot/portfolio/detail | 查询单策略详情
[**post_ai_hub_portfolio_stop**](BotApi.md#post_ai_hub_portfolio_stop) | **POST** /bot/portfolio/stop | 终止单个运行中策略


# **get_ai_hub_strategy_recommend**
> AIHubDiscoverSuccessResponse get_ai_hub_strategy_recommend(market=market, strategy_type=strategy_type, direction=direction, invest_amount=invest_amount, scene=scene, refresh_recommendation_id=refresh_recommendation_id, limit=limit, max_drawdown_lte=max_drawdown_lte, backtest_apr_gte=backtest_apr_gte, x_gate_service_id=x_gate_service_id, x_gate_app_lang=x_gate_app_lang, x_request_id=x_request_id, x_trace_id=x_trace_id)

获取 AIHub 策略推荐

discover 域唯一正式接口。  支持场景： - `top1` - `bundle` - `filter` - `refresh`  约束： - 主动推荐池仅包含 `spot_grid`、`futures_grid`、`spot_martingale` - 可返回但不主动推荐 `infinite_grid`、`margin_grid` - 不得返回 `contract_martingale`、`smart-position`、`spot-future-arbitrage` - `scene=filter` 时只允许按 `market`、`backtest_apr_gte`、`max_drawdown_lte` 过滤 - `scene=refresh` 通过 `refresh_recommendation_id` 承接刷新上下文；正式最小格式只要求 `strategy_type|market` - 若上游直接透传上一条推荐的 `recommendation_id`，其中第三段 `backtest_id` 当前会被忽略

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
market = 'market_example' # str | 交易对，例如 `BTC_USDT` (optional)
strategy_type = 'strategy_type_example' # str | 推荐目标策略类型；`contract_martingale` 不允许 (optional)
direction = 'direction_example' # str | 行情方向 (optional)
invest_amount = 'invest_amount_example' # str | 投入金额，字符串透传 (optional)
scene = 'scene_example' # str | 推荐场景；为空时 bot-service 可按实现逻辑自动推断 (optional)
refresh_recommendation_id = 'refresh_recommendation_id_example' # str | 推荐刷新上下文。`scene=refresh` 时使用；当 `scene` 为空但该字段存在时，bot-service 也会自动判定为 `refresh`。 正式最小格式为 `strategy_type|market`；若直接透传上一条推荐的 `recommendation_id`，第三段 `backtest_id` 会被忽略。 (optional)
limit = 56 # int | 返回数量；`scene=filter` 时实际结果最多 10 条 (optional)
max_drawdown_lte = 'max_drawdown_lte_example' # str | 最大回撤上限 (optional)
backtest_apr_gte = 'backtest_apr_gte_example' # str | 回测年化下限 (optional)
x_gate_service_id = 'x_gate_service_id_example' # str | 调用来源标识；如有需要由 APIv4 注入 (optional)
x_gate_app_lang = 'x_gate_app_lang_example' # str | 语言上下文，例如 `zh-CN` / `en-US` (optional)
x_request_id = 'x_request_id_example' # str | 请求链路 ID；调用方可透传 (optional)
x_trace_id = 'x_trace_id_example' # str | trace header；可由 APIv4 统一生成 (optional)

try:
    # 获取 AIHub 策略推荐
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
 **market** | **str**| 交易对，例如 &#x60;BTC_USDT&#x60; | [optional] 
 **strategy_type** | **str**| 推荐目标策略类型；&#x60;contract_martingale&#x60; 不允许 | [optional] 
 **direction** | **str**| 行情方向 | [optional] 
 **invest_amount** | **str**| 投入金额，字符串透传 | [optional] 
 **scene** | **str**| 推荐场景；为空时 bot-service 可按实现逻辑自动推断 | [optional] 
 **refresh_recommendation_id** | **str**| 推荐刷新上下文。&#x60;scene&#x3D;refresh&#x60; 时使用；当 &#x60;scene&#x60; 为空但该字段存在时，bot-service 也会自动判定为 &#x60;refresh&#x60;。 正式最小格式为 &#x60;strategy_type|market&#x60;；若直接透传上一条推荐的 &#x60;recommendation_id&#x60;，第三段 &#x60;backtest_id&#x60; 会被忽略。 | [optional] 
 **limit** | **int**| 返回数量；&#x60;scene&#x3D;filter&#x60; 时实际结果最多 10 条 | [optional] 
 **max_drawdown_lte** | **str**| 最大回撤上限 | [optional] 
 **backtest_apr_gte** | **str**| 回测年化下限 | [optional] 
 **x_gate_service_id** | **str**| 调用来源标识；如有需要由 APIv4 注入 | [optional] 
 **x_gate_app_lang** | **str**| 语言上下文，例如 &#x60;zh-CN&#x60; / &#x60;en-US&#x60; | [optional] 
 **x_request_id** | **str**| 请求链路 ID；调用方可透传 | [optional] 
 **x_trace_id** | **str**| trace header；可由 APIv4 统一生成 | [optional] 

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
**200** | 统一业务响应 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_ai_hub_spot_grid_create**
> AIHubCreateSuccessResponse post_ai_hub_spot_grid_create(spot_grid_create_request, x_gate_service_id=x_gate_service_id, x_gate_app_lang=x_gate_app_lang, x_request_id=x_request_id, x_trace_id=x_trace_id)

创建现货网格

根据传入参数创建现货网格策略。

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
x_gate_service_id = 'x_gate_service_id_example' # str | 调用来源标识；如有需要由 APIv4 注入 (optional)
x_gate_app_lang = 'x_gate_app_lang_example' # str | 语言上下文，例如 `zh-CN` / `en-US` (optional)
x_request_id = 'x_request_id_example' # str | 请求链路 ID；调用方可透传 (optional)
x_trace_id = 'x_trace_id_example' # str | trace header；可由 APIv4 统一生成 (optional)

try:
    # 创建现货网格
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
 **x_gate_service_id** | **str**| 调用来源标识；如有需要由 APIv4 注入 | [optional] 
 **x_gate_app_lang** | **str**| 语言上下文，例如 &#x60;zh-CN&#x60; / &#x60;en-US&#x60; | [optional] 
 **x_request_id** | **str**| 请求链路 ID；调用方可透传 | [optional] 
 **x_trace_id** | **str**| trace header；可由 APIv4 统一生成 | [optional] 

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
**200** | 统一业务响应 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_ai_hub_margin_grid_create**
> AIHubCreateSuccessResponse post_ai_hub_margin_grid_create(margin_grid_create_request, x_gate_service_id=x_gate_service_id, x_gate_app_lang=x_gate_app_lang, x_request_id=x_request_id, x_trace_id=x_trace_id)

创建杠杆网格

根据传入参数创建杠杆网格策略。

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
x_gate_service_id = 'x_gate_service_id_example' # str | 调用来源标识；如有需要由 APIv4 注入 (optional)
x_gate_app_lang = 'x_gate_app_lang_example' # str | 语言上下文，例如 `zh-CN` / `en-US` (optional)
x_request_id = 'x_request_id_example' # str | 请求链路 ID；调用方可透传 (optional)
x_trace_id = 'x_trace_id_example' # str | trace header；可由 APIv4 统一生成 (optional)

try:
    # 创建杠杆网格
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
 **x_gate_service_id** | **str**| 调用来源标识；如有需要由 APIv4 注入 | [optional] 
 **x_gate_app_lang** | **str**| 语言上下文，例如 &#x60;zh-CN&#x60; / &#x60;en-US&#x60; | [optional] 
 **x_request_id** | **str**| 请求链路 ID；调用方可透传 | [optional] 
 **x_trace_id** | **str**| trace header；可由 APIv4 统一生成 | [optional] 

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
**200** | 统一业务响应 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_ai_hub_infinite_grid_create**
> AIHubCreateSuccessResponse post_ai_hub_infinite_grid_create(infinite_grid_create_request, x_gate_service_id=x_gate_service_id, x_gate_app_lang=x_gate_app_lang, x_request_id=x_request_id, x_trace_id=x_trace_id)

创建无限网格

根据传入参数创建无限网格策略。

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
x_gate_service_id = 'x_gate_service_id_example' # str | 调用来源标识；如有需要由 APIv4 注入 (optional)
x_gate_app_lang = 'x_gate_app_lang_example' # str | 语言上下文，例如 `zh-CN` / `en-US` (optional)
x_request_id = 'x_request_id_example' # str | 请求链路 ID；调用方可透传 (optional)
x_trace_id = 'x_trace_id_example' # str | trace header；可由 APIv4 统一生成 (optional)

try:
    # 创建无限网格
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
 **x_gate_service_id** | **str**| 调用来源标识；如有需要由 APIv4 注入 | [optional] 
 **x_gate_app_lang** | **str**| 语言上下文，例如 &#x60;zh-CN&#x60; / &#x60;en-US&#x60; | [optional] 
 **x_request_id** | **str**| 请求链路 ID；调用方可透传 | [optional] 
 **x_trace_id** | **str**| trace header；可由 APIv4 统一生成 | [optional] 

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
**200** | 统一业务响应 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_ai_hub_futures_grid_create**
> AIHubCreateSuccessResponse post_ai_hub_futures_grid_create(futures_grid_create_request, x_gate_service_id=x_gate_service_id, x_gate_app_lang=x_gate_app_lang, x_request_id=x_request_id, x_trace_id=x_trace_id)

创建合约网格

根据传入参数创建合约网格策略。

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
x_gate_service_id = 'x_gate_service_id_example' # str | 调用来源标识；如有需要由 APIv4 注入 (optional)
x_gate_app_lang = 'x_gate_app_lang_example' # str | 语言上下文，例如 `zh-CN` / `en-US` (optional)
x_request_id = 'x_request_id_example' # str | 请求链路 ID；调用方可透传 (optional)
x_trace_id = 'x_trace_id_example' # str | trace header；可由 APIv4 统一生成 (optional)

try:
    # 创建合约网格
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
 **x_gate_service_id** | **str**| 调用来源标识；如有需要由 APIv4 注入 | [optional] 
 **x_gate_app_lang** | **str**| 语言上下文，例如 &#x60;zh-CN&#x60; / &#x60;en-US&#x60; | [optional] 
 **x_request_id** | **str**| 请求链路 ID；调用方可透传 | [optional] 
 **x_trace_id** | **str**| trace header；可由 APIv4 统一生成 | [optional] 

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
**200** | 统一业务响应 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_ai_hub_spot_martingale_create**
> AIHubCreateSuccessResponse post_ai_hub_spot_martingale_create(spot_martingale_create_request, x_gate_service_id=x_gate_service_id, x_gate_app_lang=x_gate_app_lang, x_request_id=x_request_id, x_trace_id=x_trace_id)

创建现货马丁

根据传入参数创建现货马丁策略。

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
x_gate_service_id = 'x_gate_service_id_example' # str | 调用来源标识；如有需要由 APIv4 注入 (optional)
x_gate_app_lang = 'x_gate_app_lang_example' # str | 语言上下文，例如 `zh-CN` / `en-US` (optional)
x_request_id = 'x_request_id_example' # str | 请求链路 ID；调用方可透传 (optional)
x_trace_id = 'x_trace_id_example' # str | trace header；可由 APIv4 统一生成 (optional)

try:
    # 创建现货马丁
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
 **x_gate_service_id** | **str**| 调用来源标识；如有需要由 APIv4 注入 | [optional] 
 **x_gate_app_lang** | **str**| 语言上下文，例如 &#x60;zh-CN&#x60; / &#x60;en-US&#x60; | [optional] 
 **x_request_id** | **str**| 请求链路 ID；调用方可透传 | [optional] 
 **x_trace_id** | **str**| trace header；可由 APIv4 统一生成 | [optional] 

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
**200** | 统一业务响应 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_ai_hub_contract_martingale_create**
> AIHubCreateSuccessResponse post_ai_hub_contract_martingale_create(contract_martingale_create_request, x_gate_service_id=x_gate_service_id, x_gate_app_lang=x_gate_app_lang, x_request_id=x_request_id, x_trace_id=x_trace_id)

创建合约马丁

根据传入参数创建合约马丁策略。

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
x_gate_service_id = 'x_gate_service_id_example' # str | 调用来源标识；如有需要由 APIv4 注入 (optional)
x_gate_app_lang = 'x_gate_app_lang_example' # str | 语言上下文，例如 `zh-CN` / `en-US` (optional)
x_request_id = 'x_request_id_example' # str | 请求链路 ID；调用方可透传 (optional)
x_trace_id = 'x_trace_id_example' # str | trace header；可由 APIv4 统一生成 (optional)

try:
    # 创建合约马丁
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
 **x_gate_service_id** | **str**| 调用来源标识；如有需要由 APIv4 注入 | [optional] 
 **x_gate_app_lang** | **str**| 语言上下文，例如 &#x60;zh-CN&#x60; / &#x60;en-US&#x60; | [optional] 
 **x_request_id** | **str**| 请求链路 ID；调用方可透传 | [optional] 
 **x_trace_id** | **str**| trace header；可由 APIv4 统一生成 | [optional] 

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
**200** | 统一业务响应 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ai_hub_portfolio_running**
> AIHubPortfolioRunningSuccessResponse get_ai_hub_portfolio_running(strategy_type=strategy_type, market=market, page=page, page_size=page_size, x_gate_service_id=x_gate_service_id, x_gate_app_lang=x_gate_app_lang, x_request_id=x_request_id, x_trace_id=x_trace_id)

查询运行中策略列表

查询当前用户运行中的 AIHub 策略列表，支持按策略类型、交易对和分页条件过滤。

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
strategy_type = 'strategy_type_example' # str | 按策略类型过滤 (optional)
market = 'market_example' # str | 按交易对过滤 (optional)
page = 1 # int | 页码，默认 1 (optional) (default to 1)
page_size = 20 # int | 分页大小，默认 20，最大 50 (optional) (default to 20)
x_gate_service_id = 'x_gate_service_id_example' # str | 调用来源标识；如有需要由 APIv4 注入 (optional)
x_gate_app_lang = 'x_gate_app_lang_example' # str | 语言上下文，例如 `zh-CN` / `en-US` (optional)
x_request_id = 'x_request_id_example' # str | 请求链路 ID；调用方可透传 (optional)
x_trace_id = 'x_trace_id_example' # str | trace header；可由 APIv4 统一生成 (optional)

try:
    # 查询运行中策略列表
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
 **strategy_type** | **str**| 按策略类型过滤 | [optional] 
 **market** | **str**| 按交易对过滤 | [optional] 
 **page** | **int**| 页码，默认 1 | [optional] [default to 1]
 **page_size** | **int**| 分页大小，默认 20，最大 50 | [optional] [default to 20]
 **x_gate_service_id** | **str**| 调用来源标识；如有需要由 APIv4 注入 | [optional] 
 **x_gate_app_lang** | **str**| 语言上下文，例如 &#x60;zh-CN&#x60; / &#x60;en-US&#x60; | [optional] 
 **x_request_id** | **str**| 请求链路 ID；调用方可透传 | [optional] 
 **x_trace_id** | **str**| trace header；可由 APIv4 统一生成 | [optional] 

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
**200** | 统一业务响应 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ai_hub_portfolio_detail**
> AIHubPortfolioDetailSuccessResponse get_ai_hub_portfolio_detail(strategy_id, strategy_type, x_gate_service_id=x_gate_service_id, x_gate_app_lang=x_gate_app_lang, x_request_id=x_request_id, x_trace_id=x_trace_id)

查询单策略详情

请求中必须同时传 `strategy_id` 与 `strategy_type`，其中 `strategy_type` 用于按策略类型分发到底层详情实现。

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
strategy_id = 'strategy_id_example' # str | 策略 ID
strategy_type = 'strategy_type_example' # str | 策略类型；用于底层详情分发
x_gate_service_id = 'x_gate_service_id_example' # str | 调用来源标识；如有需要由 APIv4 注入 (optional)
x_gate_app_lang = 'x_gate_app_lang_example' # str | 语言上下文，例如 `zh-CN` / `en-US` (optional)
x_request_id = 'x_request_id_example' # str | 请求链路 ID；调用方可透传 (optional)
x_trace_id = 'x_trace_id_example' # str | trace header；可由 APIv4 统一生成 (optional)

try:
    # 查询单策略详情
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
 **strategy_id** | **str**| 策略 ID | 
 **strategy_type** | **str**| 策略类型；用于底层详情分发 | 
 **x_gate_service_id** | **str**| 调用来源标识；如有需要由 APIv4 注入 | [optional] 
 **x_gate_app_lang** | **str**| 语言上下文，例如 &#x60;zh-CN&#x60; / &#x60;en-US&#x60; | [optional] 
 **x_request_id** | **str**| 请求链路 ID；调用方可透传 | [optional] 
 **x_trace_id** | **str**| trace header；可由 APIv4 统一生成 | [optional] 

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
**200** | 统一业务响应 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_ai_hub_portfolio_stop**
> AIHubPortfolioStopSuccessResponse post_ai_hub_portfolio_stop(ai_hub_portfolio_stop_request, x_gate_service_id=x_gate_service_id, x_gate_app_lang=x_gate_app_lang, x_request_id=x_request_id, x_trace_id=x_trace_id)

终止单个运行中策略

单次请求只允许终止一个策略。 风险提示与二次确认由 OpenClaw 上层承担；本接口只负责执行 stop。

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
x_gate_service_id = 'x_gate_service_id_example' # str | 调用来源标识；如有需要由 APIv4 注入 (optional)
x_gate_app_lang = 'x_gate_app_lang_example' # str | 语言上下文，例如 `zh-CN` / `en-US` (optional)
x_request_id = 'x_request_id_example' # str | 请求链路 ID；调用方可透传 (optional)
x_trace_id = 'x_trace_id_example' # str | trace header；可由 APIv4 统一生成 (optional)

try:
    # 终止单个运行中策略
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
 **x_gate_service_id** | **str**| 调用来源标识；如有需要由 APIv4 注入 | [optional] 
 **x_gate_app_lang** | **str**| 语言上下文，例如 &#x60;zh-CN&#x60; / &#x60;en-US&#x60; | [optional] 
 **x_request_id** | **str**| 请求链路 ID；调用方可透传 | [optional] 
 **x_trace_id** | **str**| trace header；可由 APIv4 统一生成 | [optional] 

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
**200** | 统一业务响应 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

