# CreateTrailOrder

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contract** | **str** | Contract name | 
**amount** | **str** | Trading quantity in contracts, positive for buy, negative for sell | 
**activation_price** | **str** | Activation price, 0 means trigger immediately | [optional] [default to '0']
**is_gte** | **bool** | true: activate when market price &gt;&#x3D; activation price, false: &lt;&#x3D; activation price | [optional] 
**price_type** | **int** | Activation price type: 1-latest price, 2-index price, 3-mark price | [optional] 
**price_offset** | **str** | Callback ratio or price distance, e.g., &#x60;0.1&#x60; or &#x60;0.1%&#x60; | [optional] 
**reduce_only** | **bool** | Whether reduce only | [optional] [default to False]
**position_related** | **bool** | Whether bound to a position (if position_related &#x3D; true (position-related), then reduce_only must also be true) | [optional] [default to False]
**text** | **str** | 订单自定义信息，可选字段。用于标识订单来源或设置用户自定义 ID。  **如果非空**，必须满足以下规则之一：  **1. 内部保留字段（标识订单来源）**： - &#x60;apiv4&#x60;: API 调用 **2. 用户自定义字段（设置自定义 ID）**： - 必须以 &#x60;t-&#x60; 开头 - &#x60;t-&#x60; 后面的内容长度不能超过 28 字节 - 只能包含：数字、字母、下划线(_)、中划线(-) 或者点(.) - 示例：&#x60;t-my-order-001&#x60;、&#x60;t-trail_2024.01&#x60;  **注意**：用户自定义字段不能与内部保留字段冲突。 | [optional] [default to 'apiv4']
**pos_margin_mode** | **str** | Position margin mode: isolated/cross | [optional] 
**position_mode** | **str** | Position mode: single, dual, and dual_plus | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


