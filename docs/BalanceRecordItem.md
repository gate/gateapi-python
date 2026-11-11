# BalanceRecordItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Balance record primary key ID | [optional] 
**user_id** | **int** | User ID | [optional] 
**change** | **str** | Cash amount change. Positive values are credits; negative values are debits. | [optional] 
**balance** | **str** | Cash balance snapshot after the change | [optional] 
**stock_change** | **str** | Stock quantity change, parsed from detail.amount for stock quantity records; may be an empty string for other records | [optional] 
**type** | **str** | Raw record type. Common values include: - deposit: Funds transferred in. - withdraw: Funds transferred out. - fee: Trading fee. - dividend: Dividend payment. - sell: Proceeds from selling stocks. - buy: Payment for buying stocks. - award: Airdrop reward. - stock_transfer_in: Stocks transferred in. - stock_transfer_out: Stocks transferred out. | [optional] 
**business** | **str** | Business identifier | [optional] 
**business_id** | **int** | Related business ID | [optional] 
**symbol** | **str** | Symbol | [optional] 
**detail** | **str** | Raw business details as a JSON string; returned only when include_detail&#x3D;true is requested | [optional] 
**version** | **int** | Record version | [optional] 
**time_create** | **int** | Business event time (Unix timestamp in seconds) | [optional] 
**create_time** | **int** | Record creation time (Unix timestamp in seconds) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


