"intro"
"""the process of hiding the internal functionality of the application from the users"""
"""a class consists of one or more abstract method is called as abstract class"""
from abc import ABC, abstractmethod
class car(ABC):
    @abstractmethod
    def engine_make(self):
        pass

    def price(self, price):
        print(price)
    @abstractmethod
    def paint_material(self):
        pass

class bmw(car):
    def engine_make(self):
        print("bmw engine")
    def paint_material(self):
        print('acenta_arora')
b = bmw()
b.price(25000)