# OtcStableCoinOrderRequest

Stablecoin Order Request Body
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pay_coin** | **str** | Currency paid by the user. Supported currencies can be queried from the OTC web stablecoin quote page. | 
**get_coin** | **str** | Currency to be received by the user. Supported currencies can be queried from the OTC web stablecoin quote page. | 
**pay_amount** | **str** | User payment currency amount | 
**get_amount** | **str** | Amount of currency received by the user | 
**side** | **str** | The side returned by the quote endpoint (used for order validation). For backward compatibility, &#x60;PAY&#x60;/&#x60;GET&#x60; are accepted; new integrations should use the value returned by the quote response. | 
**promotion_code** | **str** | Promotion code (optional) | [optional] 
**quote_token** | **str** | Parameter returned by the quote API | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


