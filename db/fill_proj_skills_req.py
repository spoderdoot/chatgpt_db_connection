import sqlite3
import random

# Connect to the SQLite database
conn = sqlite3.connect('gpt_organization.db')
cursor = conn.cursor()

# Retrieve the IDs of all projects and skills from their respective tables
cursor.execute('SELECT id FROM t_projects')
project_ids = [row[0] for row in cursor.fetchall()]

cursor.execute('SELECT id FROM t_skills')
skill_ids = [row[0] for row in cursor.fetchall()]

cursor.execute('SELECT id FROM t_skill_strengths')
skill_strength_ids = [row[0] for row in cursor.fetchall()]

# The number of random mappings you want to create
num_mappings = 15

# Randomly map employees to projects
for _ in range(num_mappings):
    # Select a random employee and project ID
    project_id = random.choice(project_ids)
    skill_id = random.choice(skill_ids)
    skill_strength_id = random.choice(skill_strength_ids)

    try:
        # Insert the mapping into the employees_in_projects table
        cursor.execute('INSERT INTO t_project_skills_required (project_id, skill_id, skill_strength_id) VALUES (?, ?, ?)',
                       (project_id, skill_id, skill_strength_id))
        conn.commit()
    except sqlite3.IntegrityError:
        # Handle duplicate entries
        pass

# Close the connection
conn.close()

print(f"{num_mappings} random project skill requirement mappings with skill strengths have been created.")
