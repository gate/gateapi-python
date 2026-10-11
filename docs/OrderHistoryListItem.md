# OrderHistoryListItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** | Order ID | [optional] 
**symbol** | **str** | Symbol | [optional] 
**exchange** | **str** | Exchange, supports us, hk, kr, and jp | [optional] 
**quote_currency** | **str** | Quote currency | [optional] 
**fx_rate** | **str** | Quote currency to USD exchange rate | [optional] 
**symbol_desc** | **str** | Symbol description | [optional] 
**price_type** | **str** | Price type (market &#x3D; market order, limit &#x3D; limit order) | [optional] 
**status** | **int** | Order status. - 0: Unknown. - 1: New order; the order has been validated and is waiting to be processed. - 2: Partially filled. - 3: Filled. - 4: Canceled. - 5: Order rejected. - 6: Cancellation rejected. - 7: Order update succeeded. - 8: Order update rejected. | [optional] 
**status_desc** | **str** | Order status description | [optional] 
**status_detail** | [**OrderHistoryListItemStatusDetail**](OrderHistoryListItemStatusDetail.md) |  | [optional] 
**finish_as** | **int** | Order completion reason. - 0: Unknown. - 1: No quote found. - 2: No match found. - 3: Trigger price exceeded. - 4: Order value exceeds the limit. - 5: Unknown rejection. - 6: Unknown cancellation. - 7: Canceled by user. - 8: Canceled after the order time in force expired. - 9: Trading is not supported in the current session. - 13: Canceled due to corporate action. | [optional] 
**side** | **int** | Side (1&#x3D;sell, 2&#x3D;buy) | [optional] 
**time_in_force** | **str** | Time in force. - day: Day order. | [optional] 
**volume** | **str** | Order quantity | [optional] 
**fill_volume** | **str** | Trading size | [optional] 
**price** | **str** | Order price | [optional] 
**avg_fill_price** | **str** | Average fill price | [optional] 
**commission** | **str** | fee | [optional] 
**time_setup** | **int** | Order creation time (Unix timestamp, seconds) | [optional] 
**time_done** | **int** | Order completion time (Unix timestamp in seconds) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


