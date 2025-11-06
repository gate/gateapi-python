# FuturesUpdatePriceTriggeredOrder

Modify Price Order Details
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**settle** | **str** | Settlement Currency (e.g., USDT, BTC) | [optional] [readonly] 
**order_id** | **int** | ID of the Pending Take-Profit/Stop-Loss Trigger Order | [optional] [readonly] 
**contact** | **str** | The order ID of the modified price-triggered order. This ID is returned upon successful creation of the price-triggered order. Note: This ID must be passed in both the request path and request body. | [optional] 
**size** | **int** | Modified Contract Quantity. Full Close: 0; Partial Close: Positive/Negative values indicate direction (consistent with the creation interface logic). | [optional] 
**price** | **str** | Represents the modified trading price. A value of 0 indicates a market order. | [optional] 
**trigger_price** | **str** | Modified Trigger Price | [optional] 
**price_type** | **int** | Reference price type. 0 - Latest trade price, 1 - Mark price, 2 - Index price | [optional] 
**auto_size** | **str** | 单仓模式不需设置auto_size 双仓模式部分平仓(size≠0)时，不需设置auto_size 双仓模式全部平仓(size&#x3D;0)时，必须设置auto_size，close_long 平多头， close_short 平空头 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


