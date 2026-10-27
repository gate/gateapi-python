# FixedTermProductSimple

Fixed-term earn product (compact)
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Product ID | [optional] 
**asset** | **str** | Currency | [optional] 
**lock_up_period** | **int** | Lock-up period (in days) | [optional] 
**year_rate** | **str** | Annual interest rate | [optional] 
**type** | **int** | Product type: 1 for regular, 2 for VIP | [optional] 
**pre_redeem** | **int** | Whether early redemption is supported: 0 for not supported, 1 for supported | [optional] 
**reinvest** | **int** | Whether auto-renewal is supported: 0 for not supported, 1 for supported | [optional] 
**simple_earn** | **int** | Whether fixed-to-flexible conversion is supported: 0 for not supported, 1 for supported | [optional] 
**min_vip** | **int** | Minimum VIP level requirement, 0 means no restriction | [optional] 
**max_vip** | **int** | Maximum VIP level requirement, 0 means no restriction | [optional] 
**sale_status** | **int** | Sale status: 1 for on sale, 2 for sold out | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


