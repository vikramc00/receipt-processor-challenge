# data validation for a Receipt object
from pydantic import BaseModel, StringConstraints
from typing import Annotated

class Item(BaseModel):
    shortDescription: Annotated[str, StringConstraints(pattern=r"^[\w\s\-]+$")] 
    price: Annotated[str, StringConstraints(pattern=r'^\d+\.\d{2}$')] 


class Receipt(BaseModel):
    retailer: Annotated[str, StringConstraints(pattern=r'^[\w\s\&-]+$')]
    purchaseDate: Annotated[str, StringConstraints(pattern=r'^\d{4}-\d{2}-\d{2}$')] 
    purchaseTime: Annotated[str, StringConstraints(pattern=r'^\d{2}:\d{2}$')]
    items: list[Item]
    total: Annotated[str, StringConstraints(pattern=r'^\d+\.\d{2}$')]
