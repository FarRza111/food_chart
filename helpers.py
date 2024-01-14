from dataclasses import dataclass
from typing import Optional, Union
from pydantic import BaseModel, validator, ValidationError, field_validator

class FoodVModel(BaseModel):
    id: Optional[int] = None
    name: str
    price: Union[float, int]

    @field_validator('price')
    def price_mustbe_positive(cls, v):
        if v < 0:
            raise ValueError('Price must be positive')
        return v

    @field_validator('id')
    def kabab_should_be_meat(cls, value):
        if value == 2:
            raise ValueError('id should not be equal to 2')
        return value