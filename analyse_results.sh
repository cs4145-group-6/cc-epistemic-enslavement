# Set variables
INPUT_PATH="resources/input/Evacuation_Task_with_AI_recomme2025-01-19_08_03_47.csv"
OUTPUT_PATH="resources/output/analysis_results.csv"

# Install requirements
pip install -r requirements.txt

# Analyse results
python main.py --input_path $INPUT_PATH --output_path $OUTPUT_PATH
