# FuturesOrderBook

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Order Book ID. Increases by 1 on every order book change. Set &#x60;with_id&#x3D;true&#x60; to include this field in response | [optional] 
**current** | **float** | Response data generation timestamp | [optional] 
**current_us** | **int** | Response data timestamp in microseconds; omitted when unavailable | [optional] 
**update** | **float** | Order book changed timestamp | [optional] 
**update_us** | **int** | Order book update timestamp in microseconds; omitted when unavailable | [optional] 
**asks** | [**list[FuturesOrderBookItem]**](FuturesOrderBookItem.md) | Ask Depth | 
**bids** | [**list[FuturesOrderBookItem]**](FuturesOrderBookItem.md) | Bid Depth | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


