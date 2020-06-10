import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread(r"C:\Users\Rachel\Desktop\hw3_q3_enhancedoutput.png",0)
edges = cv2.Canny(img,100,200)

plt.show()
plt.figure(figsize = (30,20))
plt.imshow(edges,cmap = 'gray') 
plt.show()  # display it