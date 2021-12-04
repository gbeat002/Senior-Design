#!/usr/bin/env python
import numpy as np
import cv2
import IsolateObj
import ReduceSizeAndPad
import simplified

def main():
  img1 = cv2.imread("/content/drive/MyDrive/Sift Pictures/nn images/t2.jpg")
  img2 = cv2.imread("/content/drive/MyDrive/Sift Pictures/20211104_165918.jpg")
  img3 = cv2.imread("/content/drive/MyDrive/Sift Pictures/20211104_170018.jpg")
  img4 = cv2.imread("/content/drive/MyDrive/Sift Pictures/20211104_175717.jpg")
  img5 = cv2.imread("/content/drive/MyDrive/Sift Pictures/20211104_175709.jpg")
  img6 = cv2.imread("/content/drive/MyDrive/Sift Pictures/20211104_175630.jpg")
  img7 = cv2.imread("/content/drive/MyDrive/Sift Pictures/20211104_190950.jpg")
  img8 = cv2.imread("/content/drive/MyDrive/Sift Pictures/nn images/20211031_203257.jpg")
  img9 = cv2.imread("/content/drive/MyDrive/Sift Pictures/20211105_194051.jpg")
  img10 = cv2.imread("/content/drive/MyDrive/Sift Pictures/nn images/hard_test.jpg")
  arrayOfArrays = np.array([img1, img2, img3, img4, img5, img6, img7, img8, img9, img10])


  for x in range(len(arrayOfArrays)):
    img=arrayOfArrays[x]
    img=ReduceSizeAndPad(img,10) #5 10
    #cv2_imshow(img)
    Gimg=simplified(img)
   # ContourMethod(img,Gimg)
    Gimg,centroid=IsolateObj(img,Gimg)
    #moments = cv2.moments(Gimg)
   # huMoments = cv2.HuMoments(moments)
    #cv2_imshow(Gimg)
    #print(sum(sum(Gimg/255)))
    print(centroid)
    #print(moments)


if __name__ == "__main__":
  main()