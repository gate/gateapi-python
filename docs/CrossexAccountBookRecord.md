# CrossexAccountBookRecord

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Account Change Record ID | 
**user_id** | **str** | User ID | 
**business_id** | **str** | Business ID | 
**statement_type** | **str** | Bill entry type | &#x60;TRANSACTION&#x60; trade &#x60;TRADING_FEE&#x60; fee &#x60;FUNDING_FEE&#x60; funding &#x60;LIQUIDATION_FEE&#x60; liquidation &#x60;TRANSFER_IN&#x60; deposit &#x60;TRANSFER_OUT&#x60; withdrawal &#x60;BANKRUPT_COMPENSATION&#x60; bankruptcy subsidy &#x60;AUTO_REPAY&#x60; margin auto-repay | 
**exchange_type** | **str** | Exchange | 
**coin** | **str** | Currency | 
**change** | **str** | Change amount (positive indicates transfer in; negative indicates transfer out) | 
**balance** | **str** | Balance after change | 
**create_time** | **str** | Created time | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


