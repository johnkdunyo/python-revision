# store management project
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

        # actions to execute; this add any instance created to the all class attribute
        Item.all.append(self)

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

    def calculate_total_price(self):
        return self.price * self.quantity


# test
item1 = Item("laptop", 2.50, 4)
print(item1.calculate_total_price())

print(Item.__dict__)  # attributes at class level
print(item1.__dict__)  # attributes at instance level

# prints all instance in the repr format in the class
print(Item.all)
