# AutoGit: Automated Git Commit and Push with Custom Commit Dates

This Python script automates the process of updating a `data.json` file with the current date and time, committing the changes, and pushing them to a specified GitHub branch. Additionally, it allows you to specify a custom commit date using Git's `--date` option.

> [!WARNING]
> This script is provided for educational purposes only. Misuse of Git’s `--date` option to falsify commit history can lead to ethical issues and potentially violate the terms of service of platforms like GitHub. 
> Use this feature responsibly.

## Features

- **Automatic Date and Time Update:** Automatically updates a `data.json` file with the current date and time.
- **Custom Commit Date:** Allows setting a custom commit date using Git's `--date` option.
- **Automated Git Operations:** Commits and pushes changes to a specified GitHub branch.
- **Easy Integration:** Can be adapted to work with different repositories and branches.

## Prerequisites

Before using this script, ensure you have the following installed on your system:

- **Python 3.x:** The script is written in Python, so Python 3.x is required.
- **Git:** Git must be installed and properly configured.
- **GitHub Authentication:** Ensure that your GitHub credentials are set up (e.g., SSH keys or a personal access token for HTTPS connections).

## Installation

1. **Clone the Repository:**

   Clone this repository to your local machine:

   ```bash
   git clone https://github.com/rakeshkanna-rk/AutoGit.git
   ```

2. **Navigate to the Project Directory:**

   ```bash
   cd AutoGit
   ```

3. **Configure the Script:**

   Open the `main.py` script and update the following variables:

   - **`repo_path`:** Set this to the path of your local Git repository.
   - **`branch_name` (optional):** Specify the branch you want to push the changes to. Default is `"main"`.
   - **`commit_date` (optional):** Set a custom commit date in the format `"YYYY-MM-DD HH:MM:SS"` or Git's preferred format `"Tue Aug 19 12:34:56 2024 +0200"`. If not set, the current date and time will be used.

## Usage

1. **Run the Script:**

   Execute the script to automatically update the `data.json` file, commit the changes with a custom date (if provided), and push them to GitHub:

   ```bash
   python main.py
   ```

2. **Verify on GitHub:**

   After running the script, visit your GitHub repository to ensure that the `data.json` file has been updated and that the commit has been pushed with the specified date.

## Script Overview

### Functions

- **`update_json_file(file_path)`:** 
   - Updates the `date` field in the `data.json` file with the current date and time.
   - Saves the changes back to the file.

- **`run_git_command(command, cwd=None)`:** 
   - Runs a Git command in the specified repository directory.
   - Handles and prints the output or errors from the command.

- **`commit_and_push(repo_path, commit_message, branch_name="main", commit_date=None)`:**
   - Updates the `data.json` file.
   - Stages the changes (`git add`).
   - Commits the changes using a specified commit message and an optional commit date (`--date`).
   - Pushes the commit to the specified branch.

### Example `data.json`

Ensure your `data.json` file is structured as follows:

```json
{
    "date": "2024-08-19 12:34:56"
}
```

The `date` field will be updated automatically by the script each time it is run.

## Important Notes

- **Educational Use Only:** This script is intended for educational purposes. Misrepresenting the commit date by altering it can lead to ethical concerns and may violate platform rules.
- **Timezone Awareness:** If using a custom commit date, consider including the timezone in the format (e.g., `"Tue Aug 19 12:34:56 2024 +0200"`).

## Contributing

If you'd like to contribute to this project, feel free to fork the repository, make your improvements, and submit a pull request. Contributions are always welcome!

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
