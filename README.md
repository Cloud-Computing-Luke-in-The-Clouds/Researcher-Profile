# Researcher-Profile

## Install
```
sudo apt update
sudo apt install python3.12-venv
```

Create python virtual environment
```python3 -m venv pj1```

Activate the virtual environment, install all the packages and launch the backend service
```
source pj1/bin/activate
pip3 install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```