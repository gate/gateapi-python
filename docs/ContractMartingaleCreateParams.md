# ContractMartingaleCreateParams

The creation parameters of the contract Martin strategy.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invest_amount** | **str** | Total strategy budget, not first-order margin. The server uses the complete existing ladder formula, owner fee and live contract facts, quantizes quantity down and rechecks before allocation. Minimum infeasible budget is rejected. | 
**price_deviation** | **str** |  | 
**max_orders** | **int** | Maximum additional entries, excluding the first; preserve this legacy meaning. | 
**take_profit_ratio** | **str** |  | 
**direction** | [**ContractMartingaleDirection**](ContractMartingaleDirection.md) |  | 
**leverage** | **str** |  | 
**stop_loss_price** | **str** | Positive fixed stop price; requires explicit stop_loss_price_type. Missing both leaves the old no-fixed-stop request unchanged. | [optional] 
**profit_sharing_ratio** | **str** |  | [optional] 
**stop_loss_price_type** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


