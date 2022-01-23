from datetime import date,time,datetime
import calendar,math,string
today=date.today()
time=time()
a=datetime.now()
b=datetime(2021,12,2)
print("Today date is ",today)
print("The time is ",time)
print("Current date and time is ",a)
print("Date and time of 2021 is ",b)
print("Calendar of 2018 is: ")
print(calendar.calendar(2018))
print("Calendar of 2022 feb : ")
print(calendar.month(2022,2))
r=float(input("Enter the radius of the circle: "))
pi=math.pi
area=pi*r*r
print("Area of the circle is ",area)
n=float(input("Enter a value: "))
print("Square root of the given value is ",math.sqrt(n))
print(string.digits)
print(string.ascii_letters)