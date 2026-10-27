# FixedTermBonusInfo

Bonus reward campaign information
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Activity ID | [optional] 
**product_id** | **int** | Associated product ID | [optional] 
**asset** | **str** | Product currency | [optional] 
**bonus_asset** | **str** | Reward currency | [optional] 
**kyc_limit** | **str** | KYC level restrictions, comma-separated | [optional] 
**ladder_apr** | [**list[LadderApr]**](LadderApr.md) | Tiered annual interest rate | [optional] 
**total_bonus_amount** | **str** | Total reward amount | [optional] 
**user_total_bonus_amount** | **str** | Maximum reward per user | [optional] 
**status** | **int** | Activity status: 1 for unlisted, 2 for listed, 3 for delisted | [optional] 
**start_time** | **str** | Activity start time | [optional] 
**end_time** | **str** | Activity end time | [optional] 
**create_time** | **str** | Created time | [optional] 
**start_at** | **int** | Activity start timestamp (in seconds) | [optional] 
**end_at** | **int** | Activity end timestamp (in seconds) | [optional] 
**total_issued_amount** | **str** | Total rewards distributed | [optional] 
**user_total_issued_amount** | **str** | Total rewards distributed to the user | [optional] 
**bonus_asset_price** | **str** | Reward currency price (denominated in USDT) | [optional] 
**product_asset_price** | **str** | Product currency price (denominated in USDT) | [optional] 
**product_year_rate** | **str** | Product base annual interest rate | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


