## Create conda environment
    conda create venv python==3.10 -y
## Activate conda environment
    conda activate venv/
## steps to intialize and push repo github
    echo "# mlproject" >> README.md
    git init
    git add README.md
    git commit -m "first commit"
    git branch -M main
    git remote add origin https://github.com/Mangaldeep-Singh/mlproject.git
    git push -u origin main
### .gitignore
    to ignore files and folders that we don't want to push as a part of project
### to pull changes from github to local repo
    git pull

# <center>mlproject</center>
