# TradFiClosePositionRequest

Close position request parameters
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**close_type** | **int** | Close Type Description: - 1: Partial Close (close_volume is required) - 2: Full Close (close_volume is not required) | 
**close_volume** | **str** | Close Volume Description: - Required when close_type &#x3D; 1 - Ignored when close_type &#x3D; 2 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


