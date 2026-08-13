# Symbol

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **str** | Unique trading pair identifier in the form ExchangeType_BusinessType_Base_Counter. | 
**exchange_type** | **str** | Venue bucket (&#x60;BINANCE&#x60; / &#x60;OKX&#x60; / &#x60;GATE&#x60; / &#x60;BYBIT&#x60; / &#x60;KRAKEN&#x60; / &#x60;HYPERLIQUID&#x60; / &#x60;DERIBIT&#x60;). | 
**business_type** | **str** | Business type (&#x60;SPOT&#x60; Spot / &#x60;FUTURE&#x60; Futures / &#x60;MARGIN&#x60; Margin). | 
**state** | **str** | Status (&#x60;live&#x60; running / &#x60;suspend&#x60; paused). | 
**min_size** | **str** | Minimum order quantity | 
**min_notional** | **str** | Minimum Order Value | 
**lot_size** | **str** | Quantity Step | 
**tick_size** | **str** | Price Step | 
**max_num_orders** | **str** | maximumopen orderamount | 
**max_market_size** | **str** | Maximum Market Order Quantity | 
**max_limit_size** | **str** | Maximum order quantity for limit orders. | 
**contract_size** | **str** | Contract multiplier (deprecated; quantity is used uniformly) | 
**liquidation_fee** | **str** | Liquidation Fee Rate | 
**delist_time** | **str** | Millisecond timestamp; &#x60;0&#x60; means not delisted. | 
**support_rpi** | **str** | Whether RPI order placement is supported (true if supported; false otherwise) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


