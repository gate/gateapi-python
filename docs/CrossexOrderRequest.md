# CrossexOrderRequest

Place Order Request Body
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | Client-defined Order ID, supports letters (a-z), numbers (0-9), symbols (-, _) only | [optional] 
**symbol** | **str** | Unique identifier Exchange_Business_Base_Counter Examples: To place a spot order for ADA/USDT on BINANCE, use &#x60;BINANCE_SPOT_ADA_USDT&#x60;; To place a USDT-margined perpetual futures order for ADA/USDT on OKX, use &#x60;OKX_FUTURE_ADA_USDT&#x60;; To place a spot margin order for ADA/USDT on GATE, use &#x60;GATE_MARGIN_ADA_USDT&#x60;; To place a spot order for ADA/USDT on BYBIT, use &#x60;BYBIT_SPOT_ADA_USDT&#x60;; To place a futures order for ADA/USD on KRAKEN, use &#x60;KRAKEN_FUTURE_ADA_USD&#x60;; To place a futures order for ADA/USDC on HYPERLIQUID, use &#x60;HYPERLIQUID_FUTURE_ADA_USDC&#x60;; To place a futures order for ADA/USDC on DERIBIT, use &#x60;DERIBIT_FUTURE_ADA_USDC&#x60;; To place a futures order for ADA/USDC on LIGHTER, use &#x60;LIGHTER_FUTURE_ADA_USDC&#x60;; To trade US stock AAPL, use &#x60;US_STOCK_AAPL_USDT&#x60;; To trade Hong Kong stock 00700, use &#x60;HK_STOCK_00700_USDT&#x60;; To trade US ETF SPY, use &#x60;US_ETF_SPY_USDT&#x60;; Spot, USDT-margined perpetual futures, spot margin, stock, and ETF orders are supported. BYBIT/DERIBIT do not currently support spot margin orders. KRAKEN, HYPERLIQUID, and LIGHTER do not currently support spot or margin orders. Stocks and ETFs support only cross-exchange account mode | 
**side** | **str** | BUY, SELL | 
**type** | **str** | Order type (default: &#x60;LIMIT&#x60;; supported types: &#x60;LIMIT&#x60;, &#x60;MARKET&#x60;) | [optional] [default to 'LIMIT']
**time_in_force** | **str** | Defaults to GTC. Supported values: &#x60;GTC&#x60;, &#x60;IOC&#x60;, &#x60;FOK&#x60;, &#x60;POC&#x60;, &#x60;RPI&#x60; &#x60;GTC&#x60;: GoodTillCancelled &#x60;IOC&#x60;: ImmediateOrCancelled &#x60;FOK&#x60;: FillOrKill &#x60;POC&#x60;: PendingOrCancelled or PostOnly &#x60;RPI&#x60;: RPI Stocks and ETFs support only &#x60;GTC&#x60; | [optional] [default to 'GTC']
**qty** | **str** | Order quantity (required except for spot and margin market buys; qty is required for stocks and ETFs) | [optional] 
**price** | **str** | Limit order price (required for limit orders). Stocks and ETFs use the listing market currency (USD/HKD/KRW/JPY) | [optional] 
**quote_qty** | **str** | Order quote quantity, required for spot and margin market buys. Stock and ETF orders do not support quote_qty | [optional] 
**reduce_only** | **str** | Reduce-only: &#x60;true&#x60; or &#x60;false&#x60; | [optional] 
**position_side** | **str** | Position side: &#x60;NONE&#x60;, &#x60;LONG&#x60;, &#x60;SHORT&#x60; Defaults to &#x60;NONE&#x60; (single position mode) if not specified | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


