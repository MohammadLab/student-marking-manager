import pandas as pd

# Sample students
students = [
    {'student_id': 1, 'name': 'John Smith'},
    {'student_id': 2, 'name': 'Emma Wilson'},
    {'student_id': 3, 'name': 'Michael Brown'},
    {'student_id': 4, 'name': 'Sarah Davis'},
    {'student_id': 5, 'name': 'James Johnson'}
]

# Sample marks
marks = [
    {'student_id': 1, 'lab_name': 'lab1', 'mark': 85},
    {'student_id': 1, 'lab_name': 'lab2', 'mark': 92},
    {'student_id': 2, 'lab_name': 'lab1', 'mark': 88},
    {'student_id': 3, 'lab_name': 'lab1', 'mark': 78},
    {'student_id': 4, 'lab_name': 'lab1', 'mark': 95}
]

# Save to CSV files
pd.DataFrame(students).to_csv('students.csv', index=False)
pd.DataFrame(marks).to_csv('marks.csv', index=False)

print("Sample data has been created!")
