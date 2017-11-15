class InventoryItem():
	_id = ""
	
	def __init__(self, price='N/D', quantity=0):
		self.price = price
		self.quantity = quantity

	def add_new_item(self):
		self.quantity += 1
	
monitor = InventoryItem(25, 2)
print('Price:', monitor.price)
monitor.add_new_item()
print('Price:', monitor.quantity)
