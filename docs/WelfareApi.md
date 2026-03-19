# gate_api.WelfareApi

All URIs are relative to *https://api.gateio.ws/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_user_identity**](WelfareApi.md#get_user_identity) | **GET** /rewards/getUserIdentity | Get user identity
[**get_beginner_task_list**](WelfareApi.md#get_beginner_task_list) | **GET** /rewards/getBeginnerTaskList | Get beginner task list


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

Get the current user's beginner task list, including registration tasks (type=10) and onboarding tasks (type=11). Registration tasks appear first, onboarding tasks after. Results are cached for 60 seconds. The task list is a fixed configuration with limited entries (typically no more than 10), no pagination needed.

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

