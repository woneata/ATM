print("Hello world")


class Car:
    # this defines the constructor
    def __init__(self, name, color):
      self.model=name
      self.color=color

    def my_car(self):
      print("My car’s model is ", self.model)
myCar1 = Car("BMW", "White")
del myCar1.model
myCar1.my_car()