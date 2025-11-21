# SpotPricePutOrder

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Order type，default to &#x60;limit&#x60;  - limit : Limit Order - market : Market Order | [optional] [default to 'limit']
**side** | **str** | Order side  - buy: buy side - sell: sell side | 
**price** | **str** | Order price | 
**amount** | **str** | Trading quantity, refers to the trading quantity of the trading currency, i.e., the currency that needs to be traded, for example, the quantity of BTC in BTC_USDT. | 
**account** | **str** | Trading account type. Unified account must be set to &#x60;unified&#x60;  - normal: spot trading - margin: margin trading - unified: unified account  | [default to 'normal']
**time_in_force** | **str** | time_in_force  - gtc: GoodTillCancelled - ioc: ImmediateOrCancelled, taker only  | [optional] [default to 'gtc']
**auto_borrow** | **bool** | Whether to borrow coins automatically | [optional] [default to False]
**auto_repay** | **bool** | Whether to repay the loan automatically | [optional] [default to False]
**text** | **str** | The source of the order, including: - web: Web - api: API call - app: Mobile app | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


