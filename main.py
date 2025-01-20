"""
Main script for analysing and loading experimental results.
"""
from argparse import ArgumentParser, Namespace

from analysis import analyse_results
from file_utils import load_csv, save_to_csv


def get_args() -> Namespace:
    """
    Get arguments from command line.

    ** input_path: file path (relative to root directory) of csv file containing experimental results.
    ** output_path: file path (relative to root directory) to which results should be saved. The file should have a json extension.

    :return: Namespace containing arguments
    """
    parser = ArgumentParser()

    parser.add_argument('--input_path', type=str)
    parser.add_argument('--output_path', type=str)

    return parser.parse_args()


def main() -> None:
    """
    Main method.
    Analyses experimental results from csv file.
    """
    args = get_args()
    input_path = args.input_path
    output_path = args.output_path

    # Load data from csv file
    dataframe = load_csv(input_path)

    # Analyse results
    results = analyse_results(dataframe)

    # Save results to json
    save_to_csv(results, output_path)


if __name__ == '__main__':
    main()
