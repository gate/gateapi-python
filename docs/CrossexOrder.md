# CrossexOrder

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | User ID | 
**order_id** | **str** | Order ID | 
**text** | **str** | Client-defined order ID. | 
**state** | **str** | Order status: &#x60;NEW&#x60;: validated locally, pending submission to the exchange &#x60;OPEN&#x60;: resting on the exchange order book &#x60;PARTIALLY_FILLED&#x60;: partially filled &#x60;FILLED&#x60;: fully filled &#x60;FAIL&#x60;: CrossEx validation failed; see &#x60;reason&#x60; &#x60;REJECT&#x60;: rejected by the exchange; see &#x60;reason&#x60; &#x60;CANCELLED&#x60;: cancelled | 
**symbol** | **str** | Unique trading pair identifiers, e.g. &#x60;BINANCE_SPOT_BTC_USDT&#x60;, &#x60;BINANCE_FUTURE_BTC_USDT&#x60;. | 
**side** | **str** | Side (&#x60;BUY&#x60; buy / &#x60;SELL&#x60; sell). | 
**type** | **str** | Order type (&#x60;LIMIT&#x60; limit / &#x60;MARKET&#x60; market). | 
**attribute** | **str** | Order attributes (&#x60;COMMON&#x60; normal / &#x60;LIQ&#x60; liquidation takeover / &#x60;REDUCE&#x60; liquidation reduction / &#x60;ADL&#x60; auto-deleverage / &#x60;SETTLEMENT&#x60; delisting settlement). | 
**exchange_type** | **str** | Venue bucket (&#x60;BINANCE&#x60; / &#x60;OKX&#x60; / &#x60;GATE&#x60; / &#x60;BYBIT&#x60; / &#x60;KRAKEN&#x60; / &#x60;HYPERLIQUID&#x60; / &#x60;DERIBIT&#x60;). | 
**business_type** | **str** | Business type (&#x60;SPOT&#x60; Spot / &#x60;FUTURE&#x60; Futures / &#x60;MARGIN&#x60; Margin / &#x60;CONVERT&#x60; Flash Swap). | 
**qty** | **str** | Order quantity in the base currency. | 
**quote_qty** | **str** | Order quantity in the quote currency. | 
**price** | **str** | Order price. | 
**time_in_force** | **str** | Time-in-force policy (default: GTC; allowed values: GTC, IOC, FOK, POC, and RPI) | 
**executed_qty** | **str** | Filled base amount. | 
**executed_amount** | **str** | Filled quote amount. | 
**executed_avg_price** | **str** | Average Filled Price | 
**fee_coin** | **str** | Fee currency | 
**fee** | **str** | Fee amount. | 
**reduce_only** | **str** | Reduce-only order (&#x60;\&quot;true\&quot;&#x60; or &#x60;\&quot;false\&quot;&#x60;). | 
**leverage** | **str** | Order leverage multiplier. | 
**reason** | **str** | Failure reason description. | 
**last_executed_qty** | **str** | Base quantity of the latest fill. | 
**last_executed_price** | **str** | Price of the latest fill. | 
**last_executed_amount** | **str** | Quote amount of the latest fill. | 
**position_side** | **str** | Position side (&#x60;NONE&#x60; one-way position / &#x60;LONG&#x60; long / &#x60;SHORT&#x60; short) | 
**create_time** | **str** | Created time | 
**update_time** | **str** | Update time | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


