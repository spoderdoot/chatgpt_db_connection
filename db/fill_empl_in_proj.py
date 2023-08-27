import sqlite3
import random

# Connect to the SQLite database
conn = sqlite3.connect('gpt_organization.db')
cursor = conn.cursor()

# Query to find eligible employee-project mappings
query = """
INSERT INTO t_employees_in_projects (employee_id, project_id, role_id)
SELECT DISTINCT es.employee_id, psr.project_id, tr.id AS role_id
FROM t_employee_skills AS es
INNER JOIN t_project_skills_required AS psr
ON es.skill_id = psr.skill_id
AND es.skill_strength_id > psr.skill_strength_id
JOIN t_roles AS tr
ON tr.id IN (
    SELECT id
    FROM t_roles
    ORDER BY RANDOM()  -- Select a random role ID from t_roles
)
WHERE NOT EXISTS (
    SELECT 1
    FROM t_employees_in_projects AS eip
    WHERE eip.employee_id = es.employee_id
    AND eip.project_id = psr.project_id
);
"""

# Execute the query to map eligible employees to projects with random roles
cursor.execute(query)

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Employee-project-role mappings have been updated with random roles.")
