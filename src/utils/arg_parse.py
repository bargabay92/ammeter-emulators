
import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="config/config.yaml", help="Path to the configuration file")
    parser.add_argument("--plot", action="store_true", help="Run measurements and generate plots for the measurements")
    parser.add_argument("--compare", action="store_true", help="Run measurements and compare results across different ammeters")
    return parser.parse_args()