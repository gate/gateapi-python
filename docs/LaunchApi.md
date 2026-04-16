# gate_api.LaunchApi

All URIs are relative to *https://api.gateio.ws/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_launch_pool_projects**](LaunchApi.md#list_launch_pool_projects) | **GET** /launch/project-list | Query LaunchPool project list
[**create_launch_pool_order**](LaunchApi.md#create_launch_pool_order) | **POST** /launch/create-order | Create LaunchPool staking order
[**redeem_launch_pool**](LaunchApi.md#redeem_launch_pool) | **POST** /launch/redeem | Redeem LaunchPool staked assets
[**list_launch_pool_pledge_records**](LaunchApi.md#list_launch_pool_pledge_records) | **GET** /launch/user-pledge-records | Query user pledge records
[**list_launch_pool_reward_records**](LaunchApi.md#list_launch_pool_reward_records) | **GET** /launch/get-user-reward-records | Query user reward records
[**get_hodler_airdrop_project_list**](LaunchApi.md#get_hodler_airdrop_project_list) | **GET** /launch/hodler-airdrop/project-list | 查询HODLer Airdrop活动列表
[**hodler_airdrop_order**](LaunchApi.md#hodler_airdrop_order) | **POST** /launch/hodler-airdrop/order | 参与HODLer Airdrop活动
[**get_hodler_airdrop_user_order_records**](LaunchApi.md#get_hodler_airdrop_user_order_records) | **GET** /launch/hodler-airdrop/user-order-records | 查询HODLer Airdrop参与记录
[**get_hodler_airdrop_user_airdrop_records**](LaunchApi.md#get_hodler_airdrop_user_airdrop_records) | **GET** /launch/hodler-airdrop/user-airdrop-records | 查询HODLer Airdrop空投记录
[**get_candy_drop_activity_list_v4**](LaunchApi.md#get_candy_drop_activity_list_v4) | **GET** /launch/candydrop/activity-list | 查询活动列表
[**register_candy_drop_v4**](LaunchApi.md#register_candy_drop_v4) | **POST** /launch/candydrop/register | 报名参与活动
[**get_candy_drop_activity_rules_v4**](LaunchApi.md#get_candy_drop_activity_rules_v4) | **GET** /launch/candydrop/activity-rules | 查询活动规则
[**get_candy_drop_task_progress_v4**](LaunchApi.md#get_candy_drop_task_progress_v4) | **GET** /launch/candydrop/task-progress | 查询任务完成进度
[**get_candy_drop_participation_records_v4**](LaunchApi.md#get_candy_drop_participation_records_v4) | **GET** /launch/candydrop/participation-records | 查询参与记录
[**get_candy_drop_airdrop_records_v4**](LaunchApi.md#get_candy_drop_airdrop_records_v4) | **GET** /launch/candydrop/airdrop-records | 查询空投记录


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
> RedeemLaunchPoolResponse redeem_launch_pool(redeem_v4)

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

[**RedeemLaunchPoolResponse**](RedeemLaunchPoolResponse.md)

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

# **get_hodler_airdrop_project_list**
> list[HodlerAirdropV4ProjectItem] get_hodler_airdrop_project_list(status=status, keyword=keyword, join=join, page=page, size=size)

查询HODLer Airdrop活动列表

获取HODLer Airdrop活动列表，支持按状态、币种/项目名称、参与情况筛选。此接口无需用户登录，登录用户可获取个人参与信息。

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
status = 'status_example' # str | 活动状态筛选，可选值：ACTIVE（进行中+预热中）、UNDERWAY（进行中）、PREHEAT（预热中）、FINISH（已结束），不传返回全部 (optional)
keyword = 'keyword_example' # str | 币种/项目名称关键词，模糊匹配 (optional)
join = 0 # int | 参与情况筛选：0全部（默认），1仅已参与 (optional) (default to 0)
page = 1 # int | 页码，默认1 (optional) (default to 1)
size = 10 # int | 每页条数，默认10 (optional) (default to 10)

try:
    # 查询HODLer Airdrop活动列表
    api_response = api_instance.get_hodler_airdrop_project_list(status=status, keyword=keyword, join=join, page=page, size=size)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling LaunchApi->get_hodler_airdrop_project_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**| 活动状态筛选，可选值：ACTIVE（进行中+预热中）、UNDERWAY（进行中）、PREHEAT（预热中）、FINISH（已结束），不传返回全部 | [optional] 
 **keyword** | **str**| 币种/项目名称关键词，模糊匹配 | [optional] 
 **join** | **int**| 参与情况筛选：0全部（默认），1仅已参与 | [optional] [default to 0]
 **page** | **int**| 页码，默认1 | [optional] [default to 1]
 **size** | **int**| 每页条数，默认10 | [optional] [default to 10]

### Return type

[**list[HodlerAirdropV4ProjectItem]**](HodlerAirdropV4ProjectItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returns activity list |  -  |
**400** | Invalid request parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hodler_airdrop_order**
> HodlerAirdropV4OrderResponse hodler_airdrop_order(hodler_airdrop_v4_order_request)

参与HODLer Airdrop活动

参与指定的HODLer Airdrop活动，需持有GT。此接口需要用户登录认证，且须满足KYC要求，不支持子账户、企业/机构用户。

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
hodler_airdrop_v4_order_request = gate_api.HodlerAirdropV4OrderRequest() # HodlerAirdropV4OrderRequest | 

try:
    # 参与HODLer Airdrop活动
    api_response = api_instance.hodler_airdrop_order(hodler_airdrop_v4_order_request)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling LaunchApi->hodler_airdrop_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hodler_airdrop_v4_order_request** | [**HodlerAirdropV4OrderRequest**](HodlerAirdropV4OrderRequest.md)|  | 

### Return type

[**HodlerAirdropV4OrderResponse**](HodlerAirdropV4OrderResponse.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功参与活动 |  -  |
**400** | 请求参数错误或业务校验失败（KYC不足、子账户限制、企业用户限制等） |  -  |
**401** | 用户未登录 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hodler_airdrop_user_order_records**
> list[HodlerAirdropV4UserOrderRecord] get_hodler_airdrop_user_order_records(keyword=keyword, start_timest=start_timest, end_timest=end_timest, page=page, size=size)

查询HODLer Airdrop参与记录

查询用户的HODLer Airdrop参与记录，返回每个活动的有效持仓和空投金额。此接口需要用户登录认证。

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
keyword = 'keyword_example' # str | 币种名称关键词筛选 (optional)
start_timest = 56 # int | 开始时间戳（秒） (optional)
end_timest = 56 # int | 结束时间戳（秒） (optional)
page = 1 # int | 页码，默认1 (optional) (default to 1)
size = 10 # int | 每页条数，默认10 (optional) (default to 10)

try:
    # 查询HODLer Airdrop参与记录
    api_response = api_instance.get_hodler_airdrop_user_order_records(keyword=keyword, start_timest=start_timest, end_timest=end_timest, page=page, size=size)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling LaunchApi->get_hodler_airdrop_user_order_records: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **keyword** | **str**| 币种名称关键词筛选 | [optional] 
 **start_timest** | **int**| 开始时间戳（秒） | [optional] 
 **end_timest** | **int**| 结束时间戳（秒） | [optional] 
 **page** | **int**| 页码，默认1 | [optional] [default to 1]
 **size** | **int**| 每页条数，默认10 | [optional] [default to 10]

### Return type

[**list[HodlerAirdropV4UserOrderRecord]**](HodlerAirdropV4UserOrderRecord.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功返回参与记录列表 |  -  |
**400** | Invalid request parameters |  -  |
**401** | 用户未登录 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hodler_airdrop_user_airdrop_records**
> list[HodlerAirdropV4UserAirdropRecord] get_hodler_airdrop_user_airdrop_records(keyword=keyword, start_timest=start_timest, end_timest=end_timest, page=page, size=size)

查询HODLer Airdrop空投记录

查询用户已获得的HODLer Airdrop空投发放记录，包含基础空投、额外空投和自动兑换状态。此接口需要用户登录认证。

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
keyword = 'keyword_example' # str | 币种名称关键词筛选 (optional)
start_timest = 56 # int | 开始时间戳（秒） (optional)
end_timest = 56 # int | 结束时间戳（秒） (optional)
page = 1 # int | 页码，默认1 (optional) (default to 1)
size = 10 # int | 每页条数，默认10 (optional) (default to 10)

try:
    # 查询HODLer Airdrop空投记录
    api_response = api_instance.get_hodler_airdrop_user_airdrop_records(keyword=keyword, start_timest=start_timest, end_timest=end_timest, page=page, size=size)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling LaunchApi->get_hodler_airdrop_user_airdrop_records: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **keyword** | **str**| 币种名称关键词筛选 | [optional] 
 **start_timest** | **int**| 开始时间戳（秒） | [optional] 
 **end_timest** | **int**| 结束时间戳（秒） | [optional] 
 **page** | **int**| 页码，默认1 | [optional] [default to 1]
 **size** | **int**| 每页条数，默认10 | [optional] [default to 10]

### Return type

[**list[HodlerAirdropV4UserAirdropRecord]**](HodlerAirdropV4UserAirdropRecord.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功返回空投记录列表 |  -  |
**400** | Invalid request parameters |  -  |
**401** | 用户未登录 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_candy_drop_activity_list_v4**
> list[CandyDropV4ActivityCd01] get_candy_drop_activity_list_v4(status=status, rule_name=rule_name, register_status=register_status, currency=currency, limit=limit, offset=offset)

查询活动列表

支持多维度筛选 CandyDrop 活动，每次查询返回列表排序的前十条数据。不需要登录。

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
status = 'status_example' # str | 活动状态筛选：ongoing(进行中)、upcoming(即将开始)、ended(已结束)，不传则返回全部 (optional)
rule_name = 'rule_name_example' # str | 任务类型筛选：spot(现货)、futures(合约)、deposit(充值)、invite(邀请)、trading_bot(交易机器人)、simple_earn(余币宝)、first_deposit(首笔入金)、alpha(Alpha)、flash_swap(闪兑)、tradfi(TradFi)、etf(ETF) (optional)
register_status = 'register_status_example' # str | 参与情况筛选：registered(已参与)、unregistered(未参与)，不传则返回全部 (optional)
currency = 'currency_example' # str | 币种名称筛选 (optional)
limit = 10 # int | 返回条数，默认10，最大30 (optional) (default to 10)
offset = 0 # int | 偏移量，默认0 (optional) (default to 0)

try:
    # 查询活动列表
    api_response = api_instance.get_candy_drop_activity_list_v4(status=status, rule_name=rule_name, register_status=register_status, currency=currency, limit=limit, offset=offset)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling LaunchApi->get_candy_drop_activity_list_v4: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**| 活动状态筛选：ongoing(进行中)、upcoming(即将开始)、ended(已结束)，不传则返回全部 | [optional] 
 **rule_name** | **str**| 任务类型筛选：spot(现货)、futures(合约)、deposit(充值)、invite(邀请)、trading_bot(交易机器人)、simple_earn(余币宝)、first_deposit(首笔入金)、alpha(Alpha)、flash_swap(闪兑)、tradfi(TradFi)、etf(ETF) | [optional] 
 **register_status** | **str**| 参与情况筛选：registered(已参与)、unregistered(未参与)，不传则返回全部 | [optional] 
 **currency** | **str**| 币种名称筛选 | [optional] 
 **limit** | **int**| 返回条数，默认10，最大30 | [optional] [default to 10]
 **offset** | **int**| 偏移量，默认0 | [optional] [default to 0]

### Return type

[**list[CandyDropV4ActivityCd01]**](CandyDropV4ActivityCd01.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功返回活动列表数组 |  -  |
**400** | Invalid request parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_candy_drop_v4**
> CandyDropV4RegisterRespCd02 register_candy_drop_v4(candy_drop_v4_register_req_cd02)

报名参与活动

报名参与特定 CandyDrop 活动。需要登录，需要 API Key 签名认证。

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
candy_drop_v4_register_req_cd02 = gate_api.CandyDropV4RegisterReqCd02() # CandyDropV4RegisterReqCd02 | 

try:
    # 报名参与活动
    api_response = api_instance.register_candy_drop_v4(candy_drop_v4_register_req_cd02)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling LaunchApi->register_candy_drop_v4: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **candy_drop_v4_register_req_cd02** | [**CandyDropV4RegisterReqCd02**](CandyDropV4RegisterReqCd02.md)|  | 

### Return type

[**CandyDropV4RegisterRespCd02**](CandyDropV4RegisterRespCd02.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 报名成功 |  -  |
**400** | Request failed |  -  |
**401** | User not authenticated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_candy_drop_activity_rules_v4**
> CandyDropV4ActivityRulesCd03 get_candy_drop_activity_rules_v4(activity_id=activity_id, currency=currency)

查询活动规则

查询特定活动的规则，包括奖池及对应任务数据。不需要登录。

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
activity_id = 56 # int | 活动ID，与 currency 二选一，至少须传其一 (optional)
currency = 'currency_example' # str | 项目/币种名称，与 activity_id 二选一，至少须传其一 (optional)

try:
    # 查询活动规则
    api_response = api_instance.get_candy_drop_activity_rules_v4(activity_id=activity_id, currency=currency)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling LaunchApi->get_candy_drop_activity_rules_v4: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_id** | **int**| 活动ID，与 currency 二选一，至少须传其一 | [optional] 
 **currency** | **str**| 项目/币种名称，与 activity_id 二选一，至少须传其一 | [optional] 

### Return type

[**CandyDropV4ActivityRulesCd03**](CandyDropV4ActivityRulesCd03.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功返回活动规则 |  -  |
**400** | Invalid request parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_candy_drop_task_progress_v4**
> CandyDropV4TaskProgressCd04 get_candy_drop_task_progress_v4(activity_id=activity_id, currency=currency)

查询任务完成进度

查询进行中且已报名/参与的任务完成进度。需要登录。

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
activity_id = 56 # int | 活动ID，与 currency 二选一，至少须传其一 (optional)
currency = 'currency_example' # str | 项目/币种名称，与 activity_id 二选一，至少须传其一 (optional)

try:
    # 查询任务完成进度
    api_response = api_instance.get_candy_drop_task_progress_v4(activity_id=activity_id, currency=currency)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling LaunchApi->get_candy_drop_task_progress_v4: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_id** | **int**| 活动ID，与 currency 二选一，至少须传其一 | [optional] 
 **currency** | **str**| 项目/币种名称，与 activity_id 二选一，至少须传其一 | [optional] 

### Return type

[**CandyDropV4TaskProgressCd04**](CandyDropV4TaskProgressCd04.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功返回任务进度 |  -  |
**400** | Invalid request parameters |  -  |
**401** | User not authenticated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_candy_drop_participation_records_v4**
> list[CandyDropV4ParticipationRecordCd05] get_candy_drop_participation_records_v4(currency=currency, status=status, start_time=start_time, end_time=end_time, page=page, limit=limit)

查询参与记录

查询用户的 CandyDrop 参与详情。需要登录。

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
currency = 'currency_example' # str | 币种名称筛选 (optional)
status = 'status_example' # str | 状态筛选：ongoing(进行中)、awaiting_draw(待开奖)、won(已中奖)、not_win(未中奖) (optional)
start_time = 56 # int | 开始时间（Unix 时间戳秒） (optional)
end_time = 56 # int | 结束时间（Unix 时间戳秒） (optional)
page = 1 # int | 页码，默认1 (optional) (default to 1)
limit = 10 # int | 每页条数，默认10，最大30 (optional) (default to 10)

try:
    # 查询参与记录
    api_response = api_instance.get_candy_drop_participation_records_v4(currency=currency, status=status, start_time=start_time, end_time=end_time, page=page, limit=limit)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling LaunchApi->get_candy_drop_participation_records_v4: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| 币种名称筛选 | [optional] 
 **status** | **str**| 状态筛选：ongoing(进行中)、awaiting_draw(待开奖)、won(已中奖)、not_win(未中奖) | [optional] 
 **start_time** | **int**| 开始时间（Unix 时间戳秒） | [optional] 
 **end_time** | **int**| 结束时间（Unix 时间戳秒） | [optional] 
 **page** | **int**| 页码，默认1 | [optional] [default to 1]
 **limit** | **int**| 每页条数，默认10，最大30 | [optional] [default to 10]

### Return type

[**list[CandyDropV4ParticipationRecordCd05]**](CandyDropV4ParticipationRecordCd05.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功返回参与记录列表 |  -  |
**400** | Invalid request parameters |  -  |
**401** | User not authenticated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_candy_drop_airdrop_records_v4**
> list[CandyDropV4AirdropRecordCd06] get_candy_drop_airdrop_records_v4(currency=currency, start_time=start_time, end_time=end_time, page=page, limit=limit)

查询空投记录

查询用户的 CandyDrop 空投详情。需要登录。

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
currency = 'currency_example' # str | 币种名称筛选 (optional)
start_time = 56 # int | 开始时间（Unix 时间戳秒） (optional)
end_time = 56 # int | 结束时间（Unix 时间戳秒） (optional)
page = 1 # int | 页码，默认1 (optional) (default to 1)
limit = 10 # int | 每页条数，默认10，最大30 (optional) (default to 10)

try:
    # 查询空投记录
    api_response = api_instance.get_candy_drop_airdrop_records_v4(currency=currency, start_time=start_time, end_time=end_time, page=page, limit=limit)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling LaunchApi->get_candy_drop_airdrop_records_v4: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| 币种名称筛选 | [optional] 
 **start_time** | **int**| 开始时间（Unix 时间戳秒） | [optional] 
 **end_time** | **int**| 结束时间（Unix 时间戳秒） | [optional] 
 **page** | **int**| 页码，默认1 | [optional] [default to 1]
 **limit** | **int**| 每页条数，默认10，最大30 | [optional] [default to 10]

### Return type

[**list[CandyDropV4AirdropRecordCd06]**](CandyDropV4AirdropRecordCd06.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功返回空投记录列表 |  -  |
**400** | Invalid request parameters |  -  |
**401** | User not authenticated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

