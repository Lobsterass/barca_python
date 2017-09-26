class Product:
	name = ""
	price = 0
	count = 0
	tax = 1

	def __init__(self, name, price, count, tax):
		self.name = name
		self.price = price
		self.count = count
		self.tax = tax

	def price_with_tax(self):
		total = self.price * self.count * self.tax
		if total > 500:
			return 0.9 * total
		else:
			return total

products = [Product(name="äpplen", price=900, count=2, tax=1.25), Product(name="apelsin", price=100, count=1, tax=1.06), Product(name="päron", price=200, count=2, tax=1.25)]

total_price = 0
for product in products:
	total_price = total_price + product.price_with_tax()

for product in products:
	print(product.name, product.price_with_tax())

