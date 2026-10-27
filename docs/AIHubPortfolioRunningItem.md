# AIHubPortfolioRunningItem

A single record in the list of running policies.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**strategy_id** | **str** |  | 
**strategy_type** | [**StrategyType**](StrategyType.md) |  | 
**strategy_name** | **str** |  | 
**market** | **str** | Single market, or empty string for a portfolio; use assets/markets for the latter. | 
**status** | **str** |  | 
**pnl** | **str** |  | [optional] 
**pnl_rate** | **str** |  | [optional] 
**invest_amount** | **str** |  | [optional] 
**created_at** | **str** | Created time | [optional] 
**assets** | **list[str]** |  | [optional] 
**markets** | **list[str]** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


