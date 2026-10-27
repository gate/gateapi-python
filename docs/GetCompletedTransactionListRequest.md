# GetCompletedTransactionListRequest

Get completed/historical transaction list request
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**crypto_currency** | **str** | Cryptocurrency symbol. | 
**fiat_currency** | **str** | Fiat currency | 
**select_type** | **str** | Order side filter: &#x60;buy&#x60; buy orders; &#x60;sell&#x60; sell orders; empty: all. | [optional] 
**status** | **str** | Order status filter. &#x60;closed&#x60;: filled (&#x60;ACCEPT&#x60;, &#x60;BCLOSED&#x60;); &#x60;cancel&#x60;: canceled (&#x60;CANCEL&#x60;, &#x60;BECANCEL&#x60;, &#x60;SCLOSED&#x60;, &#x60;SCANCEL&#x60;); &#x60;locked&#x60;: locked (&#x60;LOCKED&#x60;); &#x60;open&#x60;: unpaid (&#x60;OPEN&#x60;); &#x60;paid&#x60;: paid (&#x60;PAID&#x60;); &#x60;completed&#x60;: finished or canceled (&#x60;CANCEL&#x60;, &#x60;BECANCEL&#x60;, &#x60;SCLOSED&#x60;, &#x60;SCANCEL&#x60;, &#x60;ACCEPT&#x60;, &#x60;BCLOSED&#x60;); Empty or omitted uses the endpoint default range. | [optional] 
**txid** | **int** | Order ID | [optional] 
**start_time** | **int** | Start timestamp, default is 00:00 89 days ago | [optional] 
**end_time** | **int** | End timestamp, default is 23:59:59 today | [optional] 
**query_dispute** | **int** | Whether to flag dispute status in the response. &#x60;1&#x60;: yes; &#x60;0&#x60;: no. | [optional] 
**page** | **int** | Page number starting at 1; values below 1 are treated as 1. | [optional] 
**per_page** | **int** | Orders per page; default 10, max 200. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


