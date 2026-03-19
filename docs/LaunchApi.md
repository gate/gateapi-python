# gate_api.LaunchApi

All URIs are relative to *https://api.gateio.ws/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_launch_pool_projects**](LaunchApi.md#list_launch_pool_projects) | **GET** /launch/project-list | Query LaunchPool project list
[**create_launch_pool_order**](LaunchApi.md#create_launch_pool_order) | **POST** /launch/create-order | Create LaunchPool staking order
[**redeem_launch_pool**](LaunchApi.md#redeem_launch_pool) | **POST** /launch/redeem | Redeem LaunchPool staked assets
[**list_launch_pool_pledge_records**](LaunchApi.md#list_launch_pool_pledge_records) | **GET** /launch/user-pledge-records | Query user pledge records
[**list_launch_pool_reward_records**](LaunchApi.md#list_launch_pool_reward_records) | **GET** /launch/get-user-reward-records | Query user reward records


# **list_launch_pool_projects**
> list[LaunchPoolV4Project] list_launch_pool_projects(status=status, mortgage_coin=mortgage_coin, search_coin=search_coin, limit_rule=limit_rule, sort_type=sort_type, page=page, page_size=page_size)

Query LaunchPool project list

Retrieve the list of available LaunchPool projects, including basic project information and reward pool configuration. This endpoint does not require user authentication.

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
api_instance = gate_api.LaunchApi(api_client)
status = 56 # int | Filter by project status: 0 for all, 1 for ongoing, 2 for warming up, 3 for ended, 4 for ongoing and warming up (optional)
mortgage_coin = 'mortgage_coin_example' # str | Exact match by staking currency (optional)
search_coin = 'search_coin_example' # str | Fuzzy match by reward currency and name (optional)
limit_rule = 56 # int | Limit rule: 0 for regular pool, 1 for beginner pool (optional)
sort_type = 56 # int | Sort type: 1 for max APR descending, 2 for max APR ascending (optional)
page = 1 # int | Page number, default 1 (optional) (default to 1)
page_size = 10 # int | Number of items per page, default 10, maximum 30 (optional) (default to 10)

try:
    # Query LaunchPool project list
    api_response = api_instance.list_launch_pool_projects(status=status, mortgage_coin=mortgage_coin, search_coin=search_coin, limit_rule=limit_rule, sort_type=sort_type, page=page, page_size=page_size)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling LaunchApi->list_launch_pool_projects: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **int**| Filter by project status: 0 for all, 1 for ongoing, 2 for warming up, 3 for ended, 4 for ongoing and warming up | [optional] 
 **mortgage_coin** | **str**| Exact match by staking currency | [optional] 
 **search_coin** | **str**| Fuzzy match by reward currency and name | [optional] 
 **limit_rule** | **int**| Limit rule: 0 for regular pool, 1 for beginner pool | [optional] 
 **sort_type** | **int**| Sort type: 1 for max APR descending, 2 for max APR ascending | [optional] 
 **page** | **int**| Page number, default 1 | [optional] [default to 1]
 **page_size** | **int**| Number of items per page, default 10, maximum 30 | [optional] [default to 10]

### Return type

[**list[LaunchPoolV4Project]**](LaunchPoolV4Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returns project list |  -  |
**400** | Invalid request parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_launch_pool_order**
> LaunchPoolV4CreateOrderResponse create_launch_pool_order(create_order_v4)

Create LaunchPool staking order

Create a new staking order for asset staking mining. This endpoint requires API Key signature authentication.

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
api_instance = gate_api.LaunchApi(api_client)
create_order_v4 = gate_api.CreateOrderV4() # CreateOrderV4 | 

try:
    # Create LaunchPool staking order
    api_response = api_instance.create_launch_pool_order(create_order_v4)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling LaunchApi->create_launch_pool_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_order_v4** | [**CreateOrderV4**](CreateOrderV4.md)|  | 

### Return type

[**LaunchPoolV4CreateOrderResponse**](LaunchPoolV4CreateOrderResponse.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created staking order |  -  |
**400** | Invalid request parameters |  -  |
**401** | User not authenticated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **redeem_launch_pool**
> InlineResponse20010 redeem_launch_pool(redeem_v4)

Redeem LaunchPool staked assets

Redeem staked assets and end staking mining. This endpoint requires API Key signature authentication.

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
api_instance = gate_api.LaunchApi(api_client)
redeem_v4 = gate_api.RedeemV4() # RedeemV4 | 

try:
    # Redeem LaunchPool staked assets
    api_response = api_instance.redeem_launch_pool(redeem_v4)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling LaunchApi->redeem_launch_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **redeem_v4** | [**RedeemV4**](RedeemV4.md)|  | 

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully redeemed pledged assets |  -  |
**400** | Invalid request parameters |  -  |
**401** | User not authenticated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_launch_pool_pledge_records**
> list[LaunchPoolV4PledgeRecord] list_launch_pool_pledge_records(page=page, page_size=page_size, type=type, start_time=start_time, end_time=end_time, coin=coin)

Query user pledge records

Query user's staking and redemption operation records. This endpoint requires user authentication.

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
api_instance = gate_api.LaunchApi(api_client)
page = 1 # int | Page number, default 1 (optional) (default to 1)
page_size = 10 # int | Number of items per page, maximum 30 (optional) (default to 10)
type = 56 # int | Type: 1 for pledge, 2 for redemption (optional)
start_time = '2026-03-17 00:00:00' # str | Start time, format: YYYY-MM-DD HH:MM:SS (optional)
end_time = '2026-03-17 23:59:59' # str | End time, format: YYYY-MM-DD HH:MM:SS (optional)
coin = 'coin_example' # str | Collateral currency (optional)

try:
    # Query user pledge records
    api_response = api_instance.list_launch_pool_pledge_records(page=page, page_size=page_size, type=type, start_time=start_time, end_time=end_time, coin=coin)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling LaunchApi->list_launch_pool_pledge_records: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number, default 1 | [optional] [default to 1]
 **page_size** | **int**| Number of items per page, maximum 30 | [optional] [default to 10]
 **type** | **int**| Type: 1 for pledge, 2 for redemption | [optional] 
 **start_time** | **str**| Start time, format: YYYY-MM-DD HH:MM:SS | [optional] 
 **end_time** | **str**| End time, format: YYYY-MM-DD HH:MM:SS | [optional] 
 **coin** | **str**| Collateral currency | [optional] 

### Return type

[**list[LaunchPoolV4PledgeRecord]**](LaunchPoolV4PledgeRecord.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returns user staking records |  -  |
**400** | Invalid request parameters |  -  |
**401** | User not authenticated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_launch_pool_reward_records**
> list[LaunchPoolV4RewardRecord] list_launch_pool_reward_records(page=page, page_size=page_size, start_time=start_time, end_time=end_time, coin=coin)

Query user reward records

Query the user's staking reward records. This endpoint requires user authentication.

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
api_instance = gate_api.LaunchApi(api_client)
page = 1 # int | Page number, default 1 (optional) (default to 1)
page_size = 10 # int | Number of items per page, maximum 30 (optional) (default to 10)
start_time = 56 # int | Start timestamp (optional)
end_time = 56 # int | End Timestamp (optional)
coin = 'coin_example' # str | Reward currency (optional)

try:
    # Query user reward records
    api_response = api_instance.list_launch_pool_reward_records(page=page, page_size=page_size, start_time=start_time, end_time=end_time, coin=coin)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling LaunchApi->list_launch_pool_reward_records: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number, default 1 | [optional] [default to 1]
 **page_size** | **int**| Number of items per page, maximum 30 | [optional] [default to 10]
 **start_time** | **int**| Start timestamp | [optional] 
 **end_time** | **int**| End Timestamp | [optional] 
 **coin** | **str**| Reward currency | [optional] 

### Return type

[**list[LaunchPoolV4RewardRecord]**](LaunchPoolV4RewardRecord.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returns user reward records |  -  |
**400** | Invalid request parameters |  -  |
**401** | User not authenticated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

