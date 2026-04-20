class Customer:
    def __init__(
            self,
            name: str,
            location: list,
            car: any,
            money: float,
            cart: dict
    ) -> None:
        self.name = name
        self.location = location
        self.car = car
        self.money = money
        self.cart = cart

    def print_receipt(self, shop: any, products_cost: float) -> None:
        from datetime import datetime
        date_str = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        print(f"Date: {date_str}")
        print(f"Thanks, {self.name}, for your purchase!")
        print("You have bought:")

        for item, count in self.cart.items():
            price = shop.products[item]
            item_total = round(count * price, 2)
            print(f"{count} {item}s for {item_total:g} dollars")

        print(f"Total cost is {round(products_cost, 2):g} dollars")
        print("See you again!")
