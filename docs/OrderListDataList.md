# OrderListDataList

Order detail
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **int** | Order ID | [optional] 
**symbol** | **str** | Currency pair | [optional] 
**symbol_desc** | **str** | Trading symbol description | [optional] 
**price_type** | **str** | Trade type (market&#x3D;market price, trigger&#x3D;trigger price) | [optional] 
**state** | **int** | Order status code | [optional] 
**state_desc** | **str** | Order status description | [optional] 
**finished** | **int** | Is completed (0&#x3D;shown in active order list, 1&#x3D;not shown in active list) | [optional] 
**side** | **int** | Order side (1&#x3D;sell, 2&#x3D;buy) | [optional] 
**volume** | **str** | Order volume | [optional] 
**price** | **str** | Trigger price | [optional] 
**price_tp** | **str** | Take profit price | [optional] 
**price_sl** | **str** | Stop loss price | [optional] 
**time_setup** | **int** | Order time (Unix timestamp in seconds) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


