from flask import Flask, render_template, request, jsonify
import pandas as pd
import os

app = Flask(__name__)

# Initialize CSV files if they don't exist
if not os.path.exists('students.csv'):
    pd.DataFrame(columns=['name']).to_csv('students.csv', index=False)
if not os.path.exists('marks.csv'):
    pd.DataFrame(columns=['student_name', 'lab_name', 'mark']).to_csv('marks.csv', index=False)
if not os.path.exists('labs.csv'):
    pd.DataFrame(columns=['lab_name']).to_csv('labs.csv', index=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/students', methods=['POST'])
def create_student():
    data = request.json
    students_df = pd.read_csv('students.csv')
    
    if data['name'] in students_df['name'].values:
        return jsonify({"status": "error", "message": "Student already exists"}), 400
        
    new_student = pd.DataFrame([{'name': data['name']}])
    students_df = pd.concat([students_df, new_student], ignore_index=True)
    students_df.to_csv('students.csv', index=False)
    return jsonify({"status": "success"})


@app.route('/api/add_mark', methods=['POST'])
def add_mark():
    data = request.json
    marks_df = pd.read_csv('marks.csv')
    
    # Update existing mark or add new one
    existing = marks_df[
        (marks_df['student_name'] == data['student_name']) & 
        (marks_df['lab_name'] == data['lab_name'])
    ]
    
    if len(existing) > 0:
        marks_df.loc[existing.index, 'mark'] = data['mark']
    else:
        new_mark = pd.DataFrame({
            'student_name': [data['student_name']],
            'lab_name': [data['lab_name']],
            'mark': [data['mark']]
        })
        marks_df = pd.concat([marks_df, new_mark], ignore_index=True)
    
    marks_df.to_csv('marks.csv', index=False)
    return jsonify({"status": "success"})

@app.route('/api/labs', methods=['GET'])
def get_labs():
    labs = pd.read_csv('labs.csv')
    return jsonify(labs.to_dict('records'))

@app.route('/api/labs', methods=['POST'])
def create_lab():
    data = request.json
    labs_df = pd.read_csv('labs.csv')
    
    if data['lab_name'] in labs_df['lab_name'].values:
        return jsonify({"status": "error", "message": "Lab already exists"}), 400
        
    new_lab = pd.DataFrame([{'lab_name': data['lab_name']}])
    labs_df = pd.concat([labs_df, new_lab], ignore_index=True)
    labs_df.to_csv('labs.csv', index=False)
    return jsonify({"status": "success"})

@app.route('/api/get_marks/<student_name>')
def get_marks(student_name):
    marks_df = pd.read_csv('marks.csv')
    student_marks = marks_df[marks_df['student_name'] == student_name]
    return jsonify(student_marks.to_dict('records'))

@app.route('/api/all_students_marks')
def all_students_marks():
    students_df = pd.read_csv('students.csv')
    marks_df = pd.read_csv('marks.csv')
    labs_df = pd.read_csv('labs.csv')
    
    # Create a list to store all student data
    result = []
    
    for _, student in students_df.iterrows():
        student_data = {
            'name': student['name'],
            'marks': {}
        }
        
        # Get all marks for this student
        student_marks = marks_df[marks_df['student_name'] == student['name']]
        
        # Initialize all labs with None (no mark)
        for _, lab in labs_df.iterrows():
            student_data['marks'][lab['lab_name']] = None
            
        # Fill in the actual marks
        for _, mark in student_marks.iterrows():
            student_data['marks'][mark['lab_name']] = mark['mark']
            
        result.append(student_data)
    
    return jsonify(result)

# Removed direct running since we now use main.py
