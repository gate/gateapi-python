# SymbolDetailItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **str** |  | [optional] 
**exchange** | **str** | Exchange, supports us, hk, and kr | [optional] 
**exchange_desc** | **str** |  | [optional] 
**quote_currency** | **str** |  | [optional] 
**quote_currency_precision** | **int** |  | [optional] 
**fx_rate** | **str** | Quote currency to USD exchange rate | [optional] 
**symbol_desc** | **str** |  | [optional] 
**category** | **str** |  | [optional] 
**settlement_currency** | **str** |  | [optional] 
**max_order_volume** | **str** |  | [optional] 
**step_order_volume** | **str** |  | [optional] 
**min_order_volume** | **str** |  | [optional] 
**price_precision** | **int** | Price precision | [optional] 
**volume_precision** | **int** |  | [optional] 
**is_ipo** | **bool** |  | [optional] 
**ipo_price** | **str** |  | [optional] 
**price_protection** | **str** |  | [optional] 
**sell_price_protection** | **str** |  | [optional] 
**buy_price_protection** | **str** |  | [optional] 
**slippage_rate** | **str** |  | [optional] 
**commission_rate** | **str** | Fee Rate | [optional] 
**trade_status** | **str** | Trading status. - pre_market: Pre-market. - open: Regular trading session. - post_market: Post-market. - closed: Market closed. - gt_lp: GT LP session. | [optional] 
**trade_mode** | **int** | Current session trading mode. - 0: Trading disabled. - 1: Buy only. - 2: Sell only. - 4: Buy and sell supported. | [optional] 
**order_fill_timing** | **int** | Order fill timing (1&#x3D;immediate, 2&#x3D;after pre-market opens, 3&#x3D;after regular session opens) | [optional] 
**symbol_descs** | [**list[SymbolDetailItemSymbolDescs]**](SymbolDetailItemSymbolDescs.md) |  | [optional] 
**icon_link** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


