# PreviewToParam

**For preview only** `OrderPreviewV1Req.to`. Target currency + **ratio ratio**. **Forbidden** is confused with the order `CreateParam`: the `to` of the order must be **`amount`**, and there is no `ratio` field.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | **str** | Target currency symbol; often corresponds to &#x60;recommend_v2.*[].schemes[].name&#x60; in config. | 
**ratio** | **str** | The weight ratio of the target currency in the portfolio, **decimal string** (such as &#x60;0.2&#x60;, &#x60;0.5&#x60;). Often consistent with the &#x60;schemes[].ratio&#x60; of a strategy under &#x60;recommend_v2&#x60; of &#x60;GET /asset-swap/config&#x60;. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


