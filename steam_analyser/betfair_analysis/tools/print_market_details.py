import betfair_data as bfd
import matplotlib.pyplot as plt
import numpy as np

from datetime import datetime

path = "data/data.tar"

TEAM_1 = "Arsenal"
TEAM_2 = "West Ham"
if __name__ == "__main__":

    arsenal = []
    villa = []
    times = []
    i = 0
    limit = 650
    found = False
    for file in bfd.Files([path]):
        for market in file:
            if market.in_play:
                continue
            market_name = market.market_name
            if f"{TEAM_1} v " not in market.event_name:
                continue
            if "Match Odds" not in market_name or "and" in market_name:
                continue
            print("-"*75)
            print(market.event_name)
            print(market.market_name)
            print(market.market_time)
            print(market.publish_time)
            if f"{TEAM_1} v {TEAM_2}" not in market.event_name:
                if found:
                    break
                continue
            found = True
            if market.in_play:
                continue
            for runner in market.runners:
                print("\n")
                print(runner.name)
                if TEAM_1 in runner.name:
                    arsenal_odds = runner.last_price_traded
                    arsenal.append(arsenal_odds)
                if TEAM_2 in runner.name:
                    villa_odds = runner.last_price_traded
                    villa.append(villa_odds)
                print(runner.last_price_traded)
            print(i)
            i+=1
            if i == limit:
                break
            print("-"*100)
        if i == limit:
            break
        if found:
            break
    plt.figure()
    x = np.arange(0, len(arsenal), 1)
    y1 = np.array(arsenal)
    y2 = np.array(villa)
    plt.plot(x, y1, label=TEAM_1)
    plt.plot(x, y2, label=TEAM_2)
    plt.xlabel("Time")
    plt.ylabel("% Win")
    plt.title(f"{TEAM_1} v {TEAM_2}")
    plt.show()
            
