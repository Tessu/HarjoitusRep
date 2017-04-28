

class Product(object):
	

	def __init__(self, price, quantityoh, ide):
		self.id = ide
		self.price = price
		self.quantityoh = quantityoh

product1 = Product(100, 3, 1)
product2 = Product(234, 1, 2)
product3 = Product(55, 100, 3)

class Inventory(object):
	def __init__(self):
		self.products = []

	def add_product(self, prod):
		self.products.append(prod)

	def sum_inventory_value(self):
		sum = 0
		for product in self.products:
			sum += product.price

		return sum

inv1 = Inventory()
inv1.add_product(product1)
inv1.add_product(product2)
inv1.add_product(product3)

inv_value = inv1.sum_inventory_value()
print inv_value