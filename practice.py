class Budget:

   def __init__(self, category, amount):
       self.category = category
       self.amount = amount

# methods
   def deposit(self):
       return "this is a deposit method"
   def check_balance(self):
        pass

    def withdraw(self):
        pass

    def transfer(self):
        pass


category = Budget("clothing", 1000)
category_1 = Budget("Food", 1000)
category_2 = Budget("Entertainment", 1000)

print (category.deposit())