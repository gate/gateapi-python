# PositionTimerange

Contract position details (historical data)
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contract** | **str** | Futures contract | [optional] [readonly] 
**size** | **str** | Position size | [optional] [readonly] 
**leverage** | **str** | Position leverage. 0 means cross margin; positive number means isolated margin | [optional] 
**risk_limit** | **str** | Position risk limit | [optional] 
**leverage_max** | **str** | the maximum permissible leverage given to the current positon value: the higher positon value, the lower maximum permissible leverage | [optional] [readonly] 
**maintenance_rate** | **str** | The maintenance margin rate of the first tier of risk limit sheet | [optional] [readonly] 
**margin** | **str** | Position margin | [optional] 
**liq_price** | **str** | Liquidation price | [optional] [readonly] 
**realised_pnl** | **str** | Realized PnL | [optional] [readonly] 
**history_pnl** | **str** | Total realized PnL from closed positions | [optional] [readonly] 
**last_close_pnl** | **str** | PNL of last position close | [optional] [readonly] 
**realised_point** | **str** | Realized POINT PNL | [optional] [readonly] 
**history_point** | **str** | History realized POINT PNL | [optional] [readonly] 
**mode** | **str** | Position mode, including: - &#x60;single&#x60;: One-way Mode - &#x60;dual_long&#x60;: Long position in Hedge Mode - &#x60;dual_short&#x60;: Short position in Hedge Mode | [optional] 
**cross_leverage_limit** | **str** | Cross margin leverage (valid only when &#x60;leverage&#x60; is 0) | [optional] 
**entry_price** | **str** | Entry price | [optional] [readonly] 
**time** | **int** | Timestamp | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


