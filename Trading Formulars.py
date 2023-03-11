# DESCRIPTION

'''
This class includes functions for calculating the P&L formula, Sharpe Ratio, Moving Average, Relative Strength Index,
Fibonacci Retracement, Standard Deviation, and Beta, as well as a function to calculate the lot size for a forex trade.
Note that for the lot size calculation, the account_size, risk_pct, stop_loss_pips, and currency_value parameters are needed as input. 
The risk_pct parameter indicates the percentage of the account that the trader is willing to risk on the trade, 
and the stop_loss_pips parameter indicates the number of pips that the trader is willing to risk on the trade.
The currency_value parameter indicates the value of one pip in the currency of the trading account.
'''

# CODE

import math

class TradingFormulas:
    
    def __init__(self):
        pass
    
    # P&L formula
    def calculate_pnl(self, entry_price, exit_price, shares_traded):
        return (exit_price - entry_price) * shares_traded
    
    # Sharpe Ratio formula
    def calculate_sharpe_ratio(self, portfolio_return, risk_free_rate, portfolio_std_dev):
        return (portfolio_return - risk_free_rate) / portfolio_std_dev
    
    # Moving Average formula
    def calculate_ma(self, prices, time_period):
        return sum(prices[-time_period:]) / time_period
    
    # Relative Strength Index formula
    def calculate_rsi(self, gains, losses):
        rs = sum(gains) / sum(losses)
        return 100 - (100 / (1 + rs))
    
    # Fibonacci Retracement formula
    def calculate_fibonacci_retracement(self, high, low, retracement_level):
        retracement = high - ((high - low) * retracement_level)
        return retracement
    
    # Standard Deviation formula
    def calculate_standard_deviation(self, data):
        mean = sum(data) / len(data)
        variance = sum((x - mean) ** 2 for x in data) / len(data)
        return math.sqrt(variance)
    
    # Beta formula
    def calculate_beta(self, security_returns, market_returns):
        cov = sum((security_returns[i] - sum(security_returns)/len(security_returns)) * (market_returns[i] - sum(market_returns)/len(market_returns)) for i in range(len(security_returns))) / len(security_returns)
        security_std_dev = self.calculate_standard_deviation(security_returns)
        market_std_dev = self.calculate_standard_deviation(market_returns)
        return cov / (security_std_dev * market_std_dev)
    
    # Lot size formula
    def calculate_lot_size(self, account_size, risk_pct, stop_loss_pips, currency_value):
        risk_amount = account_size * (risk_pct / 100)
        pip_value = currency_value / 10000
        lot_size = risk_amount / (stop_loss_pips * pip_value)
        return round(lot_size, 2)
