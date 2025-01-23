"""
Module containing functionality relating to file utilities.
"""
import json
from typing import Dict

import pandas as pd


def load_csv(file_path: str) -> pd.DataFrame:
    """
    Load a csv file as a pandas dataframe.

    :param file_path: Path to csv file containing experimental results
    :return: Dataframe containing experimental results
    """
    return pd.read_csv(file_path)


def save_to_csv(results: Dict[str, float], output_path: str) -> None:
    """
    Save results of experimental analysis to a json file.

    :param results: Results of the experiment
    :param output_path: Path to a json file where results should be saved
    """
    with open(output_path, "w") as jsonfile:
        json.dump(results, jsonfile, indent=4)
