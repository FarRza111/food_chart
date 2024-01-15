from typing import Any
from views import FoodItem
from helpers import FoodVModel
from dataclasses import dataclass



@dataclass
class FoodItem:
    id: int
    name: str
    price: float

    def to_dict(self):
        return {'id': self.id, 'name': self.name, 'price': self.price}



class User:


    def __init__(self, username, password, membership) -> None:
        self.username = username
        self.password = password
        self.membership = membership
        self.cart = []

    def add_to_char(self, food_item, quantity):
        item_with_quantity = {"food": food_item, "quantity": quantity}
        self.cart.append(item_with_quantity)
       

    def __repr__(self) -> str:
        return f'items in the backet is {self.cart}'
    

    def viw_char(self):
        if self.cart:
            total_price = 0

            print("Items of Cart..")

            for item_and_quant in self.cart:
                food = item_and_quant.get("food", "N food")
                quant = item_and_quant.get("quantity", 0)
                price = food_item.price
                total_price+=price 
                print(food)
                print(quant)
                print(price)
                print(f'this is {food} = {quant} and price: {price}')
                
                
            discount_percentage = self.get_discount_percent()
            discounted_amnt = total_price * (discount_percentage/100)
            amnt_to_pay = total_price - discounted_amnt

            print(amnt_to_pay)
            print(discounted_amnt)
        return f'this is amnt to pay: {amnt_to_pay} and discounted amnt : {discounted_amnt}'
            
    def get_discount_percent(self):
        
        return(
            20 if self.membership == "gold" else
            30 if self.membership == "platinum" else
            10 if self.membership == "silver" else 0
        )
    

if __name__ == "__main__":

    food_item = FoodItem(1, 'pizza', 64.03)
    user_obj = User('Fariz',1233, 'silver')
    print(user_obj.add_to_char(food_item.name, 14))
    print(user_obj.viw_char())




    # user_name = input("enter your username: ")
    # user_password = input("enter ur password: ")
    # user_membership = input("enter ur membership: (options -> gold; platinum; silver)")


    # food_id = int(input("enter your id:"))
    # food_name = str(input("enter your food name:"))
    # food_price = float(input("enter your food price:"))
    # food_item_obj = FoodItem(food_id, food_name, food_price)
    



    # user_obj = User(username=user_name,password=user_password, membership=user_membership)
    # user_obj.get_discount_percent("silver")
    
    # user_obj.add_to_char(food_name, food_price)
    
    # print(user_obj.viw_char())

    # food_pirce = FoodItem(123232, 'Apple', 'gold')

    # us = User("Fariz", 91919, "gold")
    # us.add_to_char('Apple', 2)
    # us.add_to_char('Tomato', 4)
    # # print(us)
    # print(us.viw_char())    
    # print(us.get_discount_percent())
    
    





