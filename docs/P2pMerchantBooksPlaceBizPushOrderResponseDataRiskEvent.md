# P2pMerchantBooksPlaceBizPushOrderResponseDataRiskEvent

Risk control prompt event for advertisement content
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Prompt display type | [optional] 
**title** | **str** | Risk control prompt title | [optional] 
**msg** | **str** | Risk control prompt message generated based on the field that hit risk control | [optional] 
**action** | [**list[P2pMerchantBooksPlaceBizPushOrderResponseDataRiskEventAction]**](P2pMerchantBooksPlaceBizPushOrderResponseDataRiskEventAction.md) | Available actions; advertisement content risk control only returns the close action | [optional] 
**content_risk_type** | **str** | Advertisement content field that hit risk control | [optional] 
**trade_tips** | **str** | Prompt message returned when the trade terms hit risk control | [optional] 
**auto_reply** | **str** | Prompt message returned when the auto reply hits risk control | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


