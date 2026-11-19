# StockOptionClosePositionRequest

`order_type` is optional. Omitted or empty values close at market; only `market` and `limit` are supported.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **str** | Option contract symbol to close, with an available position. | 
**quantity** | **str** | Quantity to close as a positive decimal string. Must not exceed the available position and must satisfy the contract&#39;s minimum, maximum and quantity increment rules. | 
**order_type** | [**StockOptionOrderType**](StockOptionOrderType.md) |  | [optional] 
**price** | **str** | Positive limit closing price as a plain decimal string, up to 64 characters, without scientific notation. Ignored for market closing orders. | [optional] 
**client_order_id** | **str** | Custom closing order identifier. Generated automatically when omitted or whitespace-only. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


