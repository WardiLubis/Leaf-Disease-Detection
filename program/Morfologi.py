import matplotlib.pyplot as plt
import pcd
import numpy as np
import PIL

#img = plt.imread('../image/daun3.png')
img = PIL.Image.open('../image/daun3.jpg')

arr = np.array(img)
imgGray = pcd.rgb2Gray(arr)

# newImg = pcd.logTransformations(newImg, 1.3)
imgBiner = pcd.biner(imgGray, 80)

# temp = pcd.dilation(newImg, 3)
# temp = pcd.dilation(temp, 1)
# temp = pcd.dilation(temp, 1)
temp = pcd.erotion(imgBiner, 1)
temp = pcd.dilation(temp, 1)
temp = pcd.erotion(temp, 1)
temp = pcd.erotion(temp, 1)

f = plt.figure()
f.add_subplot(2,2, 1)
plt.title("Original")
plt.imshow(img, cmap = plt.get_cmap('gray'))
f.add_subplot(2,2, 2)
plt.title("Gray")
plt.imshow(imgGray, cmap = plt.get_cmap('gray'))
f.add_subplot(2,2, 3)
plt.title("biner")
plt.imshow(imgBiner, cmap = plt.get_cmap('gray'))
f.add_subplot(2,2, 4)
plt.title("Hasil")
plt.imshow(temp, cmap = plt.get_cmap('gray'))
plt.show();