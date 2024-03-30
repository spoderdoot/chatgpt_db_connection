-- 6.1 Get SQL metadata
SELECT name, sql FROM sqlite_master
WHERE type='table'
ORDER BY name;
-- 6.2 Get table metadata
PRAGMA table_info(t_employee_skills);
PRAGMA table_info(t_employee_trainings);
PRAGMA table_info(t_employees);
PRAGMA table_info(t_employees_in_projects);
PRAGMA table_info(t_project_skills_required);
PRAGMA table_info(t_projects);
PRAGMA table_info(t_roles);
PRAGMA table_info(t_skill_strengths);
PRAGMA table_info(t_skills);

-- 6.3 Generate SELECT SQL query
SELECT *
FROM t_projects;

-- 6.3 & 6.4 Generate and execute JOIN SQL query
SELECT e.name AS EmployeeName, p.name AS ProjectName, s.name AS SkillName
FROM t_employees_in_projects eip
JOIN t_employees e ON eip.employee_id = e.id
JOIN t_projects p ON eip.project_id = p.id
JOIN t_employee_skills es ON e.id = es.employee_id 
JOIN t_skills s ON es.skill_id = s.id

-- 6.5 Verify addition of new data
SELECT *
FROM t_employees te
WHERE te.name = 'Stefanny Cent'

SELECT te.name as Employee, ts.name as Skill
FROM t_employee_skills tes 
JOIN t_employees te ON tes.employee_id = te.id 
JOIN t_skills ts on tes.skill_id = ts.id 
WHERE te.name = 'Stefanny Cent'

SELECT te.name, tp.name 
FROM t_employees_in_projects teip 
JOIN t_employees te ON teip.employee_id = te.id 
JOIN t_projects tp ON teip.project_id = tp.id 
WHERE tp.name = 'Project 8'

-- 6.6 Verify addition of new relation
SELECT *
FROM t_trainings tt 

SELECT *
FROM t_employee_trainings tet 

SELECT te.name as Employee, tt.name as Training
FROM t_employee_trainings tet 
JOIN t_employees te ON tet.employee_id = te.id 
JOIN t_trainings tt ON tet.training_id = tt.id 

