print("welcome to vscode!")


Files >>> Staging Location >>> Local Repository >>Remote Repository
git init

touch repo.py
code repo.py 

#git add
git add repo.py
git add .

# git commit
git commit -m "first commit"

# Run globally:

git config --global user.email "you@example.com"
git config --global user.name "Your Name"

# Run locally:
git config user.email "you@example.com"
git config user.name "Your Name"

git status

git branch
git branch newbranchname

git checkout newbranchname

# e.g: when some modification is done, you must git add and git commit

# when to merge into master branch:
git checkout master,
git merge feature

git branch -d feature 
git checkout -b new


#Generating of SSHKEY
ssh-keygen -t ed25519 -C "adenijimujeeb@gmail.com"
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
clip < ~/.ssh/id_ed25519.pub

#connect to remote reposity
git remote add origin sshkey url

#clone repository
git clone sshkey url

# Commands to check existing keys
ls -al ~/.ssh

# local >>> remote repository
git push origin master

# remote >>> local
git pull origin master

# Advance git command
git stash: To save changes to a file that are not in the state to commit to repository (git stash -u, git stash show, git stash list)
git log: To help give context or history for a repository
git rebase: Take a set of commit and save them outside of repository
git revert: It helps to roll back to the previous version of  the file
