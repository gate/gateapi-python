# AIHubPortfolioDetailData

策略详情数据。
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**strategy_id** | **str** |  | 
**strategy_type** | [**StrategyType**](StrategyType.md) |  | 
**market** | **str** |  | 
**status** | **str** |  | 
**base_info** | **dict(str, object)** | 基础信息，字段按策略类型动态变化 | 
**metrics** | **dict(str, object)** | 指标信息，字段按策略类型动态变化 | 
**position** | **dict(str, object)** | 仓位或持仓信息，字段按策略类型动态变化 | [optional] 
**stop_supported** | **bool** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


