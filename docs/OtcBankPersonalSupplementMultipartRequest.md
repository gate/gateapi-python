# OtcBankPersonalSupplementMultipartRequest

Personal supplement `multipart/form-data`. File field names are fixed: `id_document_front`, `id_document_back`, `address_proof` (aligned with the checklist `code`); the optional string field `relationship_proof` (JSON text) is merged with the upload result.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bank_id** | **str** |  | 
**id_document_front** | **str** | ID document front-side file content (multipart file field, binary/Base64) | [optional] 
**id_document_back** | **str** | ID document back-side file content (multipart file field, binary/Base64) | [optional] 
**address_proof** | **str** | Proof-of-address file content (multipart file field, binary/Base64) | [optional] 
**relationship_proof** | **str** | Optional. JSON string of relationship_proof. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


