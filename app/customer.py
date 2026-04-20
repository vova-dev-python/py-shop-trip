import datetime
from typing import Dict, List
from app.models import Shop, Car


class Customer:
    def __init__(
        self,
        name: str,
        cart: Dict[str, int],
        location: List[int],
        money: float,
        car: Car
    ) -> None:
        self.name = name
        self.cart = cart
        self.location = location
        self.money = money
        self.car = car

    def print_receipt(self, shop: Shop, products_cost: float) -> None:
        now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"\nDate: {now}")
        print(f"Thanks, {self.name}, for your purchase!")
        print("You have bought:")

        for item, count in self.cart.items():
            price = shop.products[item]
            item_total = count * price
            print(f"{count} {item}s for {item_total:g} dollars")

        print(f"Total cost is {products_cost:g} dollars")
        print("See you again!")
