def breakout_signal(kite, symbol):
    ltp = kite.ltp(symbol)
    if ltp > 10 and ltp < 100:   # Simple condition, replace with real logic
        return True, ltp
    return False, ltp
