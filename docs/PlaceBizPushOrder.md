# PlaceBizPushOrder

Place ad order request
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency_type** | **str** | Cryptocurrency symbol. | 
**exchange_type** | **str** | Fiat currency | 
**type** | **str** | Ad operation type. &#x60;0&#x60;: publish sell ad; &#x60;1&#x60;: publish buy ad; &#x60;2&#x60;: edit sell ad; &#x60;3&#x60;: edit buy ad. | 
**unit_price** | **str** | Per-unit price in fixed-price mode. | 
**number** | **str** | Ad amount priced in &#x60;currencyType&#x60;. | 
**pay_type** | **str** | Payment types, comma-separated; from pay type list &#x60;pay_type&#x60;, e.g. &#x60;bank&#x60;, &#x60;alipay&#x60;, &#x60;wechat&#x60;, &#x60;paypal&#x60;, &#x60;swift&#x60;, &#x60;wu&#x60;. | 
**pay_type_json** | **str** | JSON map of payment type -&gt; user&#39;s payment method ID. | [optional] 
**rate_fixed** | **str** | Price type: &#x60;0&#x60; floating; &#x60;1&#x60; fixed. | [optional] 
**oid** | **str** | Pass ad ID when editing; omit or empty when publishing a new ad. | [optional] 
**min_amount** | **str** | Minimum trade amount in &#x60;exchangeType&#x60;. | 
**max_amount** | **str** | Maximum amount per trade in &#x60;exchangeType&#x60; fiat units. | 
**tier_limit** | **str** | Minimum counterparty VIP level; &#x60;0&#x60; means no requirement. | [optional] 
**verified_limit** | **str** | Minimum counterparty verification level; &#x60;0&#x60; means no limit. | [optional] 
**reg_time_limit** | **str** | Minimum counterparty account age in days; &#x60;0&#x60; means no limit. | [optional] 
**advertisers_limit** | **str** | Whether trading with the advertiser is restricted. &#x60;0&#x60;: no; &#x60;1&#x60;: yes. | [optional] 
**expire_min** | **str** | Payment timeout in minutes. | [optional] 
**trade_tips** | **str** | Advertisement trade terms displayed to ordering users; goes through off-platform traffic diversion risk control on submission, and when hit, the advertisement is not saved and code 70305102 is returned | [optional] 
**auto_reply** | **str** | Auto reply content after order creation; goes through off-platform traffic diversion risk control on submission, and when hit, the advertisement is not saved and code 70305102 is returned | [optional] 
**min_completed_limit** | **str** | Minimum completed orders for counterparty; &#x60;-1&#x60; unlimited. | [optional] 
**max_completed_limit** | **str** | Maximum completed orders for counterparty; &#x60;-1&#x60; unlimited. | [optional] 
**completed_rate_limit** | **str** | Counterparty minimum 30-day completion rate; &#x60;-1&#x60; means no limit. | [optional] 
**user_country_limit** | **str** | KYC nationality restriction; &#x60;-1&#x60; means no restriction. | [optional] 
**user_order_limit** | **str** | Maximum concurrent orders allowed for the counterparty. &#x60;-1&#x60;: unlimited. | [optional] 
**rate_reference_id** | **str** | Floating price reference. &#x60;1&#x60;: platform reference; &#x60;2&#x60;: Gate reference; &#x60;3&#x60;: spot reference. | [optional] 
**rate_offset** | **str** | Absolute floating offset ratio, e.g. &#x60;0.5&#x60; means 0.5%. | [optional] 
**float_trend** | **str** | Floating direction: &#x60;0&#x60; markup; &#x60;1&#x60; markdown. | [optional] 
**team_payment_uid** | **str** | Team payee UID; optional for non-team merchants. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


