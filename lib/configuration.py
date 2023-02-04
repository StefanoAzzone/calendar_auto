import argparse
import os
from datetime import datetime

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

    current_month = datetime.now().month
    current_year = datetime.now().year

    parser.add_argument('-year', default=current_year, help="The year")
    parser.add_argument('-month', default=current_month, help="The month")
    parser.add_argument('-scope',
                        default='day',
                        choices=['day', 'hour'],
                        help='The time measure to return, either day or hour. Defaults to day.')
    parser.add_argument('-view',
                        choices=['week', 'project'],
                        default='week',
                        help='The view to create: either work time per week or work time per project. Defaults to week')

    args = parser.parse_args()
    return args
