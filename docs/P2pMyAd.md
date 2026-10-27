# P2pMyAd

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Ad side: &#x60;buy&#x60; buy-crypto ad; &#x60;sell&#x60; sell-crypto ad. | [optional] 
**rate** | **str** | Price | [optional] 
**original_rate** | **str** | Original price | [optional] 
**amount** | **str** | Remaining crypto amount on the ad. | [optional] 
**total** | **str** | Remaining fiat amount of ad | [optional] 
**limit_total** | **str** | Single order limit range (cryptocurrency) | [optional] 
**limit_fiat** | **str** | Single order limit range (fiat) | [optional] 
**min_amount** | **str** | Minimum quantity per order | [optional] 
**max_amount** | **str** | Maximum quantity per order | [optional] 
**pay_type_num** | **str** | Payment method ID list | [optional] 
**pay_type_json** | **str** | JSON map of payment type -&gt; payment method ID. | [optional] 
**expire_min** | **str** | Ad expiration time (minutes) | [optional] 
**tier_limit** | **str** | VIP limit | [optional] 
**advertisers_limit** | **int** | Whether trading with the advertiser is restricted. &#x60;0&#x60;: no; &#x60;1&#x60;: yes. | [optional] 
**reg_time_limit** | **int** | Registration time limit | [optional] 
**verified_limit** | **int** | KYC level limit | [optional] 
**min_completed_limit** | **int** | Minimum limit of completed orders by counterparty | [optional] 
**max_completed_limit** | **int** | Maximum limit of completed orders by counterparty | [optional] 
**user_country_limit** | **int** | KYC nationality restriction | [optional] 
**completed_rate_limit** | **float** | 30-day completion rate limit | [optional] 
**user_orders_limit** | **int** | Maximum order limit for counterparty | [optional] 
**hide_payment** | **str** | Whether payment methods are hidden. &#x60;1&#x60;: hidden; &#x60;0&#x60;: visible. | [optional] 
**currency_type** | **str** | Cryptocurrency symbol. | [optional] 
**want_type** | **str** | Fiat currency | [optional] 
**trade_tips** | **str** | Trading terms | [optional] 
**new_hand** | **int** | Special ad type. &#x60;0&#x60; normal; &#x60;1&#x60; newcomer guide; &#x60;2&#x60; newcomer discount; &#x60;3&#x60; featured promo; &#x60;4&#x60; KOL ad; &#x60;5&#x60; coupon ad. | [optional] 
**id** | **str** | Advertisement ID. | [optional] 
**status** | **str** | Ad status: &#x60;OPEN&#x60; listed; &#x60;OFFLIN&#x60; delisted; &#x60;CLOSED&#x60; closed; &#x60;CANCEL&#x60; canceled. | [optional] 
**locked_amount** | **str** | Ad frozen amount | [optional] 
**hide_rate** | **str** | Hidden price | [optional] 
**is_out_time** | **int** | Whether the ad timed out. &#x60;1&#x60;: timed out; &#x60;0&#x60;: not yet. | [optional] 
**rate_ref_id** | **int** | Floating reference: &#x60;1&#x60; platform; &#x60;2&#x60; Gate; &#x60;3&#x60; spot; &#x60;&lt;&#x3D; 0&#x60; means fixed price. | [optional] 
**rate_offset** | **str** | Floating ratio | [optional] 
**rate_fixed** | **int** | Price type: &#x60;0&#x60; floating; &#x60;1&#x60; fixed. | [optional] 
**float_trend** | **int** | Floating direction: &#x60;0&#x60; markup; &#x60;1&#x60; markdown. | [optional] 
**in_dispute** | **int** | Whether the ad had a disputed trade. &#x60;1&#x60;: yes; &#x60;0&#x60;: no. | [optional] 
**auto_reply** | **str** | Auto reply data | [optional] 
**timestamp** | **int** | Ad creation time | [optional] 
**is_hedge** | **int** | Whether auto-delegation is enabled. &#x60;1&#x60;: yes; &#x60;0&#x60;: no. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


