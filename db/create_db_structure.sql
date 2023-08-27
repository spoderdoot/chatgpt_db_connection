-- Create the projects table
CREATE TABLE if NOT EXISTS t_projects (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    budget REAL,
    expenses REAL DEFAULT 0.0
);

-- Create the employees table
CREATE TABLE if NOT EXISTS t_employees (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

-- Create the skills table
CREATE TABLE IF NOT EXISTS t_skills (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

-- Create the skill strength table
CREATE TABLE IF NOT EXISTS t_skill_strengths (
    id INTEGER PRIMARY KEY,
    strength TEXT NOT NULL
);

-- Create the roles table
CREATE TABLE IF NOT EXISTS t_roles (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

-- Create the employee in projects table
CREATE TABLE IF NOT EXISTS t_employees_in_projects (
    project_id INTEGER,
    employee_id INTEGER,
    role_id INTEGER,
    FOREIGN KEY (project_id) REFERENCES t_projects (id),
    FOREIGN KEY (employee_id) REFERENCES t_employees (id),
    FOREIGN KEY (role_id) REFERENCES t_roles (id)
);

-- Create the employee skills table
CREATE TABLE IF NOT EXISTS t_employee_skills (
    employee_id INTEGER,
    skill_id INTEGER,
    skill_strength_id INTEGER,
    PRIMARY KEY (employee_id,skill_id,skill_strength_id),
    FOREIGN KEY (employee_id) REFERENCES t_employees (id),
    FOREIGN KEY (skill_id) REFERENCES t_skills (id),
    FOREIGN KEY (skill_strength_id) REFERENCES t_skill_strengths (id),
    UNIQUE (employee_id, skill_id)
);

-- Create the skills needed for projects table
CREATE TABLE IF NOT EXISTS t_project_skills_required (
    project_id INTEGER,
    skill_id INTEGER,
    skill_strength_id INTEGER,
    PRIMARY KEY (project_id,skill_id),
    FOREIGN KEY (project_id) REFERENCES t_projects (id),
    FOREIGN KEY (skill_id) REFERENCES t_skills (id),
    FOREIGN KEY (skill_strength_id) REFERENCES t_skill_strengths (id)
    UNIQUE (project_id, skill_id)
);