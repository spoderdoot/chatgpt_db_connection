 #!/bin/bash

 cd ..
 rm -f -- gpt_organization.db
 python create_db.py
 python fill_db.py
 python fill_proj_skills_req.py
 python fill_empl_skills.py
 python fill_empl_in_proj.py
 python fill_roles_in_empl_in_proj.py