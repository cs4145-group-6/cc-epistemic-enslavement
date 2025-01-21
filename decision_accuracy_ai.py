import pandas as pd
from scipy.stats import fisher_exact

# Load the dataset
# file_path = "resources/input/evacuation-ai-justification_preprocess.csv"
file_path = "resources/input/Evacuation-ai-recommendation_preprocess.csv"
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
        total_count_overall += total_count
        correct_count_overall += correct_count
        print(f"Correct count for {column}: {correct_count}")
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


# RATES

# Initialize a dictionary to store results
metrics = {}

# Metric 1: Percentage of people who followed AI advice on floor 2
floor_2_ai = "Did you consider AI in your decision for the previous scenario (floor 2)?"
floor_2_order = "Final Order Floor 2"

# Filter rows where there's a final order for floor 2
floor_2_filtered = data[data[floor_2_order].notnull()]

# Calculate percentage
if not floor_2_filtered.empty:
    floor_2_ai_followed = (floor_2_filtered[floor_2_ai] == "Yes").sum()
    floor_2_percentage = (floor_2_ai_followed / len(floor_2_filtered)) * 100
else:
    floor_2_percentage = 0

metrics["Floor 2 AI Advice"] = floor_2_percentage

# Metric 2: Percentage of people who followed AI advice on floors 1, 3, and 4
floors = [1, 3, 4]
overall_count = 0
ai_followed_count = 0

for floor in floors:
    ai_column = f"Did you consider AI in your decision for the previous scenario (floor {floor})?"
    order_column = f"Final Order Floor {floor}"

    # Filter rows where there's a final order for the current floor
    filtered = data[data[order_column].notnull()]

    if not filtered.empty:
        overall_count += len(filtered)
        ai_followed_count += (filtered[ai_column] == "Yes").sum()

# Calculate percentage
if overall_count > 0:
    combined_percentage = (ai_followed_count / overall_count) * 100
else:
    combined_percentage = 0

metrics["Floors 1, 3, and 4 AI Advice"] = combined_percentage

# Display the metrics
metrics_df = pd.DataFrame(list(metrics.items()), columns=["Metric", "Percentage"])
print(metrics_df)


# Prepare contingency table
contingency_table = [[0, 0], [0, 0]]  # [[Followed AI & Correct, Followed AI & Incorrect], [Did Not Follow AI & Correct, Did Not Follow AI & Incorrect]]

# Process floors 1, 3, and 4
for floor in [1, 3, 4]:
    ai_column = f"Did you consider AI in your decision for the previous scenario (floor {floor})?"
    order_column = f"Final Order Floor {floor}"
    correct_value = correct_order[order_column]

    # Filter rows where there's a final order for the current floor
    filtered = data[data[order_column].notnull()]
    print(f"Floor {floor} filtered count: {len(filtered)}")
    if not filtered.empty:
        # Count cases
        followed_ai_correct = ((filtered[ai_column] == "Yes") & (filtered[order_column] == correct_value)).sum()
        followed_ai_incorrect = ((filtered[ai_column] == "Yes") & (filtered[order_column] != correct_value)).sum()
        not_followed_ai_correct = ((filtered[ai_column] == "No") & (filtered[order_column] == correct_value)).sum()
        not_followed_ai_incorrect = ((filtered[ai_column] == "No") & (filtered[order_column] != correct_value)).sum()
        print(f"Floor {floor} Followed AI & Correct: {followed_ai_correct}")
        print(f"Floor {floor} Followed AI & Incorrect: {followed_ai_incorrect}")
        print(f"Floor {floor} Did Not Follow AI & Correct: {not_followed_ai_correct}")
        print(f"Floor {floor} Did Not Follow AI & Incorrect: {not_followed_ai_incorrect}")

        # Update contingency table
        contingency_table[0][0] += followed_ai_correct
        contingency_table[0][1] += followed_ai_incorrect
        contingency_table[1][0] += not_followed_ai_correct
        contingency_table[1][1] += not_followed_ai_incorrect


# Display the contingency table
print("Contingency Table:")
print(f"Followed AI: Correct={contingency_table[0][0]}, Incorrect={contingency_table[0][1]}")
print(f"Did Not Follow AI: Correct={contingency_table[1][0]}, Incorrect={contingency_table[1][1]}")

# Perform Fisher's Exact Test
odds_ratio, p_value = fisher_exact(contingency_table, alternative='two-sided')

print("\nFisher's Exact Test Results:")
print(f"Odds Ratio: {odds_ratio}")
print(f"P-value: {p_value}")