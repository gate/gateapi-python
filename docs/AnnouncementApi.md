# gate_api.AnnouncementApi

All URIs are relative to *https://api.gateio.ws/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_announcement_articles**](AnnouncementApi.md#list_announcement_articles) | **POST** /ann/list_article | List announcement articles


# **list_announcement_articles**
> AnnouncementArticleListResponse list_announcement_articles(announcement_article_list_request)

List announcement articles

Query announcement articles with pagination and filters for title, category, language, time, and other criteria. Send query parameters in the JSON request body. Both page and size are optional and must be strings when provided. No API key is required.

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
api_instance = gate_api.AnnouncementApi(api_client)
announcement_article_list_request = gate_api.AnnouncementArticleListRequest() # AnnouncementArticleListRequest | 

try:
    # List announcement articles
    api_response = api_instance.list_announcement_articles(announcement_article_list_request)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling AnnouncementApi->list_announcement_articles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **announcement_article_list_request** | [**AnnouncementArticleListRequest**](AnnouncementArticleListRequest.md)|  | 

### Return type

[**AnnouncementArticleListResponse**](AnnouncementArticleListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Announcement article list response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

