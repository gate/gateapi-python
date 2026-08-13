# OtcOrderRequest

Fiat Order Request Body
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | BUY for on-ramp, SELL for off-ramp | 
**side** | **str** | The side returned by the quote endpoint (used for order validation). For backward compatibility, &#x60;FIAT&#x60;/&#x60;CRYPTO&#x60; or &#x60;PAY&#x60;/&#x60;GET&#x60; are accepted; new integrations should use the value returned by the quote response. | 
**crypto_currency** | **str** | Cryptocurrency (supported currencies can be queried from the OTC web fiat quote page) | 
**fiat_currency** | **str** | Fiat currency (supported currencies can be queried from the OTC web fiat quote page) | 
**crypto_amount** | **str** | Amount of cryptocurrency | 
**fiat_amount** | **str** | Fiat amount | 
**promotion_code** | **str** | Promotion code | [optional] 
**quote_token** | **str** | Parameter returned by the quote API | 
**bank_id** | **str** | Bank card ID used to place the order. Select one from the list returned by &#x60;GET /otc/bank/list&#x60;; the default card has &#x60;is_default&#x3D;1&#x60;. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


