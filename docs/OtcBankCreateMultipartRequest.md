# OtcBankCreateMultipartRequest

Inner create-bank-card `multipart/form-data`. Account-opening proof file (choose one):  - **Pre-upload**: `documentation_file_key` + `file_type` (call `POST /otc/upload/pre_upload` first, `scene=bank`); - **Multipart direct upload**: `documentation_file` file field.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bank_account_name** | **str** |  | 
**bank_name** | **str** |  | 
**bank_country** | **str** |  | 
**bank_address** | **str** |  | 
**iban** | **str** |  | 
**swift** | **str** |  | 
**remittance_line_number** | **str** |  | [optional] 
**agent_bank_name** | **str** |  | [optional] 
**agent_bank_swift** | **str** |  | [optional] 
**documentation_file** | **str** | Multipart direct upload; mutually exclusive with documentation_file_key | [optional] 
**documentation_file_key** | **str** | Pre-upload mode; file_key returned by pre_upload (plaintext or base64 accepted) | [optional] 
**file_type** | **str** | Required when using documentation_file_key; plaintext MIME or its base64 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


