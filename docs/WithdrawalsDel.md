# WithdrawalsDel

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
**block_number** | **str** | Block Number | [optional] [readonly] 
**status** | **str** | Transaction Status  - BCODE: Deposit Code Operation - CANCEL: Cancelled - CANCELPEND: Withdrawal Cancellation Pending - DMOVE: Pending Manual Review - DONE: Completed (Only considered truly on-chain when block_number &gt; 0) - EXTPEND: Sent and Waiting for Confirmation - FAIL: On-Chain Failure Pending Confirmation - FVERIFY: Facial Verification in Progress - LOCKED: Wallet-Side Order Locked - MANUAL: Pending Manual Review - REJECT: Rejected - REQUEST: Request in Progress - REVIEW: Under Review  | [optional] [readonly] 
**chain** | **str** | Name of the chain used in withdrawals | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


