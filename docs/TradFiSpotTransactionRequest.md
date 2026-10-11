# TradFiSpotTransactionRequest

Fund transfer request parameters. Transfer in means moving funds from the spot account to the stock account; transfer out means moving funds from the stock account to the spot account.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | **str** | Asset, USDT only | 
**change** | **str** | Change amount, must be greater than 0 | 
**type** | **str** | Transaction type. deposit transfers funds from the spot account to the stock account; withdraw transfers funds from the stock account to the spot account. | 
**ref_id** | **str** | Business idempotent ID | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


