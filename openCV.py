import cv2

#loadtheimage
image=cv2.imread("myedit.jpg")
#resize the window to a specific size without resizing the image 
cv2.namedWindow("loaded image",cv2.WINDOW_NORMAL)
cv2.resizeWindow("loaded image",800,500)

#disply the image in the resize window
cv2.imshow("loaded image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
#print image property 
print(f'image dimensions: {image.shape}')
