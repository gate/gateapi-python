# OptionsContract

Options contract details
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Options contract name | [optional] 
**tag** | **str** | Expiry periods include day, week, and month. | [optional] 
**create_time** | **float** | Created time | [optional] 
**expiration_time** | **float** | Expiration time | [optional] 
**is_call** | **bool** | &#x60;true&#x60; means call options, &#x60;false&#x60; means put options | [optional] 
**multiplier** | **str** | The option contract multiplier indicates how many units of the underlying asset the face value of one contract represents. | [optional] 
**underlying** | **str** | Underlying | [optional] 
**underlying_price** | **str** | The forward futures price corresponding to the delivery date | [optional] 
**last_price** | **str** | Last trading price | [optional] 
**mark_price** | **str** | Current mark price (quote currency) | [optional] 
**index_price** | **str** | Current index price (quote currency) | [optional] 
**maker_fee_rate** | **str** | Maker fee rate, negative values indicate rebates | [optional] 
**taker_fee_rate** | **str** | Taker fee rate | [optional] 
**order_price_round** | **str** | Minimum order price increment | [optional] 
**mark_price_round** | **str** | Minimum mark price increment | [optional] 
**order_size_min** | **int** | Minimum order size allowed by the contract | [optional] 
**order_size_max** | **int** | Maximum order size allowed by the contract | [optional] 
**order_price_deviate** | **str** | Deprecated | [optional] 
**ref_discount_rate** | **str** | Trading fee discount for referred users | [optional] 
**ref_rebate_rate** | **str** | Commission rate for referrers | [optional] 
**orderbook_id** | **int** | Orderbook update ID | [optional] 
**trade_id** | **int** | Deprecated | [optional] 
**trade_size** | **int** | Historical cumulative trading volume | [optional] 
**position_size** | **int** | Current total long position size | [optional] 
**orders_limit** | **int** | The maximum number of open orders each user can place in this order book. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


