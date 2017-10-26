import cv2
import numpy as np
import matplotlib.pyplot as plt

#train images
img = cv2.imread('E:/temp/images/101800_sm.jpg')
gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

sift = cv2.xfeatures2d.SIFT_create()
kp, des = sift.detectAndCompute(gray,None)

print(type(des))
for p in des:
    print(len(p), type(p))
    for t in p:
        print(t)

img=cv2.drawKeypoints(gray,kp,img)
cv2.imwrite('E:/temp/result/sift_keypoints.jpg',img)

#match images
img2 = cv2.imread('E:/temp/images/112003_sm.jpg')
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
kp2, des2 = sift.detectAndCompute(gray2,None)

# create BFMatcher object
bf = cv2.BFMatcher()
# Match descriptors.
matches = bf.knnMatch(des,des2, k=2)

# Apply ratio test
good = []
for m,n in matches:
    if m.distance < 0.75*n.distance:
        good.append([m])

# cv2.drawMatchesKnn expects list of lists as matches.
#img3 = cv2.drawMatchesKnn(img,kp,img2,kp2,img3, good,flags=2)
img3 = cv2.imread('E:/temp/images/112003_sm.jpg')
img3 = cv2.drawMatchesKnn(img,kp,img2,kp2, good, img3,flags=2)

plt.imshow(img3),plt.show()