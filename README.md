# Full-Stack Developer Take-Home Assessment

## Supply-Chain-Data-Hub-Backend

This repository contains the backend and frontend implementation of the Full-Stack Developer Take-Home Assessment.

```bash
sudo apt update
sudo apt upgrade
sudo apt install python3
sudo apt install python3-pip
sudo pip3 install virtualenv

# cd /to current project path
python3 -m venv venv
source venv/bin/activate
pip install fastapi uvicorn pandas pytest

uvicorn app.main:app --reload

docker build -t fastapi-backend .
docker run -p 8000:80 fastapi-backend

pytest backend/app/tests

pip install -r requirements.txt

```
