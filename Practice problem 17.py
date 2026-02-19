L = []

c = "y"

while c == "y" or c == "Y" :
    element = float(input("Enter Your Number :"))
    L.append(element)
    c = input("Do you want to add more numbers (Y,N) : ")



mean = sum(L)/len(L)

print (mean)