from betfair_analysis.tools.odds_saver import OddsSaver

if __name__ == "__main__":

    TEAM = "Arsenal"
    FILE = "./data/football_2022.tar"

    saver = OddsSaver(team=TEAM, home_only=True, event_type="Match Odds")
    output_pickle = f"./data/{TEAM.replace(' ', '_')}_home_match_odds_2022.pkl"
    saver.save_odds(data_file=FILE, output_pickle=output_pickle)


