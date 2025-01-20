"""
Module containing functionality to analyse experimental results.
"""
from dataclasses import dataclass
from typing import List, Hashable, Callable, Dict

import pandas as pd
from pandas import Series


@dataclass
class FloorResult:
    """
    Class storing submission data for a floor.
    """
    floor_number: int
    time_left: int  # seconds
    evacuation_order: List[int]
    used_ai_advice: bool


@dataclass
class SurveySubmission:
    """
    Class storing a survey submission of a user.
    """
    prolific_id: str
    floor_data: List[FloorResult]


@dataclass
class EvaluationMetric:
    """
    Class to represent an evaluation metric.
    """
    metric_name: str
    computation_function: Callable[[List[SurveySubmission]], float]  # Function to calculate the metric given a list of submissions


def calculate_average_correct_score(submissions: List[SurveySubmission]) -> float:
    """
    Over all submission, calculate the average percentage of correct evacuation orders.

    :param: The list of survey submissions
    :return: The average percentage of correct evacuation orders
    """
    if len(submissions) == 0:
        return -1.0

    correct_orders = {
        1: [3, 5, 2, 1, 4],
        2: [5, 1, 3, 2, 4],
        3: [5, 4, 1, 2, 3],
        4: [2, 4, 1, 5, 3],
    }

    accum_score = 0.0
    floor_count = len(submissions) * len(submissions[0].floor_data)

    for submission in submissions:
        for floor in submission.floor_data:
            if floor.evacuation_order == correct_orders[floor.floor_number]:
                accum_score += 100.0

    return accum_score/floor_count


def read_submission(row: (Hashable, Series)) -> SurveySubmission:
    """
    Convert a dataframe row to a user's submission.

    :param row: Dataframe row
    :return: User's submission
    """
    prolific_id = row["Get Page URL"].split("?PROLIFIC_PID=")[1].split("&")[0]

    floor_data = []
    # iterate over 4 floors
    for i in range(1, 5):
        evacuation_order = []
        for order in ['first', 'second', 'third', 'fourth', 'fifth']:
            key = f"Which room should be evacuated {order} on floor {i}?"
            evacuation_order.append(int(row[key].replace("Room ", "")))
        time_remaining_string = row[f"time-left-floor-{i}"]
        minutes = int(time_remaining_string.split(": ")[1].split(":")[0])
        seconds = int(time_remaining_string.split(": ")[1].split(":")[1])
        time_remaining = minutes * 60 + seconds
        used_ai_advice = False
        try:
            used_ai_advice = row[f"Did you consider AI in your decision for the previous scenario (floor {i})?"] == 'Yes'
        except KeyError:
            print('Value for AI consideration not found (can be safely ignored if not part of the survey)')

        floor_data.append(FloorResult(i, time_remaining, evacuation_order, used_ai_advice))

    return SurveySubmission(prolific_id, floor_data)


def read_submissions(dataframe: pd.DataFrame) -> List[SurveySubmission]:
    """
    Convert dataframe into a list of survey submissions.

    :param dataframe: The dataframe to read
    :return: List of survey submissions
    """
    return [read_submission(row) for _, row in dataframe.iterrows()]


def analyse_results(dataframe: pd.DataFrame) -> Dict[str, float]:
    """
    Analyse experimental results.

    :param dataframe: Dataframe containing experimental results
    :return: Dictionary with evaluation metric name as keys and the values as evaluation results
    """
    # TODO implement all metrics and add them to the metrics list
    # TODO explain here and in README what metrics we use to analyse results
    submissions = read_submissions(dataframe)
    correct_metric = EvaluationMetric('average correct percentage', calculate_average_correct_score)
    metrics = [correct_metric]

    results = {}

    # Calculate all metrics for the submission
    for metric in metrics:
        results[metric.metric_name] = metric.computation_function(submissions)

    return results
