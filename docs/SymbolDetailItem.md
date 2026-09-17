# SymbolDetailItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **str** | Symbol | [optional] 
**exchange** | **str** | Exchange, supports us, hk, kr, and jp | [optional] 
**exchange_desc** | **str** | Exchange description | [optional] 
**quote_currency** | **str** | Quote currency | [optional] 
**quote_currency_precision** | **int** | Quote currency precision | [optional] 
**fx_rate** | **str** | Quote currency to USD exchange rate | [optional] 
**symbol_desc** | **str** | Symbol description | [optional] 
**category** | **str** | Symbol category. - CS: Common stock. - ETF: Exchange-traded funds. - ADRC, ADR: Depositary receipts for foreign companies listed in the U.S. - ETV: Exchange-traded products. - PFD: Preferred stock. - ETS: Exchange-traded securities. - ETN: Exchange-traded notes. - FUND: Funds. | [optional] 
**asset_type** | **str** | Asset type. - STOCK: Stock. - ETF: Exchange-traded fund. | [optional] 
**settlement_currency** | **str** | Settlement currency | [optional] 
**max_order_volume** | **str** | Maximum order quantity | [optional] 
**step_order_volume** | **str** | Order step size | [optional] 
**min_order_volume** | **str** | Minimum order quantity | [optional] 
**price_precision** | **int** | Price precision | [optional] 
**volume_precision** | **int** | Quantity precision | [optional] 
**is_ipo** | **bool** | Whether it is an IPO symbol | [optional] 
**ipo_price** | **str** | IPO price | [optional] 
**price_protection** | **str** | Price protection range | [optional] 
**sell_price_protection** | **str** | Sell price protection rate | [optional] 
**buy_price_protection** | **str** | Buy price protection rate | [optional] 
**slippage_rate** | **str** | Slippage | [optional] 
**commission_rate** | **str** | Fee Rate | [optional] 
**trade_status** | **str** | Trading status. - pre_market: Pre-market. - open: Regular trading session. - post_market: Post-market. - closed: Market closed. - gt_lp: GT LP session. | [optional] 
**trade_mode** | **int** | Current session trading mode. - 0: Trading disabled. - 1: Buy only. - 2: Sell only. - 4: Buy and sell supported. | [optional] 
**order_fill_timing** | **int** | Order fill timing (1&#x3D;immediate, 2&#x3D;after pre-market opens, 3&#x3D;after regular session opens) | [optional] 
**symbol_descs** | [**list[SymbolDetailItemSymbolDescs]**](SymbolDetailItemSymbolDescs.md) | Multilingual symbol description | [optional] 
**icon_link** | **str** | Icon URL | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


