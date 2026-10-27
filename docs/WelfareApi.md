# gate_api.WelfareApi

All URIs are relative to *https://api.gateio.ws/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_user_identity**](WelfareApi.md#get_user_identity) | **GET** /rewards/getUserIdentity | Get user identity
[**get_beginner_task_list**](WelfareApi.md#get_beginner_task_list) | **GET** /rewards/getBeginnerTaskList | Get beginner task list
[**claim_task**](WelfareApi.md#claim_task) | **POST** /rewards/claimTask | Get the task
[**claim_reward**](WelfareApi.md#claim_reward) | **POST** /rewards/claimReward | Receive mission rewards


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

Get the current user's onboarding task list. By default, the registration tasks (type=10) and guidance tasks (type=11) that have been assigned to the current user are returned. The registration tasks are ranked first and the guidance tasks are ranked behind. When the user does not have a download task and the system determines that the user has not downloaded the app, a \"Download task to be received\" card will be dynamically added. Among them: - `task_type = 23` for download tasks - `status = 0` for download tasks to be collected Results are cached for 60 seconds. Task lists are limited in number (usually no more than 10) and do not require pagination.

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

Get the task

Receive a single welfare task. The current main scene is for new customer download tasks to be collected, but the interface itself supports new customer registration, guidance, and advanced task types. Processing flow: 1. Read the logged in user 2. Verify user qualifications 3. Risk control verification (event code `task_center`) 4. Verify task configuration and task center tasks 5. Verify whether there is an ongoing task 6. If it is a download task, verify whether the App has been downloaded 7. Write `welfare_user_tasks_xx` 8. Report to task center Risk control transparent transmission fields: - Old fields: `user_id`, `ip`, `const_id`, `is_async`, `action`, `task_id` - New fields: `req_method`, `traceid` - Among them:   - `req_method` from `X-Gate-Request-Source`   - `ip` from `X-Gate-Ip`   - `traceid` from `X-Gate-Trace-Id`   - `const_id` is fixed to an empty string

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
    # Get the task
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

Receive mission rewards

Receive rewards from a single welfare task. Processing flow: 1. Read the logged in user 2. Verify user qualifications 3. Query `welfare_user_tasks_xx` and require the task status to be `StatusDone(2)` 4. Risk control verification (event code `index_page_check`) 5. Query task details and reward information in the task center 6. If the reward is m and n is selected from the prize pool, then `has_m_n_task = true` will be returned and the reward will not be actually issued. 7. Ordinary rewards will enter the original reward collection logic of the Welfare Center Risk control transparent transmission fields: - Old fields: `user_id`, `ip`, `const_id`, `is_async` - New fields: `req_method`, `traceid` - Among them:   - `req_method` from `X-Gate-Request-Source`   - `ip` from `X-Gate-Ip`   - `traceid` from `X-Gate-Trace-Id`   - `const_id` is fixed to an empty string

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
    # Receive mission rewards
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

