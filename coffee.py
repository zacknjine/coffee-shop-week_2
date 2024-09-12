class Customer:
    def __init__(self, name):
        self.name = name


class Order:
    all_orders = []


    def __init__(self, coffee, customer, price):
        if not isinstance(price, (int, float)):
            raise ValueError("Price must be a number")
        self.coffee = coffee
        self.customer = customer
        self.price = price
        Order.all_orders.append(self)


class Coffee:
    all_coffees = []


    def __init__(self, name):
        if not isinstance(name, str) or len(name) < 3:
            raise ValueError("Name must be a string with at least 3 characters")
        self._set_name(name)
        Coffee.all_coffees.append(self)


    def _set_name(self, name):
        self.name = name


    @property
    def name(self):
        return self._name


    @name.setter
    def name(self, value):
        if not hasattr(self, '_name') and isinstance(value, str) and len(value) >= 3:
            self._name = value


    def orders(self):
        return [order for order in Order.all_orders if order.coffee == self]


    def customers(self):
        return list({order.customer for order in self.orders()})


    def num_orders(self):
        return len(self.orders())


    def average_price(self):
        orders = self.orders()
        return sum(order.price for order in orders) / len(orders) if orders else 0


# Test code
if __name__ == "__main__":
    # Create some coffee instances
    espresso = Coffee("Espresso")
    latte = Coffee("Latte")


    # Create some customers
    alice = Customer("Alice")
    bob = Customer("Bob")
    charlie = Customer("Charlie")
    david = Customer("David")


    # Create some orders
    Order(espresso, alice, 3.50)
    Order(espresso, bob, 4.00)
    Order(latte, charlie, 5.00)
    Order(latte, david, 4.50)
    Order(latte, alice, 4.75)


    # Test Coffee class methods
    print(f"Coffee Name: {espresso.name}")
    print(f"Number of Orders for Espresso: {espresso.num_orders()}")
    print(f"Average Price of Espresso: ${espresso.average_price():.2f}")


    print(f"Coffee Name: {latte.name}")
    print(f"Number of Orders for Latte: {latte.num_orders()}")
    print(f"Average Price of Latte: ${latte.average_price():.2f}")


    # Test customers for Latte
    print(f"Customers for Latte: {[customer.name for customer in latte.customers()]}")