import cv2
image=cv2.imread("myedit.jpg")
grayimage=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
resizeimage=cv2.resize(grayimage,(800,500))
cv2.imshow("processed image",resizeimage)
key=cv2.waitKey(0)
if key == ord("s"):
    cv2.imwrite("mygray.jpg",resizeimage)
    print("image saved")
else:
    print("image not saved")

cv2.destroyAllWindows()   