# OtcOrderDetail

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** | Order ID | 
**uid** | **str** | User ID | 
**type** | **str** | Order Type | 
**fiat_currency** | **str** | Fiat currency | 
**fiat_amount** | **str** | Fiat amount | 
**crypto_currency** | **str** | Digital currency | 
**crypto_amount** | **str** | Cryptocurrency amount | 
**rate** | **str** | Exchange rate | 
**bank_account_name** | **str** | User payment/receiving name | [optional] 
**bank_name** | **str** | User payment/receiving bank name | [optional] 
**bank_country** | **str** | User payment/receiving bank country | [optional] 
**bank_address** | **str** | User payment/receiving bank address | [optional] 
**bank_account_number_iban** | **str** | User payment/receiving bank account number/IBAN | [optional] 
**swift_code** | **str** | User payment/receiving bank SWIFT code | [optional] 
**intermediate_bank_name** | **str** | User payment/receiving intermediary bank name | [optional] 
**intermediary_bank_swift_code** | **str** | User payment/receiving intermediary bank SWIFT code | [optional] 
**gate_bank_account_name** | **str** | Gate beneficiary name, shown for BUY only | [optional] 
**gate_bank_name** | **str** | Gate beneficiary bank name, shown for BUY only | [optional] 
**gate_bank_country** | **str** | Gate beneficiary bank country, shown for BUY only | [optional] 
**gate_bank_address** | **str** | Gate beneficiary bank address, shown for BUY only | [optional] 
**gate_bank_account_number_iban** | **str** | Gate beneficiary bank account number/IBAN, shown for BUY only | [optional] 
**gate_swift_code** | **str** | Gate beneficiary bank SWIFT code, shown for BUY only | [optional] 
**gate_intermediary_bank_name** | **str** | Gate beneficiary intermediary bank name, shown for BUY only | [optional] 
**gate_intermediary_bank_swift_code** | **str** | Gate beneficiary intermediary bank SWIFT code, shown for BUY only | [optional] 
**gate_transfer_remark** | **str** | Transfer remark (mutually exclusive with &#x60;gate_reference_code&#x60;; empty when a BUY deposit order has a reference code), shown for BUY only | [optional] 
**gate_reference_code** | **str** | Be sure to include the reference code when making the transfer so that your order can be processed promptly. (Mutually exclusive with &#x60;gate_transfer_remark&#x60;.) | [optional] 
**status** | **str** | Status | 
**create_time** | **str** | Created time | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


