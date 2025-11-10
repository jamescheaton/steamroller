from dataclasses import dataclass
from typing import List


@dataclass
class SimpleMatchOdds:
    """
    Represents simplified match odds data for a football match.
    """
    
    name: str
    times: List[datetime]
    home_odds: List[float]
    away_odds: List[float]
    draw_odds: List[float]

market_types = [
    "Match Odds",
]