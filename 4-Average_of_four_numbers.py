#fourth exercise
#Make a Program that asks for the 4 bimonthly notes and shows the average.

number_1 = 0
number_2 = 0
number_3 = 0
number_4 = 0
average = 0

print("Insert the four notes below:")
number_1 = (input("First Note: "))
number_2 = (input("Second Note: "))
number_3 = (input("Third Note: "))
number_4 = (input("Fourth Note: "))

average = (int(number_1) + int(number_2) + int(number_3) + int(number_4)) / 4
print("The final note is:", average)