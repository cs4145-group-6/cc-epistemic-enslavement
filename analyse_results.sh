# Set variables
INPUT_PATH="resources/input/Evacuation_Task_with_AI_recomme2025-01-20_15_09_17.csv"
OUTPUT_PATH="resources/output/analysis_results.json"

# Install requirements
pip install -r requirements.txt

# Analyse results
python main.py --input_path $INPUT_PATH --output_path $OUTPUT_PATH
