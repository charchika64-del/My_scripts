import math
def calc_distance(x1,x2,y1,y2):
    distance_x=(x2-x1)**2
    distance_y=(y2-y1)**2
    actual_distance=math.sqrt(distance_x+distance_y)
    #Case1:Suppose if the square root is 5.25
    #Case2:Suppose if the square root is 6.0
    actual_distance2=math.isqrt(distance_x+distance_y)
    #The above line removes the decimal part.
    #Case1:So, it is going to be 5 only
    #Case2:So, it is going to be 6 only
    if actual_distance==actual_distance2:
        #Case1:5.25==5[False]
        #Case2:6.0==6[True]
        return actual_distance
        #Runs for second case
    else:
        return f"√{distance_x+distance_y}"
        #Runs for first case
        #This avoids roots with floating numbers.
    
while True:
    x1=int(input("Enter x1: "))
    x2=int(input("Enter x2: "))
    y1=int(input("Enter y1: "))
    y2=int(input("Enter y2: "))
    distance=calc_distance(x1,x2,y1,y2)
    print(f"The distance between the two points is {distance} units")
    
