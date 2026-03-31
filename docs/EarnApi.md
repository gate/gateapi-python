# gate_api.EarnApi

All URIs are relative to *https://api.gateio.ws/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_dual_investment_plans**](EarnApi.md#list_dual_investment_plans) | **GET** /earn/dual/investment_plan | Dual Investment product list
[**list_dual_orders**](EarnApi.md#list_dual_orders) | **GET** /earn/dual/orders | Dual Investment order list
[**place_dual_order**](EarnApi.md#place_dual_order) | **POST** /earn/dual/orders | Place Dual Investment order
[**list_dual_balance**](EarnApi.md#list_dual_balance) | **GET** /earn/dual/balance | Dual-Currency Earning Assets
[**find_coin**](EarnApi.md#find_coin) | **GET** /earn/staking/coins | Staking coins
[**swap_staking_coin**](EarnApi.md#swap_staking_coin) | **POST** /earn/staking/swap | On-chain token swap for earned coins
[**order_list**](EarnApi.md#order_list) | **GET** /earn/staking/order_list | List of on-chain coin-earning orders
[**award_list**](EarnApi.md#award_list) | **GET** /earn/staking/award_list | On-chain coin-earning dividend records
[**asset_list**](EarnApi.md#asset_list) | **GET** /earn/staking/assets | On-chain coin-earning assets
[**create_auto_invest_plan**](EarnApi.md#create_auto_invest_plan) | **POST** /earn/autoinvest/plans/create | Create auto invest plan
[**update_auto_invest_plan**](EarnApi.md#update_auto_invest_plan) | **POST** /earn/autoinvest/plans/update | UpdateAuto invest plan
[**stop_auto_invest_plan**](EarnApi.md#stop_auto_invest_plan) | **POST** /earn/autoinvest/plans/stop | StopAuto invest plan
[**add_position_auto_invest_plan**](EarnApi.md#add_position_auto_invest_plan) | **POST** /earn/autoinvest/plans/add_position | Add position immediately
[**list_auto_invest_coins**](EarnApi.md#list_auto_invest_coins) | **GET** /earn/autoinvest/coins | QueryCurrencies supporting auto invest
[**get_auto_invest_min_amount**](EarnApi.md#get_auto_invest_min_amount) | **POST** /earn/autoinvest/min_invest_amount | Get minimum investment amount
[**list_auto_invest_plan_records**](EarnApi.md#list_auto_invest_plan_records) | **GET** /earn/autoinvest/plans/records | List plan execution records
[**list_auto_invest_orders**](EarnApi.md#list_auto_invest_orders) | **GET** /earn/autoinvest/orders | List plan execution recordsDetails（OrderDetails）
[**list_auto_invest_config**](EarnApi.md#list_auto_invest_config) | **GET** /earn/autoinvest/config | List investment currency configuration
[**get_auto_invest_plan_detail**](EarnApi.md#get_auto_invest_plan_detail) | **GET** /earn/autoinvest/plans/detail | QueryAuto invest planDetails
[**list_auto_invest_plans**](EarnApi.md#list_auto_invest_plans) | **GET** /earn/autoinvest/plans/list_info | QueryAuto invest planList
[**list_earn_fixed_term_products**](EarnApi.md#list_earn_fixed_term_products) | **GET** /earn/fixed-term/product | Get product list
[**list_earn_fixed_term_products_by_asset**](EarnApi.md#list_earn_fixed_term_products_by_asset) | **GET** /earn/fixed-term/product/{asset}/list | Get product list by single currency
[**list_earn_fixed_term_lends**](EarnApi.md#list_earn_fixed_term_lends) | **GET** /earn/fixed-term/user/lend | Subscription list
[**create_earn_fixed_term_lend**](EarnApi.md#create_earn_fixed_term_lend) | **POST** /earn/fixed-term/user/lend | Subscription
[**create_earn_fixed_term_pre_redeem**](EarnApi.md#create_earn_fixed_term_pre_redeem) | **POST** /earn/fixed-term/user/pre-redeem | Redeem
[**list_earn_fixed_term_history**](EarnApi.md#list_earn_fixed_term_history) | **GET** /earn/fixed-term/user/history | Subscription history


# **list_dual_investment_plans**
> list[DualGetPlans] list_dual_investment_plans(plan_id=plan_id)

Dual Investment product list

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
api_instance = gate_api.EarnApi(api_client)
plan_id = 1 # int | Financial project ID (optional)

try:
    # Dual Investment product list
    api_response = api_instance.list_dual_investment_plans(plan_id=plan_id)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling EarnApi->list_dual_investment_plans: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_id** | **int**| Financial project ID | [optional] 

### Return type

[**list[DualGetPlans]**](DualGetPlans.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dual_orders**
> list[DualGetOrders] list_dual_orders(_from=_from, to=to, page=page, limit=limit)

Dual Investment order list

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
api_instance = gate_api.EarnApi(api_client)
_from = 1740727000 # int | Start settlement time (optional)
to = 1740729000 # int | End settlement time (optional)
page = 1 # int | Page number (optional) (default to 1)
limit = 100 # int | Maximum number of records returned in a single list (optional) (default to 100)

try:
    # Dual Investment order list
    api_response = api_instance.list_dual_orders(_from=_from, to=to, page=page, limit=limit)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling EarnApi->list_dual_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **int**| Start settlement time | [optional] 
 **to** | **int**| End settlement time | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **limit** | **int**| Maximum number of records returned in a single list | [optional] [default to 100]

### Return type

[**list[DualGetOrders]**](DualGetOrders.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **place_dual_order**
> PlaceDualInvestmentOrder place_dual_order(place_dual_investment_order_params)

Place Dual Investment order

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
api_instance = gate_api.EarnApi(api_client)
place_dual_investment_order_params = gate_api.PlaceDualInvestmentOrderParams() # PlaceDualInvestmentOrderParams | 

try:
    # Place Dual Investment order
    api_response = api_instance.place_dual_order(place_dual_investment_order_params)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling EarnApi->place_dual_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **place_dual_investment_order_params** | [**PlaceDualInvestmentOrderParams**](PlaceDualInvestmentOrderParams.md)|  | 

### Return type

[**PlaceDualInvestmentOrder**](PlaceDualInvestmentOrder.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Order placed successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dual_balance**
> DualGetBalance list_dual_balance()

Dual-Currency Earning Assets

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
api_instance = gate_api.EarnApi(api_client)

try:
    # Dual-Currency Earning Assets
    api_response = api_instance.list_dual_balance()
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling EarnApi->list_dual_balance: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DualGetBalance**](DualGetBalance.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_coin**
> list[object] find_coin(cointype=cointype)

Staking coins

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
api_instance = gate_api.EarnApi(api_client)
cointype = 'cointype_example' # str | Currency type: swap - voucher; lock - locked position; debt - US Treasury bond. (optional)

try:
    # Staking coins
    api_response = api_instance.find_coin(cointype=cointype)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling EarnApi->find_coin: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cointype** | **str**| Currency type: swap - voucher; lock - locked position; debt - US Treasury bond. | [optional] 

### Return type

**list[object]**

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **swap_staking_coin**
> SwapCoinStruct swap_staking_coin(swap_coin)

On-chain token swap for earned coins

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
api_instance = gate_api.EarnApi(api_client)
swap_coin = gate_api.SwapCoin() # SwapCoin | 

try:
    # On-chain token swap for earned coins
    api_response = api_instance.swap_staking_coin(swap_coin)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling EarnApi->swap_staking_coin: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **swap_coin** | [**SwapCoin**](SwapCoin.md)|  | 

### Return type

[**SwapCoinStruct**](SwapCoinStruct.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Swap successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_list**
> OrderListStruct order_list(pid=pid, coin=coin, type=type, page=page)

List of on-chain coin-earning orders

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
api_instance = gate_api.EarnApi(api_client)
pid = 7 # int | Product ID (optional)
coin = 'ETH' # str | Currency name (optional)
type = 0 # int | Type 0-staking 1-redemption (optional)
page = 1 # int | Page number (optional) (default to 1)

try:
    # List of on-chain coin-earning orders
    api_response = api_instance.order_list(pid=pid, coin=coin, type=type, page=page)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling EarnApi->order_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pid** | **int**| Product ID | [optional] 
 **coin** | **str**| Currency name | [optional] 
 **type** | **int**| Type 0-staking 1-redemption | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]

### Return type

[**OrderListStruct**](OrderListStruct.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **award_list**
> AwardListStruct award_list(pid=pid, coin=coin, page=page)

On-chain coin-earning dividend records

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
api_instance = gate_api.EarnApi(api_client)
pid = 7 # int | Product ID (optional)
coin = 'ETH' # str | Currency name (optional)
page = 1 # int | Page number (optional) (default to 1)

try:
    # On-chain coin-earning dividend records
    api_response = api_instance.award_list(pid=pid, coin=coin, page=page)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling EarnApi->award_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pid** | **int**| Product ID | [optional] 
 **coin** | **str**| Currency name | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]

### Return type

[**AwardListStruct**](AwardListStruct.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asset_list**
> list[object] asset_list(coin=coin)

On-chain coin-earning assets

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
api_instance = gate_api.EarnApi(api_client)
coin = 'ETH' # str | Currency name (optional)

try:
    # On-chain coin-earning assets
    api_response = api_instance.asset_list(coin=coin)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling EarnApi->asset_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coin** | **str**| Currency name | [optional] 

### Return type

**list[object]**

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_auto_invest_plan**
> AutoInvestPlanCreateResp create_auto_invest_plan(auto_invest_plan_create)

Create auto invest plan

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
api_instance = gate_api.EarnApi(api_client)
auto_invest_plan_create = gate_api.AutoInvestPlanCreate() # AutoInvestPlanCreate | 

try:
    # Create auto invest plan
    api_response = api_instance.create_auto_invest_plan(auto_invest_plan_create)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling EarnApi->create_auto_invest_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auto_invest_plan_create** | [**AutoInvestPlanCreate**](AutoInvestPlanCreate.md)|  | 

### Return type

[**AutoInvestPlanCreateResp**](AutoInvestPlanCreateResp.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_auto_invest_plan**
> update_auto_invest_plan(auto_invest_plan_update)

UpdateAuto invest plan

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
api_instance = gate_api.EarnApi(api_client)
auto_invest_plan_update = gate_api.AutoInvestPlanUpdate() # AutoInvestPlanUpdate | 

try:
    # UpdateAuto invest plan
    api_instance.update_auto_invest_plan(auto_invest_plan_update)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling EarnApi->update_auto_invest_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auto_invest_plan_update** | [**AutoInvestPlanUpdate**](AutoInvestPlanUpdate.md)|  | 

### Return type

void (empty response body)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_auto_invest_plan**
> stop_auto_invest_plan(auto_invest_plan_stop)

StopAuto invest plan

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
api_instance = gate_api.EarnApi(api_client)
auto_invest_plan_stop = gate_api.AutoInvestPlanStop() # AutoInvestPlanStop | 

try:
    # StopAuto invest plan
    api_instance.stop_auto_invest_plan(auto_invest_plan_stop)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling EarnApi->stop_auto_invest_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auto_invest_plan_stop** | [**AutoInvestPlanStop**](AutoInvestPlanStop.md)|  | 

### Return type

void (empty response body)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Stopped successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_position_auto_invest_plan**
> add_position_auto_invest_plan(auto_invest_plan_add_position)

Add position immediately

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
api_instance = gate_api.EarnApi(api_client)
auto_invest_plan_add_position = gate_api.AutoInvestPlanAddPosition() # AutoInvestPlanAddPosition | 

try:
    # Add position immediately
    api_instance.add_position_auto_invest_plan(auto_invest_plan_add_position)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling EarnApi->add_position_auto_invest_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auto_invest_plan_add_position** | [**AutoInvestPlanAddPosition**](AutoInvestPlanAddPosition.md)|  | 

### Return type

void (empty response body)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Add PositionSuccess |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_auto_invest_coins**
> list[AutoInvestCoinsItem] list_auto_invest_coins(plan_money=plan_money)

QueryCurrencies supporting auto invest

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
api_instance = gate_api.EarnApi(api_client)
plan_money = 'USDT' # str | Pricing currency，Optional: USDT or BTC，Default: USDT (optional)

try:
    # QueryCurrencies supporting auto invest
    api_response = api_instance.list_auto_invest_coins(plan_money=plan_money)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling EarnApi->list_auto_invest_coins: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_money** | **str**| Pricing currency，Optional: USDT or BTC，Default: USDT | [optional] 

### Return type

[**list[AutoInvestCoinsItem]**](AutoInvestCoinsItem.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_auto_invest_min_amount**
> AutoInvestMinInvestAmountResp get_auto_invest_min_amount(auto_invest_min_invest_amount)

Get minimum investment amount

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
api_instance = gate_api.EarnApi(api_client)
auto_invest_min_invest_amount = gate_api.AutoInvestMinInvestAmount() # AutoInvestMinInvestAmount | 

try:
    # Get minimum investment amount
    api_response = api_instance.get_auto_invest_min_amount(auto_invest_min_invest_amount)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling EarnApi->get_auto_invest_min_amount: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auto_invest_min_invest_amount** | [**AutoInvestMinInvestAmount**](AutoInvestMinInvestAmount.md)|  | 

### Return type

[**AutoInvestMinInvestAmountResp**](AutoInvestMinInvestAmountResp.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_auto_invest_plan_records**
> AutoInvestPlanRecordsResp list_auto_invest_plan_records(plan_id, page=page, page_size=page_size)

List plan execution records

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
api_instance = gate_api.EarnApi(api_client)
plan_id = 141378 # int | Plan ID
page = 1 # int | page number (optional)
page_size = 10 # int | Items per page，Maximum 100 (optional)

try:
    # List plan execution records
    api_response = api_instance.list_auto_invest_plan_records(plan_id, page=page, page_size=page_size)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling EarnApi->list_auto_invest_plan_records: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_id** | **int**| Plan ID | 
 **page** | **int**| page number | [optional] 
 **page_size** | **int**| Items per page，Maximum 100 | [optional] 

### Return type

[**AutoInvestPlanRecordsResp**](AutoInvestPlanRecordsResp.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_auto_invest_orders**
> list[AutoInvestOrderItem] list_auto_invest_orders(plan_id, record_id)

List plan execution recordsDetails（OrderDetails）

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
api_instance = gate_api.EarnApi(api_client)
plan_id = 142583 # int | Plan ID
record_id = 1770805384904919 # int | Record ID

try:
    # List plan execution recordsDetails（OrderDetails）
    api_response = api_instance.list_auto_invest_orders(plan_id, record_id)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling EarnApi->list_auto_invest_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_id** | **int**| Plan ID | 
 **record_id** | **int**| Record ID | 

### Return type

[**list[AutoInvestOrderItem]**](AutoInvestOrderItem.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_auto_invest_config**
> list[AutoInvestConfigItem] list_auto_invest_config()

List investment currency configuration

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
api_instance = gate_api.EarnApi(api_client)

try:
    # List investment currency configuration
    api_response = api_instance.list_auto_invest_config()
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling EarnApi->list_auto_invest_config: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[AutoInvestConfigItem]**](AutoInvestConfigItem.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_auto_invest_plan_detail**
> AutoInvestPlanDetail get_auto_invest_plan_detail(plan_id)

QueryAuto invest planDetails

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
api_instance = gate_api.EarnApi(api_client)
plan_id = 142609 # int | Plan ID

try:
    # QueryAuto invest planDetails
    api_response = api_instance.get_auto_invest_plan_detail(plan_id)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling EarnApi->get_auto_invest_plan_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_id** | **int**| Plan ID | 

### Return type

[**AutoInvestPlanDetail**](AutoInvestPlanDetail.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_auto_invest_plans**
> AutoInvestPlanListInfoResp list_auto_invest_plans(status, page=page, page_size=page_size)

QueryAuto invest planList

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
api_instance = gate_api.EarnApi(api_client)
status = 'active' # str | Plan status，History history，Active active
page = 56 # int | page number (optional)
page_size = 56 # int | Items per page，Maximum 100 (optional)

try:
    # QueryAuto invest planList
    api_response = api_instance.list_auto_invest_plans(status, page=page, page_size=page_size)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling EarnApi->list_auto_invest_plans: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**| Plan status，History history，Active active | 
 **page** | **int**| page number | [optional] 
 **page_size** | **int**| Items per page，Maximum 100 | [optional] 

### Return type

[**AutoInvestPlanListInfoResp**](AutoInvestPlanListInfoResp.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_earn_fixed_term_products**
> ListEarnFixedTermProductsResponse list_earn_fixed_term_products(page, limit, asset=asset, type=type)

Get product list

Query fixed-term earn product list. Supports filtering by currency, product type, status, etc. Returns product interest rate, lock-up period, quota, and reward campaign information

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
api_instance = gate_api.EarnApi(api_client)
page = 1 # int | Page number
limit = 100 # int | Page size
asset = 'USDT' # str | Currency (optional)
type = 1 # int | Product type: 1 for regular, 2 for VIP (optional)

try:
    # Get product list
    api_response = api_instance.list_earn_fixed_term_products(page, limit, asset=asset, type=type)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling EarnApi->list_earn_fixed_term_products: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number | 
 **limit** | **int**| Page size | 
 **asset** | **str**| Currency | [optional] 
 **type** | **int**| Product type: 1 for regular, 2 for VIP | [optional] 

### Return type

[**ListEarnFixedTermProductsResponse**](ListEarnFixedTermProductsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Product list retrieved successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_earn_fixed_term_products_by_asset**
> ListEarnFixedTermProductsByAssetResponse list_earn_fixed_term_products_by_asset(asset, type=type)

Get product list by single currency

Sort by product term in ascending order

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
api_instance = gate_api.EarnApi(api_client)
asset = 'USDT' # str | Currency name, e.g., USDT, BTC
type = '1' # str | Product type: \"\" or 1 for regular product list, 2 for VIP product list, 0 for all products (optional)

try:
    # Get product list by single currency
    api_response = api_instance.list_earn_fixed_term_products_by_asset(asset, type=type)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling EarnApi->list_earn_fixed_term_products_by_asset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | **str**| Currency name, e.g., USDT, BTC | 
 **type** | **str**| Product type: \&quot;\&quot; or 1 for regular product list, 2 for VIP product list, 0 for all products | [optional] 

### Return type

[**ListEarnFixedTermProductsByAssetResponse**](ListEarnFixedTermProductsByAssetResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Single currency product list retrieved successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_earn_fixed_term_lends**
> ListEarnFixedTermLendsResponse list_earn_fixed_term_lends(order_type, page, limit, product_id=product_id, order_id=order_id, asset=asset, sub_business=sub_business, business_filter=business_filter)

Subscription list

Query the user's fixed-term earn subscription order list. Supports filtering by product, currency, order type, etc. Returns order details, earnings, rewards, and interest rate boost coupon information

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
api_instance = gate_api.EarnApi(api_client)
order_type = '1' # str | Order type: 1 for current orders, 2 for historical orders
page = 1 # int | Page number
limit = 10 # int | Page size
product_id = 56 # int | Product ID (optional)
order_id = 56 # int | Order ID (optional)
asset = 'asset_example' # str | Currency (optional)
sub_business = 56 # int | Sub-business (optional)
business_filter = '[{\"business\":1, \"sub_business\": 0},{\"business\":2, \"sub_business\": 0}]' # str | Business filter conditions, JSON array format, e.g., [{\"business\":1, \"sub_business\": 0}]. business: 1 for regular, 2 for VIP (optional)

try:
    # Subscription list
    api_response = api_instance.list_earn_fixed_term_lends(order_type, page, limit, product_id=product_id, order_id=order_id, asset=asset, sub_business=sub_business, business_filter=business_filter)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling EarnApi->list_earn_fixed_term_lends: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_type** | **str**| Order type: 1 for current orders, 2 for historical orders | 
 **page** | **int**| Page number | 
 **limit** | **int**| Page size | 
 **product_id** | **int**| Product ID | [optional] 
 **order_id** | **int**| Order ID | [optional] 
 **asset** | **str**| Currency | [optional] 
 **sub_business** | **int**| Sub-business | [optional] 
 **business_filter** | **str**| Business filter conditions, JSON array format, e.g., [{\&quot;business\&quot;:1, \&quot;sub_business\&quot;: 0}]. business: 1 for regular, 2 for VIP | [optional] 

### Return type

[**ListEarnFixedTermLendsResponse**](ListEarnFixedTermLendsResponse.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Subscription order list retrieved successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_earn_fixed_term_lend**
> CreateEarnFixedTermLendResponse create_earn_fixed_term_lend(fixed_term_lend_request=fixed_term_lend_request)

Subscription

Subscribe to a fixed-term earn product by specifying the product ID and subscription amount. Optionally enable auto-renewal and apply an interest rate boost coupon

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
api_instance = gate_api.EarnApi(api_client)
fixed_term_lend_request = gate_api.FixedTermLendRequest() # FixedTermLendRequest |  (optional)

try:
    # Subscription
    api_response = api_instance.create_earn_fixed_term_lend(fixed_term_lend_request=fixed_term_lend_request)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling EarnApi->create_earn_fixed_term_lend: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fixed_term_lend_request** | [**FixedTermLendRequest**](FixedTermLendRequest.md)|  | [optional] 

### Return type

[**CreateEarnFixedTermLendResponse**](CreateEarnFixedTermLendResponse.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Subscription successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_earn_fixed_term_pre_redeem**
> CreateEarnFixedTermPreRedeemResponse create_earn_fixed_term_pre_redeem(earn_fixed_term_pre_redeem_request=earn_fixed_term_pre_redeem_request)

Redeem

Early redemption of a fixed-term earn order, order ID is required

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
api_instance = gate_api.EarnApi(api_client)
earn_fixed_term_pre_redeem_request = gate_api.EarnFixedTermPreRedeemRequest() # EarnFixedTermPreRedeemRequest |  (optional)

try:
    # Redeem
    api_response = api_instance.create_earn_fixed_term_pre_redeem(earn_fixed_term_pre_redeem_request=earn_fixed_term_pre_redeem_request)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling EarnApi->create_earn_fixed_term_pre_redeem: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **earn_fixed_term_pre_redeem_request** | [**EarnFixedTermPreRedeemRequest**](EarnFixedTermPreRedeemRequest.md)|  | [optional] 

### Return type

[**CreateEarnFixedTermPreRedeemResponse**](CreateEarnFixedTermPreRedeemResponse.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Redemption successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_earn_fixed_term_history**
> ListEarnFixedTermHistoryResponse list_earn_fixed_term_history(type, page, limit, product_id=product_id, order_id=order_id, asset=asset, start_at=start_at, end_at=end_at, sub_business=sub_business, business_filter=business_filter)

Subscription history

Query the user's fixed-term earn history records. Supports filtering by type (subscription, redemption, interest, bonus rewards) and time range

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
api_instance = gate_api.EarnApi(api_client)
type = '1' # str | 1 for subscription, 2 for redemption, 3 for interest, 4 for bonus reward
page = 1 # int | Page number
limit = 10 # int | Page size
product_id = 56 # int | Product ID (optional)
order_id = 'order_id_example' # str | Order ID (optional)
asset = 'asset_example' # str | Currency (optional)
start_at = 56 # int | Start timestamp (optional)
end_at = 56 # int | End Timestamp (optional)
sub_business = 56 # int | Sub-business (optional)
business_filter = '[{\"business\":1, \"sub_business\": 0},{\"business\":2, \"sub_business\": 0}]' # str | Business filter conditions, JSON array format, e.g., [{\"business\":1, \"sub_business\": 0}]. business: 1 for regular, 2 for VIP (optional)

try:
    # Subscription history
    api_response = api_instance.list_earn_fixed_term_history(type, page, limit, product_id=product_id, order_id=order_id, asset=asset, start_at=start_at, end_at=end_at, sub_business=sub_business, business_filter=business_filter)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling EarnApi->list_earn_fixed_term_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| 1 for subscription, 2 for redemption, 3 for interest, 4 for bonus reward | 
 **page** | **int**| Page number | 
 **limit** | **int**| Page size | 
 **product_id** | **int**| Product ID | [optional] 
 **order_id** | **str**| Order ID | [optional] 
 **asset** | **str**| Currency | [optional] 
 **start_at** | **int**| Start timestamp | [optional] 
 **end_at** | **int**| End Timestamp | [optional] 
 **sub_business** | **int**| Sub-business | [optional] 
 **business_filter** | **str**| Business filter conditions, JSON array format, e.g., [{\&quot;business\&quot;:1, \&quot;sub_business\&quot;: 0}]. business: 1 for regular, 2 for VIP | [optional] 

### Return type

[**ListEarnFixedTermHistoryResponse**](ListEarnFixedTermHistoryResponse.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | History records retrieved successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

