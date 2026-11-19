
import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="config/config.yaml")
    parser.add_argument("--plot", action="store_true")
    parser.add_argument("--compare", action="store_true")
    return parser.parse_args()