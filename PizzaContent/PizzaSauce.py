from .Constants import *


class Pizza(object):
    def __init__(self,pizza_name,description,cost):
        self.pizza_name   = pizza_name
        self.description  = description
        self.cost         = cost
    def get_description(self):
        return self.description
    def get_cost(self):
        return self.cost
    def get_name(self):
        return self.pizza_name
    
class MargheritaPizza(Pizza):
    _margherita = "Margherita"
    _description= "Description"
    _cost       = "Cost"
    def __init__(self, 
                 pizza_name  = _margherita, 
                 description = PIZZA_MENU[_margherita][_description], 
                 cost        = PIZZA_MENU[_margherita][_cost]
                 ):
        super().__init__(pizza_name,description,cost)

class TexanBBQPizza(Pizza):
    _texanbbq   = "TexanBBQ"
    _description= "Description"
    _cost       = "Cost"
    def __init__(self,
                 pizza_name  = _texanbbq,
                 description = PIZZA_MENU[_texanbbq][_description],
                 cost        = PIZZA_MENU[_texanbbq][_cost]
                 ):
        super().__init__(pizza_name,description,cost)

class SupremePizza(Pizza):  
    _supreme    = "Supreme"
    _description= "Description"
    _cost       = "Cost"
    def __init__(self,
                 pizza_name  = _supreme,
                 description = PIZZA_MENU[_supreme][_description],
                 cost        = PIZZA_MENU[_supreme][_cost]
                 ):
        super().__init__(pizza_name,description,cost)

class HawaiianPizza(Pizza):
    _hawaiian   = "Hawaiian"
    _description= "Description"
    _cost       = "Cost"
    def __init__(self,
                 pizza_name  = _hawaiian,
                 description = PIZZA_MENU[_hawaiian][_description],
                 cost        = PIZZA_MENU[_hawaiian][_cost]
                 ):
        super().__init__(pizza_name,description,cost)

class PepperoniPizza(Pizza):
    _pepperoni  = "Pepperoni"
    _description= "Description"
    _cost       = "Cost"
    def __init__(self,
                 pizza_name  = _pepperoni,
                 description = PIZZA_MENU[_pepperoni][_description],
                 cost        = PIZZA_MENU[_pepperoni][_cost]
                 ):
        super().__init__(pizza_name,description,cost)

class Decorator(Pizza):
    def __init__(self, pizza, sauce_name, sauce_cost):
                self.pizza  = pizza
                self.sauce_name = sauce_name
                self.sauce_cost = sauce_cost
                super().__init__(pizza.pizza_name, pizza.description, pizza.cost)
    
    def get_description(self):
        return f"{self.pizza.get_description()} with {self.sauce_name}"
    
    def get_cost(self):
        return self.pizza.get_cost() + self.sauce_cost
    
class Olive(Decorator):
    _olive      = "Olive"
    def __init__(self, pizza,
                 sauce_name = _olive,
                 sauce_cost = SAUCE_COST_LIST[_olive]
                 ):
        super().__init__(pizza, sauce_name, sauce_cost)

class Corn(Decorator):
    _corn       = "Corn"
    def __init__(self, pizza,
                 sauce_name = _corn,
                 sauce_cost = SAUCE_COST_LIST[_corn]
                 ):
        super().__init__(pizza, sauce_name, sauce_cost)

class Mushroom(Decorator):
    _mushroom   = "Mushroom"
    def __init__(self, pizza,
                 sauce_name = _mushroom,
                 sauce_cost = SAUCE_COST_LIST[_mushroom]
                 ):
        super().__init__(pizza, sauce_name, sauce_cost)

class Chedar(Decorator):
    _chedar     = "Chedar"
    def __init__(self, pizza,
                 sauce_name = _chedar,
                 sauce_cost = SAUCE_COST_LIST[_chedar]
                 ):
        super().__init__(pizza, sauce_name, sauce_cost)
        
class Sausage(Decorator):
    _sausage    = "Sausage"
    def __init__(self, pizza,
                 sauce_name = _sausage,
                 sauce_cost = SAUCE_COST_LIST[_sausage]
                 ):
        super().__init__(pizza, sauce_name, sauce_cost)
