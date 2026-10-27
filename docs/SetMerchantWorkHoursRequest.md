# SetMerchantWorkHoursRequest

Request to set merchant working status or custom working hours
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**work_status** | **int** | Working status. 0: resting, 1: working, 2: using custom working hours | 
**cycle_type** | **str** | Custom working cycle; required when work_status is 2 | [optional] 
**day_of_week** | **str** | Weekly working days, comma-separated values 1-7 for Monday to Sunday; required when work_status is 2 and cycle_type is Weekly | [optional] 
**time_zone** | **str** | UTC timezone offset, ranging from -12 to +14; required when work_status is 2 | [optional] 
**start_time** | **str** | Custom working start time in HH:mm format; required when work_status is 2 and must not be later than end_time | [optional] 
**end_time** | **str** | Custom working end time in HH:mm format; required when work_status is 2 and must not be earlier than start_time | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


