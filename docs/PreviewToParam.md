# PreviewToParam

**仅用于预览** `OrderPreviewV1Req.to`。目标币种 + **比例 ratio**。 **禁止**与下单 `CreateParam` 混淆：下单的 `to` 必须使用 **`amount`**，没有 `ratio` 字段。
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | **str** | 目标币种符号；常与 config 中 &#x60;recommend_v2.*[].schemes[].name&#x60; 对应。 | 
**ratio** | **str** | 该目标币种在组合中的权重比例，**十进制字符串**（如 &#x60;0.2&#x60;、&#x60;0.5&#x60;）。 常与 &#x60;GET /asset-swap/config&#x60; 的 &#x60;recommend_v2&#x60; 下某策略的 &#x60;schemes[].ratio&#x60; 一致。 | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


