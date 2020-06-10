import cv2
import numpy as np
from matplotlib import pyplot as plt

path = r'C:\Users\Rachel\Desktop\ntuPresident.png'
img = cv2.imread(path, cv2.IMREAD_UNCHANGED)

f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
#print(fshift)
magnitude_spectrum = 20*np.log(np.abs(fshift))
plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')#(src*255).astype(np.uint8)
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()