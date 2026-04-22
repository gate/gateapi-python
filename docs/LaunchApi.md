# gate_api.LaunchApi

All URIs are relative to *https://api.gateio.ws/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_launch_pool_projects**](LaunchApi.md#list_launch_pool_projects) | **GET** /launch/project-list | Query LaunchPool project list
[**create_launch_pool_order**](LaunchApi.md#create_launch_pool_order) | **POST** /launch/create-order | Create LaunchPool staking order
[**redeem_launch_pool**](LaunchApi.md#redeem_launch_pool) | **POST** /launch/redeem | Redeem LaunchPool staked assets
[**list_launch_pool_pledge_records**](LaunchApi.md#list_launch_pool_pledge_records) | **GET** /launch/user-pledge-records | Query user pledge records
[**list_launch_pool_reward_records**](LaunchApi.md#list_launch_pool_reward_records) | **GET** /launch/get-user-reward-records | Query user reward records
[**get_hodler_airdrop_project_list**](LaunchApi.md#get_hodler_airdrop_project_list) | **GET** /launch/hodler-airdrop/project-list | Check the list of HODLer Airdrop activities
[**hodler_airdrop_order**](LaunchApi.md#hodler_airdrop_order) | **POST** /launch/hodler-airdrop/order | Participate in the HODLer Airdrop event
[**get_hodler_airdrop_user_order_records**](LaunchApi.md#get_hodler_airdrop_user_order_records) | **GET** /launch/hodler-airdrop/user-order-records | Check HODLer Airdrop participation records
[**get_hodler_airdrop_user_airdrop_records**](LaunchApi.md#get_hodler_airdrop_user_airdrop_records) | **GET** /launch/hodler-airdrop/user-airdrop-records | Query HODLer Airdrop records
[**get_candy_drop_activity_list_v4**](LaunchApi.md#get_candy_drop_activity_list_v4) | **GET** /launch/candydrop/activity-list | Query activity list
[**register_candy_drop_v4**](LaunchApi.md#register_candy_drop_v4) | **POST** /launch/candydrop/register | Sign up for events
[**get_candy_drop_activity_rules_v4**](LaunchApi.md#get_candy_drop_activity_rules_v4) | **GET** /launch/candydrop/activity-rules | Query activity rules
[**get_candy_drop_task_progress_v4**](LaunchApi.md#get_candy_drop_task_progress_v4) | **GET** /launch/candydrop/task-progress | Query task completion progress
[**get_candy_drop_participation_records_v4**](LaunchApi.md#get_candy_drop_participation_records_v4) | **GET** /launch/candydrop/participation-records | Query participation records
[**get_candy_drop_airdrop_records_v4**](LaunchApi.md#get_candy_drop_airdrop_records_v4) | **GET** /launch/candydrop/airdrop-records | Query airdrop records


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

Check the list of HODLer Airdrop activities

Get the HODLer Airdrop activity list, which supports filtering by status, currency/project name, and participation status. This interface does not require user login, and logged in users can obtain personal participation information.

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
status = 'status_example' # str | Activity status filtering, optional values: ACTIVE (in progress + preheating), UNDERWAY (in progress), PREHEAT (preheating), FINISH (ended), return all if not passed (optional)
keyword = 'keyword_example' # str | Currency/project name keywords, fuzzy matching (optional)
join = 0 # int | Participation filter: 0 all (default), 1 only participated (optional) (default to 0)
page = 1 # int | Page number, default 1 (optional) (default to 1)
size = 10 # int | Number of items per page, default 10 (optional) (default to 10)

try:
    # Check the list of HODLer Airdrop activities
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
 **status** | **str**| Activity status filtering, optional values: ACTIVE (in progress + preheating), UNDERWAY (in progress), PREHEAT (preheating), FINISH (ended), return all if not passed | [optional] 
 **keyword** | **str**| Currency/project name keywords, fuzzy matching | [optional] 
 **join** | **int**| Participation filter: 0 all (default), 1 only participated | [optional] [default to 0]
 **page** | **int**| Page number, default 1 | [optional] [default to 1]
 **size** | **int**| Number of items per page, default 10 | [optional] [default to 10]

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

Participate in the HODLer Airdrop event

To participate in designated HODLer Airdrop activities, you need to hold GT. This interface requires user login authentication and must meet KYC requirements. It does not support sub-accounts and enterprise/institutional users.

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
    # Participate in the HODLer Airdrop event
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
**200** | Successfully participated in the event |  -  |
**400** | Incorrect request parameters or failed business verification (insufficient KYC, sub-account restrictions, enterprise user restrictions, etc.) |  -  |
**401** | User is not logged in |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hodler_airdrop_user_order_records**
> list[HodlerAirdropV4UserOrderRecord] get_hodler_airdrop_user_order_records(keyword=keyword, start_timest=start_timest, end_timest=end_timest, page=page, size=size)

Check HODLer Airdrop participation records

Query the user's HODLer Airdrop participation record and return the effective holdings and airdrop amount of each activity. This interface requires user login authentication.

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
keyword = 'keyword_example' # str | Currency name keyword filtering (optional)
start_timest = 56 # int | Start timestamp (seconds) (optional)
end_timest = 56 # int | end timestamp (seconds) (optional)
page = 1 # int | Page number, default 1 (optional) (default to 1)
size = 10 # int | Number of items per page, default 10 (optional) (default to 10)

try:
    # Check HODLer Airdrop participation records
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
 **keyword** | **str**| Currency name keyword filtering | [optional] 
 **start_timest** | **int**| Start timestamp (seconds) | [optional] 
 **end_timest** | **int**| end timestamp (seconds) | [optional] 
 **page** | **int**| Page number, default 1 | [optional] [default to 1]
 **size** | **int**| Number of items per page, default 10 | [optional] [default to 10]

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
**200** | Successfully returned the participation record list |  -  |
**400** | Invalid request parameters |  -  |
**401** | User is not logged in |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hodler_airdrop_user_airdrop_records**
> list[HodlerAirdropV4UserAirdropRecord] get_hodler_airdrop_user_airdrop_records(keyword=keyword, start_timest=start_timest, end_timest=end_timest, page=page, size=size)

Query HODLer Airdrop records

Query the HODLer Airdrop airdrop distribution record that the user has obtained, including basic airdrops, additional airdrops and automatic redemption status. This interface requires user login authentication.

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
keyword = 'keyword_example' # str | Currency name keyword filtering (optional)
start_timest = 56 # int | Start timestamp (seconds) (optional)
end_timest = 56 # int | end timestamp (seconds) (optional)
page = 1 # int | Page number, default 1 (optional) (default to 1)
size = 10 # int | Number of items per page, default 10 (optional) (default to 10)

try:
    # Query HODLer Airdrop records
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
 **keyword** | **str**| Currency name keyword filtering | [optional] 
 **start_timest** | **int**| Start timestamp (seconds) | [optional] 
 **end_timest** | **int**| end timestamp (seconds) | [optional] 
 **page** | **int**| Page number, default 1 | [optional] [default to 1]
 **size** | **int**| Number of items per page, default 10 | [optional] [default to 10]

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
**200** | Successfully returns the airdrop record list |  -  |
**400** | Invalid request parameters |  -  |
**401** | User is not logged in |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_candy_drop_activity_list_v4**
> list[CandyDropV4ActivityCd01] get_candy_drop_activity_list_v4(status=status, rule_name=rule_name, register_status=register_status, currency=currency, limit=limit, offset=offset)

Query activity list

Supports multi-dimensional filtering of CandyDrop activities, and each query returns the top ten data sorted by the list. No login required.

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
status = 'status_example' # str | Activity status filtering: ongoing (in progress), upcoming (about to start), ended (ended), if not passed, all will be returned (optional)
rule_name = 'rule_name_example' # str | Task type filtering: spot (spot), futures (contract), deposit (recharge), invite (invitation), trading_bot (trading robot), simple_earn (Yu Bibao), first_deposit (first deposit), alpha (Alpha), flash_swap (flash swap), tradfi (TradFi), etf (ETF) (optional)
register_status = 'register_status_example' # str | Participation status screening: registered (already participated), unregistered (not participated), if not passed, all will be returned (optional)
currency = 'currency_example' # str | Currency name filter (optional)
limit = 10 # int | Number of items returned, default 10, maximum 30 (optional) (default to 10)
offset = 0 # int | Offset, default 0 (optional) (default to 0)

try:
    # Query activity list
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
 **status** | **str**| Activity status filtering: ongoing (in progress), upcoming (about to start), ended (ended), if not passed, all will be returned | [optional] 
 **rule_name** | **str**| Task type filtering: spot (spot), futures (contract), deposit (recharge), invite (invitation), trading_bot (trading robot), simple_earn (Yu Bibao), first_deposit (first deposit), alpha (Alpha), flash_swap (flash swap), tradfi (TradFi), etf (ETF) | [optional] 
 **register_status** | **str**| Participation status screening: registered (already participated), unregistered (not participated), if not passed, all will be returned | [optional] 
 **currency** | **str**| Currency name filter | [optional] 
 **limit** | **int**| Number of items returned, default 10, maximum 30 | [optional] [default to 10]
 **offset** | **int**| Offset, default 0 | [optional] [default to 0]

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
**200** | Successfully returns the activity list array |  -  |
**400** | Invalid request parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_candy_drop_v4**
> CandyDropV4RegisterRespCd02 register_candy_drop_v4(candy_drop_v4_register_req_cd02)

Sign up for events

Sign up for select CandyDrop events. Login is required and API Key signature authentication is required.

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
    # Sign up for events
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
**200** | Registration successful |  -  |
**400** | Request failed |  -  |
**401** | User not authenticated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_candy_drop_activity_rules_v4**
> CandyDropV4ActivityRulesCd03 get_candy_drop_activity_rules_v4(activity_id=activity_id, currency=currency)

Query activity rules

Query the rules of a specific activity, including prize pool and corresponding task data. No login required.

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
activity_id = 56 # int | Activity ID, choose one from currency, at least one of them must be passed (optional)
currency = 'currency_example' # str | Project/currency name, choose one from activity_id, at least one of them must be passed (optional)

try:
    # Query activity rules
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
 **activity_id** | **int**| Activity ID, choose one from currency, at least one of them must be passed | [optional] 
 **currency** | **str**| Project/currency name, choose one from activity_id, at least one of them must be passed | [optional] 

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
**200** | Successful return to activity rules |  -  |
**400** | Invalid request parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_candy_drop_task_progress_v4**
> CandyDropV4TaskProgressCd04 get_candy_drop_task_progress_v4(activity_id=activity_id, currency=currency)

Query task completion progress

Check the completion progress of tasks that are in progress and have been registered/participated. Login required.

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
activity_id = 56 # int | Activity ID, choose one from currency, at least one of them must be passed (optional)
currency = 'currency_example' # str | Project/currency name, choose one from activity_id, at least one of them must be passed (optional)

try:
    # Query task completion progress
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
 **activity_id** | **int**| Activity ID, choose one from currency, at least one of them must be passed | [optional] 
 **currency** | **str**| Project/currency name, choose one from activity_id, at least one of them must be passed | [optional] 

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
**200** | Successfully return task progress |  -  |
**400** | Invalid request parameters |  -  |
**401** | User not authenticated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_candy_drop_participation_records_v4**
> list[CandyDropV4ParticipationRecordCd05] get_candy_drop_participation_records_v4(currency=currency, status=status, start_time=start_time, end_time=end_time, page=page, limit=limit)

Query participation records

Query the user's CandyDrop participation details. Login required.

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
currency = 'currency_example' # str | Currency name filter (optional)
status = 'status_example' # str | Status filtering: ongoing (in progress), awaiting_draw (to be drawn), won (already won), not_win (not won) (optional)
start_time = 56 # int | Start time (Unix timestamp seconds) (optional)
end_time = 56 # int | End time (Unix timestamp seconds) (optional)
page = 1 # int | Page number, default 1 (optional) (default to 1)
limit = 10 # int | Number of items per page, default 10, maximum 30 (optional) (default to 10)

try:
    # Query participation records
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
 **currency** | **str**| Currency name filter | [optional] 
 **status** | **str**| Status filtering: ongoing (in progress), awaiting_draw (to be drawn), won (already won), not_win (not won) | [optional] 
 **start_time** | **int**| Start time (Unix timestamp seconds) | [optional] 
 **end_time** | **int**| End time (Unix timestamp seconds) | [optional] 
 **page** | **int**| Page number, default 1 | [optional] [default to 1]
 **limit** | **int**| Number of items per page, default 10, maximum 30 | [optional] [default to 10]

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
**200** | Successfully returned the participation record list |  -  |
**400** | Invalid request parameters |  -  |
**401** | User not authenticated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_candy_drop_airdrop_records_v4**
> list[CandyDropV4AirdropRecordCd06] get_candy_drop_airdrop_records_v4(currency=currency, start_time=start_time, end_time=end_time, page=page, limit=limit)

Query airdrop records

Query the user's CandyDrop airdrop details. Login required.

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
currency = 'currency_example' # str | Currency name filter (optional)
start_time = 56 # int | Start time (Unix timestamp seconds) (optional)
end_time = 56 # int | End time (Unix timestamp seconds) (optional)
page = 1 # int | Page number, default 1 (optional) (default to 1)
limit = 10 # int | Number of items per page, default 10, maximum 30 (optional) (default to 10)

try:
    # Query airdrop records
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
 **currency** | **str**| Currency name filter | [optional] 
 **start_time** | **int**| Start time (Unix timestamp seconds) | [optional] 
 **end_time** | **int**| End time (Unix timestamp seconds) | [optional] 
 **page** | **int**| Page number, default 1 | [optional] [default to 1]
 **limit** | **int**| Number of items per page, default 10, maximum 30 | [optional] [default to 10]

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
**200** | Successfully returns the airdrop record list |  -  |
**400** | Invalid request parameters |  -  |
**401** | User not authenticated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

