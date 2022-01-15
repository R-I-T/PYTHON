n=int(input("Enter the number : "))
s=0
temp=n
while temp>0:
	rem=temp%10
	s=s+rem**3
	temp=temp//10
if n==s:
   print(n,"is an Armstrong number")
else:
   print(n,"is not an Armstrong number")

