from dataclasses import dataclass
from helpers import FoodVModel
from typing import Optional, Union
from pydantic import BaseModel, validator, ValidationError, field_validator


@dataclass
class FoodItem:
    id: int
    name: str
    price: float

    def to_dict(self):
        return {'id': self.id, 'name': self.name, 'price': self.price}



if __name__ == "__main__":
    items = [FoodItem(1, 'Kabab', -1), FoodItem(2, 'Lavangi', 15), FoodItem(5, 'Dolma', 25)]

    for item in items:
        # print(item.to_dict())
        try:
            model = FoodVModel(**item.to_dict())
        except ValidationError as e:
            print(f'this is error: {e}')

