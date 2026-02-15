import cv2
import numpy as np
import matplotlib.pyplot as plt
image=cv2.imread('myedit.jpg')
imagergb=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

(h,w)=image.shape[:2]
center=(w/2,h/2)
M=cv2.getRotationMatrix2D(center,45,1.0)
rotated=cv2.warpAffine(imagergb,M,(w,h))
roatatedrgb=cv2.cvtColor(rotated,cv2.COLOR_BGR2RGB)
plt.imshow(rotated)
plt.title('Rotated Image')
plt.show()

brightness=np.ones(image.shape,dtype='uint8')*50
brightened=cv2.add(image,brightness)
brightergb=cv2.cvtColor(brightened,cv2.COLOR_BGR2RGB)
plt.imshow(brightergb)
plt.title('Brightened Image')
plt.show()