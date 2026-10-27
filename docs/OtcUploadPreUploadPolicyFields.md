# OtcUploadPreUploadPolicyFields

S3 POST Policy signature fields; send unchanged as form-data during direct upload
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Plaintext temporary object path, identical to base64_decode(file_key) | 
**content_type** | **str** | Must match the decoded content_type from the pre-upload request | 
**x_amz_credential** | **str** | AWS temporary credential and scope; submit them unchanged during direct upload | 
**x_amz_algorithm** | **str** | AWS signing algorithm; submit it unchanged during direct upload | 
**x_amz_date** | **str** | AWS signing timestamp; submit it unchanged during direct upload | 
**policy** | **str** | Base64-encoded S3 POST Policy; submit it unchanged during direct upload | 
**x_amz_signature** | **str** | S3 POST Policy signature; submit it unchanged during direct upload | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


