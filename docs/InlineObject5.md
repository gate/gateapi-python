# InlineObject5

Close position request parameters
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**close_type** | **int** | 平仓类型  说明： - 1：部分平仓（必须传 close_volume） - 2：全平（无需传 close_volume） | 
**close_volume** | **str** | 平仓数量  说明： - 当 close_type &#x3D; 1 时必传 - 当 close_type &#x3D; 2 时忽略该字段 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


