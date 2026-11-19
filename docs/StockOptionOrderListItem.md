# StockOptionOrderListItem

Current unfinished orders, excluding filled, cancelled and rejected terminal orders.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** | Order ID. | [optional] 
**symbol** | **str** | Full option contract symbol. | [optional] 
**symbol_display** | **str** | Option contract name for display. | [optional] 
**underlying** | **str** | Option underlying symbol. | [optional] 
**side** | [**StockOptionOrderSide**](StockOptionOrderSide.md) |  | [optional] 
**order_type** | [**StockOptionOrderType**](StockOptionOrderType.md) |  | [optional] 
**status** | **int** | Current order status: - 1: New, validated and awaiting processing. - 2: Partially filled, with a remaining unfilled quantity. | [optional] 
**status_desc** | **str** | Human-readable order status description in the requested language. | [optional] 
**time_in_force** | [**StockOptionTimeInForce**](StockOptionTimeInForce.md) |  | [optional] 
**quantity** | **str** | Order quantity. | [optional] 
**filled_quantity** | **str** | Filled quantity. | [optional] 
**price** | **str** | Order price. | [optional] 
**time_setup** | **int** | Order creation time. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


