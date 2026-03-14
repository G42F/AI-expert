import cv2
import numpy as np
def apply_filter(image, filter_type):
    '''Applies a filter to an image using convolution.'''
    filterimage = image.copy()
    if filter_type == 'red_tint':
        filterimage[:, :, 0] = 0
        filterimage[:, :, 1] = 0
    elif filter_type == 'green_tint':
        filterimage[:, :, 0] = 0
        filterimage[:, :, 2] = 0
    elif filter_type == 'blue_tint':
        filterimage[:, :, 1] = 0
        filterimage[:, :, 2] = 0
    elif filter_type == 'increase_red':
        filterimage[:,:,2]= cv2.add(filterimage[:,:,2], 50)
    elif filter_type == 'decrease_blue':
        filterimage[:,:,0]= cv2.add(filterimage[:,:,0], 50)
    return filterimage

# Load the image
image = cv2.imread('myedit.jpg')
if image is None:
    print("Error: Image not found.")
    
else: 
    filter_type = "original"
    print("Press the following keys to apply filters:")
    print("r: Red Tint")
    print("g: Green Tint")
    print("b: Blue Tint")
    print("i: Increase Red")
    print("d: Decrease Blue")
    print("q: Quit")
    while True:
        filterimage =   apply_filter(image, filter_type)
        cv2.imshow('Filtered Image', filterimage)
        key = cv2.waitKey(0) & 0xFF
        if key == ord('r'):
            filter_type = 'red_tint'
        elif key == ord('g'):
            filter_type = 'green_tint'
        elif key == ord('b'):
            filter_type = 'blue_tint'
        elif key == ord('i'):
            filter_type = 'increase_red'
        elif key == ord('d'):
            filter_type = 'decrease_blue'
        elif key == ord('q'):
            break   
        else:
            print("Invalid key. Please enter r,g,b,i,d,q.")
cv2.destroyAllWindows()     