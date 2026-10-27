# P2pChatMessagePayload

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Order status when sending a message. Typical values: &#x60;OPEN&#x60;, &#x60;PAID&#x60;, &#x60;LOCKED&#x60;, &#x60;ACCEPT&#x60;, &#x60;BCLOSED&#x60;, &#x60;CANCEL&#x60;, &#x60;BECANCEL&#x60;, &#x60;SCLOSED&#x60;, &#x60;SCANCEL&#x60;. | [optional] 
**text** | **str** | Message content | [optional] 
**payment_voucher** | **list[str]** | Payment voucher | [optional] 
**reason_id** | **int** | Cancel reason ID. &#x60;1&#x60; no longer want to buy; &#x60;2&#x60; cannot reach seller; &#x60;3&#x60; will not pay; &#x60;4&#x60; seller account not real; &#x60;5&#x60; payout account issue; &#x60;6&#x60; price mismatch; &#x60;7&#x60; mutually agreed cancel; &#x60;8&#x60; poor communication; &#x60;9&#x60; other; &#x60;10&#x60; seller cannot release with refund; &#x60;11&#x60; terms not met; &#x60;12&#x60; seller payout risk-controlled. | [optional] 
**toast_id** | **int** | Cancellation reason popup | [optional] 
**reason_memo** | **str** | Cancel reason description. | [optional] 
**cancel_time** | **int** | Cancellation time | [optional] 
**seller_confirm** | **int** | Seller confirmation of cancel reason: &#x60;0&#x60; pending; &#x60;1&#x60; confirmed; &#x60;2&#x60; rejected. | [optional] 
**id** | **str** | Payment method information ID | [optional] 
**account_des** | **str** | Payment method description | [optional] 
**pay_type** | **str** | Payment method type | [optional] 
**file** | **str** | Payment method file link | [optional] 
**file_key** | **str** | Payment method file key | [optional] 
**account** | **str** | Payment account or masked payment account. | [optional] 
**memo** | **str** | Payment method note | [optional] 
**code** | **str** | Payment method code | [optional] 
**memo_ext** | **str** | Payment method additional note | [optional] 
**trade_tips** | **str** | Payment method tip | [optional] 
**real_name** | **str** | Payment method username | [optional] 
**is_delete** | **int** | Whether the payment method was deleted. &#x60;1&#x60;: deleted; &#x60;0&#x60;: not deleted. | [optional] 
**pay_name** | **str** | Payment method full name | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


