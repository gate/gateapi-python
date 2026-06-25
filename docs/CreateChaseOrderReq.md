# CreateChaseOrderReq

Request body for creating a chase order
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contract** | **str** | Contract name; server-side converted to uppercase | 
**settle** | **str** | Settle currency, overridden by the path parameter and converted to lowercase | [optional] 
**amount** | **str** | Total order size in contracts, decimal string. Positive for buy, negative for sell. Cannot be 0 | 
**price_limit** | **str** | 最高追逐价，合法十进制字符串；未设置限价时请传 \&quot;0\&quot; | 
**offset_limit** | **str** | Maximum chasing distance from the best price, mutually exclusive with price_limit | [optional] 
**reduce_only** | **bool** | Whether reduce only | [optional] 
**text** | **str** | Optional custom tag | [optional] 
**is_dual_mode** | **bool** | Whether dual-position mode is enabled | [optional] 
**price_type** | **int** | Price type: 1 best bid/ask, 2 distance from best bid/ask | [optional] 
**price_gap_type** | **int** | Used when price_type &#x3D;&#x3D; 2: 1 absolute price gap, 2 percentage | [optional] 
**price_gap_value** | **str** | Price gap value paired with price_gap_type | [optional] 
**pos_margin_mode** | **str** | Position margin mode, e.g. isolated or cross | [optional] 
**position_mode** | **str** | Position mode (e.g. single, dual, dual_plus) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


