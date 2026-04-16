# gate_api.AssetswapApi

All URIs are relative to *https://api.gateio.ws/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_asset_swap_assets**](AssetswapApi.md#list_asset_swap_assets) | **GET** /asset-swap/asset/list | Portfolio optimization — currency list
[**get_asset_swap_config**](AssetswapApi.md#get_asset_swap_config) | **GET** /asset-swap/config | Portfolio optimization — configuration
[**evaluate_asset_swap**](AssetswapApi.md#evaluate_asset_swap) | **GET** /asset-swap/evaluate | Portfolio optimization — valuation
[**create_asset_swap_order_v1**](AssetswapApi.md#create_asset_swap_order_v1) | **POST** /asset-swap/order/create | Portfolio optimization — place order
[**list_asset_swap_orders_v1**](AssetswapApi.md#list_asset_swap_orders_v1) | **GET** /asset-swap/order/list | Portfolio optimization — order list
[**preview_asset_swap_order_v1**](AssetswapApi.md#preview_asset_swap_order_v1) | **POST** /asset-swap/order/preview | Portfolio optimization — preview
[**get_asset_swap_order_v1**](AssetswapApi.md#get_asset_swap_order_v1) | **GET** /asset-swap/order/{order_id} | Portfolio optimization — query order


# **list_asset_swap_assets**
> ApiResponseAssetSwapListAssets list_asset_swap_assets()

Portfolio optimization — currency list

Project-Id-Version: GateApiTools 1.0.0 Report-Msgid-Bugs-To: EMAIL@ADDRESS POT-Creation-Date: 2025-11-12 18:14+0800 PO-Revision-Date: 2019-01-02 17:30+0800 Last-Translator: FULL NAME <EMAIL@ADDRESS> Language: en Language-Team: en <L@li.org> Plural-Forms: nplurals=2; plural=(n !=1) MIME-Version: 1.0 Content-Type: text/plain; charset=utf-8 Content-Transfer-Encoding: 8bit Generated-By: Babel 2.8.0 

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
api_instance = gate_api.AssetswapApi(api_client)

try:
    # Portfolio optimization — currency list
    api_response = api_instance.list_asset_swap_assets()
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling AssetswapApi->list_asset_swap_assets: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiResponseAssetSwapListAssets**](ApiResponseAssetSwapListAssets.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | HTTP 200，业务结果通过 code 字段区分 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_swap_config**
> ApiResponseAssetSwapConfig get_asset_swap_config()

Portfolio optimization — configuration

Project-Id-Version: GateApiTools 1.0.0 Report-Msgid-Bugs-To: EMAIL@ADDRESS POT-Creation-Date: 2025-11-12 18:14+0800 PO-Revision-Date: 2019-01-02 17:30+0800 Last-Translator: FULL NAME <EMAIL@ADDRESS> Language: en Language-Team: en <L@li.org> Plural-Forms: nplurals=2; plural=(n !=1) MIME-Version: 1.0 Content-Type: text/plain; charset=utf-8 Content-Transfer-Encoding: 8bit Generated-By: Babel 2.8.0 

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
api_instance = gate_api.AssetswapApi(api_client)

try:
    # Portfolio optimization — configuration
    api_response = api_instance.get_asset_swap_config()
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling AssetswapApi->get_asset_swap_config: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiResponseAssetSwapConfig**](ApiResponseAssetSwapConfig.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | HTTP 200，业务结果通过 code 字段区分 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **evaluate_asset_swap**
> ApiResponseAssetSwapEvaluate evaluate_asset_swap(max_evaluate_value=max_evaluate_value, cursor=cursor, size=size)

Portfolio optimization — valuation

Project-Id-Version: GateApiTools 1.0.0 Report-Msgid-Bugs-To: EMAIL@ADDRESS POT-Creation-Date: 2025-11-12 18:14+0800 PO-Revision-Date: 2019-01-02 17:30+0800 Last-Translator: FULL NAME <EMAIL@ADDRESS> Language: en Language-Team: en <L@li.org> Plural-Forms: nplurals=2; plural=(n !=1) MIME-Version: 1.0 Content-Type: text/plain; charset=utf-8 Content-Transfer-Encoding: 8bit Generated-By: Babel 2.8.0 

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
api_instance = gate_api.AssetswapApi(api_client)
max_evaluate_value = 56 # int | Project-Id-Version: GateApiTools 1.0.0 Report-Msgid-Bugs-To: EMAIL@ADDRESS POT-Creation-Date: 2025-11-12 18:14+0800 PO-Revision-Date: 2019-01-02 17:30+0800 Last-Translator: FULL NAME <EMAIL@ADDRESS> Language: en Language-Team: en <L@li.org> Plural-Forms: nplurals=2; plural=(n !=1) MIME-Version: 1.0 Content-Type: text/plain; charset=utf-8 Content-Transfer-Encoding: 8bit Generated-By: Babel 2.8.0  (optional)
cursor = 'cursor_example' # str | Project-Id-Version: GateApiTools 1.0.0 Report-Msgid-Bugs-To: EMAIL@ADDRESS POT-Creation-Date: 2025-11-12 18:14+0800 PO-Revision-Date: 2019-01-02 17:30+0800 Last-Translator: FULL NAME <EMAIL@ADDRESS> Language: en Language-Team: en <L@li.org> Plural-Forms: nplurals=2; plural=(n !=1) MIME-Version: 1.0 Content-Type: text/plain; charset=utf-8 Content-Transfer-Encoding: 8bit Generated-By: Babel 2.8.0  (optional)
size = 56 # int | Project-Id-Version: GateApiTools 1.0.0 Report-Msgid-Bugs-To: EMAIL@ADDRESS POT-Creation-Date: 2025-11-12 18:14+0800 PO-Revision-Date: 2019-01-02 17:30+0800 Last-Translator: FULL NAME <EMAIL@ADDRESS> Language: en Language-Team: en <L@li.org> Plural-Forms: nplurals=2; plural=(n !=1) MIME-Version: 1.0 Content-Type: text/plain; charset=utf-8 Content-Transfer-Encoding: 8bit Generated-By: Babel 2.8.0  (optional)

try:
    # Portfolio optimization — valuation
    api_response = api_instance.evaluate_asset_swap(max_evaluate_value=max_evaluate_value, cursor=cursor, size=size)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling AssetswapApi->evaluate_asset_swap: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **max_evaluate_value** | **int**| Project-Id-Version: GateApiTools 1.0.0 Report-Msgid-Bugs-To: EMAIL@ADDRESS POT-Creation-Date: 2025-11-12 18:14+0800 PO-Revision-Date: 2019-01-02 17:30+0800 Last-Translator: FULL NAME &lt;EMAIL@ADDRESS&gt; Language: en Language-Team: en &lt;L@li.org&gt; Plural-Forms: nplurals&#x3D;2; plural&#x3D;(n !&#x3D;1) MIME-Version: 1.0 Content-Type: text/plain; charset&#x3D;utf-8 Content-Transfer-Encoding: 8bit Generated-By: Babel 2.8.0  | [optional] 
 **cursor** | **str**| Project-Id-Version: GateApiTools 1.0.0 Report-Msgid-Bugs-To: EMAIL@ADDRESS POT-Creation-Date: 2025-11-12 18:14+0800 PO-Revision-Date: 2019-01-02 17:30+0800 Last-Translator: FULL NAME &lt;EMAIL@ADDRESS&gt; Language: en Language-Team: en &lt;L@li.org&gt; Plural-Forms: nplurals&#x3D;2; plural&#x3D;(n !&#x3D;1) MIME-Version: 1.0 Content-Type: text/plain; charset&#x3D;utf-8 Content-Transfer-Encoding: 8bit Generated-By: Babel 2.8.0  | [optional] 
 **size** | **int**| Project-Id-Version: GateApiTools 1.0.0 Report-Msgid-Bugs-To: EMAIL@ADDRESS POT-Creation-Date: 2025-11-12 18:14+0800 PO-Revision-Date: 2019-01-02 17:30+0800 Last-Translator: FULL NAME &lt;EMAIL@ADDRESS&gt; Language: en Language-Team: en &lt;L@li.org&gt; Plural-Forms: nplurals&#x3D;2; plural&#x3D;(n !&#x3D;1) MIME-Version: 1.0 Content-Type: text/plain; charset&#x3D;utf-8 Content-Transfer-Encoding: 8bit Generated-By: Babel 2.8.0  | [optional] 

### Return type

[**ApiResponseAssetSwapEvaluate**](ApiResponseAssetSwapEvaluate.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | HTTP 200，业务结果通过 code 字段区分 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_asset_swap_order_v1**
> ApiResponseAssetSwapOrderCreateV1 create_asset_swap_order_v1(order_create_v1_req)

Portfolio optimization — place order

将账户内若干源币种按指定数量换入目标币种侧配置，**正式下单前强烈建议先调用** `POST /asset-swap/order/preview` **且 `code=0` 后再用一致的语义提交本接口**。  **请求体不含 `ratio`** - 本接口 `OrderCreateV1Req` 仅含 `from` / `to`，且数组元素均为 `CreateParam`（**仅** `asset` + `amount`）。**请勿**在下单 JSON 中传入 `ratio`；比例字段 `ratio` 只存在于预览接口 `OrderPreviewV1Req.to`（`PreviewToParam`）。  **与预览接口的关键差异（易错点）** - 本接口 `to` 数组元素为 `CreateParam`：**`asset` + `amount`（目标侧数量，十进制字符串）**。 - 预览接口 `to` 为 **`asset` + `ratio`（比例字符串）**，**二者不可混用**：不要把预览里的 `ratio` 原样填到下单的 `amount`，也不要把下单的 `amount` 当成预览的 `ratio`。  **推荐调用顺序** 1. `GET /asset-swap/asset/list`：确认币种支持。 2. `GET /asset-swap/config`：读取 `recommend` / `recommend_v2`（如 `recommend_v2.market` 下某策略的 `schemes`，将 `scheme.name` 作为目标 `asset`、`scheme.ratio` 仅用于 **preview** 的 `to[].ratio`）。 3. `GET /asset-swap/evaluate`（可选）：参考可卖数量。 4. `POST /asset-swap/order/preview`：`from` 与 `to`（比例）构造询价。 5. 预览成功后，按产品/服务端约定将预览结果映射为下单的 `from`/`to`（**均为 amount**）再调用本接口。  **字段约定** - `from`：卖出侧，每项为 `asset` + `amount`（字符串，十进制，表示该币种卖出数量）。 - `to`：买入/目标侧，每项为 `asset` + **`amount`**（字符串，十进制，表示该目标币种侧数量；语义与预览的 `ratio` 不同）。 - 本接口仅校验上述 `amount` 的精度与范围；不满足时返回非 0 `code` 及 `message`。预览侧 `to[].ratio` 的校验规则见 `POST /asset-swap/order/preview` 文档。

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
api_instance = gate_api.AssetswapApi(api_client)
order_create_v1_req = gate_api.OrderCreateV1Req() # OrderCreateV1Req | 下单请求体（`OrderCreateV1Req`）。**无 `ratio` 字段**；`from`/`to` 每项仅 `asset` + `amount`。`to` 使用目标侧**数量** `amount`，与 preview 中 `to` 的 **ratio**（比例）语义不同，勿混用。

try:
    # Portfolio optimization — place order
    api_response = api_instance.create_asset_swap_order_v1(order_create_v1_req)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling AssetswapApi->create_asset_swap_order_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_create_v1_req** | [**OrderCreateV1Req**](OrderCreateV1Req.md)| 下单请求体（&#x60;OrderCreateV1Req&#x60;）。**无 &#x60;ratio&#x60; 字段**；&#x60;from&#x60;/&#x60;to&#x60; 每项仅 &#x60;asset&#x60; + &#x60;amount&#x60;。&#x60;to&#x60; 使用目标侧**数量** &#x60;amount&#x60;，与 preview 中 &#x60;to&#x60; 的 **ratio**（比例）语义不同，勿混用。 | 

### Return type

[**ApiResponseAssetSwapOrderCreateV1**](ApiResponseAssetSwapOrderCreateV1.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | HTTP 200，业务结果通过 code 字段区分 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_asset_swap_orders_v1**
> ApiResponseAssetSwapOrderListV1 list_asset_swap_orders_v1(_from=_from, to=to, status=status, offset=offset, size=size, sort_mode=sort_mode, order_by=order_by)

Portfolio optimization — order list

Project-Id-Version: GateApiTools 1.0.0 Report-Msgid-Bugs-To: EMAIL@ADDRESS POT-Creation-Date: 2025-11-12 18:14+0800 PO-Revision-Date: 2019-01-02 17:30+0800 Last-Translator: FULL NAME <EMAIL@ADDRESS> Language: en Language-Team: en <L@li.org> Plural-Forms: nplurals=2; plural=(n !=1) MIME-Version: 1.0 Content-Type: text/plain; charset=utf-8 Content-Transfer-Encoding: 8bit Generated-By: Babel 2.8.0 

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
api_instance = gate_api.AssetswapApi(api_client)
_from = 56 # int | Project-Id-Version: GateApiTools 1.0.0 Report-Msgid-Bugs-To: EMAIL@ADDRESS POT-Creation-Date: 2025-11-12 18:14+0800 PO-Revision-Date: 2019-01-02 17:30+0800 Last-Translator: FULL NAME <EMAIL@ADDRESS> Language: en Language-Team: en <L@li.org> Plural-Forms: nplurals=2; plural=(n !=1) MIME-Version: 1.0 Content-Type: text/plain; charset=utf-8 Content-Transfer-Encoding: 8bit Generated-By: Babel 2.8.0  (optional)
to = 56 # int | Project-Id-Version: GateApiTools 1.0.0 Report-Msgid-Bugs-To: EMAIL@ADDRESS POT-Creation-Date: 2025-11-12 18:14+0800 PO-Revision-Date: 2019-01-02 17:30+0800 Last-Translator: FULL NAME <EMAIL@ADDRESS> Language: en Language-Team: en <L@li.org> Plural-Forms: nplurals=2; plural=(n !=1) MIME-Version: 1.0 Content-Type: text/plain; charset=utf-8 Content-Transfer-Encoding: 8bit Generated-By: Babel 2.8.0  (optional)
status = 56 # int | Project-Id-Version: GateApiTools 1.0.0 Report-Msgid-Bugs-To: EMAIL@ADDRESS POT-Creation-Date: 2025-11-12 18:14+0800 PO-Revision-Date: 2019-01-02 17:30+0800 Last-Translator: FULL NAME <EMAIL@ADDRESS> Language: en Language-Team: en <L@li.org> Plural-Forms: nplurals=2; plural=(n !=1) MIME-Version: 1.0 Content-Type: text/plain; charset=utf-8 Content-Transfer-Encoding: 8bit Generated-By: Babel 2.8.0  (optional)
offset = 56 # int | Project-Id-Version: GateApiTools 1.0.0 Report-Msgid-Bugs-To: EMAIL@ADDRESS POT-Creation-Date: 2025-11-12 18:14+0800 PO-Revision-Date: 2019-01-02 17:30+0800 Last-Translator: FULL NAME <EMAIL@ADDRESS> Language: en Language-Team: en <L@li.org> Plural-Forms: nplurals=2; plural=(n !=1) MIME-Version: 1.0 Content-Type: text/plain; charset=utf-8 Content-Transfer-Encoding: 8bit Generated-By: Babel 2.8.0  (optional)
size = 56 # int | Project-Id-Version: GateApiTools 1.0.0 Report-Msgid-Bugs-To: EMAIL@ADDRESS POT-Creation-Date: 2025-11-12 18:14+0800 PO-Revision-Date: 2019-01-02 17:30+0800 Last-Translator: FULL NAME <EMAIL@ADDRESS> Language: en Language-Team: en <L@li.org> Plural-Forms: nplurals=2; plural=(n !=1) MIME-Version: 1.0 Content-Type: text/plain; charset=utf-8 Content-Transfer-Encoding: 8bit Generated-By: Babel 2.8.0  (optional)
sort_mode = 56 # int | Project-Id-Version: GateApiTools 1.0.0 Report-Msgid-Bugs-To: EMAIL@ADDRESS POT-Creation-Date: 2025-11-12 18:14+0800 PO-Revision-Date: 2019-01-02 17:30+0800 Last-Translator: FULL NAME <EMAIL@ADDRESS> Language: en Language-Team: en <L@li.org> Plural-Forms: nplurals=2; plural=(n !=1) MIME-Version: 1.0 Content-Type: text/plain; charset=utf-8 Content-Transfer-Encoding: 8bit Generated-By: Babel 2.8.0  (optional)
order_by = 56 # int | Project-Id-Version: GateApiTools 1.0.0 Report-Msgid-Bugs-To: EMAIL@ADDRESS POT-Creation-Date: 2025-11-12 18:14+0800 PO-Revision-Date: 2019-01-02 17:30+0800 Last-Translator: FULL NAME <EMAIL@ADDRESS> Language: en Language-Team: en <L@li.org> Plural-Forms: nplurals=2; plural=(n !=1) MIME-Version: 1.0 Content-Type: text/plain; charset=utf-8 Content-Transfer-Encoding: 8bit Generated-By: Babel 2.8.0  (optional)

try:
    # Portfolio optimization — order list
    api_response = api_instance.list_asset_swap_orders_v1(_from=_from, to=to, status=status, offset=offset, size=size, sort_mode=sort_mode, order_by=order_by)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling AssetswapApi->list_asset_swap_orders_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **int**| Project-Id-Version: GateApiTools 1.0.0 Report-Msgid-Bugs-To: EMAIL@ADDRESS POT-Creation-Date: 2025-11-12 18:14+0800 PO-Revision-Date: 2019-01-02 17:30+0800 Last-Translator: FULL NAME &lt;EMAIL@ADDRESS&gt; Language: en Language-Team: en &lt;L@li.org&gt; Plural-Forms: nplurals&#x3D;2; plural&#x3D;(n !&#x3D;1) MIME-Version: 1.0 Content-Type: text/plain; charset&#x3D;utf-8 Content-Transfer-Encoding: 8bit Generated-By: Babel 2.8.0  | [optional] 
 **to** | **int**| Project-Id-Version: GateApiTools 1.0.0 Report-Msgid-Bugs-To: EMAIL@ADDRESS POT-Creation-Date: 2025-11-12 18:14+0800 PO-Revision-Date: 2019-01-02 17:30+0800 Last-Translator: FULL NAME &lt;EMAIL@ADDRESS&gt; Language: en Language-Team: en &lt;L@li.org&gt; Plural-Forms: nplurals&#x3D;2; plural&#x3D;(n !&#x3D;1) MIME-Version: 1.0 Content-Type: text/plain; charset&#x3D;utf-8 Content-Transfer-Encoding: 8bit Generated-By: Babel 2.8.0  | [optional] 
 **status** | **int**| Project-Id-Version: GateApiTools 1.0.0 Report-Msgid-Bugs-To: EMAIL@ADDRESS POT-Creation-Date: 2025-11-12 18:14+0800 PO-Revision-Date: 2019-01-02 17:30+0800 Last-Translator: FULL NAME &lt;EMAIL@ADDRESS&gt; Language: en Language-Team: en &lt;L@li.org&gt; Plural-Forms: nplurals&#x3D;2; plural&#x3D;(n !&#x3D;1) MIME-Version: 1.0 Content-Type: text/plain; charset&#x3D;utf-8 Content-Transfer-Encoding: 8bit Generated-By: Babel 2.8.0  | [optional] 
 **offset** | **int**| Project-Id-Version: GateApiTools 1.0.0 Report-Msgid-Bugs-To: EMAIL@ADDRESS POT-Creation-Date: 2025-11-12 18:14+0800 PO-Revision-Date: 2019-01-02 17:30+0800 Last-Translator: FULL NAME &lt;EMAIL@ADDRESS&gt; Language: en Language-Team: en &lt;L@li.org&gt; Plural-Forms: nplurals&#x3D;2; plural&#x3D;(n !&#x3D;1) MIME-Version: 1.0 Content-Type: text/plain; charset&#x3D;utf-8 Content-Transfer-Encoding: 8bit Generated-By: Babel 2.8.0  | [optional] 
 **size** | **int**| Project-Id-Version: GateApiTools 1.0.0 Report-Msgid-Bugs-To: EMAIL@ADDRESS POT-Creation-Date: 2025-11-12 18:14+0800 PO-Revision-Date: 2019-01-02 17:30+0800 Last-Translator: FULL NAME &lt;EMAIL@ADDRESS&gt; Language: en Language-Team: en &lt;L@li.org&gt; Plural-Forms: nplurals&#x3D;2; plural&#x3D;(n !&#x3D;1) MIME-Version: 1.0 Content-Type: text/plain; charset&#x3D;utf-8 Content-Transfer-Encoding: 8bit Generated-By: Babel 2.8.0  | [optional] 
 **sort_mode** | **int**| Project-Id-Version: GateApiTools 1.0.0 Report-Msgid-Bugs-To: EMAIL@ADDRESS POT-Creation-Date: 2025-11-12 18:14+0800 PO-Revision-Date: 2019-01-02 17:30+0800 Last-Translator: FULL NAME &lt;EMAIL@ADDRESS&gt; Language: en Language-Team: en &lt;L@li.org&gt; Plural-Forms: nplurals&#x3D;2; plural&#x3D;(n !&#x3D;1) MIME-Version: 1.0 Content-Type: text/plain; charset&#x3D;utf-8 Content-Transfer-Encoding: 8bit Generated-By: Babel 2.8.0  | [optional] 
 **order_by** | **int**| Project-Id-Version: GateApiTools 1.0.0 Report-Msgid-Bugs-To: EMAIL@ADDRESS POT-Creation-Date: 2025-11-12 18:14+0800 PO-Revision-Date: 2019-01-02 17:30+0800 Last-Translator: FULL NAME &lt;EMAIL@ADDRESS&gt; Language: en Language-Team: en &lt;L@li.org&gt; Plural-Forms: nplurals&#x3D;2; plural&#x3D;(n !&#x3D;1) MIME-Version: 1.0 Content-Type: text/plain; charset&#x3D;utf-8 Content-Transfer-Encoding: 8bit Generated-By: Babel 2.8.0  | [optional] 

### Return type

[**ApiResponseAssetSwapOrderListV1**](ApiResponseAssetSwapOrderListV1.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | HTTP 200，业务结果通过 code 字段区分 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **preview_asset_swap_order_v1**
> ApiResponseAssetSwapOrderPreviewV1 preview_asset_swap_order_v1(order_preview_v1_req)

Portfolio optimization — preview

根据卖出币种数量与**目标分配比例**估算成交与费用，**不写入订单**。`code=0` 时 `data` 含预估 `order` 与 `transaction_fee`。  **与下单接口的关键差异（易错点）** - 本接口 `to` 数组元素为 `PreviewToParam`：**`asset` + `ratio`（比例，十进制字符串）**，表示目标币种在组合中的权重/占比。 - 下单接口 `POST /asset-swap/order/create` 的 `to` 为 **`asset` + `amount`（绝对数量）**，**不是** `ratio`。调用方切勿把两套字段混用。  **如何构造 `to`（ratio）** - 优先从 `GET /asset-swap/config` 的 `data.recommend_v2` 取值：按分组键（如 `market`、`faith`、`conservative`）找到策略列表中的某条 `RecommendV2Strategy`（如 `name` 为 `top2`），将其 `schemes` 映射为预览请求：   - `to[].asset` ← `scheme.name`（目标币种符号）   - `to[].ratio` ← `scheme.ratio`（与配置一致的比例字符串） - 亦可使用 `recommend` 下扁平 map（币种 → 比例字符串）自行展开为多元素 `to`（每项一个 `asset` + `ratio`）。 - 多目标时各 `ratio` 建议与前端/运营配置一致；是否需加总为 1 以服务端校验为准。  **`from`（卖出侧）** - 每项为 `asset` + `amount`（字符串，十进制），表示本次参与换出的该币种数量。币种应在 `GET /asset-swap/asset/list` 支持范围内；数量级过小或市场深度不足时可能返回非 0 `code`（如无法询价）。  **与下单的衔接** - 预览成功后，将业务允许的预览结果转换为下单所需的 **`from`/`to` 全为 amount** 的请求体再调用 create（具体映射规则以产品文档或服务端约定为准）。

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
api_instance = gate_api.AssetswapApi(api_client)
order_preview_v1_req = gate_api.OrderPreviewV1Req() # OrderPreviewV1Req | 预览请求体。`to` 必须为 **ratio**；与 create 的 **amount** 语义不同。

try:
    # Portfolio optimization — preview
    api_response = api_instance.preview_asset_swap_order_v1(order_preview_v1_req)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling AssetswapApi->preview_asset_swap_order_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_preview_v1_req** | [**OrderPreviewV1Req**](OrderPreviewV1Req.md)| 预览请求体。&#x60;to&#x60; 必须为 **ratio**；与 create 的 **amount** 语义不同。 | 

### Return type

[**ApiResponseAssetSwapOrderPreviewV1**](ApiResponseAssetSwapOrderPreviewV1.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | HTTP 200，业务结果通过 code 字段区分 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_swap_order_v1**
> ApiResponseAssetSwapOrderQueryV1 get_asset_swap_order_v1(order_id)

Portfolio optimization — query order

Project-Id-Version: GateApiTools 1.0.0 Report-Msgid-Bugs-To: EMAIL@ADDRESS POT-Creation-Date: 2025-11-12 18:14+0800 PO-Revision-Date: 2019-01-02 17:30+0800 Last-Translator: FULL NAME <EMAIL@ADDRESS> Language: en Language-Team: en <L@li.org> Plural-Forms: nplurals=2; plural=(n !=1) MIME-Version: 1.0 Content-Type: text/plain; charset=utf-8 Content-Transfer-Encoding: 8bit Generated-By: Babel 2.8.0 

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
api_instance = gate_api.AssetswapApi(api_client)
order_id = 'order_id_example' # str | Project-Id-Version: GateApiTools 1.0.0 Report-Msgid-Bugs-To: EMAIL@ADDRESS POT-Creation-Date: 2025-11-12 18:14+0800 PO-Revision-Date: 2019-01-02 17:30+0800 Last-Translator: FULL NAME <EMAIL@ADDRESS> Language: en Language-Team: en <L@li.org> Plural-Forms: nplurals=2; plural=(n !=1) MIME-Version: 1.0 Content-Type: text/plain; charset=utf-8 Content-Transfer-Encoding: 8bit Generated-By: Babel 2.8.0 

try:
    # Portfolio optimization — query order
    api_response = api_instance.get_asset_swap_order_v1(order_id)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling AssetswapApi->get_asset_swap_order_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| Project-Id-Version: GateApiTools 1.0.0 Report-Msgid-Bugs-To: EMAIL@ADDRESS POT-Creation-Date: 2025-11-12 18:14+0800 PO-Revision-Date: 2019-01-02 17:30+0800 Last-Translator: FULL NAME &lt;EMAIL@ADDRESS&gt; Language: en Language-Team: en &lt;L@li.org&gt; Plural-Forms: nplurals&#x3D;2; plural&#x3D;(n !&#x3D;1) MIME-Version: 1.0 Content-Type: text/plain; charset&#x3D;utf-8 Content-Transfer-Encoding: 8bit Generated-By: Babel 2.8.0  | 

### Return type

[**ApiResponseAssetSwapOrderQueryV1**](ApiResponseAssetSwapOrderQueryV1.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | HTTP 200，业务结果通过 code 字段区分 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

