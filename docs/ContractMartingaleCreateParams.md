# ContractMartingaleCreateParams

The creation parameters of the contract Martin strategy.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invest_amount** | **str** | Margin allocated; the server converts it to initial contract size using live contract price, contract multiplier, and minimum lot size. | 
**price_deviation** | **str** |  | 
**max_orders** | **int** |  | 
**take_profit_ratio** | **str** |  | 
**direction** | [**ContractMartingaleDirection**](ContractMartingaleDirection.md) |  | 
**leverage** | **str** |  | 
**stop_loss_price** | **str** | Legacy field name. The AIHub &#x60;contract_martingale&#x60; creation path does not map this field today; follow contract martingale rules from the underlying API. MCP tooling must match bot-service behavior. | [optional] 
**profit_sharing_ratio** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


