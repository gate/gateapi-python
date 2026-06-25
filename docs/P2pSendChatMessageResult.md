# P2pSendChatMessageResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**srvtm** | **int** | Timestamp when message was successfully sent (current timestamp) | [optional] 
**txid** | **int** | Order ID | [optional] 
**conversation_id** | **str** | Chat ID, formatted as both parties&#39; UIDs concatenated in ascending order | [optional] 
**msg_type** | **int** | Message content type when risk control is hit. 0: text | [optional] 
**risk_type** | **int** | Risk control display type. 1: off-platform traffic diversion risk; returned only when risk control is hit | [optional] 
**toast_msg** | **str** | Risk control prompt message; returned only when risk_type&#x3D;1 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


