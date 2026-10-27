# AIHubContractMartingaleConfiguration

AIHub-supported persisted contract settings. This is not a complete advanced native configuration.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invest_amount** | **str** |  | [optional] 
**investment_currency** | **str** |  | [optional] 
**price_deviation** | **str** |  | [optional] 
**take_profit_ratio** | **str** |  | [optional] 
**direction** | **str** |  | [optional] 
**first_order_size** | **str** | Exact decimal contract quantity from the product snapshot; empty remains unverified, never inferred from the total budget. | [optional] 
**max_orders** | **int** | Maximum additional entries excluding the first. | [optional] 
**leverage** | **int** |  | [optional] 
**stop_loss_price_rule** | [**AIHubMartingalePriceRule**](AIHubMartingalePriceRule.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


