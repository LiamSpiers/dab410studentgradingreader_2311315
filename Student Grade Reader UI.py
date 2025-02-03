import pandas as pd
import tkinter as tk
from tkinter import messagebox

# This reads the CSV file and turns it into a DataFrame
file_path = 'student_grades.csv'

#This allows the program to inform user and exit gracefully without crashing if CSV file is missing or the path is incorrect
#This will also inform the user how to use the program with instructions
try:
    df = pd.read_csv(file_path)
except FileNotFoundError:
    print("Error: CSV file not found.")
    print(
        "Please make sure your CSV file is named 'student_grades.csv' and is located in the same directory as this script.")
    exit()

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

# This creates the main window for the user interface (UI)
window = tk.Tk()
window.title("Student Grade Reader")


# This function is used to display the selected result
def show_result(choice):
    # Debugging - this confirms the function is being run
    print(f"Button clicked: {choice}")

    # This checks which option was clicked and then displays the correct result
    if choice == "Average Grade":
        result = f"The average student grade is: {average_grade}"
    elif choice == "Average Attendance":
        result = f"The average student attendance is: {average_attendance}"
    elif choice == "Number of Fails":
        result = f"The number of students who failed (grade below 40) is: {number_of_fails}"
    elif choice == "Number of Passes":
        result = f"The number of students who passed (grade 40 and above) is: {number_of_passes}"
    elif choice == "Number of As":
        result = f"The number of students with grade A (70 and above) is: {number_of_As}"
    elif choice == "Number of Bs":
        result = f"The number of students with grade B (50-69) is: {number_of_Bs}"
    elif choice == "Number of Cs":
        result = f"The number of students with grade C (40-49) is: {number_of_Cs}"

    # Debugging - Was unable to get the buttons to provide results, This prints the result before updating the label
    print(f"Result to display: {result}")

    # This clears the label text before updating it
    result_label.config(text="")

    # This updates the label with the result
    result_label.config(text=result, font=("Helvetica", 12))

    # This forces an update to the window
    window.update()


# This creates a button for each option
button1 = tk.Button(window, text="Average Grade", command=lambda: show_result("Average Grade"))
button1.pack(pady=10)

button2 = tk.Button(window, text="Average Attendance", command=lambda: show_result("Average Attendance"))
button2.pack(pady=10)

button3 = tk.Button(window, text="Number of Fails", command=lambda: show_result("Number of Fails"))
button3.pack(pady=10)

button4 = tk.Button(window, text="Number of Passes", command=lambda: show_result("Number of Passes"))
button4.pack(pady=10)

button5 = tk.Button(window, text="Number of As", command=lambda: show_result("Number of As"))
button5.pack(pady=10)

button6 = tk.Button(window, text="Number of Bs", command=lambda: show_result("Number of Bs"))
button6.pack(pady=10)

button7 = tk.Button(window, text="Number of Cs", command=lambda: show_result("Number of Cs"))
button7.pack(pady=10)

# This creates a label to display the result
result_label = tk.Label(window, text="", font=("Helvetica", 12), wraplength=300)
result_label.pack(pady=20)

window.mainloop()