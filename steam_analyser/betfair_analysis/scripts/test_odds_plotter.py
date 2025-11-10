
from betfair_analysis.tools.odds_plotter import OddsPlotter

if __name__ == "__main__":

    input_pickle = "./data/Arsenal_home_match_odds_2022.pkl"
    plotter = OddsPlotter(file_path=input_pickle)
    plotter.plot_odds()