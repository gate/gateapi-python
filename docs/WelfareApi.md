# gate_api.WelfareApi

All URIs are relative to *https://api.gateio.ws/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_user_identity**](WelfareApi.md#get_user_identity) | **GET** /rewards/getUserIdentity | Get user identity
[**get_beginner_task_list**](WelfareApi.md#get_beginner_task_list) | **GET** /rewards/getBeginnerTaskList | Get beginner task list
[**claim_task**](WelfareApi.md#claim_task) | **POST** /rewards/claimTask | 领取任务
[**claim_reward**](WelfareApi.md#claim_reward) | **POST** /rewards/claimReward | 领取任务奖励


# **get_user_identity**
> ApiResponseExSkillGetUserIdentityResp get_user_identity()

Get user identity

Validate whether the user is eligible for new user rewards. Returns the corresponding error code on validation failure, data is an empty object on success.

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
api_instance = gate_api.WelfareApi(api_client)

try:
    # Get user identity
    api_response = api_instance.get_user_identity()
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling WelfareApi->get_user_identity: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiResponseExSkillGetUserIdentityResp**](ApiResponseExSkillGetUserIdentityResp.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The endpoint always returns HTTP 200. Business results are distinguished by the code field |  -  |
**400** | Invalid request parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_beginner_task_list**
> ApiResponseExSkillGetBeginnerTaskListResp get_beginner_task_list()

Get beginner task list

获取当前用户的新客入门任务列表。  默认返回已经归属到当前用户的注册任务（type=10）和引导任务（type=11），注册任务排在前面，引导任务排在后面。 当用户尚未拥有下载任务、且系统判断用户未下载过 App 时，会动态补充一条“待领取下载任务”卡片。  其中： - 下载任务的 `task_type = 23` - 待领取下载任务的 `status = 0`  结果缓存 60 秒。任务列表数量有限（通常不超过 10 条），无需分页。

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
api_instance = gate_api.WelfareApi(api_client)

try:
    # Get beginner task list
    api_response = api_instance.get_beginner_task_list()
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling WelfareApi->get_beginner_task_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiResponseExSkillGetBeginnerTaskListResp**](ApiResponseExSkillGetBeginnerTaskListResp.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The endpoint always returns HTTP 200. Business results are distinguished by the code field |  -  |
**400** | Invalid request parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **claim_task**
> ApiResponseExSkillClaimTaskResp claim_task(ex_skill_claim_task_req)

领取任务

领取单个福利任务。  当前主场景为新客下载任务领取，但接口本身支持新客注册、引导、进阶任务类型。  处理流程： 1. 读取登录用户 2. 做用户资格校验 3. 风控校验（事件码 `task_center`） 4. 校验任务配置与任务中心任务 5. 校验是否已存在进行中任务 6. 若为下载任务，校验是否已下载 App 7. 写入 `welfare_user_tasks_xx` 8. 上报任务中心  风控透传字段： - 老字段：`user_id`、`ip`、`const_id`、`is_async`、`action`、`task_id` - 新增字段：`req_method`、`traceid` - 其中：   - `req_method` 来自 `X-Gate-Request-Source`   - `ip` 来自 `X-Gate-Ip`   - `traceid` 来自 `X-Gate-Trace-Id`   - `const_id` 固定为空字符串

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
api_instance = gate_api.WelfareApi(api_client)
ex_skill_claim_task_req = gate_api.ExSkillClaimTaskReq() # ExSkillClaimTaskReq | 

try:
    # 领取任务
    api_response = api_instance.claim_task(ex_skill_claim_task_req)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling WelfareApi->claim_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ex_skill_claim_task_req** | [**ExSkillClaimTaskReq**](ExSkillClaimTaskReq.md)|  | 

### Return type

[**ApiResponseExSkillClaimTaskResp**](ApiResponseExSkillClaimTaskResp.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The endpoint always returns HTTP 200. Business results are distinguished by the code field |  -  |
**400** | Invalid request parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **claim_reward**
> ApiResponseExSkillClaimRewardResp claim_reward(ex_skill_claim_reward_req)

领取任务奖励

领取单个福利任务奖励。  处理流程： 1. 读取登录用户 2. 做用户资格校验 3. 查询 `welfare_user_tasks_xx`，要求任务状态为 `StatusDone(2)` 4. 风控校验（事件码 `index_page_check`） 5. 查询任务中心任务详情与奖励信息 6. 若奖励为 m 选 n 奖池，则返回 `has_m_n_task = true`，不实际发奖 7. 普通奖励则进入福利中心原领奖逻辑  风控透传字段： - 老字段：`user_id`、`ip`、`const_id`、`is_async` - 新增字段：`req_method`、`traceid` - 其中：   - `req_method` 来自 `X-Gate-Request-Source`   - `ip` 来自 `X-Gate-Ip`   - `traceid` 来自 `X-Gate-Trace-Id`   - `const_id` 固定为空字符串

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
api_instance = gate_api.WelfareApi(api_client)
ex_skill_claim_reward_req = gate_api.ExSkillClaimRewardReq() # ExSkillClaimRewardReq | 

try:
    # 领取任务奖励
    api_response = api_instance.claim_reward(ex_skill_claim_reward_req)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling WelfareApi->claim_reward: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ex_skill_claim_reward_req** | [**ExSkillClaimRewardReq**](ExSkillClaimRewardReq.md)|  | 

### Return type

[**ApiResponseExSkillClaimRewardResp**](ApiResponseExSkillClaimRewardResp.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The endpoint always returns HTTP 200. Business results are distinguished by the code field |  -  |
**400** | Invalid request parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

