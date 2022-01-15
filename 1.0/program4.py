# Program to calculate salary of an employee

# Getting the basic salary details of the employee
nameOfEmployee=input("Enter name of the Employee\n")
basicPay=float(input("Enter Basic Pay\n"))

# Calculating the HRA, DA and Salary
hra=(10/100)*basicPay
ta=(5/100)*basicPay
salary=basicPay+hra+ta

# Printing the salary details
print("Name of the Employee:",nameOfEmployee)
print("Basic Pay:",basicPay)
print("HRA:",hra)
print("TA:",ta)
print("Salary:",salary)