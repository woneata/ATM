class Category:

    def __init__(self, category, amount):
        self.category = category
        self.amount = amount

    def deposit(self, amount):
        self.amount += amount
        return "You have successfully deposited {} in {} category".format(amount, self.category)

    def budget_balance(self):
        return "This is your current balance: {}".format(self.amount)

    def check_balance(self, amount):
        # this should return a True or False, it checks if amount is less or greater than self.amount
        if amount == 1:
            return True
        else:
            return False
        pass

    def withdraw(self, amount):
        self.amount -= amount
        return "You have successfully withdrawn {} in {} category".format(amount, self.category)

    def transfer(self, amount, category):
        # transfer between two instantiated categories
        return self.withdraw(amount) + ' ' + category.deposit(amount)
        #return "You have successfully transferred {} from {} to {}".format(amount, self.category, self.category)
    # clothing_category.deposit(food_category.transfer(100)


clothing_category = Category('Clothing', 300)
food_category = Category('Food', 500)
car_category = Category('Car Expenses', 600)

# print(food_category.deposit(250))
# print(food_category.budget_balance())
# print(food_category.transfer(25, clothing_category))
# print(food_category.check_balance)

