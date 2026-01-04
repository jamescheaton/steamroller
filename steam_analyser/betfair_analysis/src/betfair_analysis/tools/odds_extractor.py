import pickle

import betfair_data as bfd

from betfair_analysis.data.definitions import SimpleMatchOdds, market_types


class OddsExtractor:
    """
    Extracts match odds for a given team using a particular betfair data file.
    This streams the data and then saves the odds to a pickle file for the given team.
    Can filter by home/away matches.
    Can specify the event type
    """

    def __init__(self, team: str, home_only: bool = True, event_type: str = "Match Odds"):
        self.team = team
        self.home_only = home_only
        if event_type not in market_types:
            raise ValueError(f"Unsupported event type: {event_type}")
        self.event_type = event_type

    def save_odds(self, data_file: str, output_pickle: str = None):

        print("Processing data file:", data_file)
        matches = {}
        for file in bfd.Files([data_file]):
            for market in file:
                if market.in_play:
                    continue
                market_name = market.market_name
                pub_time = market.publish_time

                # only home/away games for TEAM_1
                if self.home_only and not market.event_name.startswith(f"{self.team} v "):
                    continue
                elif not market.event_name.startswith(f"{self.team} v ") and not market.event_name.endswith(f" v {self.team}"):
                    continue
                if self.event_type not in market_name:
                    continue

                print("Processing market for team:", market.event_name)


                key = f"{market.event_name} - {market.market_time}"

                if key not in matches:
                    matches[key] = SimpleMatchOdds(
                        name=key, times=[], home_odds=[], away_odds=[], draw_odds=[]
                    )

                for runner in market.runners:
                    # Home team odds
                    if self.team in runner.name:
                        matches[key].home_odds.append(runner.last_price_traded)
                    # Draw odds
                    elif "Draw" in runner.name:
                        matches[key].draw_odds.append(runner.last_price_traded)
                    # Away team odds
                    else:
                        matches[key].away_odds.append(runner.last_price_traded)
                matches[key].times.append(pub_time)
        
        if output_pickle:
            self.save_to_pickle(matches, output_pickle)
        
        return matches

    def save_to_pickle(self, matches: dict, output_pickle: str):

        with open(output_pickle, "wb") as f:
            pickle.dump(matches, f)
        print(f"Saved odds data to {output_pickle}")
