# Task 1
class BudgetCategory:
    def __init__(self, food, entertainment, utilities, shopping):
        self.__food = food
        self.__entertainment = entertainment
        self.__utilities = utilities
        self.__shopping = shopping

# Task 2
    def get_food_budget(self):
        return self.__food

    def get_entertainment_budget(self):
        return self.__entertainment

    def get_utilities_budget(self):
        return self.__utilities

    def get_shopping_budget(self):
        return self.__shopping

    def set_food_budget(self, food_budget):
        if food_budget > 0:
            self.__food = food_budget
            print(f"Set new food budget {self.get_food_budget()}")
        else:
            print("Invalid input. Budget must be more than 0")

    def set_entertainment_budget(self, entertainment_budget):
        if entertainment_budget > 0:
            self.__entertainment = entertainment_budget
            print(f"Set new entertainment budget {self.get_entertainment_budget()}")
        else:
            print("Invalid input. Budget must be more than 0")

    def set_utilities_budget(self, utilities_budget):
        if utilities_budget > 0:
            self.__utilities = utilities_budget
            print(f"Set new utility budget {self.get_utilities_budget()}")
        else:
            print("Invalid input. Budget must be more than 0")

    def set_shopping_budget(self, shopping_budget):
        if shopping_budget > 0:
            self.__shopping = shopping_budget
            print(f"Set new shopping budget {self.get_shopping_budget()}")
        else:
            print("Invalid input. Budget must be more than 0")

# Task 3

    def add_expense(self, expense_amount):
        print("Expense Categories: Food, Entertainment, Utilities, or Shopping")
        select_category = input("Please select a category that you would like to add an expense to: ").lower()
        if select_category == "food":
            if expense_amount > 0:
                self.__food -= expense_amount
                print(f"Added expense amount: {expense_amount}")
            else:
                print("Expense must be greater than 0.")
        elif select_category == "entertainment":
            if expense_amount > 0:
                self.__entertainment -= expense_amount
                print(f"Added expense amount: {expense_amount}")
            else:
                print("Expense must be greater than 0.")
        elif select_category == "utilities":
            if expense_amount > 0:
                self.__utilities -= expense_amount
                print(f"Added expense amount: {expense_amount}")
            else:
                print("Expense must be greater than 0.")
        elif select_category == "shopping":
            if expense_amount > 0:
                self.__shopping -= expense_amount
                print(f"Added expense amount: {expense_amount}")
            else:
                print("Expense must be greater than 0.")
        else:
            print("Invalid input. Please enter a category mentioned above")

# Task 4

    def display_category_summary(self):
        print(f"Food Budget: {new_budget.get_food_budget()} \n Entertainment Budget: {new_budget.get_entertainment_budget()}")
        print(f"Utility Budget: {new_budget.get_utilities_budget()} \n Shopping Budget: {new_budget.get_shopping_budget()}")

# Creating new budget
new_budget = BudgetCategory(200, 50, 500, 100)

# Setting new food budget
new_budget.set_food_budget(500)

# Adding a new expense to the selected budget
new_budget.add_expense(25)

# Displaying all the budget categories
new_budget.display_category_summary()