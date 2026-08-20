# OrderCreateV1Req

Asset allocation optimization order request. **The array elements of `from` and `to` are both `CreateParam`, and the fields are `asset` + `amount`. ** There is no `ratio` field; if you copy parameters from the preview interface, you must convert the `to[].ratio` in the preview into the `to[].amount` required for placing an order (according to the product agreement, usually based on the order details returned by the preview, etc.). The `ratio` string cannot be directly reused as `amount`.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_from** | [**list[CreateParam]**](CreateParam.md) | Sell side list, at least one item; each item is the currency and amount &#x60;amount&#x60; to be swapped out. | 
**to** | [**list[CreateParam]**](CreateParam.md) | Target side list, at least one item; each item is the target currency and **amount** &#x60;amount&#x60; (non-proportional). The structural semantics are different from &#x60;OrderPreviewV1Req.to&#x60; (&#x60;PreviewToParam&#x60;, including &#x60;ratio&#x60;), so do not mix them. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


