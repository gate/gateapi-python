# AIHubRecommendation

A single piece of strategy recommendation information.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recommendation_id** | **str** |  | 
**market** | **str** |  | 
**strategy_type** | [**StrategyType**](StrategyType.md) |  | 
**strategy_name** | **str** |  | 
**backtest_apr** | **str** |  | [optional] 
**max_drawdown** | **str** |  | [optional] 
**summary** | **str** |  | 
**strategy_params_preview** | **str** | Recommended-parameter preview as JSON text (string-encoded so clients deserialize it consistently). The value is a serialized JSON object whose structure varies by strategy type; callers or upper-layer models must parse it. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


