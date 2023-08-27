import sqlite3
import random

# Connect to the SQLite database
conn = sqlite3.connect('gpt_organization.db')
cursor = conn.cursor()

# Retrieve the IDs of all employees, skills and their strenghts from their respective tables
cursor.execute('SELECT id FROM t_employees')
employee_ids = [row[0] for row in cursor.fetchall()]

cursor.execute('SELECT id FROM t_skills')
skill_ids = [row[0] for row in cursor.fetchall()]

cursor.execute('SELECT id FROM t_skill_strengths')
skill_strength_ids = [row[0] for row in cursor.fetchall()]

# The number of random mappings you want to create
num_mappings = 40

# Randomly map employees to projects
for _ in range(num_mappings):
    # Select a random employee and project ID
    employee_id = random.choice(employee_ids)
    skill_id = random.choice(skill_ids)
    skill_strength_id = random.choice(skill_strength_ids)

    # Insert the mapping into the employees_in_projects table
    cursor.execute('INSERT INTO t_employee_skills (employee_id, skill_id, skill_strength_id) VALUES (?, ?, ?)',
                   (employee_id, skill_id, skill_strength_id))

# Commit the changes and close the connection
conn.commit()
conn.close()

print(f"{num_mappings} random employee skill mappings with respective skill strengths have been created.")
