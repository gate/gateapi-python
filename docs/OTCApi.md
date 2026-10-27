# gate_api.OTCApi

All URIs are relative to *https://api.gateio.ws/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_otc_quote**](OTCApi.md#create_otc_quote) | **POST** /otc/quote | Fiat and stablecoin quote
[**create_otc_order**](OTCApi.md#create_otc_order) | **POST** /otc/order/create | Create fiat order
[**create_stable_coin_order**](OTCApi.md#create_stable_coin_order) | **POST** /otc/stable_coin/order/create | Create stablecoin order
[**get_bank_list_inner_path**](OTCApi.md#get_bank_list_inner_path) | **GET** /otc/bank/list | Get user bank card list
[**create_otc_bank**](OTCApi.md#create_otc_bank) | **POST** /otc/bank/create | Create bank card
[**delete_otc_bank**](OTCApi.md#delete_otc_bank) | **POST** /otc/bank/delete | Delete bank card
[**set_default_otc_bank**](OTCApi.md#set_default_otc_bank) | **POST** /otc/bank/set_default | Set default bank card
[**get_otc_bank_supplement_checklist**](OTCApi.md#get_otc_bank_supplement_checklist) | **GET** /otc/bank/bank_supplement_checklist | Query the checklist of materials to supplement for a bank card
[**submit_otc_bank_personal_supplement**](OTCApi.md#submit_otc_bank_personal_supplement) | **POST** /otc/bank/personal/bank_supplement | Submit Bank Card Supplement Materials (Personal)
[**submit_otc_bank_enterprise_supplement**](OTCApi.md#submit_otc_bank_enterprise_supplement) | **POST** /otc/bank/enterprise/bank_supplement | Submit Bank Card Supplement Materials (Enterprise)
[**create_otc_upload_pre_upload**](OTCApi.md#create_otc_upload_pre_upload) | **POST** /otc/upload/pre_upload | Pre-upload file (temporary bucket)
[**mark_otc_order_paid**](OTCApi.md#mark_otc_order_paid) | **POST** /otc/order/paid | Mark fiat order as paid (deposit confirmation)
[**cancel_otc_order**](OTCApi.md#cancel_otc_order) | **POST** /otc/order/cancel | Fiat order cancellation
[**list_otc_orders**](OTCApi.md#list_otc_orders) | **GET** /otc/order/list | Fiat order list
[**list_stable_coin_orders**](OTCApi.md#list_stable_coin_orders) | **GET** /otc/stable_coin/order/list | Stablecoin order list
[**get_otc_order_detail**](OTCApi.md#get_otc_order_detail) | **GET** /otc/order/detail | Fiat order details


# **create_otc_quote**
> OtcQuoteResponse create_otc_quote(otc_quote_request)

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
otc_quote_request = gate_api.OtcQuoteRequest() # OtcQuoteRequest | 

try:
    # Fiat and stablecoin quote
    api_response = api_instance.create_otc_quote(otc_quote_request)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling OTCApi->create_otc_quote: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **otc_quote_request** | [**OtcQuoteRequest**](OtcQuoteRequest.md)|  | 

### Return type

[**OtcQuoteResponse**](OtcQuoteResponse.md)

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
> OtcActionResponse create_otc_order(otc_order_request)

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
otc_order_request = gate_api.OtcOrderRequest() # OtcOrderRequest | 

try:
    # Create fiat order
    api_response = api_instance.create_otc_order(otc_order_request)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling OTCApi->create_otc_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **otc_order_request** | [**OtcOrderRequest**](OtcOrderRequest.md)|  | 

### Return type

[**OtcActionResponse**](OtcActionResponse.md)

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
> OtcStableCoinOrderCreateResponse create_stable_coin_order(otc_stable_coin_order_request)

Create stablecoin order

Create a stablecoin order. All request body fields except `promotion_code` are required.

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
otc_stable_coin_order_request = gate_api.OtcStableCoinOrderRequest() # OtcStableCoinOrderRequest | 

try:
    # Create stablecoin order
    api_response = api_instance.create_stable_coin_order(otc_stable_coin_order_request)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling OTCApi->create_stable_coin_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **otc_stable_coin_order_request** | [**OtcStableCoinOrderRequest**](OtcStableCoinOrderRequest.md)|  | 

### Return type

[**OtcStableCoinOrderCreateResponse**](OtcStableCoinOrderCreateResponse.md)

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

# **get_bank_list_inner_path**
> OtcBankListResponse get_bank_list_inner_path()

Get user bank card list

List the user's bank cards for selecting a card when placing an order. **Default card**: use the `is_default` field in each list item (`1` indicates the default). The deprecated standalone default-bank-card endpoint is no longer required.

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
    api_response = api_instance.get_bank_list_inner_path()
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling OTCApi->get_bank_list_inner_path: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**OtcBankListResponse**](OtcBankListResponse.md)

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

# **create_otc_bank**
> OtcBankCreateResponse create_otc_bank(bank_account_name, bank_name, bank_country, bank_address, iban, swift, remittance_line_number=remittance_line_number, agent_bank_name=agent_bank_name, agent_bank_swift=agent_bank_swift, documentation_file=documentation_file, documentation_file_key=documentation_file_key, file_type=file_type)

Create bank card

Bind a bank card. Under the Global entity, non-same-name accounts may enter manual review (`status` pending) and require supplementary materials later. Corresponds to Inner: `POST /bank/create`. Fields and protocol follow the live form/gateway; `bank_account_name` may be Base64-encoded in some environments—see integration notes.  Account-opening proof supports two methods (choose one):  1. **Pre-upload (recommended)**: call `POST /otc/upload/pre_upload` (`scene=bank`) to obtain a temporary-bucket Policy and upload directly to S3, then pass `documentation_file_key` + `file_type` in this endpoint; 2. **Multipart direct upload**: pass the `documentation_file` file field; the server writes directly to the production bucket.  When using pre-upload, the server validates object existence and that the uid in the `file_key` path matches the caller; after validation, the object is moved to the production bucket and persisted. Cross-user references return `Invalid parameters file_key`; incomplete direct upload returns `Invalid parameters file not uploaded`.

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
bank_account_name = 'bank_account_name_example' # str | 
bank_name = 'bank_name_example' # str | 
bank_country = 'bank_country_example' # str | 
bank_address = 'bank_address_example' # str | 
iban = 'iban_example' # str | 
swift = 'swift_example' # str | 
remittance_line_number = 'remittance_line_number_example' # str |  (optional)
agent_bank_name = 'agent_bank_name_example' # str |  (optional)
agent_bank_swift = 'agent_bank_swift_example' # str |  (optional)
documentation_file = 'documentation_file_example' # str | Multipart direct upload; mutually exclusive with documentation_file_key (optional)
documentation_file_key = 'documentation_file_key_example' # str | Pre-upload mode; file_key returned by pre_upload (plaintext or base64 accepted) (optional)
file_type = 'file_type_example' # str | Required when using documentation_file_key; plaintext MIME or its base64 (optional)

try:
    # Create bank card
    api_response = api_instance.create_otc_bank(bank_account_name, bank_name, bank_country, bank_address, iban, swift, remittance_line_number=remittance_line_number, agent_bank_name=agent_bank_name, agent_bank_swift=agent_bank_swift, documentation_file=documentation_file, documentation_file_key=documentation_file_key, file_type=file_type)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling OTCApi->create_otc_bank: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_account_name** | **str**|  | 
 **bank_name** | **str**|  | 
 **bank_country** | **str**|  | 
 **bank_address** | **str**|  | 
 **iban** | **str**|  | 
 **swift** | **str**|  | 
 **remittance_line_number** | **str**|  | [optional] 
 **agent_bank_name** | **str**|  | [optional] 
 **agent_bank_swift** | **str**|  | [optional] 
 **documentation_file** | **str**| Multipart direct upload; mutually exclusive with documentation_file_key | [optional] 
 **documentation_file_key** | **str**| Pre-upload mode; file_key returned by pre_upload (plaintext or base64 accepted) | [optional] 
 **file_type** | **str**| Required when using documentation_file_key; plaintext MIME or its base64 | [optional] 

### Return type

[**OtcBankCreateResponse**](OtcBankCreateResponse.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Accepted successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_otc_bank**
> OtcActionResponse delete_otc_bank(otc_bank_id_request)

Delete bank card

Delete the specified bank card. Corresponds to Inner: `POST /bank/delete`.

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
otc_bank_id_request = gate_api.OtcBankIdRequest() # OtcBankIdRequest | 

try:
    # Delete bank card
    api_response = api_instance.delete_otc_bank(otc_bank_id_request)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling OTCApi->delete_otc_bank: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **otc_bank_id_request** | [**OtcBankIdRequest**](OtcBankIdRequest.md)|  | 

### Return type

[**OtcActionResponse**](OtcActionResponse.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Deleted successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_default_otc_bank**
> OtcActionResponse set_default_otc_bank(otc_bank_id_request)

Set default bank card

Set the specified bank card as default. Corresponds to Inner: `POST /bank/set_default`.

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
otc_bank_id_request = gate_api.OtcBankIdRequest() # OtcBankIdRequest | 

try:
    # Set default bank card
    api_response = api_instance.set_default_otc_bank(otc_bank_id_request)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling OTCApi->set_default_otc_bank: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **otc_bank_id_request** | [**OtcBankIdRequest**](OtcBankIdRequest.md)|  | 

### Return type

[**OtcActionResponse**](OtcActionResponse.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Set successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_otc_bank_supplement_checklist**
> OtcBankSupplementChecklistResponse get_otc_bank_supplement_checklist(bank_id)

Query the checklist of materials to supplement for a bank card

**①** `bank_id` must be specified. After verifying that the card belongs to the current user and its status allows supplementary documents, the endpoint returns the required items based on the user's **approved advanced verification type** (personal/enterprise); each item's `description` states the submission requirements. Corresponding Inner endpoint: `GET /bank/bank_supplement_checklist`.

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
bank_id = 'bank_id_example' # str | Bank card ID (otc_rds / the id returned by the list endpoint).

try:
    # Query the checklist of materials to supplement for a bank card
    api_response = api_instance.get_otc_bank_supplement_checklist(bank_id)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling OTCApi->get_otc_bank_supplement_checklist: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_id** | **str**| Bank card ID (otc_rds / the id returned by the list endpoint). | 

### Return type

[**OtcBankSupplementChecklistResponse**](OtcBankSupplementChecklistResponse.md)

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

# **submit_otc_bank_personal_supplement**
> OtcActionResponse submit_otc_bank_personal_supplement(bank_id, id_document_front=id_document_front, id_document_back=id_document_back, address_proof=address_proof, relationship_proof=relationship_proof)

Submit Bank Card Supplement Materials (Personal)

**Personal professional verification (type=1)** users submit non-same-person/supplementary materials. Must match `user_type=personal` from `GET /otc/bank/bank_supplement_checklist?bank_id=`; otherwise rejected.  Two submission methods (can be mixed):  1. **Pre-upload (recommended)**: call `POST /otc/upload/pre_upload` (`scene=bank`) to upload to the temporary bucket, then fill file items by category in the `relationship_proof` JSON; pass **`key` as plaintext** object path (`base64_decode(pre_upload.file_key)`, e.g. `otc_temp/{uid}/bank/xxx.png`), and `file_type` as plaintext MIME; the server base64-encodes before persistence—do not pass base64 `file_key` directly; 2. **Multipart direct upload**: one file field per material item; field names match checklist `code` (`id_document_front`, `id_document_back`, `address_proof`).

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
bank_id = 'bank_id_example' # str | 
id_document_front = 'id_document_front_example' # str | ID document front-side file content (multipart file field, binary/Base64) (optional)
id_document_back = 'id_document_back_example' # str | ID document back-side file content (multipart file field, binary/Base64) (optional)
address_proof = 'address_proof_example' # str | Proof-of-address file content (multipart file field, binary/Base64) (optional)
relationship_proof = 'relationship_proof_example' # str | Optional. JSON string of relationship_proof. (optional)

try:
    # Submit Bank Card Supplement Materials (Personal)
    api_response = api_instance.submit_otc_bank_personal_supplement(bank_id, id_document_front=id_document_front, id_document_back=id_document_back, address_proof=address_proof, relationship_proof=relationship_proof)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling OTCApi->submit_otc_bank_personal_supplement: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_id** | **str**|  | 
 **id_document_front** | **str**| ID document front-side file content (multipart file field, binary/Base64) | [optional] 
 **id_document_back** | **str**| ID document back-side file content (multipart file field, binary/Base64) | [optional] 
 **address_proof** | **str**| Proof-of-address file content (multipart file field, binary/Base64) | [optional] 
 **relationship_proof** | **str**| Optional. JSON string of relationship_proof. | [optional] 

### Return type

[**OtcActionResponse**](OtcActionResponse.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Accepted successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_otc_bank_enterprise_supplement**
> OtcActionResponse submit_otc_bank_enterprise_supplement(bank_id, uid=uid, certificate=certificate, share_holders=share_holders, passport=passport, share_holding_structure=share_holding_structure, funds_statement=funds_statement, additional=additional, relationship_proof=relationship_proof)

Submit Bank Card Supplement Materials (Enterprise)

**Enterprise professional verification (type=2)** users submit supplementary materials. Must match `user_type=enterprise` from the checklist.  Two submission methods (can be mixed):  1. **Pre-upload (recommended)**: call `POST /otc/upload/pre_upload` (`scene=bank`), fill file items by category in `relationship_proof`; pass **`key` as plaintext** object path (`base64_decode(pre_upload.file_key)`), and `file_type` as plaintext MIME; 2. **Multipart direct upload**: file field names `certificate`, `share_holders`, `passport`, `share_holding_structure`; optional `funds_statement`, `additional`.

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
bank_id = 'bank_id_example' # str | 
uid = 'uid_example' # str |  (optional)
certificate = 'certificate_example' # str | Business license / registration certificate file content (multipart file field, binary/Base64) (optional)
share_holders = 'share_holders_example' # str | Register of shareholders file content (multipart file field, binary/Base64) (optional)
passport = 'passport_example' # str | Legal representative / shareholder passport file content (multipart file field, binary/Base64) (optional)
share_holding_structure = 'share_holding_structure_example' # str | Ownership structure chart file content (multipart file field, binary/Base64) (optional)
funds_statement = 'funds_statement_example' # str | Proof-of-funds file content (multipart file field, binary/Base64, optional) (optional)
additional = 'additional_example' # str | Other supplementary material file content (multipart file field, binary/Base64, optional) (optional)
relationship_proof = 'relationship_proof_example' # str | Optional. JSON string of relationship_proof. (optional)

try:
    # Submit Bank Card Supplement Materials (Enterprise)
    api_response = api_instance.submit_otc_bank_enterprise_supplement(bank_id, uid=uid, certificate=certificate, share_holders=share_holders, passport=passport, share_holding_structure=share_holding_structure, funds_statement=funds_statement, additional=additional, relationship_proof=relationship_proof)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling OTCApi->submit_otc_bank_enterprise_supplement: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_id** | **str**|  | 
 **uid** | **str**|  | [optional] 
 **certificate** | **str**| Business license / registration certificate file content (multipart file field, binary/Base64) | [optional] 
 **share_holders** | **str**| Register of shareholders file content (multipart file field, binary/Base64) | [optional] 
 **passport** | **str**| Legal representative / shareholder passport file content (multipart file field, binary/Base64) | [optional] 
 **share_holding_structure** | **str**| Ownership structure chart file content (multipart file field, binary/Base64) | [optional] 
 **funds_statement** | **str**| Proof-of-funds file content (multipart file field, binary/Base64, optional) | [optional] 
 **additional** | **str**| Other supplementary material file content (multipart file field, binary/Base64, optional) | [optional] 
 **relationship_proof** | **str**| Optional. JSON string of relationship_proof. | [optional] 

### Return type

[**OtcActionResponse**](OtcActionResponse.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Accepted successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_otc_upload_pre_upload**
> OtcUploadPreUploadResponse create_otc_upload_pre_upload(otc_upload_pre_upload_request)

Pre-upload file (temporary bucket)

After selecting a file, the client calls this endpoint first to obtain a temporary-bucket POST Policy and `file_key`; then upload directly to S3 using the returned `url` and `fields` (success HTTP 204); finally, in business submit endpoints (e.g. `POST /otc/order/paid`, `POST /otc/bank/create`), pass the **same base64 `file_key` unchanged** (do not decode). The server validates ownership and object existence, then moves to the production bucket and persists. Unsubmitted files remain in the temporary bucket and are reclaimed by lifecycle rules.  Corresponds to Inner: `POST /upload/pre_upload`.  **`content_type` must be sent as base64** (plaintext containing `/` may be blocked by the gateway). Only the following MIME types are supported:  | MIME | base64 | Extension | | --- | --- | --- | | image/png | aW1hZ2UvcG5n | .png | | image/jpeg | aW1hZ2UvanBlZw== | .jpeg | | image/jpg | aW1hZ2UvanBn | .jpg | | application/pdf | YXBwbGljYXRpb24vcGRm | .pdf |  **`scene` mapping to downstream endpoints**:  | scene | Typical use | | --- | --- | | general | Fiat buy payment receipt (`payment_receipt_file_key` in `POST /otc/order/paid`) | | bank | Add card, bank card supplementary materials | | assessment | Professional verification materials | | credit | Credit limit increase materials |  **Credential validity**: response `expires_in` is **5400 seconds (90 minutes)**; `fields.Policy` `expiration` matches it. Complete the S3 direct upload within this window; after expiry, call this endpoint again for a new credential.  **File size**: the S3 POST Policy enforces `content-length-range` **1 byte ~ 10MB** (10485760 bytes). Uploads exceeding the limit are rejected by S3; all `scene` values share this limit.  **Direct S3 upload**: `url` is the upload address; send each key-value pair in `fields` unchanged as form-data; the `file` field must be last. Object path is generated as `otc_temp/{uid}/{scene}/{unique filename}`; uid is taken from the login session.  This endpoint returns `content type is required.` when `content_type` is missing. Ownership and object-existence checks for `file_key` are performed by the subsequent business submission endpoint.

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
otc_upload_pre_upload_request = gate_api.OtcUploadPreUploadRequest() # OtcUploadPreUploadRequest | 

try:
    # Pre-upload file (temporary bucket)
    api_response = api_instance.create_otc_upload_pre_upload(otc_upload_pre_upload_request)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling OTCApi->create_otc_upload_pre_upload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **otc_upload_pre_upload_request** | [**OtcUploadPreUploadRequest**](OtcUploadPreUploadRequest.md)|  | 

### Return type

[**OtcUploadPreUploadResponse**](OtcUploadPreUploadResponse.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Pre-upload credentials issued successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mark_otc_order_paid**
> OtcActionResponse mark_otc_order_paid(otc_mark_order_paid_request)

Mark fiat order as paid (deposit confirmation)

Mark a fiat buy order as paid (deposit confirmation). **A user payment receipt must be uploaded**: `payment_receipt_file_key` is required; supported formats are jpg / jpeg / png / pdf, with a maximum size of 10 MB per file (validated jointly by the service and gateway). The compatible field name `payment_receipt` depends on the gateway and production contract. The persisted field is `otc_trade_record.payment_receipt_file_key`. The Pay Inner path is `POST .../pay/order_set_paid` (which commonly identifies orders by `client_order_id`); the Inner path corresponding to this OpenAPI operation, `POST /order/paid`, still primarily uses `order_id`. If the gateway standardizes on the merchant order ID, follow the gateway documentation.  **Recommended pre-upload flow**: first call `POST /otc/upload/pre_upload` (`scene=general`) and upload directly to the temporary bucket, then pass the returned **base64 `file_key` unchanged** (do not decode) to this endpoint. The service validates the uid and object existence before moving the object to the production bucket. A cross-user key returns `Invalid parameters file_key`; an object that has not been uploaded returns `Invalid parameters file not uploaded`. The legacy flow using a base64 key for an object uploaded directly to the production bucket remains supported.

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
otc_mark_order_paid_request = gate_api.OtcMarkOrderPaidRequest() # OtcMarkOrderPaidRequest | 

try:
    # Mark fiat order as paid (deposit confirmation)
    api_response = api_instance.mark_otc_order_paid(otc_mark_order_paid_request)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling OTCApi->mark_otc_order_paid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **otc_mark_order_paid_request** | [**OtcMarkOrderPaidRequest**](OtcMarkOrderPaidRequest.md)|  | 

### Return type

[**OtcActionResponse**](OtcActionResponse.md)

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
> OtcActionResponse cancel_otc_order(order_id)

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

[**OtcActionResponse**](OtcActionResponse.md)

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
> OtcOrderListResponse list_otc_orders(type=type, fiat_currency=fiat_currency, crypto_currency=crypto_currency, start_time=start_time, end_time=end_time, status=status, pn=pn, ps=ps)

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
status = 'status_example' # str | DONE: completed CANCEL: canceled PROCESSING: in progress DISBURSED: disbursed (optional)
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
 **status** | **str**| DONE: completed CANCEL: canceled PROCESSING: in progress DISBURSED: disbursed | [optional] 
 **pn** | **str**| Page number | [optional] 
 **ps** | **str**| Number of items per page | [optional] 

### Return type

[**OtcOrderListResponse**](OtcOrderListResponse.md)

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
> OtcStableCoinOrderListResponse list_stable_coin_orders(page_size=page_size, page_number=page_number, coin_name=coin_name, start_time=start_time, end_time=end_time, status=status)

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

[**OtcStableCoinOrderListResponse**](OtcStableCoinOrderListResponse.md)

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
> OtcOrderDetailResponse get_otc_order_detail(order_id)

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

[**OtcOrderDetailResponse**](OtcOrderDetailResponse.md)

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

