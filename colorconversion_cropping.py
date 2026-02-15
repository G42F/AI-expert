import cv2
import matplotlib.pyplot as plt

image=cv2.imread('myedit.jpg')
imagegb=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
plt.imshow(imagegb)
plt.title("rgbimage")
plt.show()

#convert the image to grayscale
grayimage=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
plt.imshow(grayimage,cmap='gray')
plt.title("grayscale image")
plt.show()



#crop the image
croppedimage=image[3000:0,100:400] 
croppedrgb=cv2.cvtColor(croppedimage,cv2.COLOR_BGR2RGB)
plt.imshow(croppedrgb)    
plt.title("cropped image")
plt.show()