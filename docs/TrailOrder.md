# TrailOrder

Trail order details
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Order ID | [optional] [readonly] 
**user_id** | **int** | User ID | [optional] [readonly] 
**user** | **int** | User ID | [optional] [readonly] 
**contract** | **str** | Contract name | [optional] 
**settle** | **str** | Settle currency | [optional] 
**amount** | **str** | Trading quantity in contracts, positive for buy, negative for sell | [optional] 
**is_gte** | **bool** | true: activate when market price &gt;&#x3D; activation price, false: &lt;&#x3D; activation price | [optional] 
**activation_price** | **str** | Activation price, 0 means trigger immediately | [optional] 
**price_type** | **int** | Activation price type: 0-unknown, 1-latest price, 2-index price, 3-mark price | [optional] 
**price_offset** | **str** | Callback ratio or price distance, e.g., &#x60;0.1&#x60; or &#x60;0.1%&#x60; | [optional] 
**text** | **str** | Custom field | [optional] 
**reduce_only** | **bool** | Reduce Position Only | [optional] 
**position_related** | **bool** | Whether bound to position | [optional] 
**created_at** | **int** | Created time | [optional] [readonly] 
**activated_at** | **int** | Activation time | [optional] [readonly] 
**finished_at** | **int** | End time | [optional] [readonly] 
**create_time** | **int** | Created time | [optional] [readonly] 
**active_time** | **int** | Activation time | [optional] [readonly] 
**finish_time** | **int** | End time | [optional] [readonly] 
**reason** | **str** | End reason | [optional] [readonly] 
**suborder_text** | **str** | Sub-order text field | [optional] [readonly] 
**is_dual_mode** | **bool** | Whether dual position mode when creating order | [optional] [readonly] 
**trigger_price** | **str** | Trigger price | [optional] [readonly] 
**suborder_id** | **int** | Sub-order ID | [optional] [readonly] 
**side_label** | **str** | Order direction label: long/short/open long/open short/close long/close short | [optional] [readonly] 
**original_status** | **int** | Order status | [optional] [readonly] 
**status** | **str** | Simplified order status: open/finished | [optional] [readonly] 
**position_side_output** | **str** | Same as side_label, client requires consistency with other order types | [optional] [readonly] 
**updated_at** | **int** | Update time | [optional] [readonly] 
**extremum_price** | **str** | Extremum price | [optional] [readonly] 
**status_code** | **str** | Status code value | [optional] [readonly] 
**created_at_precise** | **str** | Creation time (high precision, seconds.microseconds format) | [optional] [readonly] 
**finished_at_precise** | **str** | End time (high precision, seconds.microseconds format) | [optional] [readonly] 
**activated_at_precise** | **str** | Activation time (high precision, seconds.microseconds format) | [optional] [readonly] 
**status_label** | **str** | Status internationalization label (translated status text) | [optional] [readonly] 
**pos_margin_mode** | **str** | Position margin mode: isolated/cross | [optional] [readonly] 
**position_mode** | **str** | Position mode: single, dual, and dual_plus | [optional] [readonly] 
**error_label** | **str** | Error label | [optional] [readonly] 
**leverage** | **str** | leverage | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


