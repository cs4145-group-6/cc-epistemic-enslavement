import pandas as pd

# Load the dataset
file_path = "resources/input/evacuation_no_ai_preprocess.csv"
data = pd.read_csv(file_path)

# DECISION ACCURACY
# Correct order for each floor
correct_order = {
    "Final Order Floor 1": 35214,
    "Final Order Floor 2": 51324,
    "Final Order Floor 3": 54123,
    "Final Order Floor 4": 24153
}

# Initialize a dictionary to store results
results = {}

total_count_overall = 0
correct_count_overall = 0

entries = data.shape[0]

# Iterate through each floor's column to compute correctness
for column, correct_value in correct_order.items():
    if column in data.columns:
        # Count the correct values (ignoring NaN)
        correct_count = (data[column] == correct_value).sum()
        # exclude missing values
        total_count = entries - data[column].isnull().sum()
        print(f"Total count for {column}: {total_count}")
        # Calculate percentage
        print(f"Correct count for {column}: {correct_count}")
        total_count_overall += total_count
        correct_count_overall += correct_count
        percentage_correct = (correct_count / total_count) * 100 if total_count > 0 else 0
        results[column] = percentage_correct

# print total count and correct count
print("Total count overall: ", total_count_overall)
print("Correct count overall: ", correct_count_overall)


# Convert results to a DataFrame for better visualization
results_df = pd.DataFrame(list(results.items()), columns=["Floor", "Percentage Correct"])

# print the results
print(results_df)

# print overall precentage correct
overall_percentage_correct = (correct_count_overall / total_count_overall) * 100 if total_count_overall > 0 else 0

print(f"Overall percentage correct: {overall_percentage_correct}")

