import sys
import subprocess
import time

directory = sys.argv[1]

while True:
    # Check if there are any changes in the repository
    result = subprocess.run(["git", "--git-dir", directory + "/.git", "status", "--porcelain"], stdout=subprocess.PIPE)
    if len(result.stdout) > 0:
        # Add all changes to the staging area
        subprocess.run(["git", "--git-dir", directory + "/.git", "add", "."], cwd=directory)

        # Commit the changes with a message including the date
        subprocess.run(["git", "--git-dir", directory + "/.git", "commit", "-m", "Auto commit $(date)"], cwd=directory)

        # Push the changes to the remote repository
        subprocess.run(["git", "--git-dir", directory + "/.git", "push", "origin", "master"], cwd=directory)

    # Wait for 10 seconds before checking again
    time.sleep(10)
