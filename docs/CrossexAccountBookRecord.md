# CrossexAccountBookRecord

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Account Change Record ID | 
**user_id** | **str** | User ID | 
**business_id** | **str** | Business ID. Its meaning varies by &#x60;statement_type&#x60;. TRANSACTION: order ID TRADING_FEE: order ID LIQUIDATION_FEE: liquidation order ID FUNDING_FEE: position ID and funding fee settlement time For other types, it is a system-generated processing ID with no business meaning | 
**statement_type** | **str** | Account book transaction type &#x60;TRANSACTION&#x60;: Trade &#x60;TRADING_FEE&#x60;: Trading fee &#x60;FUNDING_FEE&#x60;: Futures funding fee &#x60;LIQUIDATION_FEE&#x60;: Liquidation fee &#x60;TRANSFER_IN&#x60;: Incoming transfer &#x60;TRANSFER_OUT&#x60;: Outgoing transfer &#x60;BANKRUPT_COMPENSATION&#x60;: Bankruptcy compensation &#x60;AUTO_REPAY&#x60;: Automatic margin liability repayment &#x60;INTEREST_ISOLATED&#x60;: Interest transaction &#x60;ACCOUNT_MODE_CHANGE&#x60;: Funds movement on account mode change &#x60;KRAKEN_CONVERSION&#x60;: Conversion of other collateral currencies to cover a negative KRAKEN_USD balance &#x60;SECURITY_DIVIDEND&#x60;: Stock or ETF dividend payout &#x60;SECURITY_CORPORATE_ACTION&#x60;: Stock or ETF split or reverse split &#x60;OTHER&#x60;: Other | 
**exchange_type** | **str** | Exchange | 
**coin** | **str** | Currency | 
**symbol** | **str** | Trading Pair | [optional] 
**change** | **str** | Change amount (positive values indicate an increase; negative values indicate a decrease) | 
**balance** | **str** | Balance after change | 
**create_time** | **str** | Created time | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


