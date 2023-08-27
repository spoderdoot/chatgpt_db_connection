import sqlite3
import random

# Connect to the SQLite database
conn = sqlite3.connect('gpt_organization.db')
cursor = conn.cursor()

# Get the list of role_ids from the t_roles table
cursor.execute("SELECT id FROM t_roles")
role_ids = [row[0] for row in cursor.fetchall()]

# Shuffle the list of role_ids to ensure randomness
random.shuffle(role_ids)

# Update t_employees_in_projects with randomly selected role_ids for each row
cursor.execute("SELECT rowid FROM t_employees_in_projects")
rowids = [row[0] for row in cursor.fetchall()]

for rowid in rowids:
    random_role_id = random.choice(role_ids)
    cursor.execute("UPDATE t_employees_in_projects SET role_id = ? WHERE rowid = ?", (random_role_id, rowid))

# Commit the changes and close the connection
conn.commit()
conn.close()

print("t_employees_in_projects table has been updated with randomly selected role_ids for each row.")
