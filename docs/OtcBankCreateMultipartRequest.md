# OtcBankCreateMultipartRequest

Inner create-bank-card `multipart/form-data`. Use the form field `documentation_file` to upload the account-opening proof.
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
**documentation_file** | **str** | Account opening proof file content (multipart file field, binary/Base64; jpg/jpeg/png/pdf, etc.; maximum 10 MB per file, subject to the live environment) | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


