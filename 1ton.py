def method_a(n):
	sum = 0
	for i in range(n+1):
		sum += i
	return sum

def method_b(n):
	sum = 0
	current_value = 0
	while current_value <= n:
		sum += current_value
		current_value += 1
	return sum

def method_c(n):
	if n == 0:
		return 0
	return n+method_c(n-1)

n = int(input("Enter n:"))
print(method_a(n))
print(method_b(n))
print(method_c(n))