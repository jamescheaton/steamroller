import pickle

import matplotlib.pyplot as plt


class OddsPlotter:

    def __init__(self, file_path: str):
        self.file_path = file_path
        self.matches = self.load_odds()

    def load_odds(self) -> dict:
        with open(self.file_path, "rb") as f:
            matches = pickle.load(f)
        return matches

    def plot_odds(self):
        for match_key, match_data in self.matches.items():
            times = match_data.times
            home_odds = match_data.home_odds
            away_odds = match_data.away_odds
            draw_odds = match_data.draw_odds

            plt.figure(figsize=(10, 6))
            plt.plot(times, home_odds, label='Home Odds', color='blue')
            plt.plot(times, away_odds, label='Away Odds', color='red')
            plt.plot(times, draw_odds, label='Draw Odds', color='green')
            plt.xlabel('Time')
            plt.ylabel('Odds')
            plt.title(f'Odds Over Time for {match_data.name}')
            plt.legend()
            plt.grid()
            plt.tight_layout()
            plt.show()