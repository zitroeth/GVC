import cv2
import numpy as np
import matplotlib.pyplot as plt

image1 = cv2.imread("Images/image1.png")
image2 = cv2.imread("Images/image2.jpg")


def activity1():
    cv2.imshow("Image 1", image1)
    cv2.waitKey(0)
    
    image1_gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    print("Pixel value at [33, 33]: ", image1_gray[33,33])
    cv2.imshow("Image 1 Grayscale", image1_gray)
    cv2.waitKey(0)
    
def main():
    while(1):
        option = int(input("Enter Activity: "))
        match option:
            case 1:
                activity1()
            case _:
                break
main()