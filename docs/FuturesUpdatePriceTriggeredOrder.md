# FuturesUpdatePriceTriggeredOrder

Modify Price Order Details
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**settle** | **str** | Settlement Currency (e.g., USDT, BTC) | [optional] [readonly] 
**order_id** | **str** | The order ID of the modified price-triggered order. This ID is returned upon successful creation of the price-triggered order. Note: This ID must be passed in both the request path and request body. | 
**size** | **int** | Modified Contract Quantity. Full Close: 0; Partial Close: Positive/Negative values indicate direction (consistent with the creation interface logic). | [optional] 
**price** | **str** | Represents the modified trading price. A value of 0 indicates a market order. | [optional] 
**trigger_price** | **str** | Modified Trigger Price | [optional] 
**price_type** | **int** | Reference price type. 0 - Latest trade price, 1 - Mark price, 2 - Index price | [optional] 
**auto_size** | **str** | One-way Mode: auto_size is not required Hedge Mode partial closing (size≠0): auto_size is not required Hedge Mode full closing (size&#x3D;0): auto_size must be set, close_long for closing long positions, close_short for closing short positions | [optional] 
**close** | **bool** | When fully closing a position in single-position mode, close must be set to true to execute the close operation. When partially closing a position in single-position mode or in dual-position mode, close can be left unset or set to false. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


