# ListUserCouponsResponseData

Returned when code=0; empty object {} otherwise
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_page** | **bool** | Whether there is a next page. &#x60;true&#x60; means more data is available. Pass the &#x60;id&#x60; of the last record as &#x60;last_id&#x60; and &#x60;expire_time_order_by&#x60; as &#x60;expire_time&#x60; in the next request | [optional] 
**list** | [**list[ListUserCouponsResponseDataList]**](ListUserCouponsResponseDataList.md) | Coupon object array, see field details below | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


