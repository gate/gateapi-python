# gate_api.SquareApi

All URIs are relative to *https://api.gateio.ws/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_square_ai_search**](SquareApi.md#list_square_ai_search) | **GET** /social/message/search | AI MCP Dynamic Search
[**list_live_replay**](SquareApi.md#list_live_replay) | **GET** /social/live/tag_coin_live_replay | Gate AI Assistant live stream data retrieval


# **list_square_ai_search**
> InlineResponse2008 list_square_ai_search(keyword=keyword, currency=currency, time_range=time_range, sort=sort, limit=limit, page=page)

AI MCP Dynamic Search

Dynamic search endpoint for AI MCP platform. All parameters are passed via query string. Returns simplified fields. Designed for LLM function calling / MCP tool scenarios.

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
api_instance = gate_api.SquareApi(api_client)
keyword = 'keyword_example' # str | Search keyword (currency name or content keyword, e.g., BTC, ETH) (optional)
currency = 'currency_example' # str | Filter by currency (exact currency code, e.g., BTC, ETH, SOL) (optional)
time_range = 0 # int | Time range: 0 = unlimited (default), 1 = last day, 2 = last week, 3 = last month (optional) (default to 0)
sort = 0 # int | Sort order: 0 = most popular (default), 1 = latest (optional) (default to 0)
limit = 10 # int | Return count, 1-50, default 10 (optional) (default to 10)
page = 1 # int | Page number (optional) (default to 1)

try:
    # AI MCP Dynamic Search
    api_response = api_instance.list_square_ai_search(keyword=keyword, currency=currency, time_range=time_range, sort=sort, limit=limit, page=page)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling SquareApi->list_square_ai_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **keyword** | **str**| Search keyword (currency name or content keyword, e.g., BTC, ETH) | [optional] 
 **currency** | **str**| Filter by currency (exact currency code, e.g., BTC, ETH, SOL) | [optional] 
 **time_range** | **int**| Time range: 0 &#x3D; unlimited (default), 1 &#x3D; last day, 2 &#x3D; last week, 3 &#x3D; last month | [optional] [default to 0]
 **sort** | **int**| Sort order: 0 &#x3D; most popular (default), 1 &#x3D; latest | [optional] [default to 0]
 **limit** | **int**| Return count, 1-50, default 10 | [optional] [default to 10]
 **page** | **int**| Page number | [optional] [default to 1]

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The endpoint always returns HTTP 200. Business results are distinguished by the code field (code&#x3D;0 means success) |  -  |
**400** | Invalid request parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_live_replay**
> InlineResponse2009 list_live_replay(tag=tag, coin=coin, sort=sort, limit=limit)

Gate AI Assistant live stream data retrieval

AI assistant live stream/replay search endpoint. Filters live rooms or replay videos by business tags and currency. Each record in the returned list is distinguished by content_type: streaming = live broadcast (live field has value), video = replay video (video field has value). The number of results is controlled by the limit parameter (max 10), no additional pagination needed.

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
api_instance = gate_api.SquareApi(api_client)
tag = 'tag_example' # str | Business type filter. Available values: Market Analysis, Hot Topics, Blockchain, Others (optional)
coin = 'coin_example' # str | Filter by currency name (e.g., BTC, ETH) (optional)
sort = 'hot' # str | Sort order: hot = most popular (default), new = latest (optional) (default to 'hot')
limit = 3 # int | Return count, 1-10, default 3 (optional) (default to 3)

try:
    # Gate AI Assistant live stream data retrieval
    api_response = api_instance.list_live_replay(tag=tag, coin=coin, sort=sort, limit=limit)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling SquareApi->list_live_replay: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag** | **str**| Business type filter. Available values: Market Analysis, Hot Topics, Blockchain, Others | [optional] 
 **coin** | **str**| Filter by currency name (e.g., BTC, ETH) | [optional] 
 **sort** | **str**| Sort order: hot &#x3D; most popular (default), new &#x3D; latest | [optional] [default to &#39;hot&#39;]
 **limit** | **int**| Return count, 1-10, default 3 | [optional] [default to 3]

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The endpoint always returns HTTP 200. Business results are distinguished by the code field (code&#x3D;200 means success) |  -  |
**400** | Invalid request parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

