# OrderHistoryListDataList

Order detail
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **int** | Order ID | [optional] 
**symbol** | **str** | Currency pair | [optional] 
**symbol_desc** | **str** | Trading symbol description | [optional] 
**price_type** | **str** | Trade type (market&#x3D;market price, trigger&#x3D;trigger price) | [optional] 
**order_opt_type** | **int** | Order operation type (1&#x3D;sell, 2&#x3D;buy, 3&#x3D;close long, 4&#x3D;close short, 5&#x3D;force close long, 6&#x3D;force close short) | [optional] 
**state** | **int** | Order status code | [optional] 
**state_desc** | **str** | Order status description | [optional] 
**side** | **int** | Order side (1&#x3D;sell, 2&#x3D;buy) | [optional] 
**volume** | **str** | Order volume | [optional] 
**fill_volume** | **str** | Trading size | [optional] 
**close_pnl** | **str** | Close Position P&amp;L | [optional] 
**price** | **str** | Average fill price | [optional] 
**trigger_price** | **str** | Trigger price | [optional] 
**price_tp** | **str** | Take profit price | [optional] 
**price_sl** | **str** | Stop loss price | [optional] 
**time_setup** | **int** | Order time (Unix timestamp in seconds) | [optional] 
**time_done** | **int** | End time (Unix timestamp in seconds) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


