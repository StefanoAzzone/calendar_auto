import argparse
import os

import yaml
from yaml import Loader


def load_config(path):
    config_file = open(path)
    config = yaml.load(config_file, Loader)
    config_file.close()
    return config


def parse_args():
    parser = argparse.ArgumentParser(
        prog="devops_auto",
        description="Automate DevOps management"
    )

    script_folder = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    parser.add_argument('-year', help="The year", required=True)
    parser.add_argument('-month', help="The month", required=True)

    args = parser.parse_args()
    return args
