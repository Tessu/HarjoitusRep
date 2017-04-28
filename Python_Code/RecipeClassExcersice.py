keyword_list = ["soup", "beef", "chicken", "vegetable", "dessert"]

class Recipe(object):

	def __init__(self, keyword, ingredient1, ingredient2, ingredient3):
		self.keyword = keyword
		self.ingredient1 = ingredient1
		self.ingredient2 = ingredient2
		self.ingredient3 = ingredient3
	def __repr__(self):
		return ", ".join(self.keyword, self.ingredient1, self.ingredient2, self.ingredient3)

recipe1 = Recipe("chickensoup", "chicken", "carrot", "potatoes")
recipe2 = Recipe("vegetablesoup", "carrot", "potatoes", "cucumber")
recipe3 = Recipe("beefstew", "beef", "mushroom", "onion")
recipe4 = Recipe("dessert", "chocolate", "flour", "sugar")
recipe5 = Recipe("pizza", "beef", "tuna", "pineapple")




class RecipeManager(object):
	def __init__(self):
		self.beef_dishes = []
		self.vegetable_dishes = []
		self.desserts = []
		self.soup_dishes = []
		self.chicken_dishes = []
		self.uncategorized_dishes = []

	def add_recipe_uncategorized(self, rec):
		self.uncategorized_dishes.append(rec)

	def add_chicken_dish(self, dish):
		self.chicken_dishes.append(dish)

	def add_beef_dish(self, dish):
		self.beef_dishes.append(dish)

	def add_vegetable_dish(self,dish):
		self.vegetable_dishes.append(dish)

	def add_dessert(self,dish):
		self.desserts.append(dish)

	def add_soup(self,dish):
		self.soup_dishes.append(dish)

	def add_soup(self,dish):
		self.chicken_dishes.append(dish)

	def get_soups(self):
		return soup_dishes
	def get_beefs(self):
		return beef_dishes
	def get_chickens(self):
		return chicken_dishes
	def get_vegetables(self):
		return vegetable_dishes
	def get_desserts(self):
		return desserts



	def add_recipe(self):
		for recipe in self.uncategorized_dishes:
			if "beef" in recipe:
				recipemanager.add_beef_dish(recipe)
			if "vegetable" in recipe:
				recipemanager.add_vegetable_dish(recipe)
			if "dessert" in recipe:
				recipemanager.add_dessert(recipe)
			if "soup" in recipe:
				recipemanager.add_soup(recipe)
			if "chicken" in recipe:
				recipemanager.add_chicken_dish(recipe)





recipemanager = RecipeManager()
recipemanager.add_recipe_uncategorized(recipe1)
recipemanager.add_recipe_uncategorized(recipe2)
recipemanager.add_recipe_uncategorized(recipe3)
recipemanager.add_recipe_uncategorized(recipe4)
recipemanager.add_recipe_uncategorized(recipe5)


print recipemanager.get_desserts