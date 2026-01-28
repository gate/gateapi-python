# InlineObject8

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**crypto_currency** | **str** | Cryptocurrency | 
**fiat_currency** | **str** | Fiat currency | 
**select_type** | **str** | Buy/Sell (sell&#x3D;Sell, buy&#x3D;Buy, others&#x3D;All) | [optional] 
**status** | **str** | 订单状态（dispute: 申诉订单； closed: ACCEPT、BCLOSED； cancel： CANCEL、BECANCEL、SCLOSED、SCANCEL； locked: LOCKED； open: OPEN； paid： PAID； completed： CANCEL、BECANCEL、SCLOSED、SCANCEL、ACCEPT、BCLOSED） | [optional] 
**txid** | **int** | Order ID | [optional] 
**start_time** | **int** | Start timestamp, default is 00:00 89 days ago | [optional] 
**end_time** | **int** | End timestamp, default is 23:59:59 today | [optional] 
**query_dispute** | **int** | 1: Include appeal status, 0: None | [optional] 
**page** | **int** | page number | [optional] 
**per_page** | **int** | Number of orders per page | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


