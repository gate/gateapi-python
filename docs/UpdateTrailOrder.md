# UpdateTrailOrder

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Order ID | 
**amount** | **str** | Total trading quantity in contracts, positive for buy, negative for sell, 0 means no modification | [optional] 
**activation_price** | **str** | Activation price, 0 means trigger immediately, empty means no modification | [optional] 
**is_gte_str** | **str** | true: activate when market price &gt;&#x3D; activation price, false: &lt;&#x3D; activation price, empty means no modification | [optional] 
**price_type** | **int** | Activation price type, not provided or 0 means no modification, 1-latest price, 2-index price, 3-mark price | [optional] 
**price_offset** | **str** | Callback ratio or price distance, e.g., &#x60;0.1&#x60; or &#x60;0.1%&#x60;; empty means no modification | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


