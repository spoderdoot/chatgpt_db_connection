# chatgpt_db_connection 
This project sets up a DB and API for the local use with ChatGPT. The database uses **SQLite** and **Flask** is used to provide server functionalities.

# Requirements
* Install Python 3.11.4

# Setup

## Enable the virtual environment to use the application 

1. Create the virtual environment  
`python -m venv env`

2. Activate to the virtual environment  
```
cd env/  
source Scripts/activate
```

## Install the dependencies
* Navigate to the virtual environment and execute:  
`pip install -r ../requirements.txt`
### Dependencies  
- Flask  
Flask enables the software to provide API endpoints. These can be called by external services such as ChatGPT via a Plugin and others.
