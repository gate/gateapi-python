# PositionHistoryListDataList

Position close history
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position_id** | **int** | Position ID | 
**symbol** | **str** | Market / Trading symbol | 
**realized_pnl** | **str** | Realized PnL | 
**realized_pnl_rate** | **str** | Realized return rate | [optional] 
**volume** | **str** | Position size / Maximum position size | 
**volume_closed** | **str** | Close volume | 
**price_open** | **str** | Average Opening Price | 
**position_dir** | **str** | Position Direction - Long: Long Position - Short: Short Position | 
**price_tp** | **str** | Take profit price | [optional] 
**price_sl** | **str** | Stop loss price | [optional] 
**counterparty_price** | **str** | Counterparty price | [optional] 
**close_price** | **str** | Close price | 
**time_create** | **str** | Open time (timestamp in seconds) | 
**time_close** | **str** | Close time (timestamp in seconds) | 
**position_status** | **str** | Position Status - 1: Fully Closed - 2: Forced Liquidation | 
**close_detail** | [**PositionHistoryListDataCloseDetail**](PositionHistoryListDataCloseDetail.md) |  | [optional] 
**realized_pnl_detail** | [**PositionHistoryListDataRealizedPnlDetail**](PositionHistoryListDataRealizedPnlDetail.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


