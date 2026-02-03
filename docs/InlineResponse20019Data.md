# InlineResponse20019Data

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rate** | **str** | Price | 
**type** | **str** | Buy/Sell order | 
**amount** | **str** | Cryptocurrency amount | 
**min_amount** | **str** | Minimum limit | 
**max_amount** | **str** | Maximum limit | 
**total** | **str** | Fiat amount | 
**pay_ali** | **int** | Whether Alipay payment is supported | 
**pay_bank** | **int** | Whether bank payment is supported | 
**pay_paypal** | **int** | Whether PayPal payment is supported | 
**pay_wechat** | **int** | Whether WeChat payment is supported | 
**pay_type_num** | **str** | Payment method ID list | 
**pay_type_json** | **str** | Payment method list | 
**locked_amount** | **str** | Locked amount | 
**orderid** | **int** | Order ID | 
**timestamp** | **int** | Created time | 
**currency_type** | **str** | Cryptocurrency type | 
**want_type** | **str** | Fiat type | 
**hide_rate** | **str** | Hidden price | 
**trade_tips** | **str** | Trading terms | 
**auto_reply** | **str** | Auto reply | 
**new_hand** | **str** | Merchant-friendly order | 
**rate_ref_id** | **int** | Floating price reference ID: 1&#x3D;Platform reference price, 3&#x3D;Spot reference price (≤0 means fixed price, &gt;0 means floating price) | 
**rate_offset** | **float** | Floating ratio (absolute value) | 
**status** | **str** | Status | 
**rate_fixed** | **int** | 0&#x3D;Floating, 1&#x3D;Fixed | 
**float_trend** | **int** | 0&#x3D;Upward float, 1&#x3D;Downward float | 
**expire_min** | **int** | Timeout (minutes) | 
**tier_limit** | **int** | Tier limit | 
**reg_time_limit** | **int** | Registration time limit | 
**advertisers_limit** | **int** | Do not trade with advertisers, advertiser limit: 0&#x3D;No limit, 1&#x3D;Limit | 
**verified_limit** | **int** | kyclimit | 
**min_completed_limit** | **int** | Minimum limit of completed orders | 
**max_completed_limit** | **int** | Maximum limit of completed orders | 
**user_orders_limit** | **int** | Order count limit | 
**completed_rate_limit** | **int** | 30-day completion rate limit | 
**user_country_limit** | **int** | KYC nationality restriction | 
**limit_country_cn** | **str** | Restricted nationality (Chinese) | 
**limit_country_en** | **str** | Restricted nationality (English) | 
**is_hedge** | **int** | Whether auto delegation | 
**hide_payment** | **int** | Whether to hide payment method | 
**fee** | **int** | fee | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


