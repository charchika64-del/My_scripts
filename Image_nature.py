#This program gives what type if nature image has by getting user input.
import math

def image_nature(magni):
    magni_pos = abs(magni)  # for size
    if magni < 0:
        if magni_pos == 1:
            print("The image is real, inverted and same size.")
        elif magni_pos > 1:
            print("The image is real, inverted and enlarged.")
        else:
            print("The image is real, inverted and diminished.")
    elif magni > 0:
        if magni_pos == 1:
            print("The image is virtual, erect and same size.")
        elif magni_pos > 1:
            print("The image is virtual, erect and enlarged.")
        else:
            print("The image is virtual, erect and diminished.")
    else:
        print("The image is point sized.")


while True:
    magnification=float(input("Enter magnification: "))
    image_nature(magnification)
