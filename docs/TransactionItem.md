# TransactionItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | **str** | Asset | [optional] 
**symbol** | **str** | Symbol | [optional] 
**symbol_display** | **str** | Symbol display name | [optional] 
**type** | **str** | Transaction type. - deposit: Funds transfer in. - withdraw: Funds transfer out. - fee: Trading fee. - dividend: Dividend payout. - sell: Stock sale credit. - buy: Stock purchase debit. - award: Airdrop reward. - stock_transfer_in: Stock transfer in. - stock_transfer_out: Stock transfer out. | [optional] 
**type_desc** | **str** | Transaction type description | [optional] 
**change** | **str** | Change amount | [optional] 
**balance** | **str** | Balance after change | [optional] 
**ref_id** | **str** | Business idempotent ID | [optional] 
**time** | **int** | Unix timestamp (seconds) | [optional] 
**unit_text** | **str** | Unit display text | [optional] 
**detail** | **dict(str, object)** | Business details | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


