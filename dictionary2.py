basket = { 'blueberry': 22, 'coconut': 2, 'almond': 15, 'salmon': 1 }
print(basket['coconut'])
print(basket.keys())
print(basket.values())
basket['salmon']  = 3
basket.pop('salmon')
del basket['almond']
print(basket)