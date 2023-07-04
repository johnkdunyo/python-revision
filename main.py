# store management project
import csv


class Item:
    pay_rate: 0.8

    all = []

    def __init__(self, name: str, price: float, quantity=0):
        # running validations
        assert price >= 0, f"Price {price} should be greater than 0"
        assert quantity >= 0, f"Quantity {quantity} should be greater than or equal 0"

        self.name = name
        self.price = price
        self.quantity = quantity

        # actions to execute; this adds any instance created to the all class attribute
        Item.all.append(self)

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

    def calculate_total_price(self):
        return self.price * self.quantity

    # decorate to make the method a class method
    # this reads from the csv file and instantiates new instances for each record
    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as file:
            reader = csv.DictReader(file)
            items = list(reader)

        for item in items:
            Item(item.get("name"), float(item.get("price")), int(item.get('quantity')))


# test

Item.instantiate_from_csv()
# prints all instance in the repr format in the class
print(Item.all)
