import matplotlib.pyplot as plt
import program.pcd as pcd


img = plt.imread('../image/lena.png')

imgGray = pcd.rgb2Gray(img)

f = plt.figure()

for i in range(1, 9):
    f.add_subplot(3, 3, i)
    plt.title(i-1)
    plt.imshow(pcd.bitPlaneSlicing(imgGray, i-1), cmap=plt.get_cmap('gray'))

f.add_subplot(3, 3, 9)
plt.imshow(imgGray, cmap=plt.get_cmap('gray'))
plt.show()