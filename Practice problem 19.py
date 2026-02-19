print ("Welcome, Know Your Percentage Here ;")

c = "y"

while c == "y" or c == "Y":

    marks1 = float(input("Enter Your Marks Subject 1 : "))
    marks2 = float(input("Enter Your Marks Subject 2 : "))
    marks3 = float(input("Enter Your Marks Subject 3 : "))

    if marks1 > 100 or marks2 > 100 or marks3 > 100:
        print ("You Entered Incorrect marks, Please Re-enter Your Marks ;")
        continue
    
    else:
        print("Your Percentage is : ", (marks1 + marks2 + marks3)/3)
    
    c = input("Do you want to calculate again (y,n) :")

    

