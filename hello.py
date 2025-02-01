import pandas as pd

# Adjust the path to your CSV file
file_path = 'student_grades.csv'

# Read the CSV file
df = pd.read_csv(file_path)

# Show the first few rows of the data
print(df.head())
