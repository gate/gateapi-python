# InlineObject11

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | Client-defined Order ID, supports letters (a-z), numbers (0-9), symbols (-, _) only | [optional] 
**symbol** | **str** | Unique Identifier Exchange_Business_Base_Counter Examples: - To place a Spot order for ADA/USDT on BINANCE: Use identifier &#x60;BINANCE_SPOT_ADA_USDT&#x60;;   - To place a USDT-margined Perpetual Futures order for ADA/USDT on OKX: Use identifier &#x60;OKX_FUTURE_ADA_USDT&#x60;;   - To place a Spot Margin order for ADA/USDT on GATE: Use identifier &#x60;GATE_MARGIN_ADA_USDT&#x60;;   - To place a Spot order for ADA/USDT on BYBIT: Use identifier &#x60;BYBIT_SPOT_ADA_USDT&#x60;;   Currently supports three order types: Spot orders, USDT-margined Perpetual Futures orders, and Spot Margin orders. BYBIT does not currently support Spot Margin orders | 
**side** | **str** | BUY, SELL | 
**type** | **str** | Order type (default: &#x60;LIMIT&#x60;; supported types: &#x60;LIMIT&#x60;, &#x60;MARKET&#x60;) | [optional] [default to 'LIMIT']
**time_in_force** | **str** | Default GTC, supports enumerated types: GTC, IOC, FOK, POC GTC: GoodTillCancelled IOC: ImmediateOrCancelled FOK: FillOrKill POC: PendingOrCancelled or PostOnly | [optional] [default to 'GTC']
**qty** | **str** | Order quantity (required unless spot market buy) | [optional] 
**price** | **str** | Limit Order Price (Required for Limit Orders) | [optional] 
**quote_qty** | **str** | Order quote quantity; required for spot and margin market buy orders | [optional] 
**reduce_only** | **str** | Reduce-only: &#x60;true&#x60; or &#x60;false&#x60; | [optional] 
**position_side** | **str** | Position side: &#x60;NONE&#x60;, &#x60;LONG&#x60;, &#x60;SHORT&#x60; Defaults to &#x60;NONE&#x60; (single position mode) if not specified | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


