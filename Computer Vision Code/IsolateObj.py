#!/usr/bin/env python

def  IsolateObj(img,Gimg):
    if sum(sum(Gimg/255))<350:
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

    while LH_Ratio<1.1 or LH_Ratio>1.6 or huMoments[0]<0.00067 or huMoments[0]>0.00083 or area<350:

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
    #  print(area)
      if area<350:
        return Gimg*0,[-1,-1]
    #output = img.copy()
    #cv2.rectangle(output, (x, y), (x + w, y + h), (0, 255, 0), 1)
    #cv2.circle(output, (int(cX), int(cY)), 3, (0, 0, 255), -1)
    #cv2_imshow(output)
    
    centroid=[int(cY),int(cX)]

    return componentMask,centroid