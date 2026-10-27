# OrderResponse

Order response
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** | Order ID | [optional] 
**tx_hash** | **str** | Transaction Hash | [optional] 
**side** | **str** | Buy or sell orders - buy - sell | [optional] 
**usdt_amount** | **str** | Amount (USDT) | [optional] 
**currency** | **str** | Token | [optional] 
**currency_amount** | **str** | Token amount | [optional] 
**status** | **int** | Order Status - &#x60;0&#x60; : All - &#x60;1&#x60; : Processing - &#x60;2&#x60; : Successful - &#x60;3&#x60; : Failed - &#x60;4&#x60; : Cancelled - &#x60;5&#x60; : Buy order placed but transfer not completed - &#x60;6&#x60; : Order cancelled but transfer not completed | [optional] 
**gas_mode** | **str** | Trading mode affects slippage selection - &#x60;speed&#x60; : Smart mode - &#x60;custom&#x60; : Custom mode, uses &#x60;slippage&#x60; parameter | [optional] 
**chain** | **str** | Blockchain | [optional] 
**gas_fee** | **str** | Gas Fee (USDT-based) | [optional] 
**transaction_fee** | **str** | Trading Fee (USDT-based) | [optional] 
**failed_reason** | **str** | Failure reason (if applicable) | [optional] 
**create_time** | **int** | Creation timestamp | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


