# TradFiOrderRequest

Place order request parameters
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price** | **str** | Order price | 
**price_type** | **str** | Price type (trigger&#x3D;trigger price, market&#x3D;market price) | 
**side** | **int** | Side (1&#x3D;sell, 2&#x3D;buy) | 
**symbol** | **str** | Base trading symbol code | 
**volume** | **str** | Order quantity | 
**price_tp** | **str** | Take profit price (optional) | [optional] 
**price_sl** | **str** | Stop loss price (optional) | [optional] 
**leverage** | **int** | Leverage multiplier (must be one of the leverage multipliers allowed for the symbol in the trading symbol details response) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


