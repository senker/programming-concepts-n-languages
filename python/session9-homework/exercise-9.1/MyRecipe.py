class MyRecipe:
    def __init__(self, calories, cooking_time):
        self.calories = calories
        self.cooking_time = cooking_time

    def cook(self):
        print("Cooking the recipe...")

# Create some recipe objects
recipe1 = MyRecipe(300, 45)
recipe2 = MyRecipe(400, 60)
recipe3 = MyRecipe(250, 30)
recipe4 = MyRecipe(500, 90)
recipe5 = MyRecipe(350, 50)

# Print out the recipes
print("Recipe 1 - Calories:", recipe1.calories, "Cooking time:", recipe1.cooking_time)
recipe1.cook()
print()
print("Recipe 2 - Calories:", recipe2.calories, "Cooking time:", recipe2.cooking_time)
recipe2.cook()
print()
print("Recipe 3 - Calories:", recipe3.calories, "Cooking time:", recipe3.cooking_time)
recipe3.cook()
print()
print("Recipe 4 - Calories:", recipe4.calories, "Cooking time:", recipe4.cooking_time)
recipe4.cook()
print()
print("Recipe 5 - Calories:", recipe5.calories, "Cooking time:", recipe5.cooking_time)
recipe5.cook()
