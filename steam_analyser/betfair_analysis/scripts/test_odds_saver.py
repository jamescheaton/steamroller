import os
from betfair_analysis.tools.odds_extractor import OddsExtractor

if __name__ == "__main__":

    TEAM = "Arsenal"
    YEAR = 2025
    FILE = f"./data/UK_football_{str(YEAR)}.tar"

    extractor = OddsExtractor(team=TEAM, home_only=True, event_type="Match Odds")
    out_dir = f"./data/{YEAR}/{TEAM}"

    os.makedirs(out_dir, exist_ok=True)
    output_pickle = f"{out_dir}/{TEAM.replace(' ', '_')}_home_match_odds.pkl"
    extractor.save_odds(data_file=FILE, output_pickle=output_pickle)


