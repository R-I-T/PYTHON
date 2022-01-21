str=input("Enter a string: ")
ch=str[0]
str1=""
str1=str1+ch
length=len(str)
for i in range(1,length):
	if str[i]==ch:
		str1+='$'
	else:
	    str1+=str[i]
print(str1)
