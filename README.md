# receipt-processor-challenge
A simple receipt processor using python and FastAPI.

## Run Application

### Set up
Install python (macOS: `brew install python`)

Navigate to directory, create and activate virtual environment to isolate dependencies:
```
python3 -m venv myenv
source myenv/bin/activate
```

Install requirements
`pip install -r requirements.txt`

### Run
```
cd app
uvicorn main:app --reload
```

To view comprehensive docs and test endpoints of the API (routes, schema), go to: http://127.0.0.1:8000/docs (or whichever port you use).


## App directory breakdown
- main.py: FastAPI app containing HTTP routes
- models.py: data validation for a Receipt object
- points.py: contains method calc_points(receipt) that calculates points for a given receiptREAD
