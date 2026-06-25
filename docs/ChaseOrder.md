# ChaseOrder

Chase order detail or list item
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**user** | **str** |  | [optional] 
**contract** | **str** |  | [optional] 
**settle** | **str** |  | [optional] 
**amount** | **str** | Total size in contracts; positive for buy, negative for sell | [optional] 
**price_limit** | **str** |  | [optional] 
**reduce_only** | **bool** |  | [optional] 
**text** | **str** |  | [optional] 
**create_time** | **int** |  | [optional] 
**finish_time** | **int** |  | [optional] 
**original_status** | **int** | Raw status enum | [optional] 
**status** | **str** | Simplified status, e.g. open / finished | [optional] 
**reason** | **str** |  | [optional] 
**fill_amount** | **str** |  | [optional] 
**average_fill_price** | **str** |  | [optional] 
**suborder_id** | **str** |  | [optional] 
**is_dual_mode** | **bool** |  | [optional] 
**side_label** | **str** |  | [optional] 
**position_side_output** | **str** |  | [optional] 
**chase_price** | **str** |  | [optional] 
**interval_sec** | **int** |  | [optional] 
**updated_at** | **int** |  | [optional] 
**suborder_price** | **str** |  | [optional] 
**suborder_ongoing** | **bool** |  | [optional] 
**suborder_finish_as** | **str** |  | [optional] 
**price_type** | **int** | PriceType enum: 1 latest, 2 index, 3 mark | [optional] 
**price_gap_type** | **str** |  | [optional] 
**price_gap_value** | **str** |  | [optional] 
**status_code** | **str** |  | [optional] 
**create_time_precise** | **str** | Creation time (seconds.microseconds) | [optional] 
**finish_time_precise** | **str** |  | [optional] 
**pos_margin_mode** | **str** |  | [optional] 
**position_mode** | **str** |  | [optional] 
**leverage** | **str** |  | [optional] 
**error_label** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


