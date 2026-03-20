# gate_api.DefaultApi

All URIs are relative to *https://api.gateio.ws/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_my_activity_entry**](DefaultApi.md#get_my_activity_entry) | **GET** /rewards/activity/my-activity-entry | My activity entry
[**list_activities**](DefaultApi.md#list_activities) | **GET** /rewards/activity/activity-list | Recommended activity list
[**list_activity_types**](DefaultApi.md#list_activity_types) | **GET** /rewards/activity/activity-type | Activity type list


# **get_my_activity_entry**
> InlineResponse20012 get_my_activity_entry()

My activity entry

Query user's Activity Center entry information, including activity icon and redirect link

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
api_instance = gate_api.DefaultApi(api_client)

try:
    # My activity entry
    api_response = api_instance.get_my_activity_entry()
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling DefaultApi->get_my_activity_entry: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returns activity entry information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_activities**
> InlineResponse20013 list_activities(recommend_type=recommend_type, type_ids=type_ids, keywords=keywords, page=page, page_size=page_size, sort_by=sort_by)

Recommended activity list

Query recommended activity list from Activity Center, supports pagination and sorting

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
api_instance = gate_api.DefaultApi(api_client)
recommend_type = 'recommend_type_example' # str | Recommendation type: hot for popular activities, type for filtering by activity type (type_ids), scenario for matching by activity name (optional)
type_ids = 'type_ids_example' # str | Activity type ID, multiple IDs separated by commas (supports filtering by activity type through this field) (optional)
keywords = 'keywords_example' # str | Activity name. When scenario type is used, keyword matching is applied (optional)
page = 1 # int | Page number, starting from 1 (optional) (default to 1)
page_size = 10 # int | Items per page (optional) (default to 10)
sort_by = 'sort_by_example' # str | Sort order, e.g., hot for sorting by popularity (optional)

try:
    # Recommended activity list
    api_response = api_instance.list_activities(recommend_type=recommend_type, type_ids=type_ids, keywords=keywords, page=page, page_size=page_size, sort_by=sort_by)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling DefaultApi->list_activities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recommend_type** | **str**| Recommendation type: hot for popular activities, type for filtering by activity type (type_ids), scenario for matching by activity name | [optional] 
 **type_ids** | **str**| Activity type ID, multiple IDs separated by commas (supports filtering by activity type through this field) | [optional] 
 **keywords** | **str**| Activity name. When scenario type is used, keyword matching is applied | [optional] 
 **page** | **int**| Page number, starting from 1 | [optional] [default to 1]
 **page_size** | **int**| Items per page | [optional] [default to 10]
 **sort_by** | **str**| Sort order, e.g., hot for sorting by popularity | [optional] 

### Return type

[**InlineResponse20013**](InlineResponse20013.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returns activity list |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_activity_types**
> InlineResponse20014 list_activity_types()

Activity type list

Query all activity types supported by Activity Center

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
api_instance = gate_api.DefaultApi(api_client)

try:
    # Activity type list
    api_response = api_instance.list_activity_types()
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling DefaultApi->list_activity_types: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returns activity type list |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

