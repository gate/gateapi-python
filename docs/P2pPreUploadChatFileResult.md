# P2pPreUploadChatFileResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | S3 POST upload URL. Use it before the credentials expire. | [optional] 
**fields** | **dict(str, str)** | Signed S3 form fields. Submit all keys and values unchanged when uploading. | [optional] 
**file_key** | **str** | Chat file identifier. After uploading, use it as message in [send_chat_message](#send-text-message) with type&#x3D;1. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


