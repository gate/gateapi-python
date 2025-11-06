# DepositRecord

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Record ID | [optional] [readonly] 
**txid** | **str** | Hash record of the withdrawal | [optional] [readonly] 
**timestamp** | **str** | Operation time | [optional] [readonly] 
**amount** | **str** | Token amount | 
**currency** | **str** | Currency name | 
**address** | **str** | Withdrawal address. Required for withdrawals | [optional] 
**memo** | **str** | Additional remarks with regards to the withdrawal | [optional] 
**status** | **str** | Transaction Status  - BLOCKED: Deposit Blocked - DEP_CREDITED: Deposit Credited, Withdrawal Pending Unlock - DONE: Funds Credited to Spot Account - INVALID: Invalid Transaction - MANUAL: Manual Review Required - PEND: Processing - REVIEW: Under Compliance Review - TRACK: Tracking Block Confirmations, Pending Spot Account Credit | [optional] [readonly] 
**chain** | **str** | Name of the chain used in withdrawals | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


