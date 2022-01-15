n=int(input("Enter the limit: "))
a=0
b=1
count=0
print("Fibonacci Series: ")
while(count < n):
	print(a)
	c=a+b
	a=b
	b=c
	count += 1
