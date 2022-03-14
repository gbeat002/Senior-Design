#!/usr/bin/env python3
import cv2
import numpy as np
def  IsolateObj(img,Gimg):
    if sum(sum(Gimg/255))<800:
      return Gimg*0,[-1,-1]
    output = cv2.connectedComponentsWithStats(Gimg)
    (numLabels, labels, stats, centroids) = output
    
    centroids=centroids[1:numLabels]
    stats=stats[1:numLabels]

    ind=np.argmax(stats[:,4])
    x = stats[ind,0]
    y = stats[ind,1]
    w = stats[ind,2]
    h = stats[ind,3]
    LH_Ratio=h/w
    area = stats[ind,4]
    (cX, cY) = centroids[ind]
    componentMask = (labels == ind+1).astype("uint8") * 255
    huMoments = cv2.HuMoments(cv2.moments(componentMask))

    while (LH_Ratio<1.1 or LH_Ratio>1.6 or area<800) and (area<40000):
    #while LH_Ratio<1.1 or LH_Ratio>1.6 or huMoments[0]<0.00067 or huMoments[0]>0.00083 or area<800:

      stats[ind]=[0,0,0,0,0]
      ind=np.argmax(stats[:,4])

      componentMask = (labels == ind+1).astype("uint8") * 255

      huMoments = cv2.HuMoments(cv2.moments(componentMask))

      x = stats[ind,0]
      y = stats[ind,1]
      w = stats[ind,2]
      h = stats[ind,3]
      LH_Ratio=h/w
      area = stats[ind,4]
      (cX, cY) = centroids[ind]
      if area<800:
        return Gimg*0,[-1,-1]
#extra stuff
    output = img.copy()
    cv2.rectangle(output, (x, y), (x + w, y + h), (0, 255, 0), 1)
    cv2.circle(output, (int(cX), int(cY)), 3, (0, 0, 255), -1)
#extra stuff    
    centroid=[int(cY),int(cX)]
    print(area)
    return output,centroid
