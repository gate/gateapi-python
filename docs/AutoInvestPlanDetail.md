# AutoInvestPlanDetail

Auto invest planDetails
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Plan ID | 
**version** | **int** | PlanVersion | [optional] 
**name** | **str** | Plan name | 
**create_time** | **int** | Creation time (Unix timestamp) | 
**update_time** | **int** | Update time (Unix timestamp) | 
**user_id** | **int** | User ID | 
**money** | **str** | Quote Currency | 
**amount** | **str** | Per PeriodInvestment amount | 
**period_type** | **str** | Cycle type（e.g., monthly） | 
**period_day** | **int** | Cycle day | 
**period_hour** | **int** | CycleHours | 
**portfolio** | [**list[AutoInvestPortfolioItem]**](AutoInvestPortfolioItem.md) | InvestmentPortfolio | 
**next_time** | **int** | Next execution time (Unix timestamp) | 
**period** | **int** | Executed periods | 
**fund_source** | **str** | Fund source（spot/earn） | 
**fund_flow** | **str** | Fund flow direction (auto_invest/earn) | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


