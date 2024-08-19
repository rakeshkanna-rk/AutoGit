import json
from datetime import datetime
import subprocess
import os

def update_json_file(file_path):
    # Get current date and time
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Load the JSON data
    with open(file_path, 'r') as file:
        data = json.load(file)

    # Update the date field
    data['date'] = current_datetime

    # Save the updated JSON back to the file
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def run_git_command(command, cwd=None):
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, cwd=cwd)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
    else:
        print(result.stdout)

def commit_and_push(repo_path, commit_message, branch_name="main", commit_date=None):
    # Update the JSON file with current date and time
    json_file_path = os.path.join(repo_path, 'data.json')
    update_json_file(json_file_path)
    print(f"data.json Updated @ {json_file_path}")

    # Add changes to the staging area
    run_git_command(["git", "add", "."], cwd=repo_path)

    # Prepare the commit command
    commit_command = ["git", "commit", "-m", commit_message]

    if commit_date:
        # Add the --date option if a commit date is provided
        commit_command += ["--date", commit_date]

    # Commit the changes
    run_git_command(commit_command, cwd=repo_path)

    # Push the changes to the specified branch
    run_git_command(["git", "push", "origin", branch_name], cwd=repo_path)

    print("\nLast Command Exicuted: ".join(map(str, commit_command)))

if __name__ == "__main__":
    # Replace with your repository path
    repo_path = "."
    
    # Commit message
    # commit_message = f"Update date and time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    commit_message = f"Testing..."

    # Optionally, replace with your branch name
    branch_name = "main"

    # Optionally, set a specific commit date (e.g., "Tue Aug 19 12:34:56 2024 +0200")
    commit_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print("\nCommit Date: ", commit_date)
    print("Commit Messager: ", commit_message)
    print("Branch: ", branch_name)

    commit_and_push(repo_path, commit_message, branch_name, commit_date)

