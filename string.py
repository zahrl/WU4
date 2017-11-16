s = "ThisString"

print(s[0])
print(s[4:])
print(s[4:7])

len(s)

for x in s:
	print(x)

s = 'Hello, name'
s = s.replace('name', 'Sveta')

array = s.split()

print(array)

time = '00:11:22'
hrs, mins, sec = time.split(':')
print(time + " hrs: " + hrs + " mins: " + mins + " sec: " + sec)