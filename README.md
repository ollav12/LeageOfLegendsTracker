# LeageOfLegendsTracker FastAPI project

## Prerequisites
- Python 3.7 or higher
- `pip` (Python package installer)
- Git (for version control)

## Setup Instructions

### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/ollav12/LeageOfLegendsTracker
cd your-repository
```

### 2. Create and Activate a Virtual Environment

#### On Windows
```bash
python -m venv venv
.\venv\Scripts\activate
```
#### On MacOS/Linux
```bash
python -m venv venv
source venv/bin/activate
```
### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a .env file in the root directory of the project and add your environment variables.
Look at .env.example for what to include.

### 5. Run the Application
```bash
uvicorn app.main:app --reload
```

### 6. Access the Application
```bash
http://127.0.0.1:8000
```
You should now see the homepage of the application.

## Project Structure

```bash 
project_root/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   ├── js/
│   │   │   └── script.js
│   │   └── images/
│   └── templates/
│       └── index.html
│
├── .env     # Your .env file created for environment variables
├── .gitignore
├── requirements.txt
└── venv/    # Virtual environment directory
```

### License
This project is licensed under the MIT License - see the LICENSE file for details.