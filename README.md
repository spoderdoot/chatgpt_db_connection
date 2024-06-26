# chatgpt_db_connection 
This project sets up a DB and API for the local use with ChatGPT. The database uses **SQLite** and **Flask** is used to provide server functionalities. The API is documented with **Swagger**. To provide the endpoints to a GPT opening a tunnel with **serveo** is required.

# Requirements
| Technology  | Version |
| ------------- | ------------- |
| Python  | 3.11.4  |
| SQLite  | 2.6.0  |
| npm  | 10.2.4  |

# Setup

## Enable and activate the virtual environment 

0. Open a **git bash** terminal and navigate to this project  

1. Create the virtual environment in the root directory 
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
- Navigate to the virtual environment /env and execute:  
`pip install -r ../requirements.txt`  
- Install [localtunnel](https://localtunnel.github.io/www/) with  
`npm install -g localtunnel`  

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
1. Execute   
`lt --port 5000`
2. Copy the _Forwarding_ URL
3. Paste the URL in the **LT_URL** placeholders in the _openapi.yaml_ file

# Start the application
In the root directory run:  
`python api.py`

# Set up the connection from ChatGPT to the API
1. Go to your own ChatGPT
2. Configure a _name_ and _instructions_
3. Configure _actions_
4. Import the _openapi.yaml_ content from  
`LT_URL/info/openapi`
5. Verify the that the API endpoints **getDatabaseMetadata** and **executeSQLQuery** are there
6. (Optional) Test the API by using a prompt which gets the current metadata of the database

# Testing the endpoints
Thanks to Flask-restx when the application is started you can go to the [Swagger UI](http://127.0.0.1:5000/). The endpoints are assigned to their relevant namespaces. 