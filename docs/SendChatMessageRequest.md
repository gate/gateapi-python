# SendChatMessageRequest

Send chat message request
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**txid** | **int** | Order ID | 
**type** | **int** | Message type: 0 for text, 1 for files. Defaults to 0 when omitted. | [optional] 
**message** | **str** | Message content. For type&#x3D;0, provide text up to 500 characters. Off-platform solicitation risk checks may return risk_type&#x3D;1 and toast_msg. For type&#x3D;1, after a successful S3 upload, provide the file_key returned by pre_upload_chat_file. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


