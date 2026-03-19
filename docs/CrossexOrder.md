# CrossexOrder

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | 
**order_id** | **str** | Order ID | 
**text** | **str** | Customer-defined order ID | 
**state** | **str** | Order State:  NEW: The order is legal and waiting to be sent to the exchange  OPEN: The order has been placed on the orderbook of the exchange  PARTIALLY_FILLED: The order has been partially completed  FILLED: The order has been fully executed  FAIL: The order verification in CrossEx did not pass. Please check the order reason  REJECT：The order was rejected by the exchange. Please check the order reason | 
**symbol** | **str** | Trading pair unique identifier ,example: BINANCE_SPOT_BTC_USDT, BINANCE_FUTURE_BTC_USDT | 
**side** | **str** | Side(BUY,SELL) | 
**type** | **str** | Type(LIMIT, MARKET) | 
**attribute** | **str** | COMMON, LIQ, REDUCE, ADL | 
**exchange_type** | **str** | Exchange type(BINANCE,OKX,GATE,BYBIT) | 
**business_type** | **str** | Business type(SPOT,FUTURE,MARGIN) | 
**qty** | **str** | Order base quantity | 
**quote_qty** | **str** | Order quote quantity | 
**price** | **str** | Order price | 
**time_in_force** | **str** | Timeinforce (default GTC, enums:GTC,IOC,FOK,POC) | 
**executed_qty** | **str** | Executed quantity | 
**executed_amount** | **str** | Executed quote quantity | 
**executed_avg_price** | **str** | Average transaction price | 
**fee_coin** | **str** | Transaction fee coin | 
**fee** | **str** | Transaction fee amount | 
**reduce_only** | **str** | Reduce position orders only, \&quot;true\&quot; or \&quot;false\&quot; | 
**leverage** | **str** | Order leverage | 
**reason** | **str** | Fail message | 
**last_executed_qty** | **str** | Last transaction quantity | 
**last_executed_price** | **str** | Last transaction price | 
**last_executed_amount** | **str** | Last transaction amount | 
**position_side** | **str** | Position side(NONE/LONG/SHORT) | 
**create_time** | **str** | Create time | 
**update_time** | **str** | Update time | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


