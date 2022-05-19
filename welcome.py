print("welcome to vscode!")


Files >>> Staging Location >>> Local Repository
git init

touch repo.py
code repor.py 

git add repo.py
git add .

 git commit -m "first commit"

Run globally:

  git config --global user.email "you@example.com"
  git config --global user.name "Your Name"

Run locally:
  git config user.email "you@example.com"
  git config user.name "Your Name"

  git status

  git branch
  git branch newbranchname

  git checkout newbranchname

# e.g: when some modification is done, you must git add and git commit

when to merge into master branch:
git checkout master,
git merge feature

git branch -d feature 

git checkout -b new

