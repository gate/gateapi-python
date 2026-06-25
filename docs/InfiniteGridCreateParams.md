# InfiniteGridCreateParams

Infinite grid creation parameters. Aligned with the app: **`money`**, **`price_floor`**, and **`profit_per_grid`** are required; `grid_num` and `price_type` are optional (defaults applied server-side when omitted).
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**money** | **str** |  | 
**price_floor** | **str** | price floor | 
**profit_per_grid** | **str** | Profit per square | 
**grid_num** | **int** | Optional; may be omitted like in the app. | [optional] 
**price_type** | **int** | Optional. &#x60;0&#x60; arithmetic grid; &#x60;1&#x60; geometric; omit for server defaults. | [optional] 
**trigger_price** | **str** |  | [optional] 
**stop_profit** | **str** |  | [optional] 
**stop_loss** | **str** |  | [optional] 
**profit_sharing_ratio** | **str** |  | [optional] 
**is_use_base** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


