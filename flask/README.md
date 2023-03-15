## Steps to configuration 

1. python --version
2. pyenv shell 3.11.1
3. python -m venv .venv
4. touch .gitignore
5. touch requirements.txt
6. source .venv/bin/activate
7. change the python interpreter to .venv 3.11.1 
8. git init
9. git branch -M main
10. pip install --upgrade pip
11. pip install -r requirements.txt 
12. pip freeze
13. chmod 777 run_server.sh
14. ./run_server.sh

## Run project
1. flask --app main run // MAIN is the name of my file
2. flask --app main run --debug // change to debug on
3. 
