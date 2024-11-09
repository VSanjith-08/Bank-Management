# Bank-Management
This is the project created by Sanjith and Balaji Sanjay for school project on the topic bank management.

# Basics about git:

# Config your remote git
git config --global user.name 'Username'
git config --global user.email 'Mailid'

# To clone your repository file to local device.
git clone https://github.com/VSanjith-08/Bank-Management.git
cd Bank-Management

# To push the changes to the origin(repo)
# Procedures [ Working folder --> stagging area ]
git status
git add filename
git status

# Procedures [Stagging area --> .Git folder]
git commit -m "filename file added"

# Procedures [.Git folder --> origin]
git push origin

# To view the status
git status

# Modified command from local drive (M-Main) to origin [ Modify( Main --> origin )]
git add filename
git commit -m "Modified filename file"
git push origin main

# Modified command from origin to local drive (M-Main) [ Modify( origin --> Main )]
git pull

# if any file deleted
git status 
git add the-name-of-file-deleted 
git commit -m "deleted filename file"
git push origin main

# To view files in the staging area
git ls-files

# To ignore files going to staging area
create and add file names to .gitignore file before adding the file to staging area
# If it is already created and added to staging area use:
git rm --cached -r file/folder-name
git ls-files

###### ########## ######
# To make a folder as repo
# go to that folder and type the following:
git init 
git status
git add .
git commit -m "Created filenames"
git branch # If it returns master to display main
git push origin master

# [or] to change branch
git branch -M main
git branch

git push origin main

# To view all the branch
git branch -a

# To switch from branches
git checkout branch-name

# To see the difference btw the main and the given branch
git diff branch-name 

# To merge given branch to the main branch
git merge branch-name
git push origin main
