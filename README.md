# chatgpt_db_connection 
This project sets up a DB and API for the local use with ChatGPT. The database uses **SQLite** and **Flask** is used to provide server functionalities. The API is documented with **Swagger**. To provide the endpoints to a GPT **ngrok** is required.

# Requirements
- Python 3.11.4
- SQLite 2.6.0 (comes pre-installed)

# Setup

## Enable and activate the virtual environment 

1. Create the virtual environment  
`python -m venv env`

2. Navigate to the virtual environment  
`cd env/`  

3. Activate the virtual environment  
`source Scripts/activate`

## Set environment variables  
1. Name of the Flask application:  
`export FLASK_APP=main`  
2. Environment of the Flask application:  
`export FLASK_ENV=development`


## Install the dependencies
- Navigate to the virtual environment and execute:  
`pip install -r ../requirements.txt`  
### Dependencies  
- _Flask_  
Flask enables the software to provide API endpoints. These can be called by external services such as ChatGPT via a Plugin and others.
- _Flask-restx_  
Flas-restx enables the automatic generation of an API documentation using Swagger. It makes it easier to present the available endpoints to users or third-parties. Swagger shows the existing endpoints, the parameters that they need and the output of each endpoint.

## Set up the database  
Navigate to the db directory and execute the following commands
1. Navigate to the _db/util_ directory  
2. Execute  
`sh recreate_db.sh`

# Enable a GPT to access the application running on localhost (For the Database API example)  
1. Download [ngrok](https://ngrok.com/download)
2. Extract the folder
3. Open a CLI window in the folder
4. Execute  
`./ngrok.exe http 5000` 
5. Copy the _Forwarding_ URL
6. Paste the URL in the **NGROK_URL** placeholders in the _ai-plugin.json_ and _openapi.yaml_ files

# Start the application
In the root directory run:  
`python api.py`

# Set up the connection from ChatGPT to the API
1. Go to your own ChatGPT
2. Configure a _name_ and _instructions_
3. Configure _actions_
4. Import the _openapi.yaml_ content from  
`NGROK_URL/info/openapi`
5. Verify the that the API endpoints **getDatabaseMetadata** and **executeSQLQuery** are there
6. (Optional) Test the API by using a prompt which gets the current metadata of the database

# Testing the endpoints
Thanks to Flask-restx when the application is started you can go to the [Swagger UI](http://127.0.0.1:5000/). The endpoints are assigned to their relevant namespaces. 