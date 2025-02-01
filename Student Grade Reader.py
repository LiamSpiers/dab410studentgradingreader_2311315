import pandas as pd

# This reads the CSV file and turns it into a DataFrame
file_path = 'student_grades.csv'
df = pd.read_csv(file_path)

# This prints  the entire DataFrame
print(df.to_string())

# This calculates the average student grade
average_grade = df['grade'].mean()

# This calculates the average student attendance
average_attendance = df['attendance'].mean()

# This calculates the number of students who failed (a grade < 40)
number_of_fails = len(df[df['grade'] < 40])

# This calculates the number of students who passed (a grade > or = 40)
number_of_passes = len(df[df['grade'] >= 40])

# This Calculates the number of As, Bs and C grades
# A grade = 70+
# B grade = 50-69
# C grade = 40-49
number_of_As = len(df[df['grade'] >= 70])
number_of_Bs = len(df[(df['grade'] >= 50) & (df['grade'] < 70)])
number_of_Cs = len(df[(df['grade'] >= 40) & (df['grade'] < 50)])

# This prints the results in a clear easy to read view
print(f"The average student grade is: {average_grade}")
print(f"The average student attendance is: {average_attendance}")
print(f"The number of students who failed (grade below 40) is: {number_of_fails}")
print(f"The number of students who passed (grade 40 and above) is: {number_of_passes}")
print(f"The number of students with grade A (70 and above) is: {number_of_As}")
print(f"The number of students with grade B (50-69) is: {number_of_Bs}")
print(f"The number of students with grade C (40-49) is: {number_of_Cs}")
