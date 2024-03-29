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
    
    image1_bw = cv2.adaptiveThreshold(src=image1_gray, maxValue=255, adaptiveMethod=cv2.ADAPTIVE_THRESH_GAUSSIAN_C, thresholdType=cv2.THRESH_BINARY_INV, blockSize=3, C=2)
    _, image1_bw2 = cv2.threshold(image1_gray, 50, 255, cv2.THRESH_BINARY)
    
    fig = plt.figure(figsize=(10, 7)) 
    # setting values to rows and column variables 
    rows = 1
    columns = 2
    
    fig.add_subplot(rows, columns, 1)
    plt.imshow(image1_bw) 
    plt.axis('off') 
    plt.title("First") 
    
    fig.add_subplot(rows, columns, 2) 
    plt.imshow(image1_bw2) 
    plt.axis('off') 
    plt.title("Second") 
    
    
    #cv2.imshow("Image 1 Black and White", image1_bw)
    #cv2.waitKey(0)
    fig.show()
    
def activity2():
    print("Size of image: ", image1.size)
    print("Value of pixel at [33][33]: ", image1[33][33])    
    
def main():
    while(1):
        option = int(input("Enter Activity: "))
        match option:
            case 1:
                activity1()
            case 2:
                activity2()
            case _:
                break
main()