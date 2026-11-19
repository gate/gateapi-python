# StockOptionPutOrderRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **str** | Full option contract symbol to trade, obtained from the contract list or option chain. | 
**side** | [**StockOptionOrderSide**](StockOptionOrderSide.md) |  | 
**order_type** | [**StockOptionOrderType**](StockOptionOrderType.md) |  | 
**time_in_force** | [**StockOptionTimeInForce**](StockOptionTimeInForce.md) |  | 
**price** | **str** | Limit order price as a positive plain decimal string, up to 64 characters, without scientific notation. Required for limit orders and ignored for market orders. | [optional] 
**quantity** | **str** | Order quantity as a positive decimal string within the contract&#39;s minimum and maximum order quantities. | 
**client_order_id** | **str** | Optional custom order identifier, up to 30 UTF-8 bytes. Generated automatically when omitted or whitespace-only. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


