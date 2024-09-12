class Customer:
    all_customers = []

    def __init__(self, name):
        self._set_name(name)
        Customer.all_customers.append(self)

    @property
    def name(self):
        return self._name
    
    

    @name.setter
    def name(self, value):
        self._set_name(value)

    def _set_name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value

    def orders(self):
        return [order for order in Order.all_orders if order.customer == self]

    def coffees(self):
        return list({order.coffee for order in self.orders()})

    def create_order(self, coffee, price):
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        spending = {}
        for customer in cls.all_customers:
            total = sum(order.price for order in customer.orders() if order.coffee == coffee)
            spending[customer] = total
        return max(spending, key=spending.get, default=None)



class Order:
    all_orders = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all_orders.append(self)


# Create some customers
alice = Customer("Alice")
bob = Customer("Bob")
carol = Customer("Carol")

# Create some orders
alice.create_order("Latte", 5.0)
alice.create_order("Espresso", 3.5)
bob.create_order("Latte", 4.5)
bob.create_order("Latte", 4.5)
carol.create_order("Espresso", 3.0)
carol.create_order("Latte", 5.5)

# Test the `name` property and setter
print("Alice's name:", alice.name)  # Output: Alice
alice.name = "Alicia"
print("Alice's new name:", alice.name)  # Output: Alicia

# Test the `coffees` method
print("Alice's coffees:", alice.coffees())  # Output: ['Latte', 'Espresso']
print("Bob's coffees:", bob.coffees())  # Output: ['Latte']
print("Carol's coffees:", carol.coffees())  # Output: ['Espresso', 'Latte']

# Test the `most_aficionado` method
print("Most aficionado for 'Latte':", Customer.most_aficionado("Latte"))  # Output: Bob

# Test the `most_aficionado` method for a coffee not ordered
print("Most aficionado for 'Mocha':", Customer.most_aficionado("Mocha"))  # Output: None
