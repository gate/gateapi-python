# OptionsAccount

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | **int** | User ID | [optional] 
**total** | **str** | Account balance, invalid for unified account | [optional] 
**position_value** | **str** | Position value, long position value is positive, short position value is negative | [optional] 
**equity** | **str** | Account equity &#x3D; balance + option position value, invalid for unified account | [optional] 
**short_enabled** | **bool** | If the account is allowed to short | [optional] 
**mmp_enabled** | **bool** | Whether to enable MMP | [optional] 
**liq_triggered** | **bool** | Whether the account is in a liquidation state | [optional] 
**margin_mode** | **int** | This field indicates the margin mode used by the unified account:  - 0: Classic Spot Margin Mode - 1: Cross-Currency Margin Mode - 2: Portfolio Margin Mode - 3: Single-Currency Margin Mode | [optional] 
**unrealised_pnl** | **str** | Unrealised PnL &#x3D; (mark price - entry price) * position size. For long postion, size is positive; for short positon, size is negative.This value is for reference only. | [optional] 
**init_margin** | **str** | Initial position margin | [optional] 
**maint_margin** | **str** | Position maintenance margin | [optional] 
**order_margin** | **str** | Order margin of unfinished orders | [optional] 
**ask_order_margin** | **str** | Margin for outstanding sell orders | [optional] 
**bid_order_margin** | **str** | Margin for outstanding buy orders | [optional] 
**available** | **str** | Available balance to transfer out or trade | [optional] 
**point** | **str** | Point card amount | [optional] 
**currency** | **str** | Settlement currency | [optional] 
**orders_limit** | **int** | Maximum number of outstanding orders | [optional] 
**position_notional_limit** | **int** | Notional value upper limit, including the nominal value of positions and outstanding orders | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


