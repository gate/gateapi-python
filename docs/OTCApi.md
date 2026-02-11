# gate_api.OTCApi

All URIs are relative to *https://api.gateio.ws/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_otc_quote**](OTCApi.md#create_otc_quote) | **POST** /otc/quote | Fiat and stablecoin quote
[**create_otc_order**](OTCApi.md#create_otc_order) | **POST** /otc/order/create | Create fiat order
[**create_stable_coin_order**](OTCApi.md#create_stable_coin_order) | **POST** /otc/stable_coin/order/create | Create stablecoin order
[**get_user_default_bank**](OTCApi.md#get_user_default_bank) | **GET** /otc/get_user_def_bank | Get user&#39;s default bank account information
[**get_bank_list**](OTCApi.md#get_bank_list) | **GET** /otc/bank_list | Get user bank card list
[**mark_otc_order_paid**](OTCApi.md#mark_otc_order_paid) | **POST** /otc/order/paid | Mark fiat order as paid
[**cancel_otc_order**](OTCApi.md#cancel_otc_order) | **POST** /otc/order/cancel | Fiat order cancellation
[**list_otc_orders**](OTCApi.md#list_otc_orders) | **GET** /otc/order/list | Fiat order list
[**list_stable_coin_orders**](OTCApi.md#list_stable_coin_orders) | **GET** /otc/stable_coin/order/list | Stablecoin order list
[**get_otc_order_detail**](OTCApi.md#get_otc_order_detail) | **GET** /otc/order/detail | Fiat order details


# **create_otc_quote**
> InlineResponse2006 create_otc_quote(inline_object1)

Fiat and stablecoin quote

Create fiat and stablecoin quotes, supporting both PAY and GET directions

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
api_instance = gate_api.OTCApi(api_client)
inline_object1 = gate_api.InlineObject1() # InlineObject1 | 

try:
    # Fiat and stablecoin quote
    api_response = api_instance.create_otc_quote(inline_object1)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling OTCApi->create_otc_quote: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object1** | [**InlineObject1**](InlineObject1.md)|  | 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Quote retrieved successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_otc_order**
> InlineResponse2007 create_otc_order(inline_object2)

Create fiat order

Create a fiat order, supporting BUY for on-ramp and SELL for off-ramp

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
api_instance = gate_api.OTCApi(api_client)
inline_object2 = gate_api.InlineObject2() # InlineObject2 | 

try:
    # Create fiat order
    api_response = api_instance.create_otc_order(inline_object2)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling OTCApi->create_otc_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object2** | [**InlineObject2**](InlineObject2.md)|  | 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Order created successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_stable_coin_order**
> InlineResponse2008 create_stable_coin_order(inline_object3)

Create stablecoin order

Create stablecoin order

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
api_instance = gate_api.OTCApi(api_client)
inline_object3 = gate_api.InlineObject3() # InlineObject3 | 

try:
    # Create stablecoin order
    api_response = api_instance.create_stable_coin_order(inline_object3)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling OTCApi->create_stable_coin_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object3** | [**InlineObject3**](InlineObject3.md)|  | 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Stablecoin order created successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_default_bank**
> InlineResponse2009 get_user_default_bank()

Get user's default bank account information

Get user's default bank account information for order placement

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
api_instance = gate_api.OTCApi(api_client)

try:
    # Get user's default bank account information
    api_response = api_instance.get_user_default_bank()
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling OTCApi->get_user_default_bank: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Query successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bank_list**
> InlineResponse20010 get_bank_list()

Get user bank card list

Get user bank card list for selecting bank card when placing orders

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
api_instance = gate_api.OTCApi(api_client)

try:
    # Get user bank card list
    api_response = api_instance.get_bank_list()
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling OTCApi->get_bank_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Query successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mark_otc_order_paid**
> InlineResponse2007 mark_otc_order_paid(inline_object4)

Mark fiat order as paid

Mark fiat order as paid

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
api_instance = gate_api.OTCApi(api_client)
inline_object4 = gate_api.InlineObject4() # InlineObject4 | 

try:
    # Mark fiat order as paid
    api_response = api_instance.mark_otc_order_paid(inline_object4)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling OTCApi->mark_otc_order_paid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object4** | [**InlineObject4**](InlineObject4.md)|  | 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The order has been marked as paid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_otc_order**
> InlineResponse2007 cancel_otc_order(order_id)

Fiat order cancellation

Cancel fiat order

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
api_instance = gate_api.OTCApi(api_client)
order_id = 'order_id_example' # str | Order ID

try:
    # Fiat order cancellation
    api_response = api_instance.cancel_otc_order(order_id)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling OTCApi->cancel_otc_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| Order ID | 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Order cancelled successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_otc_orders**
> InlineResponse20011 list_otc_orders(type=type, fiat_currency=fiat_currency, crypto_currency=crypto_currency, start_time=start_time, end_time=end_time, status=status, pn=pn, ps=ps)

Fiat order list

Query the fiat order list with filters such as type, currency, time range, and status

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
api_instance = gate_api.OTCApi(api_client)
type = 'type_example' # str | BUY for on-ramp, SELL for off-ramp (optional)
fiat_currency = 'fiat_currency_example' # str | Fiat currency (optional)
crypto_currency = 'crypto_currency_example' # str | Digital currency (optional)
start_time = 'start_time_example' # str | starttime   for example : 2025-09-09 (optional)
end_time = 'end_time_example' # str | endtime  for example :2025-09-09 (optional)
status = 'status_example' # str | DONE: Completed CANCEL: Canceled PROCESSING: In Progress (optional)
pn = 'pn_example' # str | Page number (optional)
ps = 'ps_example' # str | Number of items per page (optional)

try:
    # Fiat order list
    api_response = api_instance.list_otc_orders(type=type, fiat_currency=fiat_currency, crypto_currency=crypto_currency, start_time=start_time, end_time=end_time, status=status, pn=pn, ps=ps)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling OTCApi->list_otc_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| BUY for on-ramp, SELL for off-ramp | [optional] 
 **fiat_currency** | **str**| Fiat currency | [optional] 
 **crypto_currency** | **str**| Digital currency | [optional] 
 **start_time** | **str**| starttime   for example : 2025-09-09 | [optional] 
 **end_time** | **str**| endtime  for example :2025-09-09 | [optional] 
 **status** | **str**| DONE: Completed CANCEL: Canceled PROCESSING: In Progress | [optional] 
 **pn** | **str**| Page number | [optional] 
 **ps** | **str**| Number of items per page | [optional] 

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Query successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_stable_coin_orders**
> InlineResponse20012 list_stable_coin_orders(page_size=page_size, page_number=page_number, coin_name=coin_name, start_time=start_time, end_time=end_time, status=status)

Stablecoin order list

Query stablecoin order list with filtering by currency, time range, status, etc.

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
api_instance = gate_api.OTCApi(api_client)
page_size = '10' # str | Number of records per page (optional)
page_number = '1' # str | Page number (optional)
coin_name = 'USDT' # str | ordercurrency (optional)
start_time = 'start_time_example' # str | Start Time (optional)
end_time = 'end_time_example' # str | End time (optional)
status = 'status_example' # str | Status: PROCESSING: in progress / DONE：completed / FAILED: failed (optional)

try:
    # Stablecoin order list
    api_response = api_instance.list_stable_coin_orders(page_size=page_size, page_number=page_number, coin_name=coin_name, start_time=start_time, end_time=end_time, status=status)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling OTCApi->list_stable_coin_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **str**| Number of records per page | [optional] 
 **page_number** | **str**| Page number | [optional] 
 **coin_name** | **str**| ordercurrency | [optional] 
 **start_time** | **str**| Start Time | [optional] 
 **end_time** | **str**| End time | [optional] 
 **status** | **str**| Status: PROCESSING: in progress / DONE：completed / FAILED: failed | [optional] 

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
**200** | Query successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_otc_order_detail**
> InlineResponse20013 get_otc_order_detail(order_id)

Fiat order details

Query fiat order details

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
api_instance = gate_api.OTCApi(api_client)
order_id = 'order_id_example' # str | Order ID

try:
    # Fiat order details
    api_response = api_instance.get_otc_order_detail(order_id)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling OTCApi->get_otc_order_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| Order ID | 

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
**200** | Query successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

