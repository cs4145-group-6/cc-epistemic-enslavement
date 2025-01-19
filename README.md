# Experimental Results Analysis Epistemic Enslavement
This repository contains code to analyse results from a study about Human-AI decision-making under stress in the presence of epistemic enslavement.

## Repository Structure
The repository is organized in a simple manner.
- The [main.py](main.py) file functions as the entrypoint of the experiment.
- The [analysis.py](analysis.py) file contains code to analyse the results.
- The [file_utils.py](file_utils.py) file contains code to load and save files.
- The [analyse_results.sh](analyse_results.sh) file can be used to execute the full pipeline.
- The resources directory contains two directories, one for input file (where the experiment results should be placed) and another for output files where results should be saved.

## Run Instructions
First make sure that input and output variables are properly set up in the [analyse_results.sh](analyse_results.sh) file.
Then you can run this script after which results will be saved to your specified output file (make sure this is a csv file).
