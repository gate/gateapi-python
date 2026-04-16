# OrderPreviewV1Req

资产配置优化**预览**请求。`from` 为卖出数量；`to` 为目标币种及**分配比例 ratio**（不是绝对数量）。 正式下单请使用 `OrderCreateV1Req`，其 `to` 为 `amount`。
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_from** | [**list[PreviewFromParam]**](PreviewFromParam.md) | 卖出侧；每项为币种 + 换出数量 &#x60;amount&#x60;（字符串十进制）。 | 
**to** | [**list[PreviewToParam]**](PreviewToParam.md) | 目标侧；每项为币种 + **比例** &#x60;ratio&#x60;（字符串十进制，如 &#x60;0.5&#x60;）。 典型来源：&#x60;GET /asset-swap/config&#x60; → &#x60;recommend_v2&#x60; 某分组下策略的 &#x60;schemes[].name&#x60; / &#x60;schemes[].ratio&#x60;。 | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


