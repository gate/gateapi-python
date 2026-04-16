# CreateParam

**下单专用**。表示某一侧（`from` 或 `to`）的一个币种及其**数量 amount**。 用于 `OrderCreateV1Req`；**不要**用于预览接口的 `to`（预览 `to` 使用 `PreviewToParam.ratio`）。
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | **str** | 币种符号，与 &#x60;GET /asset-swap/asset/list&#x60; 及业务支持范围一致。 | 
**amount** | **str** | 该币种在本侧的数量，**十进制字符串**（非科学计数法）。&#x60;from&#x60; 表示卖出数量，&#x60;to&#x60; 表示目标侧数量。 与预览接口 &#x60;to[].ratio&#x60; 不同。 | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


