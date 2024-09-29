# Researcher-Profile

Create python virtual environment
```python3 -m venv pj1```

Activate the virtual environment, install all the packages and launch the backend service
```
source pj1/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```