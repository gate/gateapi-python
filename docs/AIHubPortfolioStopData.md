# AIHubPortfolioStopData

The result information returned after the termination strategy is successful.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**strategy_id** | **str** |  | [optional] 
**strategy_type** | [**StrategyType**](StrategyType.md) |  | [optional] 
**status** | **str** | Observed product lifecycle state, or unknown. Creation acceptance/starting is not running; stopping/finished alone does not prove funds settled. | [optional] 
**result_message** | **str** |  | [optional] 
**operation_status** | **str** | pending when the write result requires verification; rejected for a proven pre-effect refusal. | [optional] 
**recovery_required** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


