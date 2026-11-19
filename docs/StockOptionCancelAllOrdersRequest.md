# StockOptionCancelAllOrdersRequest

Filters for cancelling limit orders in bulk. side is 1 (sell) or 2 (buy); omit it to include both sides.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**underlying** | **str** | Option underlying symbol. Empty or omitted values disable underlying filtering. | [optional] 
**symbol** | **str** | Option contract symbol. Empty or omitted values disable contract filtering. | [optional] 
**side** | [**StockOptionOrderListSide**](StockOptionOrderListSide.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


