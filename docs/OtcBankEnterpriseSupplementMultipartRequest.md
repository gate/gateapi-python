# OtcBankEnterpriseSupplementMultipartRequest

Enterprise supplement `multipart/form-data`. File field names: `certificate`, `share_holders`, `passport`, `share_holding_structure`; optional `funds_statement`, `additional`. Optional string field `relationship_proof` (JSON) is merged into the request.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uid** | **str** |  | [optional] 
**bank_id** | **str** |  | 
**certificate** | **str** | Business license / registration certificate file content (multipart file field, binary/Base64) | [optional] 
**share_holders** | **str** | Register of shareholders file content (multipart file field, binary/Base64) | [optional] 
**passport** | **str** | Legal representative / shareholder passport file content (multipart file field, binary/Base64) | [optional] 
**share_holding_structure** | **str** | Ownership structure chart file content (multipart file field, binary/Base64) | [optional] 
**funds_statement** | **str** | Proof-of-funds file content (multipart file field, binary/Base64, optional) | [optional] 
**additional** | **str** | Other supplementary material file content (multipart file field, binary/Base64, optional) | [optional] 
**relationship_proof** | **str** | Optional. JSON string of relationship_proof. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


