import random

# Define the number of projects to generate
num_projects = 10  # You can change this number as needed

# Open the file for writing
with open('../tabledata/project_data.txt', 'w') as file:
    # Loop to generate project data
    for project_number in range(1, num_projects + 1):
        # Generate a random budget between 10,000 and 1,000,000
        budget = random.uniform(10000, 1000000)
        
        # Generate the project name
        project_name = f"Project {project_number}"
        
        # Write the project data to the file in the specified format
        file.write(f"{project_name}, {budget:.2f}\n")

print(f"{num_projects} project records have been generated in project_data.txt.")
