# Import the 'os' module to interact with your computer's operating system
import os

# Create a variable to store the project name
project_name = "PDF Chat Project"

# Create a welcome message
welcome_message = "Welcome to your AI Command Center!"

# Print the welcome message
print(welcome_message)

# Print the project name
print("Project Name:", project_name)

# Check if config.txt exists
if os.path.exists("config.txt"):
    print("Success: VS Code sees your project files!")
else:
    print("Error: config.txt not found in this folder.")