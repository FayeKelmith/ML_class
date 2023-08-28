import cv2 as opcv
import numpy as np
import matplotlib.pyplot as plt
import read

img = read.rescaleFrame(opcv.imread('photos/cat2.jpg'), 0.2)

# histogram for grayscale imgaes
gray = opcv.cvtColor(img, opcv.COLOR_BGR2GRAY)


blank = np.zeros(gray.shape[:2], dtype='uint8')
circle = opcv.circle(
    blank, (gray.shape[1]//2, gray.shape[0]//2), 200, 255, -1)
masked = opcv.bitwise_and(img, img, mask=circle)

# gray_hist = opcv.calcHist([gray], [0], masked, [256], [0, 256])
# plt.figure()
# plt.title('Grayscale Histogram')
# plt.xlabel('Bins')
# plt.ylabel('# pixels')
# plt.plot(gray_hist)
# plt.xlim([0, 256])
# plt.show()

# Colorscale histrogram
colors = ('b', 'g', 'r')

plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# pixels')
for i, col in enumerate(colors):
    hist = opcv.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist, color=col)
    plt.xlim([0, 256])
plt.show()

opcv.waitKey(10)
