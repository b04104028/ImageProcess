import cv2
import numpy as np
from matplotlib import pyplot as plt

path = r'C:\Users\Rachel\Desktop\RS\MS.img'
f = open( path , mode = 'rb')
data = np.fromfile(f, dtype=np.uint16)
f.close
img_MS = data.reshape(4, 800, 1200)
ms_band1 = img_MS[0,:,:];
ms_band2 = img_MS[1,:,:];
ms_band3 = img_MS[2,:,:];
ms_band4 = img_MS[3,:,:];
#以上ok


img = cv2.merge((ms_band1/np.max(ms_band1),ms_band2/np.max(ms_band2),ms_band3/np.max(ms_band3)))
#print(img)
cv2.imshow("image", img)