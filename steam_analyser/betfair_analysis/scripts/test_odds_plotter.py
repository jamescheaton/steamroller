
from betfair_analysis.tools.odds_plotter import OddsPlotter

if __name__ == "__main__":

    input_pickle = "./data/2025/Man City/Man_City_home_match_odds.pkl"
    plotter = OddsPlotter(file_path=input_pickle)
    plotter.save_odds(out_dir="./data/2025/Man City")