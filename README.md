# Student Marks Manager

A simple web application to manage student marks for lab assignments.

## Setup

1. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Linux/Mac
# or
venv\Scripts\activate  # On Windows
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

4. Open your browser and go to: http://localhost:5000

## Features

- Search for students by name
- Add/update marks for lab assignments
- View all marks for a student
- Automatic CSV storage of data

## Sample Data

The application will create two CSV files on first run:
- students.csv: Contains student information
- marks.csv: Contains marks for lab assignments
