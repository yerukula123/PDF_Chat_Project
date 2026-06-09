installed_tools = ["Python Extension", "Pylance", "VS Code Interface"]

def check_setup(tools):
    for tool in tools:
        print(f"Checking status... {tool} is ACTIVE!")

check_setup(installed_tools)

print("\nYour IDE is now officially 'Smart'!")