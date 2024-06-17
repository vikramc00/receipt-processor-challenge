# receipt-processor-challenge
A simple receipt processor

## Run Application

### Install python and pip
Install python (macOS: `brew install python`)

Navigate to directory, create and activate virtual environment to isolate dependencies:
```
python3 -m venv myenv
source myenv/bin/activate
```

Install requirements and run app
```
pip install -r requirements.txt
cd app
uvicorn main:app --reload
```

## App directory breakdown
- main.py: FastAPI app containing HTTP routes
- models.py: data validation for a Receipt object
- points.py: contains method calc_points(receipt) that calculates points for a given receiptREAD