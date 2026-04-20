import json
import os
import math
from app.models import Shop, Car
from app.customer import Customer


def shop_trip() -> None:
    config_path = os.path.join(os.path.dirname(__file__), "config.json")
    with open(config_path, "r") as file:
        config = json.load(file)

    fuel_price = config["FUEL_PRICE"]
    shops = [
        Shop(s["name"], s["location"], s["products"])
        for s in config["shops"]
    ]

    for c_data in config["customers"]:
        car = Car(c_data["car"]["brand"], c_data["car"]["fuel_consumption"])
        customer = Customer(
            c_data["name"],
            c_data["product_cart"],
            c_data["location"],
            c_data["money"],
            car
        )

        print(f"{customer.name} has {customer.money} dollars")

        cheapest_shop = None
        min_total_cost = float("inf")
        trips_info = []

        for shop in shops:
            # Розрахунок дистанції з перенесенням рядків для E501
            dist_to_shop = math.sqrt(
                (shop.location[0] - customer.location[0]) ** 2
                + (shop.location[1] - customer.location[1]) ** 2
            )

            total_distance = dist_to_shop * 2
            fuel_needed = total_distance * customer.car.fuel_consumption / 100
            fuel_cost = fuel_needed * fuel_price
            products_cost = shop.get_products_cost(customer.cart)

            total_trip_cost = round(fuel_cost + products_cost, 2)

            trips_info.append(
                f"{customer.name}'s trip to the {shop.name} "
                f"costs {total_trip_cost}"
            )

            if total_trip_cost < min_total_cost:
                min_total_cost = total_trip_cost
                cheapest_shop = shop

        for info in trips_info:
            print(info)

        if cheapest_shop and customer.money >= min_total_cost:
            print(f"{customer.name} rides to {cheapest_shop.name}")

            p_cost = cheapest_shop.get_products_cost(customer.cart)
            customer.print_receipt(cheapest_shop, p_cost)

            print(f"\n{customer.name} rides home")
            customer.money = round(customer.money - min_total_cost, 2)
            print(f"{customer.name} now has {customer.money:g} dollars\n")
        else:
            print(
                f"{customer.name} doesn't have enough money "
                "to make a purchase in any shop"
            )
