# AIHubPortfolioStopRequest

Single owner-scoped stop. Existing six-type ID/type requests retain default exits. smart_position requires explicit mode, limit requires options; futures_combo uses fixed whole-portfolio close/settlement.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**strategy_id** | **str** |  | 
**strategy_type** | [**StrategyType**](StrategyType.md) |  | 
**stop_mode** | **str** | Required only for smart_position. Other types reject custom exit options. | [optional] 
**stop_options** | [**AIHubRebalanceStopOptions**](AIHubRebalanceStopOptions.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


