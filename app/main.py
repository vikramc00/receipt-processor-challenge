# FastAPI app containing HTTP routes
from fastapi import FastAPI, HTTPException
from pydantic import StringConstraints
from typing import Annotated

from uuid import uuid4
from models import Receipt
from points import calc_points

app = FastAPI()


# Database: hashmap of receipt IDs to points
db: dict[str, int] = {}


@app.get("/")
def root():
    return {"Message": "Hello World"}


@app.post("/receipts/process", summary="Submits a receipt for processing", description="Returns the ID assigned to the receipt", response_model=dict[str, Annotated[str, StringConstraints(pattern=r"^\S+$")]])
def process_receipts(receipt: Receipt):
    try:
        id = str(uuid4())
        db[id] = calc_points(receipt)
        return {'id': id}
    except Exception as e:
        raise HTTPException(status_code=400, detail="The receipt is invalid")


@app.get("/receipts/{id}/points", summary="Returns the points awarded for the receipt", description="The number of points awarded", response_model=dict[str, int])
def get_points(id: Annotated[str, StringConstraints(pattern=r"^\S+$")]):
    try:
        points = db[id]
        return {'points': points}
    except KeyError:
        raise HTTPException(status_code=404, detail="No receipt found for that id")