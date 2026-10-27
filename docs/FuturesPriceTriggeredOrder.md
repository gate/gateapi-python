# FuturesPriceTriggeredOrder

Futures price-triggered order details
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**initial** | [**FuturesInitialOrder**](FuturesInitialOrder.md) |  | 
**trigger** | [**FuturesPriceTrigger**](FuturesPriceTrigger.md) |  | 
**id** | **int** | Auto order ID | [optional] [readonly] 
**id_string** | **str** | String form of the auto order ID; the same order as numeric &#x60;id&#x60;, as the decimal string of &#x60;id&#x60; to avoid int64 precision loss in JavaScript and similar environments. Prefer this field to display the order ID or when a string unique identifier is needed; one-to-one with &#x60;id&#x60;. Same meaning as the field of the same name in futures price-trigger REST APIs and in &#x60;futures.orders&#x60; / &#x60;futures.autoorders&#x60; WebSocket pushes. | [optional] [readonly] 
**user** | **int** | User ID | [optional] [readonly] 
**create_time** | **float** | Created time | [optional] [readonly] 
**finish_time** | **float** | End time | [optional] [readonly] 
**trade_id** | **int** | ID of the order created after trigger | [optional] [readonly] 
**status** | **str** | Order status  - &#x60;open&#x60;: Active - &#x60;finished&#x60;: Finished - &#x60;inactive&#x60;: Inactive, only applies to order take-profit/stop-loss - &#x60;invalid&#x60;: Invalid, only applies to order take-profit/stop-loss | [optional] [readonly] 
**finish_as** | **str** | Finish status: cancelled - Cancelled; succeeded - Succeeded; failed - Failed; expired - Expired | [optional] [readonly] 
**reason** | **str** | Additional description of how the order was completed | [optional] [readonly] 
**order_type** | **str** | Types of take-profit and stop-loss orders, including:  - &#x60;close-long-order&#x60;: Order take-profit/stop-loss, close long position - &#x60;close-short-order&#x60;: Order take-profit/stop-loss, close short position - &#x60;close-long-position&#x60;: Position take-profit/stop-loss, used to close all long positions - &#x60;close-short-position&#x60;: Position take-profit/stop-loss, used to close all short positions - &#x60;plan-close-long-position&#x60;: Position plan take-profit/stop-loss, used to close all or partial long positions - &#x60;plan-close-short-position&#x60;: Position plan take-profit/stop-loss, used to close all or partial short positions  The two types of order take-profit/stop-loss are read-only and cannot be passed in requests | [optional] 
**me_order_id** | **int** | Corresponding order ID for order take-profit/stop-loss orders | [optional] [readonly] 
**pos_margin_mode** | **str** | Position margin mode: &#x60;isolated&#x60; (isolated margin) or &#x60;cross&#x60; (cross margin). Returned by the server in simple split-position mode; when writing, use only the values below. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


