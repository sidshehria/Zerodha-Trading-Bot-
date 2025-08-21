import schedule, time

def auto_squareoff(kite):
    positions = kite.kite.positions()["net"]
    for pos in positions:
        if pos["quantity"] > 0:
            kite.place_market_order(pos["tradingsymbol"], pos["quantity"], "SELL")
            print(f"Square-off: {pos['tradingsymbol']}")

def run_scheduler(kite, squareoff_time="15:25"):
    schedule.every().day.at(squareoff_time).do(auto_squareoff, kite=kite)
    while True:
        schedule.run_pending()
        time.sleep(10)
