#Distance taken in cenntimeters#

'''
distance = float(input("Enter the distance in Centimeters :"))

dist_in_meters = distance / 100

print (dist_in_meters, "meters")

'''

def distance(distance_in_cm):
    dist_in_meters = distance_in_cm / 100
    print(dist_in_meters, "meters")
    return dist_in_meters

distance(50.1)