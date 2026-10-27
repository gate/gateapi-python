# SpotOrderStopLoss

Stop loss for limit orders. Pass {} to cancel stop loss; pass null to leave stop loss unchanged.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trigger_price** | **str** | Stop loss trigger price When &#x60;side &#x3D;&#x3D; \&quot;buy\&quot;&#x60;, &#x60;trigger_price&#x60; must be less than &#x60;price&#x60; When &#x60;side &#x3D;&#x3D; \&quot;sell\&quot;&#x60;, &#x60;trigger_price&#x60; must be greater than &#x60;price&#x60; | [optional] 
**order_price** | **str** | Stop-loss order price | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


