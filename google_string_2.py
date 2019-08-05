s=input("enter")
n = s.find('not')
b = s.find('bad')
print(n)
print(b)

if n != -1 and b != -1 and b > n:
	s = s[:n] + 'good' + s[b+3:]
	print(s)	