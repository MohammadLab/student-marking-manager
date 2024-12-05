# Student Marks Manager

A web-based application for managing student lab marks with an intuitive interface.

## Features

- 🔍 Real-time student search with auto-suggestions
- ➕ Add new students on the fly
- 📝 Create and manage lab assignments
- ✏️ Add marks for multiple labs simultaneously
- 📊 View all student marks in a comprehensive table
- 💾 Automatic data persistence using CSV storage

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/YOUR_ACTUAL_GITHUB_USERNAME/student-marks-manager.git
cd student-marks-manager
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Linux/Mac
# or
venv\Scripts\activate     # On Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the application:
```bash
python main.py
```

2. Open your web browser and navigate to:
```
http://localhost:8080
```

## Data Storage

The application automatically manages three CSV files:
- `students.csv`: Student records
- `labs.csv`: Lab assignment definitions
- `marks.csv`: Student marks for each lab

These files are created automatically on first run.

## Development

To contribute to this project:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
