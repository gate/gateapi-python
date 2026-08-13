# SpotPovOrderCreator

Spot POV order creation request
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency_pair** | **str** | Currency pair | 
**side** | **str** | Buy or sell order | 
**amount** | **str** | Trade amount | 
**participation_rate** | **int** | Target participation rate as a percentage. Valid values: 5, 10, 20, and 40 | 
**ttl** | **str** | Time to live. Valid values: 1h, 6h, 12h, 1d, 2d, 3d, 4d, 5d, 6d, and 7d | 
**limit_price** | **str** | Limit price. If omitted, the market price is used | [optional] 
**trigger_price** | **str** | Trigger price. If omitted, the order is triggered immediately | [optional] 
**text** | **str** | Order custom information. Users can set custom ID with this field. Custom fields must meet the following conditions:  1. Must start with &#x60;t-&#x60; 2. Excluding &#x60;t-&#x60;, length cannot exceed 28 bytes 3. Can only contain numbers, letters, underscore(_), hyphen(-) or dot(.)  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


