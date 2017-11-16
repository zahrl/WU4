shopping_list = ['Milk', 'Apples', 'Eggs', 'Honey', 'Bananas', 'Bread']

print(shopping_list[1])
print(shopping_list[-2])
print(shopping_list[0:2])
print(shopping_list[0:-2])
print('Milk' in shopping_list)

print("FIFO: " + shopping_list.pop(0))

shopping_list.append("Dark Chocolate")
shopping_list.insert(0, "Blueberries")
shopping_list.insert(0, "Chocolate")
shopping_list.remove("Chocolate")

print("LIFO: " + shopping_list.pop())

for x in shopping_list:
	print("Get " + x)

for x in range(3):
	print("The 'count' is: ", x)

print('single quotation marks do not need to escape "double quotation" mark')