# SpotMartingaleCreateParams

Spot martingale creation parameters (serialized fields aligned with `MartingaleBot`). - **Stop-loss**: use `stop_loss_per_cycle` (ratio per round), same as the app; **do not** use `stop_loss_price`. - Optional **`trigger_price`**: trigger price. - If `stop_loss_per_cycle` is passed and > 0, the server validates roughly between `0.001` and `0.9999` (same as `check_martingale`).
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invest_amount** | **str** |  | 
**price_deviation** | **str** | Add-position deviation ratio as a decimal string (e.g. a 2% drop is &#x60;0.02&#x60;). | 
**max_orders** | **int** |  | 
**take_profit_ratio** | **str** | Take-profit ratio per round as a decimal string. | 
**stop_loss_per_cycle** | **str** | Stop-loss ratio per round as a decimal string; optional; aligned with app &#x60;stop_loss_per_cycle&#x60;. | [optional] 
**trigger_price** | **str** | Trigger price; optional. | [optional] 
**profit_sharing_ratio** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


