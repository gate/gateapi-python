# InlineObject7

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**crypto_currency** | **str** | Cryptocurrency | 
**fiat_currency** | **str** | Fiat currency | 
**order_tab** | **str** | 订单标签页，默认pending（pending：处理中（pending:  AND status in (&#39;OPEN&#39;, &#39;PAID&#39;, &#39;LOCKED&#39;, &#39;TEMP&#39;)）；dispute：申诉中（status in (&#39;ACCEPT&#39;, &#39;BCLOSED&#39;, &#39;CANCEL&#39;, &#39;BECANCEL&#39;, &#39;SCLOSED&#39;, &#39;SCANCEL&#39;))) | [optional] 
**select_type** | **str** | Buy/Sell (sell&#x3D;Sell, buy&#x3D;Buy, others&#x3D;All) | [optional] 
**status** | **str** | Order Status (dispute: Disputed Order; closed: ACCEPT, BCLOSED; cancel: CANCEL, BECANCEL, SCLOSED, SCANCEL; locked: LOCKED; open: OPEN; paid: PAID; completed: CANCEL, BECANCEL, SCLOSED, SCANCEL, ACCEPT, BCLOSED) | [optional] 
**txid** | **int** | Order ID | [optional] 
**start_time** | **int** | Start timestamp, default is 00:00 89 days ago | [optional] 
**end_time** | **int** | End timestamp, default is 23:59:59 today | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


