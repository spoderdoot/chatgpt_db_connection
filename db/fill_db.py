import sqlite3


# Function to load project names and budgets from a file
def load_data_from_file_with_comma(file_path):
    array = []
    with open(file_path, 'r') as file:
        for line in file:
            first_value, second_value = line.strip().split(',')
            array.append((first_value, float(second_value)))
    return array

# Function to load employee names from a file
def load_data_from_file(file_path):
    with open(file_path, 'r') as file:
        data = [line.strip() for line in file]
    return data

# List of project names and budgets (loaded from a file)
project_data_file = 'tabledata/project_data.txt'
projects = load_data_from_file_with_comma(project_data_file)

# List of employee names (loaded from a file)
employee_names_file = 'tabledata/employee_data.txt'
employee_names = load_data_from_file(employee_names_file)

# List of roles (loaded from a file)
role_names_file = 'tabledata/roles_data.txt'
roles = load_data_from_file(role_names_file)

# List of skills (loaded from a file)
skills_data_file = 'tabledata/skills_data.txt'
skills = load_data_from_file(skills_data_file)

# List of skill strength (loaded from a file)
skill_strengths_data_file = 'tabledata/skill_strength_data.txt'
skill_strengths = load_data_from_file(skill_strengths_data_file)

# Define the name of the SQLite database file
db_filename = 'gpt_organization.db'

# Establish a connection to the database (this will create the database if it doesn't exist)
conn = sqlite3.connect(db_filename)
cursor = conn.cursor()

# Insert data into t_projects table
for project in projects:
    cursor.execute('INSERT INTO t_projects (name, budget) VALUES (?, ?)', project)

# Insert data into t_employees table
for name in employee_names:
    cursor.execute('INSERT INTO t_employees (name) VALUES (?)', (name,))

# Insert data into t_roles table
for role in roles:
    cursor.execute('INSERT INTO t_roles (name) VALUES (?)', (role,))

# Insert data into t_skills table
for skill in skills:
    cursor.execute('INSERT INTO t_skills (name) VALUES (?)', (skill,))

# Insert data into t_roles table
for skill_strength in skill_strengths:
    cursor.execute('INSERT INTO t_skill_strengths (strength) VALUES (?)', (skill_strength,))

# Commit the changes and close the connection
conn.commit()
conn.close()

print('Data has been inserted into the tables.')