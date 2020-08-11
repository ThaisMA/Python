#Sixth Program
#Make a Program that asks for the radius of a circle, calculate and show its area.

pi = 3.1415

radius = (input("Enter the value of the radium: "))
circle = (float(radius) ** 2) * pi
print("The area of the circle is: {0}".format((round(circle,2))))


#Notes (both expressions remove the excess of the floating number leaving only two numbers after the comma)
#round(value,2)
#format(value,'.2f')


