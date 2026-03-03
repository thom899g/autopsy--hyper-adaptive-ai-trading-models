"""
Trading system configuration with validation and defaults.
Ensures all variables are initialized before use.
"""
import os
from dataclasses import dataclass
from typing import Dict, Any, Optional
import logging

@dataclass
class TradingConfig:
    """Centralized configuration with validation"""
    
    # Exchange Configuration
    EXCHANGE_ID: str = "binance"
    SYMBOL: str = "BTC/USDT"
    TIMEFRAME: str = "1h"
    
    # Trading Parameters
    INITIAL_CAPITAL: float = 10000.0
    MAX_POSITION_SIZE: float = 0.1  # 10% of capital
    STOP_LOSS_PCT: float = 0.02  # 2%
    TAKE_PROFIT_PCT: float = 0.05  # 5%
    
    # Model Parameters
    LOOKBACK_PERIOD: int = 100
    TRAIN_TEST_SPLIT: float = 0.8
    MODEL_UPDATE_HOURS: int = 24
    
    # Risk Management
    MAX_DRAWDOWN_PCT: float = 0.20
    MAX_DAILY_LOSS_PCT: float = 0.05
    MAX_CONCURRENT_TRAD