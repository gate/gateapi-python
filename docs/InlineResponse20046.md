# InlineResponse20046

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Account Change Record ID | 
**user_id** | **str** | User ID | 
**business_id** | **str** | Business ID | 
**type** | **str** | 变更类型| &#x60;TRANSACTION&#x60; 成交 &#x60;TRADING_FEE&#x60; 手续费 &#x60;FUNDING_FEE&#x60; 合约资金费 &#x60;LIQUIDATION_FEE&#x60; 强平费 &#x60;TRANSFER_IN&#x60; 资金转入 &#x60;TRANSFER_OUT&#x60; 资金转出 &#x60;BANKRUPT_COMPENSATION&#x60; 穿仓补贴 &#x60;AUTO_REPAY&#x60; 杠杆仓位自动还负债 | 
**exchange_type** | **str** | Exchange | 
**coin** | **str** | Currency | 
**change** | **str** | Change amount (positive indicates transfer in; negative indicates transfer out) | 
**balance** | **str** | Balance after change | 
**create_time** | **str** | Created time | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


