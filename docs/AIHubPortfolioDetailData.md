# AIHubPortfolioDetailData

Policy details data.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**strategy_id** | **str** |  | 
**strategy_type** | [**StrategyType**](StrategyType.md) |  | 
**market** | **str** | Single market, or empty string for a portfolio; use assets/markets for the latter. | 
**status** | **str** |  | 
**base_info** | [**AIHubPortfolioBaseInfo**](AIHubPortfolioBaseInfo.md) |  | 
**metrics** | [**AIHubPortfolioMetrics**](AIHubPortfolioMetrics.md) |  | 
**position** | [**AIHubPortfolioPosition**](AIHubPortfolioPosition.md) |  | [optional] 
**stop_supported** | **bool** |  | 
**assets** | **list[str]** |  | [optional] 
**markets** | **list[str]** |  | [optional] 
**positions** | [**list[AIHubPortfolioAssetPosition]**](AIHubPortfolioAssetPosition.md) |  | [optional] 
**positions_status** | **str** |  | [optional] 
**configuration** | [**object**](.md) | Product-specific saved configuration. spot_martingale exposes AIHubSpotMartingaleConfiguration; absence is unverified. Runtime recovery internals are excluded. | [optional] 
**stop_progress** | [**AIHubStopProgress**](AIHubStopProgress.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


