# OtcUploadPreUploadData

Pre-upload credentials and S3 direct-upload parameters
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_key** | **str** | Base64 temporary object path; pass back **unchanged** on business submit—do not decode | 
**url** | **str** | S3 direct upload URL | 
**fields** | [**OtcUploadPreUploadPolicyFields**](OtcUploadPreUploadPolicyFields.md) |  | 
**expires_in** | **int** | Policy validity period in seconds; currently 5400 (90 minutes); aligns with &#x60;expiration&#x60; in &#x60;fields.Policy&#x60;; call this endpoint again after expiry | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


