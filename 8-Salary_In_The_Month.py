#Eighth Exercise
#Make a Program that asks how much you earn per hour and the number of 
#hours worked in the month. Calculate and show your total salary in that month.

salary = (input("Enter your salary per hour: "))
hours = (input("Enter the number of hours worked: "))

total = float(salary) * float(hours)
print("Your Salary in that month is:{0}".format(total))
