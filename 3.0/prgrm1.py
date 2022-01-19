def calculate(p,n,r):
	si=(p*n*r)/100
	print("Simple interest=",si)
	
age=int(input("Enter the age: "))
p=int(input("Enter the principle amt: "))
n=int(input("Enter the no. of years: "))
if(age<60):
	r=10
else:
	r=12
print(r)
calculate(p,n,r)
