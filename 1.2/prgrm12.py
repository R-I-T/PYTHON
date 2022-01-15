n=int(input("Enter the number : "))

print("Multiplication table of {} is ".format(n))
for i in range(1,11):
	print(n , '*' , i ,'=' ,n*i)
