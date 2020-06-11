import numpy as np
from matplotlib import pyplot as plt
import cv2
import matplotlib as mpl


path = r'C:\Users\Rachel\Desktop\RS\PAN.img'
f = open( path , mode = 'rb')
data = np.fromfile(f, dtype=np.uint16)
f.close
img_PAN = data.reshape(3200,4800)

img_PAN = img_PAN/np.max(img_PAN)*255


gray = cv2.equalizeHist(img_PAN.astype(np.uint8))

cv2.imwrite("ImageGray.png",gray)