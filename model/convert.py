import pandas as pd

# Function to check if a value is a likely human name (basic assumption: strings with alphabets)
def is_human_name(value):
    return value.isalpha() and value.lower() != 'name'  # Ignore the keyword 'name'

# Step 1: Read the `new.data` file
file_path = 'new.data'  # Adjust this path to your actual file location

# Read the file into a list of lines
with open(file_path, 'r') as file:
    lines = file.readlines()

# Step 2: Reorganize the data (combine lines until a name or 'name' is found)
records = []
temp_record = []

for line in lines:
    values = line.strip().split()  # Split each line into values
    temp_record.extend(values)  # Add the current line's values to the temporary record
    
    # Check if the last value is a human name or the keyword 'name'
    if len(values) > 0 and (is_human_name(values[-1]) or 'name' in values):
        # End of a record (because a human name or 'name' signals the end of a record)
        records.append(temp_record)  # Save the full record
        temp_record = []  # Start a new record

# Step 3: Create a DataFrame from the records
df = pd.DataFrame(records)

# Step 4: Select the required columns (adjusted for 0-indexing in Python)
columns_needed = [2, 3, 8, 9, 11, 15, 18, 31, 37, 39, 40, 43, 50, 57]

# Ensure the required columns are within bounds of the dataset
valid_columns = [col for col in columns_needed if col < df.shape[1]]

# Select only the needed columns
selected_data = df.iloc[:, valid_columns]

# Step 5: Modify the column corresponding to index 50 from the original dataset
# We need to find the actual position of this column in the `selected_data` DataFrame.
# It's located at index 12 in the selected columns list.

# Apply the transformation: 3 -> 1, 6 -> 2, 7 -> 3
selected_data.iloc[:, 12] = selected_data.iloc[:, 12].replace({'3': '1', '6': '2', '7': '3'})

# Step 6: Save the selected attributes into a CSV file
selected_data.to_csv('heart.csv', index=False, header=False)
print("Selected attributes from `new.data` saved successfully, including column transformation for values 3, 6, and 7.")
