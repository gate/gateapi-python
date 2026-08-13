# SymbolListItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **str** | Symbol | [optional] 
**exchange** | **str** | Exchange, supports us, hk, and kr | [optional] 
**exchange_desc** | **str** | Exchange description | [optional] 
**quote_currency** | **str** | Quote currency | [optional] 
**quote_currency_precision** | **int** | Quote currency precision | [optional] 
**fx_rate** | **str** | Quote currency to USD exchange rate | [optional] 
**symbol_desc** | **str** | Symbol description | [optional] 
**category** | **str** | Category | [optional] 
**trade_status** | **str** | Trading status. - pre_market: Pre-market. - open: Regular trading session. - post_market: Post-market. - closed: Market closed. - gt_lp: GT LP session. | [optional] 
**trade_mode** | **int** | Current session trading mode. - 0: Trading disabled. - 1: Buy only. - 2: Sell only. - 4: Buy and sell supported. | [optional] 
**order_fill_timing** | **int** | Order fill timing (1&#x3D;immediate, 2&#x3D;after pre-market opens, 3&#x3D;after regular session opens) | [optional] 
**icon_link** | **str** | Icon URL | [optional] 
**quote_currency_symbol** | **str** | Quote currency symbol | [optional] 
**price_precision** | **int** | Price precision | [optional] 
**volume_precision** | **int** | Quantity precision | [optional] 
**is_ipo** | **bool** | Whether it is an IPO symbol | [optional] 
**ipo_price** | **str** | IPO price | [optional] 
**sell_price_protection** | **str** | Sell price protection rate | [optional] 
**buy_price_protection** | **str** | Buy price protection rate | [optional] 
**symbol_descs** | [**list[I18nTxt]**](I18nTxt.md) | Multilingual symbol description | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


