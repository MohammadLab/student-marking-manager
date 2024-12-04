from flask import Flask, render_template, request, jsonify
import pandas as pd
import os

app = Flask(__name__)

# Initialize CSV files if they don't exist
if not os.path.exists('students.csv'):
    pd.DataFrame(columns=['student_id', 'name']).to_csv('students.csv', index=False)
if not os.path.exists('marks.csv'):
    pd.DataFrame(columns=['student_id', 'lab_name', 'mark']).to_csv('marks.csv', index=False)
if not os.path.exists('labs.csv'):
    pd.DataFrame(columns=['lab_name']).to_csv('labs.csv', index=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/students', methods=['GET'])
def get_students():
    students = pd.read_csv('students.csv')
    return jsonify(students.to_dict('records'))

@app.route('/api/search_student', methods=['GET'])
def search_student():
    query = request.args.get('query', '').lower()
    students = pd.read_csv('students.csv')
    filtered = students[students['name'].str.lower().str.contains(query, na=False)]
    return jsonify(filtered.to_dict('records'))

@app.route('/api/add_mark', methods=['POST'])
def add_mark():
    data = request.json
    marks_df = pd.read_csv('marks.csv')
    
    # Update existing mark or add new one
    existing = marks_df[
        (marks_df['student_id'] == data['student_id']) & 
        (marks_df['lab_name'] == data['lab_name'])
    ]
    
    if len(existing) > 0:
        marks_df.loc[existing.index, 'mark'] = data['mark']
    else:
        new_mark = pd.DataFrame([data])
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

@app.route('/api/get_marks/<student_id>')
def get_marks(student_id):
    marks_df = pd.read_csv('marks.csv')
    student_marks = marks_df[marks_df['student_id'] == int(student_id)]
    return jsonify(student_marks.to_dict('records'))

# Removed direct running since we now use main.py
