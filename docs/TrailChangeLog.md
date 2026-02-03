# TrailChangeLog

Trail order modification records
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**updated_at** | **int** | Update time | [optional] [readonly] 
**amount** | **str** | Trading quantity in contracts, positive for buy, negative for sell | [optional] [readonly] 
**is_gte** | **bool** | true: activate when market price &gt;&#x3D; activation price, false: &lt;&#x3D; activation price | [optional] [readonly] 
**activation_price** | **str** | Activation price, 0 means trigger immediately | [optional] [readonly] 
**price_type** | **int** | Activation price type: 0-unknown, 1-latest price, 2-index price, 3-mark price | [optional] [readonly] 
**price_offset** | **str** | Callback ratio or price distance, e.g., &#x60;0.1&#x60; or &#x60;0.1%&#x60; | [optional] [readonly] 
**is_create** | **bool** | true - order creation, false - order modification | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


