# FixedTermLendOrder

Fixed-term earn subscription order
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Subscription record ID | [optional] 
**business** | **int** | Business type: 1 for regular, 2 for VIP | [optional] 
**order_id** | **int** | Order ID | [optional] 
**user_id** | **int** | User ID | [optional] 
**asset** | **str** | Currency | [optional] 
**product_id** | **int** | Product ID | [optional] 
**lock_up_period** | **int** | Lock-up period (in days) | [optional] 
**principal** | **str** | Subscription principal | [optional] 
**year_rate** | **str** | Annual interest rate | [optional] 
**product_type** | **int** | Product type: 1 for regular, 2 for VIP | [optional] 
**interest** | **str** | Accrued interest | [optional] 
**status** | **int** | Order status: 1 for holding, 2 for redeemed, 3 for matured, 4 for settled | [optional] 
**reinvest_status** | **int** | Auto-renewal status: 0 for disabled, 1 for enabled | [optional] 
**redeem_account_type** | **int** | Redemption payout account type: 1 for spot account | [optional] 
**origin_order** | **str** | Original order ID, linked to previous order IDs in auto-renewal scenarios | [optional] 
**redeem_type** | **int** | Redemption type: 1 for early redemption, 2 for maturity redemption | [optional] 
**redeem_time** | **str** | Redemption time | [optional] 
**finish_time** | **str** | Expiration time | [optional] 
**create_time** | **str** | Created time | [optional] 
**year_rate_perent** | **str** | Annual interest rate percentage display value | [optional] 
**total_year_rate_percent** | **str** | Comprehensive annualized yield percentage (including interest rate boost, rewards, etc.) | [optional] 
**total_interest** | **str** | Total earnings (including interest and bonus rewards) | [optional] 
**product_info** | [**FixedTermProductInfo**](FixedTermProductInfo.md) |  | [optional] 
**bonus_info** | [**FixedTermBonusInfo**](FixedTermBonusInfo.md) |  | [optional] 
**coupon_info** | [**FixedTermCouponInfo**](FixedTermCouponInfo.md) |  | [optional] 
**redeem_at** | **int** | Redemption timestamp (in seconds) | [optional] 
**finish_at** | **int** | Expiration timestamp (in seconds) | [optional] 
**create_at** | **int** | Creation timestamp (in seconds) | [optional] 
**icon** | **str** | Currency icon URL | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


