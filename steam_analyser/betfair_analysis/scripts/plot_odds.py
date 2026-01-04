import configparser
from pathlib import Path
from betfair_analysis.tools.odds_extractor import OddsExtractor
from betfair_analysis.tools.odds_plotter import OddsPlotter


def load_config(config_file: str = "plot_odds_config.ini") -> configparser.ConfigParser:
    """Load configuration from INI file."""
    config_path = Path(__file__).parent / config_file
    config = configparser.ConfigParser()
    config.read(config_path)
    return config


def format_paths(config: configparser.ConfigParser) -> dict:
    """Format path templates with team and year values."""
    team = config.get("team", "name")
    year = config.getint("data", "year")
    
    input_file = config.get("data", "input_file").format(year=year)
    output_directory = config.get("data", "output_directory").format(team=team, year=year)
    
    return {
        "team": team,
        "year": year,
        "input_file": input_file,
        "output_directory": output_directory,
        "filter_hours": config.getint("plotting", "filter_hours"),
        "save_to_file": config.getboolean("plotting", "save_to_file"),
        "home_only": config.getboolean("team", "home_only"),
        "event_type": config.get("market", "event_type")
    }


if __name__ == "__main__":
    # Load and parse configuration
    config = load_config()
    settings = format_paths(config)
    
    team = settings["team"]
    input_file = settings["input_file"]
    output_directory = settings["output_directory"]
    filter_hours = settings["filter_hours"]
    save_to_file = settings["save_to_file"]
    home_only = settings["home_only"]
    event_type = settings["event_type"]

    # Read and process odds directly from the data file without saving to intermediate pickle
    extractor = OddsExtractor(team=team, home_only=home_only, event_type=event_type)
    matches = extractor.save_odds(data_file=input_file, output_pickle=None)
    
    # Create plotter with the matches and plot
    plotter = OddsPlotter()
    plotter.matches = matches
    
    # Save plots to files
    if save_to_file:
        import os
        os.makedirs(output_directory, exist_ok=True)
        plotter.save_odds(out_dir=output_directory, filter_hours=filter_hours)
    else:
        print("Saving disabled in configuration (save_to_file: false)")
