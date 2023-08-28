from flask import Flask
from flask_restx import fields, Api, Resource, Namespace
from business_logic import *

app = Flask(__name__)
api = Api(app)

PORT = 5000

employee_namespace = Namespace('Employees', description='This namespace contains the employee relevant endpoints.')
project_namespace = Namespace('Projects', description='This namespace contains the profect relevant endpoints.')

api.add_namespace(employee_namespace)
api.add_namespace(project_namespace)

@employee_namespace.route('/employees')
class Employees(Resource):
    def get(self):
        employees = get_employees_from_db()
        return {'employees': employees}

@project_namespace.route('/projects')
class Projects(Resource):
    def get(self):
        projects = get_projects_from_db()
        return {'projects': projects}

@employee_namespace.route('/employee-skills')
class EmployeeSkills(Resource):
    def get(self):
        employee_skills = get_employee_skills_from_db()
        return {'employee_skills': employee_skills}

@employee_namespace.route('/employees-in-projects')
class EmployeeProjects(Resource):
    def get(self):
        employee_in_projects = get_employees_in_projects_from_db()
        return {'employees-in-projects': employee_in_projects}

if __name__ == '__main__':
    app.run(port=PORT, debug=True)