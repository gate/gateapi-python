# InlineObject2

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | BUY for on-ramp, SELL for off-ramp | 
**side** | **str** | Quote direction returned by the quote API (used for order validation) | 
**crypto_currency** | **str** | Cryptocurrency (supported currencies can be queried from the OTC web fiat quote page) | 
**fiat_currency** | **str** | Fiat currency (supported currencies can be queried from the OTC web fiat quote page) | 
**crypto_amount** | **str** | Amount of cryptocurrency | 
**fiat_amount** | **str** | Fiat amount | 
**promotion_code** | **str** | Promotion code | [optional] 
**quote_token** | **str** | Parameter returned by the quote API | 
**bank_id** | **str** | Bank card ID used for the order (retrieved via the default bank card API) | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


