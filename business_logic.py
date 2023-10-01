import sqlite3

def get_metadata_from_db():
    conn = sqlite3.connect('db/gpt_organization.db')
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = [row[0] for row in cursor.fetchall()]

    metadata = {}
    for table in tables:
        cursor.execute(f"PRAGMA table_info({table})")
        table_metadata = cursor.fetchall()
        metadata[table] = table_metadata

    return {'metadata': metadata}



def get_employees_from_db():
    conn = sqlite3.connect('db/gpt_organization.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT name FROM t_employees")
    employees = cursor.fetchall()
    
    conn.close()
    
    formatted_employees = [{'name': employee[0]} for employee in employees]
    
    return formatted_employees

def get_projects_from_db():
    conn = sqlite3.connect('db/gpt_organization.db')
    cursor = conn.cursor()

    cursor.execute("SELECT name, budget, expenses FROM t_projects")
    projects = cursor.fetchall()

    conn.close()

    formatted_projects = [{'name': project[0], 'budget': project[1], 'expenses': project[2]} for project in projects]

    return formatted_projects

def get_employee_skills_from_db():
    conn = sqlite3.connect('db/gpt_organization.db')
    cursor = conn.cursor()

    cursor.execute("""SELECT e.name AS employee_name, s.name AS skill_name, ss.strength AS skill_strength 
                      FROM t_employee_skills AS es 
                      JOIN t_employees AS e ON es.employee_id = e.id 
                      JOIN t_skills AS s ON es.skill_id = s.id 
                      JOIN t_skill_strengths AS ss ON es.skill_strength_id = ss.id
                      ORDER BY es.employee_id;""")
    employee_skills = cursor.fetchall()

    conn.close()

    formatted_employee_skills = [{'name':skill[0],'skill_name':skill[1],'skill_strength':skill[2],} for skill in employee_skills]

    return formatted_employee_skills

def get_employees_in_projects_from_db():
    conn = sqlite3.connect('db/gpt_organization.db')
    cursor = conn.cursor()

    cursor.execute("""SELECT p.name as project_name, e.name as employee_name, r.name as role_name, s.name as skill_name, ss.strength as skill_strength
                      FROM t_employees_in_projects AS ep
                      JOIN t_employees AS e ON ep.employee_id = e.id 
                      JOIN t_projects AS p ON ep.project_id = p.id 
                      JOIN t_roles AS r ON ep.role_id = r.id
                      JOIN t_project_skills_required as psr ON psr.project_id = ep.project_id
                      JOIN t_skills as s on psr.skill_id = s.id
                      JOIN t_skill_strengths as ss on psr.skill_strength_id = ss.id
                      ORDER BY ep.project_id;""")
    employees_in_projects = cursor.fetchall()

    conn.close()

    formatted_employee_skills = [{'project_name':employee_in_project[0],'employee_name':employee_in_project[1],'role_name':employee_in_project[2],} for employee_in_project in employees_in_projects]

    return employees_in_projects