# CrossexIsolatedMarginRequest

Request body for increasing or decreasing isolated margin
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **str** | Hyperliquid futures trading pair | 
**margin** | **str** | Margin adjustment amount. Positive values increase margin, while negative values decrease margin. Values with more than two decimal places are truncated to two decimal places | 
**position_side** | **str** | Position side (NONE/LONG/SHORT). Defaults to NONE for one-way positions if omitted | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


