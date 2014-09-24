#3.23
for i in lst:
	if i[0] < 'N':
		print(i)

#3.25
n = eval(input('Enter n:'))
for i in range(4):
	 print(n*i)

#3.26
n = eval(input('Enter n:'))
for i in range(n):
	print(i**2)

#3.27
n = eval(input('Enter n:'))
for i in range(1,n+1):
	if (n % i == 0):
		print(i)

#3.30(Extra Credit Problem)

n = eval(input('Enter n:'))
a1 = n // 1000
a2 = (n % 1000)//100
a3 = (n % 100)//10
a4 = n % 10

print(a1)
print(a2)
print(a3)
print(a4)

