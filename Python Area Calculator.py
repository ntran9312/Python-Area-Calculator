# Create a program that allows the user to enter 2 numbers representing the width and length of a rectangle. The program calculates and displays the area of the rectangle.
width = int(input("Enter the width of your rectangle:"))
length = int(input("Enter the length of your rectangle:"))
area = width * length
print("The area of your rectangle is " + str(area))

# BONUS PROGRAMS >>>>

#PerimeterCalc
#Create a program that allows the user to enter 2 numbers representing the width and length of a rectangle. The program calculates and displays the perimeter of the rectangle.
print("")
width = int(input("Enter the width of your rectangle:"))
length = int(input("Enter the length of your rectangle:"))
perimeter = (width * 2) + (length * 2)
print("The perimeter of your rectangle is " + str(perimeter))
#Restaurant Tip Calculator 
#Create a program that allows the user to enter the price of a meal at a restaurant. The program calculates the amount of the tip to be paid at 20%. The tip and total price are then displayed separately.

#Volume and Surface Calc 
#Create a program that allows the user to enter 3 numbers representing the height, width and length of a cuboid. The program calculates and displays the volume and total surface area of the cuboid. 
print("")
width = int(input("Enter the width of your cuboid:")) 
length = int(input("Enter the length of your cuboid:"))
height = int(input("Enter the height of your cuboid:"))
volume = width * length *  height
print("The volume of your cuboid is " + str(volume))
