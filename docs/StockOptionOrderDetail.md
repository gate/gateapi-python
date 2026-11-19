# StockOptionOrderDetail

Order details for a current or finished order.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** | Order ID. | [optional] 
**symbol** | **str** | Full option contract symbol. | [optional] 
**symbol_display** | **str** | Option contract name for display. | [optional] 
**underlying** | **str** | Option underlying symbol. | [optional] 
**side** | [**StockOptionOrderSide**](StockOptionOrderSide.md) |  | [optional] 
**order_type** | [**StockOptionOrderType**](StockOptionOrderType.md) |  | [optional] 
**status** | **int** | Order status in order details. The details endpoint does not filter by status. - 1: New, validated and awaiting processing. - 2: Partially filled, with a remaining unfilled quantity. - 3: Filled, terminal. - 4: Cancelled, terminal; the order may have been partially filled. - 5: Rejected, terminal. Current orders include only 1 and 2; order history includes only 3, 4 and 5. | [optional] 
**status_desc** | **str** | Human-readable order status description in the requested language. | [optional] 
**time_in_force** | [**StockOptionTimeInForce**](StockOptionTimeInForce.md) |  | [optional] 
**quantity** | **str** | Order quantity. | [optional] 
**filled_quantity** | **str** | Filled quantity. | [optional] 
**price** | **str** | Order price. | [optional] 
**time_setup** | **int** | Order creation time. | [optional] 
**avg_fill_price** | **str** | Average fill price. | [optional] 
**fee** | **str** | Trading fee. | [optional] 
**time_done** | **int** | Order completion time. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


