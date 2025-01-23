# Set variables
INPUT_PATH="resources/input/evacuation-ai-justification.csv"
OUTPUT_PATH="resources/output/analysis_results.json"

# Install requirements
pip install -r requirements.txt

# Analyse results
python main.py --input_path $INPUT_PATH --output_path $OUTPUT_PATH
