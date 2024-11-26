# Tick Tac Toe Game
This is a tic tac toe game playable in the temrinal

## How to Play

1. Make sure you have Python installed
2. 

## How to Develop

### Setup fresh development environment
```
git clone git@github.com:itsgreddy/TECHIN509-AU24.git
cd TECHIN509-AU24
cd Week9
```
## Setup a new virtual environment, and acrivate it for this temrinal session
```
python -m venv venv
```
```
source venv/bin/activate 
```
(or)
```
venv/Scripts/activate
```
### Install packages and freeze into requirements.txt file
```
pip install numpy openai django
pip freeze > requirements.txt
```

## Commit requirements.txt to GitHub so others can use to reproduce your environment
```
git add requirements.txt
```

### Setup Environment for developing existing project
```
git clone git@github.com:itsgreddy/TECHIN509-AU24.git
cd TECHIN509-AU24
cd Week9
```
### Create an activate Python virtual environment
```
python -m venv venv
```
```
source venv/bin/activate 
```
(or)
```
venv/Scripts/activate
```
### Install packages listeed in requirements.txt to the virtual environment
```
pip install -r requirements.txt
```