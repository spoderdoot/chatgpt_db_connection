from flask import Flask, request, send_file, make_response
from flask_restx import fields, Api, Resource, Namespace
from business_logic import *

app = Flask(__name__)
api = Api(app)

PORT = 5000

# These namespaces define groups in which the endpoints should be located
database_namespace = Namespace('database', description='This namespace contains the database relevant endpoints.')
info_namespace = Namespace('info', description='This namespace provides endpoints for ChatGPT')

api.add_namespace(database_namespace)
api.add_namespace(info_namespace)

model = api.model('SQLQueryModel', {
    'query': fields.String(description='SQL Query', required=True)
})

# This route gets the underlying metadata of the SQLite database and returns it
@database_namespace.route('/metadata')
class Database(Resource):
    def get(self):
        metadata = get_metadata_from_db()
        return metadata
    
# This route posts a SQL query and returns the inserted data
@database_namespace.route('/execute_query')
class Database(Resource):
    @api.expect(model)
    def post(self):
        metadata = post_sql_query_to_db(request.json.get('query'))
        return metadata

# This route returns the contents of the openapi.yaml file
@info_namespace.route('/openapi')
class OpenApi(Resource):
    def get(self):
        with open('openapi.yaml', 'r') as file:
            content = file.read()
        return make_response(content, 200, {'Content-Type': 'text/yaml'})

# This route returns the logo
@info_namespace.route('/logo')
class Logo(Resource):
    def get(self):
        return send_file('logo.png', mimetype='image/png')

if __name__ == '__main__':
    app.run(port=PORT, debug=True)