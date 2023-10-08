from flask import Flask, request, send_file
from flask_restx import fields, Api, Resource, Namespace
from business_logic import *

app = Flask(__name__)
api = Api(app)

PORT = 5000

database_namespace = Namespace('database', description='This namespace contains the database relevant endpoints.')
employee_namespace = Namespace('employees', description='This namespace contains the employee relevant endpoints.')
project_namespace = Namespace('projects', description='This namespace contains the profect relevant endpoints.')
info_namespace = Namespace('info', description='This namespace provides endpoints for ChatGPT')

api.add_namespace(database_namespace)
#api.add_namespace(employee_namespace)
#api.add_namespace(project_namespace)
api.add_namespace(info_namespace)

model = api.model('SQLQueryModel', {
    'query': fields.String(description='SQL Query', required=True)
})

@database_namespace.route('/metadata')
class Database(Resource):
    def get(self):
        metadata = get_metadata_from_db()
        return metadata
    
@database_namespace.route('/execute_query')
class Database(Resource):
    @api.expect(model)
    def post(self):
        metadata = post_sql_query_to_db(request.json.get('query'))
        return metadata

@info_namespace.route('/openapi')
class OpenApi(Resource):
    def get(self):
        return send_file('openapi.yaml')

@info_namespace.route('/logo')
class Logo(Resource):
    def get(self):
        return send_file('logo.png', mimetype='image/png')

# @employee_namespace.route('')
# class Employees(Resource):
#     def get(self):
#         employees = get_employees_from_db()
#         return {'employees': employees}

# @project_namespace.route('')
# class Projects(Resource):
#     def get(self):
#         projects = get_projects_from_db()
#         return {'projects': projects}

# @employee_namespace.route('/skills')
# class EmployeeSkills(Resource):
#     def get(self):
#         employee_skills = get_employee_skills_from_db()
#         return {'employee_skills': employee_skills}

# @employee_namespace.route('/projects')
# class EmployeeProjects(Resource):
#     def get(self):
#         employee_in_projects = get_employees_in_projects_from_db()
#         return {'employees-in-projects': employee_in_projects}

if __name__ == '__main__':
    app.run(port=PORT, debug=True)