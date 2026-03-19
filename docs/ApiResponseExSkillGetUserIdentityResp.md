# ApiResponseExSkillGetUserIdentityResp

Get user identity response
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | Business error code: 0 &#x3D; success, 1001 &#x3D; existing user, 1002 &#x3D; risk-controlled user, 1003 &#x3D; sub-account, 1004 &#x3D; agent, 1005 &#x3D; market maker, 1006 &#x3D; enterprise account, 1008 &#x3D; not logged in | [optional] 
**label** | **str** | Error identifier code. Empty string on success, machine-readable error label on error | [optional] 
**message** | **str** | Error description | [optional] 
**data** | [**object**](.md) | Empty object {} on success, null on failure | [optional] 
**timestamp** | **int** | Server timestamp (milliseconds) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


