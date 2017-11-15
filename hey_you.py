for i in range(1, 101):
	phrase = ""
	if i % 3 == 0:
		phrase += "Hey"
	if i % 5 == 0:
		phrase += "You"

	if phrase == "":
		print(i)
	else:
		print(phrase)