# P2pChatMessage

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_sell** | **int** | Whether the current user is the seller. &#x60;1&#x60;: yes; &#x60;0&#x60;: no. | [optional] 
**msg_type** | **int** | Message type: &#x60;0&#x60; text; &#x60;1&#x60; file; &#x60;2&#x60; template; &#x60;3&#x60; order-share; &#x60;4&#x60; payment-share; &#x60;5&#x60; status update. | [optional] 
**msg** | **str** | Message content; for file messages, usually URL or file key. | [optional] 
**username** | **str** | Message sender username | [optional] 
**timest** | **int** | Message timestamp | [optional] 
**msg_obj** | [**P2pChatMessagePayload**](P2pChatMessagePayload.md) |  | [optional] 
**uid** | **str** | Sender&#39;s crypto UID; system messages may use &#x60;System&#x60; or an empty string. | [optional] 
**type** | **int** | Display type: &#x60;1&#x60; file message; &#x60;2&#x60; system message. | [optional] 
**pic** | **str** | File link | [optional] 
**file_key** | **str** | File key | [optional] 
**file_type** | **str** | File type: &#x60;image&#x60; for images, &#x60;video&#x60; for videos. | [optional] 
**risk_type** | **int** | Risk control display type. 1: off-platform traffic diversion risk; returned when a text message hits risk control | [optional] 
**toast_msg** | **str** | Risk control prompt message; returned only when risk_type&#x3D;1 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


