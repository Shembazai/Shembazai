#!/usr/bin/env python3
import subprocess
import sys
import os

# Mapping of option numbers to (description, script filename)
AGENT_SCRIPTS = {
    1: ("Plan a Task", "task_planner.py"),
    2: ("Consult Weather", "weather_ai.py"),
    3: ("Manage Finances", "financial_agent.py"),
    4: ("Homesteading Guidance", "homestead_guidance.py")
}

def main():
    print("WELCOME. I am an off-grid AI trained to help you along your homesteading journey.")
    print("What do you wish to accomplish today?")
    
    while True:
        print("\nPlease choose an option:")
        for num, (desc, _) in AGENT_SCRIPTS.items():
            print(f"{num}. {desc}")
        print("0. Exit")
        
        choice = input("Enter your choice: ")
        try:
            choice = int(choice)
        except ValueError:
            print("Invalid input, please enter a number.")
            continue
        
        if choice == 0:
            print("Goodbye!")
            sys.exit(0)
        elif choice in AGENT_SCRIPTS:
            desc, script = AGENT_SCRIPTS[choice]
            full_path = os.path.join(os.getcwd(), script)
            if not os.path.exists(full_path):
                print(f"Script '{script}' not found!")
            else:
                print(f"\nLaunching {desc}...\n")
                subprocess.run([sys.executable, full_path])
                input("\nPress Enter to return to the menu...")
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
