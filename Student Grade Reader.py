import pandas as pd
import matplotlib.pyplot as plt

# This reads the CSV file and turns it into a DataFrame
file_path = 'student_grades.csv'

#This allows the program to inform user and exit gracefully without crashing if CSV file is missing or the path is incorrect
#This will also inform the user how to use the program with instructions
try:
    df = pd.read_csv(file_path)
except FileNotFoundError:
    print("Error: CSV file not found.")
    print( "Please make sure your CSV file is named 'student_grades.csv' and is located in the same directory as this script.")
    exit()


# This verifies if grade and attendance columns exist, informs user reason for error
if 'grade' not in df.columns or 'attendance' not in df.columns:
    print("Error: CSV file must include 'grade' and 'attendance' columns.")
    exit()

# This combines first and last name into a full name column and strip feature to strip any extra spaces so user can search for just first or last name.
df['name'] = (df['first_name'].str.strip() + ' ' + df['last_name'].str.strip())


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

# This prints results in the terminal in a clear way for the user
print(f"\nThe average student grade is: {average_grade}")
print(f"The average student attendance is: {average_attendance}")
print(f"The number of students who failed (grade below 40) is: {number_of_fails}")
print(f"The number of students who passed (grade 40 and above) is: {number_of_passes}")
print(f"The number of students with grade A (70 and above) is: {number_of_As}")
print(f"The number of students with grade B (50-69) is: {number_of_Bs}")
print(f"The number of students with grade C (40-49) is: {number_of_Cs}")

    # This groups by 'country' and calculates the average grade for each country
average_grade_by_country = df.groupby('country')['grade'].mean().sort_values(ascending=False)

# This limits the number of countries to the top 10 so the graph is not too overcrowded and unreadable
top_n = 10
average_grade_by_country = average_grade_by_country.head(top_n)

# This creates a bar chart that shows the average grades by country
def plot_average_grade_by_country():
    plt.figure(figsize=(10, 6))
    average_grade_by_country.plot(kind='bar', color='skyblue')

    plt.title(f"Top {top_n} Countries by Average Student Grade", fontsize=14)
    plt.xlabel("Country", fontsize=12)
    plt.ylabel("Average Grade", fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

# This displays the graph
plot_average_grade_by_country()

# This is the search function for individual student
def search_student(name):
    try:
        name = name.strip().lower()
        student_info = df[df['name'].str.lower() == name]

        if student_info.empty:
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

# This is a loop to allow search and display results
while True:
    search_name = input("\nEnter a student's name to view their grade and attendance (or type 'exit' to quit): ")
    if search_name.lower() == 'exit':
        print("Exiting the program.")
        break
    search_student(search_name)
