# CrossexTransferRecord

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Order ID | 
**text** | **str** | Client Custom ID | 
**from_account_type** | **str** | &#x60;from&#x60; credit account touched by this operation (&#x60;CROSSEX_BINANCE&#x60;, &#x60;CROSSEX_OKX&#x60;, &#x60;CROSSEX_GATE&#x60;, &#x60;CROSSEX_BYBIT&#x60;, &#x60;CROSSEX_KRAKEN&#x60;, &#x60;CROSSEX_HYPERLIQUID&#x60;, &#x60;CROSSEX&#x60;, &#x60;SPOT&#x60;). | 
**to_account_type** | **str** | &#x60;to&#x60; debit account handled by this operation (&#x60;CROSSEX_BINANCE&#x60;, &#x60;CROSSEX_OKX&#x60;, &#x60;CROSSEX_GATE&#x60;, &#x60;CROSSEX_BYBIT&#x60;, &#x60;CROSSEX_KRAKEN&#x60;, &#x60;CROSSEX_HYPERLIQUID&#x60;, &#x60;CROSSEX&#x60;, &#x60;SPOT&#x60;). | 
**coin** | **str** | Currency | 
**amount** | **str** | Transfer amount, the amount requested for the transfer | 
**actual_receive** | **str** | Actual credited amount (has a value when status &#x3D; SUCCESS; empty for other statuses) | [optional] 
**status** | **str** | Transfer Status - &#x60;FAIL&#x60;: Failed - &#x60;SUCCESS&#x60;: Successful - &#x60;PENDING&#x60;: Transfer in Progress | 
**fail_reason** | **str** | Failure reason (has a value when status &#x3D; FAIL; empty for other statuses) | [optional] 
**create_time** | **int** | Creation time of order | 
**update_time** | **int** | OrderUpdateTime | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


