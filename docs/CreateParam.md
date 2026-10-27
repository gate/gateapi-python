# CreateParam

**For order only**. Represents a currency and its **amount** on a certain side (`from` or `to`). Used with `OrderCreateV1Req`; **Don't** be used with `to` of the preview interface (preview `to` uses `PreviewToParam.ratio`).
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | **str** | Currency symbol, consistent with &#x60;GET /asset-swap/asset/list&#x60; and business support scope. | 
**amount** | **str** | The quantity of this currency on this side, **decimal string** (non-scientific notation). &#x60;from&#x60; represents the selling quantity, and &#x60;to&#x60; represents the target side quantity. Different from preview interface &#x60;to[].ratio&#x60;. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


