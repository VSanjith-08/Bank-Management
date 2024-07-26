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

###### ########## ######
# To make a folder as repo
go to that folder and type the following:
git init 
git status
git add .
git commit -m "Created filenames"
git remote add origin link
git branch # If it returns master to display main
git push origin master
# [or] to change branch
git branch -M main
git branch

git push origin main
