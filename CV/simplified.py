#!/usr/bin/env python3

def simplified(image):


  g = ((image[:,:,1]>image[:,:,2])*image[:,:,1]).astype("int")
  g = ((g-40>image[:,:,0])).astype("uint8")*255


  r = ((image[:,:,2]>image[:,:,0])*image[:,:,2]).astype("int")
  r = ((r-60>image[:,:,1])).astype("uint8")*255

  
  b=  ((image[:,:,0]>image[:,:,1])*image[:,:,0]).astype("int")
  b = ((b-60>image[:,:,2])).astype("uint8")*255
 
 
  rgb=r+g+b


  return rgb
