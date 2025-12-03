# -*- coding: utf-8 -*-
"""
Created on Wed Dec  3 12:01:22 2025

@author: DELL
"""
#Author:Aadit Prashar
#Roll Number: 2501010073
#Course:B-Tech CSE
#DATE:3-12-2025


import csv
import pandas as pd    # <-- Pandas added

# ---------------- INPUT METHODS -------------------

def input_manual():
    marks = {}
    total = int(input("Enter number of students: "))

    for i in range(total):
        name = input("Enter student's name: ")
        score = int(input("Enter marks: "))
        marks[name] = score
    return marks


def input_csv(file_name):
    marks = {}
    file = open(file_name, "r")
    reader = csv.reader(file)

    for row in reader:
        name = row[0]
        score = int(row[1])
        marks[name] = score

    file.close()
    return marks


# ---------------- FUNCTIONS -----------------------

def average_score(marks):
    return sum(marks.values()) / len(marks)


def median_score(marks):
    nums = sorted(marks.values())
    n = len(nums)
    mid = n // 2

    if n % 2 == 1:
        return nums[mid]
    else:
        return (nums[mid - 1] + nums[mid]) / 2


def max_scored(marks):
    name = max(marks, key=marks.get)
    return name, marks[name]


def min_scored(marks):
    name = min(marks, key=marks.get)
    return name, marks[name]


def grades_given(marks):
    grades = {}
    for name, score in marks.items():
        if score >= 90:
            grades[name] = "A"
        elif score >= 80:
            grades[name] = "B"
        elif score >= 70:
            grades[name] = "C"
        elif score >= 60:
            grades[name] = "D"
        else:
            grades[name] = "F"
    return grades


def grade_count(grades):
    count = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    for g in grades.values():
        count[g] += 1
    return count


def passed_failed(marks):
    passed = [name for name, score in marks.items() if score >= 40]
    failed = [name for name, score in marks.items() if score < 40]
    return passed, failed


# ---------------- PANDAS TABLE ---------------------

def pandas_table(marks, grades):
    df = pd.DataFrame({
        "Name": list(marks.keys()),
        "Marks": list(marks.values()),
        "Grade": [grades[n] for n in marks]
    })

    print("\n--- ANALYSIS TABLE ---")
    print(df)


# ---------------- MAIN PROGRAM ---------------------

def main():
    print("---------------------------------")
    print("       GRADEBOOK ANALYSIS        ")
    print("---------------------------------")

    while True:
        print("\n1. Enter data manually")
        print("2. Upload CSV file")
        print("3. Exit")
        option = input("Enter your option: ")

        if option == "1":
            marks = input_manual()

        elif option == "2":
            file_name = input("Enter CSV filename: ")
            marks = input_csv(file_name)

        elif option == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice! Try again.")
            continue

        # ---- CALCULATIONS ----
        avg = average_score(marks)
        med = median_score(marks)
        top_name, top_score = max_scored(marks)
        bottom_name, bottom_score = min_scored(marks)

        print("\n--- RESULTS ---")
        print("Average:", avg)
        print("Median:", med)
        print("Highest:", top_name, top_score)
        print("Lowest:", bottom_name, bottom_score)

        grades = grades_given(marks)
        passed, failed = passed_failed(marks)

        print("\nPassed:", passed)
        print("Failed:", failed)

        # ---- PANDAS TABLE ----
        pandas_table(marks, grades)


# Run program---------------------------
main()
