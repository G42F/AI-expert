import cv2
import numpy as np
import matplotlib.pyplot as plt

def display_image(title,image):
    '''Utility function to display an image'''
    plt.figure(figsize=(8,8))
    if len(image.shape) == 2: # Grayscale image
        plt.imshow(image, cmap='gray')
    
    else:
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    plt.title(title)
    plt.axis("off")
    plt.show()

def edge_detection(image_path="Screenshot 2025-10-15 203444.png"):
    '''Interactive activity to perform edge detection on an image and filtering'''

    Image=cv2.imread(image_path)
    if Image is None:
        print("Error: Image not found. Please check the path and try again.")
        return
    
    gray_image=cv2.cvtColor(Image,cv2.COLOR_BGR2GRAY)
    display_image("Grayscale Image", gray_image)
    print("Select the edge detection method:")
    print("1. Sobel Edge Detection")
    print("2. Canny Edge Detection")
    print("3. Laplacian Edge Detection")
    print("4. Gaussian Blur")
    print("5. Median Blur")
    print("6. Exit")

    while True:
        choice = input("Enter your choice (1-6): ")
        if choice == '1':
            sobelx = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=5)
            sobely = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=5)
            sobel_edges = cv2.magnitude(sobelx, sobely)
            display_image("Sobel Edge Detection", sobel_edges)
        
        elif choice == '2':
            canny_edges = cv2.Canny(gray_image, 100, 200)
            display_image("Canny Edge Detection", canny_edges)

        elif choice == '3':
            laplacian_edges = cv2.Laplacian(gray_image, cv2.CV_64F)
            display_image("Laplacian Edge Detection", laplacian_edges)

        elif choice == '4':
            gaussian_blur = cv2.GaussianBlur(gray_image, (5, 5), 0)
            display_image("Gaussian Blur", gaussian_blur)

        elif choice == '5':
            median_blur = cv2.medianBlur(gray_image, 5)
            display_image("Median Blur", median_blur)

        elif choice == '6':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


edge_detection()
