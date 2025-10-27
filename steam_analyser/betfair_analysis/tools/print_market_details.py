import betfair_data as bfd
import matplotlib.pyplot as plt
import numpy as np

from datetime import datetime

path = "data/data.tar"

if __name__ == "__main__":

    arsenal = []
    villa = []
    times = []
    i = 0
    for file in bfd.Files([path]):
        for market in file:
            market_name = market.market_name
            if "Arsenal v Aston Villa" not in market.event_name:
                continue
            if "Match Odds" not in market.market_name or "and" in market.market_name:
                continue
            if market.in_play:
                continue
            print(market.event_name)
            print(market.market_name)
            print(market.market_type)
            print(market.market_time)
            print(market.publish_time)
            for runner in market.runners:
                print("\n")
                print(runner.name)
                if "Arsenal" in runner.name:
                    arsenal_odds = runner.last_price_traded
                    arsenal.append(arsenal_odds)
                if "Aston" in runner.name:
                    villa_odds = runner.last_price_traded
                    villa.append(villa_odds)
                print(runner.last_price_traded)
            print(i)
            i+=1
            if i == 877:
                break
            print("-"*100)
        year = 2025
        if i == 877:
            break
    plt.figure()
    x = np.arange(0, len(arsenal), 1)
    y1 = np.array(arsenal)
    y2 = np.array(villa)
    plt.plot(x, y1)
    plt.plot(x, y2)
    plt.show()
            
