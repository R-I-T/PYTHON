n=int(input("Enter the first number : "))
m=int(input("Enter the second number  : "))
i=1
while(i<=n and i<=m):
  if(n%i==0 and m%i==0):
    gcd = i
  i=i+1
print("GCD is", gcd)
