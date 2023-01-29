#!/bin/bash
# do after add this sh file 
#sed -i -e 's/\r$//' push.sh

#another variant via cli 
#inotifywait -q -m -e CLOSE_WRITE --format="git add . && git commit -m 'auto commit' %w && git push origin master" /home/user/MikroTik/ | bash

cd /home/user/MikroTik/

while true; do
    # Check if there are any changes in the repository
    if [ $(git status --porcelain | wc -l) -ne 0 ]; then
        # Add all changes to the staging area
        git add .

        # Commit the changes with a message "Auto commit"
        git commit -m "Auto commit $(date)"

        # Push the changes to the remote repository
        git push origin master
    fi

    # Wait for 10 seconds before checking again
    sleep 10
done
