#!/usr/bin/env python

def ReduceSizeAndPad(image,percent):
  image = cv2.resize(image, (0, 0), fx=percent/100, fy=percent/100,interpolation=cv2.INTER_CUBIC)
  image=np.pad(image, [(1, 1), (1, 1),(0,0)], mode='constant', constant_values=0) #pad array
  return image