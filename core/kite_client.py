from kiteconnect import KiteConnect
import json, os

class ZerodhaClient:
    def __init__(self, config_path="config/config.json"):
        with open(config_path) as f:
            self.cfg = json.load(f)

        self.kite = KiteConnect(api_key=self.cfg["api_key"])
        self.kite.set_access_token(self.cfg["access_token"])

    def ltp(self, symbol):
        data = self.kite.ltp(f"NSE:{symbol}")
        if isinstance(data, dict) and f"NSE:{symbol}" in data:
            return data[f"NSE:{symbol}"]["last_price"]
        raise ValueError(f"LTP data for symbol {symbol} not found or invalid response: {data}")

    def place_market_order(self, symbol, qty, txn_type):
        return self.kite.place_order(
            tradingsymbol=symbol,
            exchange=self.kite.EXCHANGE_NSE,
            transaction_type=txn_type,
            quantity=qty,
            order_type=self.kite.ORDER_TYPE_MARKET,
            product=self.kite.PRODUCT_MIS,
            variety=self.kite.VARIETY_REGULAR
        )
