# Contract

Futures contract details
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Futures contract | [optional] 
**type** | **str** | Contract type: inverse - inverse contract, direct - direct contract | [optional] 
**quanto_multiplier** | **str** | The contract multiplier indicates how many units of the underlying asset the face value of one contract represents. | [optional] 
**leverage_min** | **str** | Minimum leverage | [optional] 
**leverage_max** | **str** | Maximum leverage | [optional] 
**maintenance_rate** | **str** | The maintenance margin rate of the first tier of risk limit sheet | [optional] 
**mark_type** | **str** | Deprecated | [optional] 
**mark_price** | **str** | Current mark price | [optional] 
**index_price** | **str** | Current index price | [optional] 
**last_price** | **str** | Last trading price | [optional] 
**maker_fee_rate** | **str** | Maker fee rate, negative values indicate rebates | [optional] 
**taker_fee_rate** | **str** | Taker fee rate | [optional] 
**order_price_round** | **str** | Minimum order price increment | [optional] 
**mark_price_round** | **str** | Minimum mark price increment | [optional] 
**funding_rate** | **str** | Current funding rate | [optional] 
**funding_interval** | **int** | Funding application interval, unit in seconds | [optional] 
**funding_next_apply** | **float** | Next funding time | [optional] 
**risk_limit_base** | **str** | Base risk limit (deprecated) | [optional] 
**risk_limit_step** | **str** | Risk limit adjustment step (deprecated) | [optional] 
**risk_limit_max** | **str** | Maximum risk limit allowed by the contract (deprecated). It is recommended to use /futures/{settle}/risk_limit_tiers to query risk limits | [optional] 
**order_size_min** | **str** | Minimum order size allowed by the contract | [optional] 
**order_size_max** | **str** | Maximum order size allowed by the contract | [optional] 
**order_price_deviate** | **str** | Maximum allowed deviation between order price and current mark price. The order price &#x60;order_price&#x60; must satisfy the following condition:      abs(order_price - mark_price) &lt;&#x3D; mark_price * order_price_deviate | [optional] 
**ref_discount_rate** | **str** | Trading fee discount for referred users | [optional] 
**ref_rebate_rate** | **str** | Commission rate for referrers | [optional] 
**orderbook_id** | **int** | Orderbook update ID | [optional] 
**trade_id** | **int** | Current trade ID | [optional] 
**trade_size** | **str** | Historical cumulative trading volume | [optional] 
**position_size** | **str** | Current total long position size | [optional] 
**config_change_time** | **float** | Last configuration update time | [optional] 
**in_delisting** | **bool** | &#x60;in_delisting&#x3D;true&#x60; and position_size&gt;0 indicates the contract is in delisting transition period &#x60;in_delisting&#x3D;true&#x60; and position_size&#x3D;0 indicates the contract is delisted | [optional] 
**orders_limit** | **int** | Maximum number of pending orders | [optional] 
**enable_bonus** | **bool** | Whether bonus is enabled | [optional] 
**enable_credit** | **bool** | Whether portfolio margin account is enabled | [optional] 
**create_time** | **float** | Created time of the contract | [optional] 
**funding_cap_ratio** | **str** | Deprecated | [optional] 
**status** | **str** | Contract status types include: prelaunch (pre-launch), trading (active), delisting (delisting), delisted (delisted), circuit_breaker (circuit breaker) | [optional] 
**launch_time** | **int** | Contract expiry timestamp | [optional] 
**delisting_time** | **int** | Timestamp when contract enters reduce-only state | [optional] 
**delisted_time** | **int** | Contract delisting time | [optional] 
**market_order_slip_ratio** | **str** | The maximum slippage allowed for market orders, with the slippage rate calculated based on the latest market price | [optional] 
**market_order_size_max** | **str** | The maximum number of contracts supported for market orders, with a default value of 0. When the default value is used, the maximum number of contracts is limited by the &#x60;order_size_max&#x60; field | [optional] 
**funding_rate_limit** | **str** | Upper and lower limits of funding rate | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


