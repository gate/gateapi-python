# StockOptionPositionListItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **str** | Full option contract symbol. | [optional] 
**symbol_display** | **str** | Option contract name for display. | [optional] 
**underlying** | **str** | Option underlying symbol. | [optional] 
**side** | **str** | Position side. - long: Long position. - short: Short position. | [optional] 
**open_time** | **int** | Position opening time as a Unix timestamp in seconds; 0 when unavailable. | [optional] 
**quantity** | **str** | Position quantity. | [optional] 
**available** | **str** | Available quantity; currently equal to quantity. | [optional] 
**frozen** | **str** | Frozen quantity; may be empty when not calculated separately. | [optional] 
**avg_entry_price** | **str** | Average entry price. | [optional] 
**last_price** | **str** | Last traded price; 0 when no valid value is available. | [optional] 
**mark_price** | **str** | Mark price; 0 when no valid value is available. | [optional] 
**previous_close** | **str** | Previous closing price. If no valid positive value exists, this field may be empty and daily PnL calculation is skipped. | [optional] 
**market_value** | **str** | Market value &#x3D; valuation price × signed position quantity × contract multiplier. The valuation price is selected by &#x60;price_type&#x60; (&#x60;latest&#x60; uses last_price; &#x60;mark&#x60; uses mark_price). | [optional] 
**unrealized_pnl** | **str** | Unrealized PnL &#x3D; (valuation price - average entry price) × signed position quantity × contract multiplier. Returns 0 if the average entry price or quantity is invalid. The valuation price follows the same rules as market_value. | [optional] 
**today_pnl** | **str** | Daily PnL for this contract. Requires a valid previous_close; 0 if unavailable. The valuation price follows the same rules as market_value. | [optional] 
**today_buy_qty** | **str** | Quantity bought today (user&#39;s daily trading totals). | [optional] 
**today_sell_qty** | **str** | Quantity sold today (user&#39;s daily trading totals). | [optional] 
**today_buy_value** | **str** | Amount bought today (user&#39;s daily trading totals). | [optional] 
**today_sell_value** | **str** | Amount sold today (user&#39;s daily trading totals). | [optional] 
**trade_status** | [**StockOptionTradeStatus**](StockOptionTradeStatus.md) |  | [optional] 
**trade_mode** | [**StockOptionTradeMode**](StockOptionTradeMode.md) |  | [optional] 
**multiplier** | **str** | Contract multiplier. | [optional] 
**price_precision** | **int** | Number of decimal places for prices. | [optional] 
**min_order_volume** | **str** | Minimum order quantity. | [optional] 
**max_order_volume** | **str** | Maximum order quantity. | [optional] 
**step_order_volume** | **str** | Order quantity increment. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


