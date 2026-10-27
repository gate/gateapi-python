# P2pChatListResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**messages** | [**list[P2pChatMessage]**](P2pChatMessage.md) | Message List | [optional] 
**memo** | **str** | Payment tip (displayed on homepage only) | [optional] 
**has_history** | **bool** | Whether historical records exist | [optional] 
**txid** | **int** | Order ID | [optional] 
**srvtm** | **int** | Timestamp of the latest message. | [optional] 
**order_status** | **str** | Raw order status in DB; typical values: &#x60;OPEN&#x60;, &#x60;PAID&#x60;, &#x60;LOCKED&#x60;, &#x60;ACCEPT&#x60;, &#x60;BCLOSED&#x60;, &#x60;CANCEL&#x60;, &#x60;BECANCEL&#x60;, &#x60;SCLOSED&#x60;, &#x60;SCANCEL&#x60;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


