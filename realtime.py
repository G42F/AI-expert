import cv2
import numpy as np
def apply_filter(image,ftype):
    '''Applies the specified filter to the input image.'''
    img=image.copy()
    if ftype=="red_tin":
        img[:,:,1]=0
        img[:,:,0]=0
    elif ftype=="green_tin":
        img[:,:,2]=0
        img[:,:,0]=0
    elif ftype=="blue_tin":
        img[:,:,2]=0
        img[:,:,1]=0
    elif ftype=="sobel":
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        sobelx=cv2.Sobel(gray,cv2.CV_64F,1,0,ksize=5)
        sobely=cv2.Sobel(gray,cv2.CV_64F,0,1,ksize=5)
        sobel=cv2.bitwise_or(sobelx.astype('uint8'),sobely.astype('uint8'))
        img=cv2.cvtColor(sobel,cv2.COLOR_GRAY2BGR)
    elif ftype=="canny":
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        can=cv2.Canny(gray,100,200)
        img=cv2.cvtColor(can,cv2.COLOR_GRAY2BGR)
    elif ftype=="cartoon":
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        gray=cv2.medianBlur(gray,5)
        edges=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,9,9)
        color=cv2.bilateralFilter(img,9,250,250)
        img=cv2.bitwise_and(color,color,mask=edges)
    return img
def main():
    print("Hello")
    cap=cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return
    filter_type="original"
    while True:
        ret,frame=cap.read()
        if not ret:
            break
        filtered_frame=apply_filter(frame,filter_type)
        cv2.imshow('Filtered Video',filtered_frame)
        key=cv2.waitKey(1) & 0xFF
        if key==ord('q'):
            break
        elif key==ord('1'):
            filter_type="red_tin"
        elif key==ord('2'):
            filter_type="green_tin"
        elif key==ord('3'):
            filter_type="blue_tin"
        elif key==ord('4'):
            filter_type="sobel"
        elif key==ord('5'):
            filter_type="canny"
        elif key==ord('6'):
            filter_type="cartoon"
    cap.release()
    cv2.destroyAllWindows()
if __name__=="__main__":
    main()