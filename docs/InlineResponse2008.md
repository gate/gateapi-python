# InlineResponse2008

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | Response code. &#x60;0&#x60; &#x3D; success; &#x60;2002&#x60; &#x3D; user not logged in; &#x60;50105&#x60; &#x3D; parameter validation failed; &#x60;10001&#x60; &#x3D; coupon record does not exist or does not belong to current user; &#x60;10000&#x60; &#x3D; invalid parameter (e.g., task coupon missing coupon_info) | [optional] 
**label** | **str** | Error identifier code. Empty string on success, machine-readable error label on error | [optional] 
**message** | **str** |  | [optional] 
**data** | [**InlineResponse2008Data**](InlineResponse2008Data.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


