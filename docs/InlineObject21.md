# InlineObject21

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | Client-defined Order ID, supports letters (a-z), numbers (0-9), symbols (-, _) only | [optional] 
**symbol** | **str** | 唯一标识 Exchange_Business_Base_Counter  示例：  如果您想在币安交易所上为ADA/USDT交易对下现货订单，您可以使用这样的唯一标识符：&#x60;BINANCE_SPOT_ADA_USDT&#x60;;   如果您想在欧易交易所上为ADA/USDT交易对下U本位永续合约订单，您可以使用这样的唯一标识符：&#x60;OKX_FUTURE_ADA_USDT&#x60;;   如果您想在Gate交易所上为ADA/USDT交易对下现货杠杆订单，您可以使用这样的唯一标识符：&#x60;GATE_MARGIN_ADA_USDT&#x60;;   目前支持三种订单：现货订单、U本位永续合约订单和现货杠杆订单 | 
**side** | **str** | BUY, SELL | 
**type** | **str** | Order type (default: &#x60;LIMIT&#x60;; supported types: &#x60;LIMIT&#x60;, &#x60;MARKET&#x60;) | [optional] [default to 'LIMIT']
**time_in_force** | **str** | Default GTC, supports enumerated types: GTC, IOC, FOK, POC GTC: GoodTillCancelled IOC: ImmediateOrCancelled FOK: FillOrKill POC: PendingOrCancelled or PostOnly | [optional] [default to 'GTC']
**qty** | **str** | Order quantity (required unless spot market buy) | [optional] 
**price** | **str** | Limit Order Price (Required for Limit Orders) | [optional] 
**quote_qty** | **str** | Order quote quantity; required for spot and margin market buy orders | [optional] 
**reduce_only** | **str** | Reduce-only: &#x60;true&#x60; or &#x60;false&#x60; | [optional] 
**position_side** | **str** | Position side: &#x60;NONE&#x60;, &#x60;LONG&#x60;, &#x60;SHORT&#x60; Defaults to &#x60;NONE&#x60; (single position mode) if not specified | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


