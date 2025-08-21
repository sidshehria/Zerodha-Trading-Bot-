from core.kite_client import ZerodhaClient
from core.trade_manager import TradeManager
from core.scheduler import run_scheduler
from strategies.breakout_strategy import breakout_signal
import json, threading

with open("config/config.json") as f:
    config = json.load(f)

kite = ZerodhaClient()
trade_manager = TradeManager(config, kite)

# Run strategies
for symbol in config["watchlist"]:
    signal, price = breakout_signal(kite, symbol)
    if signal:
        trade_manager.execute_trade(symbol, price)

# Run square-off scheduler in background
t = threading.Thread(target=run_scheduler, args=(kite, config["squareoff_time"]))
t.start()
