# OtcQuoteRequest

Fiat and Stablecoin Quote Request Body
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**side** | **str** | PAY: specify the payment amount (&#x60;pay_amount&#x60; is required); GET: specify the receive amount (&#x60;get_amount&#x60; is required). | 
**pay_coin** | **str** | Payment currency. Supported currencies are available on the OTC web quote page. | 
**get_coin** | **str** | Receive currency. Supported currencies are available on the OTC web quote page. | 
**pay_amount** | **str** | User payment currency amount | [optional] 
**get_amount** | **str** | Amount of currency received by the user | [optional] 
**create_quote_token** | **str** | Create quote token: 0: quote preview only; 1: generate quote token for order placement. | [optional] 
**promotion_code** | **str** | Promotion code | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


