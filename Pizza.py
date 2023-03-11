# The pizza superclass was defined by cost and description methods
class Pizza:
    def __init__(self, cost, description):
        self.description = description
        self.cost = cost

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost


# Pizza subclass was created
class ClassicPizza(Pizza):
    price = 80
    description = "Classic Pizza: sausage, cheddar cheese, special sauce"

    def __init__(self):
        super().__init__(self.price, self.description)


class MargheritaPizza(Pizza):
    price = 95
    description = "Margherita Pizza: tomato, sausage, mozzarella cheese, special sauce"

    def __init__(self):
        super().__init__(self.price, self.description)


class TurkPizza(Pizza):
    price = 90
    description = "Turk Pizza: sausage, pepper, mushroom, special sauce"

    def __init__(self):
        super().__init__(self.price, self.description)


class PlainPizza(Pizza):
    price = 70
    description = "Plain Pizza: olive, tomato, pepper"

    def __init__(self):
        super().__init__(self.price, self.description)


# Decorator is called superclass of all sauce classes
class Decorator(Pizza):
    def __init__(self, component):
        self.component = component

    def get_cost(self):
        return self.component.get_cost() + Pizza.get_cost(self)

    def get_description(self):
        return self.component.get_description() + ' ' + Pizza.get_description(self)


class Olives(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.cost = 3
        self.description = "with olive sauce."


class Mushrooms(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.cost = 7
        self.description = 'With mushroom sauce.'


class GoatCheese(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.cost = 8
        self.description = "With goat cheese sauce."


class Meat(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.cost = 12
        self.description = "With meat sauce."


class Onions(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.cost = 4
        self.description = "with onion sauce."


class Corn(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.cost = 6
        self.description = "With corn"
