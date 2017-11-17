inventory = [("00010-100", "Monitor", 1, 350.00), ("00010-200", "Desk lamps", 3, 55.00), ("00025-275", "Phone", 5, 85.00)]

print(inventory)

for x in inventory:
	(partno, descr, qty, price) = x
	print(partno)
	print(descr)
	print(qty)
	print(price)

inventory_dict = { "00010-100": ("Monitor", 1, 350.00) }
