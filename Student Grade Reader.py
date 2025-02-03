import pandas as pd

# Read the CSV file and create a DataFrame
file_path = 'student_grades.csv'

try:
    df = pd.read_csv(file_path)
except FileNotFoundError:
    print("Error: CSV file not found.")
    print("Ensure the file is named 'student_grades.csv' and is in the same directory as this script.")
    exit()

# his will check the actual column names in the CSV
df.columns = df.columns.str.strip()  # Debugging - Strips any accidental spaces around column names so you are able to find student just by first or last name
print(f"Column names in the CSV: {list(df.columns)}")  # Debugging - This verifies the column names

# This verifies if the 'grade' and 'attendance' columns exist
if 'grade' not in df.columns or 'attendance' not in df.columns:
    print("Error: CSV file must include 'grade' and 'attendance' columns.")
    exit()

# This combines the first and last name into a full name column and strips spaces
df['name'] = (df['first_name'].str.strip() + ' ' + df['last_name'].str.strip())

# This displays the entire DataFrame
print(df.to_string())

# This calculates the average student grade
average_grade = df['grade'].mean()

# This calculates the average student attendance
average_attendance = df['attendance'].mean()

# This calculates the number of students who failed (a grade < 40)
number_of_fails = len(df[df['grade'] < 40])

# This calculates the number of students who passed (a grade > or = 40)
number_of_passes = len(df[df['grade'] >= 40])

# This Calculates the number of As, Bs and Cs
# A grade = 70+
# B grade = 50-69
# C grade = 40-49
number_of_As = len(df[df['grade'] >= 70])
number_of_Bs = len(df[(df['grade'] >= 50) & (df['grade'] < 70)])
number_of_Cs = len(df[(df['grade'] >= 40) & (df['grade'] < 50)])

# This is how it will display the  results
print(f"\nThe average student grade is: {average_grade}")
print(f"The average student attendance is: {average_attendance}")
print(f"The number of students who failed (grade below 40) is: {number_of_fails}")
print(f"The number of students who passed (grade 40 and above) is: {number_of_passes}")
print(f"The number of students with grade A (70 and above) is: {number_of_As}")
print(f"The number of students with grade B (50-69) is: {number_of_Bs}")
print(f"The number of students with grade C (40-49) is: {number_of_Cs}")


# This is the Search Feature with will include partial matching to help user experience
def search_student(name):
    try:
        # This strips any extra spaces from the search input and make it case-insensitive
        name = name.strip().lower()

        # This will attempt exact matching first
        student_info = df[df['name'].str.lower() == name]

        if student_info.empty:
            # If no exact match, try partial matching (contains)
            student_info = df[df['name'].str.lower().str.contains(name)]

        if not student_info.empty:
            grade = student_info['grade'].values[0]
            attendance = student_info['attendance'].values[0]
            print(f"\nStudent Found: {student_info['name'].values[0]}")
            print(f"Grade: {grade}")
            print(f"Attendance: {attendance}%")
        else:
            print(f"\nStudent '{name}' not found in the records.")
    except Exception as e:
        print(f"An error occurred while searching: {e}")


# This will promt the user for student name to search if they wanted
# This will inform user how to use the program and how to exit
while True:
    search_name = input("\nEnter a student's name to view their grade and attendance (or type 'exit' to quit): ")
    if search_name.lower() == 'exit':
        print("Exiting the program.")
        break
    search_student(search_name)
