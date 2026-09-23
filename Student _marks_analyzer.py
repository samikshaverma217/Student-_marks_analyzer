# Student Marks Analyzer
# Made by Samiksha V. - CSE Data Science

students = {
    "Aman": 85,
    "Rahul": 72,
    "Priya": 91,
    "Anjali": 45,
    "Vikram": 68,
    "Samiksha": 88
}

print("--- Student Marks Report ---")
average = sum(students.values()) / len(students)
print(f"Average Marks: {average:.2f}")

highest_student = max(students, key=students.get)
print(f"Highest Marks: {highest_student} - {students[highest_student]}")

print("\n--- Pass / Fail Status (Pass = 50+) ---")
for name, marks in students.items():
    status = "Pass" if marks >= 50 else "Fail"
    print(f"{name}: {marks} - {status}")

passed = sum(1 for m in students.values() if m >= 50)
print(f"\nTotal Passed: {passed} out of {len(students)}")
