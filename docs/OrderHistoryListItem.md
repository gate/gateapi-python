# OrderHistoryListItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**exchange** | **str** | Exchange, supports us, hk, and kr | [optional] 
**quote_currency** | **str** |  | [optional] 
**fx_rate** | **str** | Quote currency to USD exchange rate | [optional] 
**symbol_desc** | **str** |  | [optional] 
**price_type** | **str** | Price type (market &#x3D; market order, limit &#x3D; limit order) | [optional] 
**status** | **int** | Order status | [optional] 
**status_desc** | **str** | Order status description | [optional] 
**status_detail** | [**OrderHistoryListItemStatusDetail**](OrderHistoryListItemStatusDetail.md) |  | [optional] 
**finish_as** | **int** | Order completion reason | [optional] 
**side** | **int** | Side (1&#x3D;sell, 2&#x3D;buy) | [optional] 
**time_in_force** | **str** | Time in force. - day: Day order. | [optional] 
**volume** | **str** |  | [optional] 
**fill_volume** | **str** |  | [optional] 
**price** | **str** |  | [optional] 
**avg_fill_price** | **str** |  | [optional] 
**commission** | **str** | fee | [optional] 
**time_setup** | **int** |  | [optional] 
**time_done** | **int** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


