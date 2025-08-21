import math

class TradeManager:
    def __init__(self, config, kite):
        self.capital = config["capital"]
        self.risk_percent = config["risk_percent"]
        self.sl_percent = config["sl_percent"]
        self.target_rr = config["target_rr"]
        self.kite = kite

    def calc_qty(self, entry, sl):
        risk_amt = self.capital * (self.risk_percent / 100)
        risk_per_share = max(entry - sl, 0.05)
        qty = math.floor(risk_amt / risk_per_share)
        return max(qty, 1)

    def execute_trade(self, symbol, entry_price):
        sl = entry_price * (1 - self.sl_percent / 100)
        target = entry_price + (entry_price - sl) * self.target_rr
        qty = self.calc_qty(entry_price, sl)

        order_id = self.kite.place_market_order(symbol, qty, "BUY")
        print(f"BUY {symbol} @ {entry_price} | SL={sl} | Target={target} | Qty={qty}")
        return order_id
