# CrossexAccountUpdateResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position_mode** | **str** | Requested futures position mode to modify (SINGLE/DUAL) | [optional] 
**account_mode** | **str** | Requested account mode to modify (CROSS_EXCHANGE/ISOLATED_EXCHANGE, default: CROSS_EXCHANGE) | [optional] 
**exchange_type** | **str** | Exchange targeted by the requested change (&#x60;BINANCE&#x60; / &#x60;OKX&#x60; / &#x60;GATE&#x60; / &#x60;BYBIT&#x60; / &#x60;KRAKEN&#x60; / &#x60;HYPERLIQUID&#x60; / &#x60;DERIBIT&#x60; / &#x60;CROSSEX&#x60;). When account mode is &#x60;ISOLATED_EXCHANGE&#x60;, the exchange must be specified to change futures position mode. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


