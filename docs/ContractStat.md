# ContractStat

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time** | **int** | Stat timestamp | [optional] 
**lsr_taker** | **float** | Long/short taker ratio | [optional] 
**lsr_account** | **float** | Long/short position user ratio | [optional] 
**long_liq_size** | **str** | Long liquidation size (contracts) | [optional] 
**long_liq_amount** | **float** | Long liquidation amount (base currency) | [optional] 
**long_liq_usd** | **float** | Long liquidation volume (quote currency) | [optional] 
**long_liq_usd_new** | **float** | Long liquidations in quote currency; USDT settlement: long_liq_size × multiplier × mark price | [optional] 
**short_liq_size** | **str** | Short liquidation size (contracts) | [optional] 
**short_liq_amount** | **float** | Short liquidation amount (base currency) | [optional] 
**short_liq_usd** | **float** | Short liquidation volume (quote currency) | [optional] 
**short_liq_usd_new** | **float** | Short liquidations in quote currency; USDT settlement: short_liq_size × multiplier × mark price | [optional] 
**open_interest** | **str** | Total open interest size (contracts) | [optional] 
**open_interest_usd** | **float** | Total open interest volume (quote currency) | [optional] 
**top_lsr_account** | **float** | Top trader long/short account ratio | [optional] 
**top_lsr_size** | **str** | Top trader long/short position ratio | [optional] 
**mark_price** | **float** | Mark price | [optional] 
**top_long_size** | **str** | Top long open interest (contracts) | [optional] 
**top_short_size** | **str** | Top short open interest (contracts) | [optional] 
**long_taker_size** | **str** | Long taker trade volume (contracts) | [optional] 
**short_taker_size** | **str** | Short taker trade volume (contracts) | [optional] 
**top_long_account** | **int** | Number of top long accounts (large holders) | [optional] 
**top_short_account** | **int** | Number of top short accounts (large holders) | [optional] 
**long_users** | **int** | Number of users holding long positions | [optional] 
**short_users** | **int** | Number of users holding short positions | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


