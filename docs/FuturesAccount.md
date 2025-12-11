# FuturesAccount

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **str** | Balance, only applicable to classic contract account.The balance is the sum of all historical fund flows, including historical transfers in and out, closing settlements, and transaction fee expenses, but does not include upl of positions.total &#x3D; SUM(history_dnw, history_pnl, history_fee, history_refr, history_fund) | [optional] 
**unrealised_pnl** | **str** | Unrealized PNL | [optional] 
**position_margin** | **str** | Deprecated | [optional] 
**order_margin** | **str** | initial margin of all open orders | [optional] 
**available** | **str** | Refers to the available withdrawal or trading amount in per-position, specifically the per-position available balance under the unified account that includes the credit line (which incorporates trial funds; since trial funds cannot be withdrawn, the actual withdrawal amount needs to deduct the trial fund portion when processing withdrawals) | [optional] 
**point** | **str** | Point card amount | [optional] 
**currency** | **str** | Settlement currency | [optional] 
**in_dual_mode** | **bool** | Whether Hedge Mode is enabled | [optional] 
**position_mode** | **str** | Position mode: single - one-way, dual - dual-side, split - sub-positions (in_dual_mode is deprecated) | [optional] 
**enable_credit** | **bool** | Whether portfolio margin account mode is enabled | [optional] 
**position_initial_margin** | **str** | Initial margin occupied by positions, applicable to unified account mode | [optional] 
**maintenance_margin** | **str** | Maintenance margin occupied by positions, applicable to new classic account margin mode and unified account mode | [optional] 
**bonus** | **str** | Bonus | [optional] 
**enable_evolved_classic** | **bool** | Deprecated | [optional] 
**cross_order_margin** | **str** | Cross margin order margin, applicable to new classic account margin mode | [optional] 
**cross_initial_margin** | **str** | Cross margin initial margin, applicable to new classic account margin mode | [optional] 
**cross_maintenance_margin** | **str** | Cross margin maintenance margin, applicable to new classic account margin mode | [optional] 
**cross_unrealised_pnl** | **str** | Cross margin unrealized P&amp;L, applicable to new classic account margin mode | [optional] 
**cross_available** | **str** | Cross margin available balance, applicable to new classic account margin mode | [optional] 
**cross_margin_balance** | **str** | Cross margin balance, applicable to new classic account margin mode | [optional] 
**cross_mmr** | **str** | Cross margin maintenance margin rate, applicable to new classic account margin mode | [optional] 
**cross_imr** | **str** | Cross margin initial margin rate, applicable to new classic account margin mode | [optional] 
**isolated_position_margin** | **str** | Isolated position margin, applicable to new classic account margin mode | [optional] 
**enable_new_dual_mode** | **bool** | Deprecated | [optional] 
**margin_mode** | **int** | Margin mode of the account 0: classic future account or Classic Spot Margin Mode of unified account; 1:  Multi-Currency Margin Mode; 2:  Portoforlio Margin Mode; 3:  Single-Currency Margin Mode | [optional] 
**enable_tiered_mm** | **bool** | Whether to enable tiered maintenance margin calculation | [optional] 
**history** | [**FuturesAccountHistory**](FuturesAccountHistory.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


