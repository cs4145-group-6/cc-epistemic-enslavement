"""
Module containing functionality relating to file utilities.
"""
from typing import Any

import pandas as pd


def load_csv(file_path: str) -> pd.DataFrame:
    """
    Load a csv file as a pandas dataframe.

    :param file_path: Path to csv file containing experimental results
    :return: Dataframe containing experimental results
    """
    return pd.read_csv(file_path)


# TODO implement this method
# TODO determine type of results and remove Any import
def save_to_csv(results: Any, output_path: str) -> None:
    """
    Save results of experimental analysis to a csv file.

    :param results: Results of the experiment
    :param output_path: Path to a csv file where results should be saved
    :return:
    """
    pass
