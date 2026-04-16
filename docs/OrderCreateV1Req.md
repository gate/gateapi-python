# OrderCreateV1Req

资产配置优化下单请求。**`from` 与 `to` 数组元素均为 `CreateParam`，字段均为 `asset` + `amount`。** 不存在 `ratio` 字段；若从预览接口抄参，须将预览中的 `to[].ratio` 转换为下单所需的 `to[].amount`（按产品约定，通常依据预览返回的订单明细等），不可直接复用 `ratio` 字符串作为 `amount`。
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_from** | [**list[CreateParam]**](CreateParam.md) | 卖出侧列表，至少一项；每项为要换出的币种及数量 &#x60;amount&#x60;。 | 
**to** | [**list[CreateParam]**](CreateParam.md) | 目标侧列表，至少一项；每项为目标币种及**数量** &#x60;amount&#x60;（非比例）。 与 &#x60;OrderPreviewV1Req.to&#x60;（&#x60;PreviewToParam&#x60;，含 &#x60;ratio&#x60;）结构语义不同，勿混用。 | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


