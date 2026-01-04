import pickle
from datetime import datetime, timedelta

import matplotlib.pyplot as plt


class OddsPlotter:

    def __init__(self, file_path: str = None):
        self.file_path = file_path
        self.matches = self.load_odds() if file_path else {}

    def load_odds(self) -> dict:
        if not self.file_path:
            return {}
        with open(self.file_path, "rb") as f:
            matches = pickle.load(f)
        return matches

    def _filter_last_n_hours(self, times, home_odds, away_odds, draw_odds, hours: int):
        """Filter data to only include the last N hours."""
        if not times:
            return times, home_odds, away_odds, draw_odds
        
        max_time = max(times)
        cutoff_time = max_time - timedelta(hours=hours)
        
        filtered_times = []
        filtered_home = []
        filtered_away = []
        filtered_draw = []
        
        for t, h, a, d in zip(times, home_odds, away_odds, draw_odds):
            if t >= cutoff_time:
                filtered_times.append(t)
                filtered_home.append(h)
                filtered_away.append(a)
                filtered_draw.append(d)
        
        return filtered_times, filtered_home, filtered_away, filtered_draw

    def iterate_plot(self, filter_hours: int = None):
        for match_key, match_data in self.matches.items():
            times = match_data.times
            home_odds = match_data.home_odds
            away_odds = match_data.away_odds
            draw_odds = match_data.draw_odds

            if filter_hours is not None:
                times, home_odds, away_odds, draw_odds = self._filter_last_n_hours(
                    times, home_odds, away_odds, draw_odds, filter_hours
                )

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
            yield plt, match_data.name
        
    def plot_odds(self, filter_hours: int = None):
        for plot,_ in self.iterate_plot(filter_hours=filter_hours):
            plot.show()

    def save_odds(self, out_dir: str, filter_hours: int = None):
        for plt, name in self.iterate_plot(filter_hours=filter_hours):
            plt.savefig(f"{out_dir}/{name.replace(' ', '_')}_odds_plot.png")
            plt.close()