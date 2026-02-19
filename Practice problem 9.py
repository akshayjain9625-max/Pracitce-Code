import math 

# side1 = float(input("Enter the first side of your triangle : "))
# side2 = float(input("Enter the second side of your triangle : "))
# side3 = float(input("Enter the third side of your triangle : "))


# if (side1 == side2 and side1 == side3 and side2 == side3):
#     print ("This is an Equilateral triangle")

# elif (side1 == side2 or side1 == side3 or side2 == side3):
#     print("This is an Isoceles Triangle")

# else:
#     print ("This is an Scalane Triangle")


def triangle_side(side1, side2, side3):
    if (side1 == side2 and side1 == side3 and side2 == side3):
        return "This is an Equilateral triangle"

    elif (side1 == side2 or side1 == side3 or side2 == side3):
        return "This is an Isoceles Triangle"

    else:
        return "This is an Scalane Triangle"

side1 = float(input("Enter the first side of your triangle : "))
side2 = float(input("Enter the second side of your triangle : "))
side3 = float(input("Enter the third side of your triangle : "))


print (triangle_side(side1 , side2, side3))





