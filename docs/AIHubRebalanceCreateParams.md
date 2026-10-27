# AIHubRebalanceCreateParams

Creation parameters for a smart-position strategy.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**begin_money_amount** | **str** |  | 
**begin_money_currency** | **str** |  | 
**asset_info** | [**list[AIHubRebalanceAsset]**](AIHubRebalanceAsset.md) |  | 
**period** | **str** | Product interval between 1m and 28d. | [optional] 
**threshold** | **str** | Positive ratio below 1, at most four decimal places. | [optional] 
**close_flag** | **int** |  | [optional] [default to 1]
**is_use_base** | **bool** |  | [optional] 
**stop_profit** | **str** |  | [optional] 
**stop_loss** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


