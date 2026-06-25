# OtcMarkOrderPaidRequest

Request body for marking a fiat order as paid (deposit confirmation). Must include the user's payment receipt (consistent with §3.2).  **`payment_receipt_file_key` is required**; the order primary key for this path is `order_id`. When accessed via the Pay gateway using `client_order_id`, the gateway's rewritten field prevails.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** | Order ID | 
**client_order_id** | **str** | Client order ID (used by some gateway/Inner Pay paths, optional) | [optional] 
**payment_receipt_file_key** | **str** | User payment receipt: **required**. Stored as a file_key. Single file; jpg/jpeg/png/pdf; ≤4MB. | 
**payment_receipt** | **str** | Alias compatible with &#x60;payment_receipt_file_key&#x60; (depends on the gateway&#39;s external field name) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


