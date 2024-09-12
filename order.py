class Customer:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Customer(name={self.name!r})"


class Coffee:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Coffee(name={self.name!r})"


class Order:
    all_orders = []

    def __init__(self, coffee, customer, price):
        self.coffee = coffee
        self.customer = customer
        self._set_price(price)
        Order.all_orders.append(self)

    def _set_price(self, price):
        if not hasattr(self, '_price') and isinstance(price, float) and 1.0 <= price <= 10.0:
            self._price = price

    @property
    def price(self):
        return self._price

    def __repr__(self):
        return f"Order(coffee={self.coffee!r}, customer={self.customer!r}, price={self.price!r})"


def test_order():
    # Create instances of Customer and Coffee
    customer1 = Customer("Alice")
    coffee1 = Coffee("Espresso")

    customer2 = Customer("Bob")
    coffee2 = Coffee("Latte")

    # Create Order instances
    order1 = Order(coffee=coffee1, customer=customer1, price=4.5)
    order2 = Order(coffee=coffee2, customer=customer2, price=7.0)

    # Print the orders
    print("Order 1:", order1.customer, order1.coffee, order1.price)
    print("Order 2:", order2.customer, order2.coffee, order2.price)

    # Print all orders
    print("All orders:", Order.all_orders)

    # Attempt to set invalid prices
    print("Attempt to set an invalid price on order1:")
    try:
        order1._set_price(12.0)  # Should not change
    except AttributeError:
        print("Price cannot be changed after order is instantiated")
    print("Order 1 price after invalid set attempt:", order1.price)

    # Attempt to set valid prices
    print("Setting a valid price on order1:")
    try:
        order1._set_price(5.0)  # Should not change
    except AttributeError:
        print("Price cannot be changed after order is instantiated")
    print("Order 1 price after valid set attempt:", order1.price)


test_order()