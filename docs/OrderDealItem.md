# OrderDealItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Trade record primary key ID | [optional] 
**deal_id** | **int** | Trade ID | [optional] 
**order_id** | **int** | Order ID | [optional] 
**client_order_id** | **str** | Client-defined order ID | [optional] 
**user_id** | **int** | User ID | [optional] 
**symbol** | **str** | Symbol | [optional] 
**exchange** | **str** | Exchange. - us: US stocks. - hk: Hong Kong stocks. - kr: Korean stocks. - jp: Japanese stocks. | [optional] 
**side** | **int** | Side (1&#x3D;sell, 2&#x3D;buy) | [optional] 
**role** | **str** | Liquidity role. - maker: Maker. - taker: Taker. | [optional] 
**price** | **str** | Trade price in the instrument trading currency | [optional] 
**quantity** | **str** | Trading size | [optional] 
**position_qty** | **str** | Position quantity after the trade | [optional] 
**avg_entry_price** | **str** | Average entry price | [optional] 
**value** | **str** | Trade value in the instrument trading currency | [optional] 
**fx_rate** | **str** | Quote currency to USD exchange rate | [optional] 
**fee** | **str** | Fee in the instrument trading currency | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


