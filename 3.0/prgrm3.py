def sum(a,b,c):
	s=a+b+c
	if(a==b==c):
		print("the numbers are equal thus thrice of sum is",3*s)
	else:
		print("sum is",s)
	


a=int(input("Enter the number: "))
b=int(input("Enter the number: "))
c=int(input("Enter the number: "))
sum(a,b,c)
