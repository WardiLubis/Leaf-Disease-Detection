import matplotlib.pyplot as plt
import pcd

tempA = plt.imread('../image/object1.png')
tempB= plt.imread('../image/object2.png')

print(tempA.shape)
print(tempB.shape)

tempA = pcd.rgb2Gray(tempA)
tempB = pcd.rgb2Gray(tempB)

newTemp = pcd.substraction(tempA, tempB)
newTemp1 = pcd.bitwiseAnd(tempA, tempB)
newTemp2 = pcd.bitwiseOr(tempA, tempB)
newTemp3 = pcd.bitwiseXOR(tempA, tempB)

f = plt.figure()
f.add_subplot(3,2, 1)
plt.title("Gray 1")
plt.imshow(tempA, cmap = plt.get_cmap('gray'))
f.add_subplot(3,2, 2)
plt.title("Gray 2")
plt.imshow(tempB, cmap = plt.get_cmap('gray'))
f.add_subplot(3,2, 3)
plt.title("Substraction")
plt.imshow(newTemp, cmap = plt.get_cmap('gray'))
f.add_subplot(3,2, 4)
plt.title("Bitwise AND")
plt.imshow(newTemp1, cmap = plt.get_cmap('gray'))
f.add_subplot(3,2, 5)
plt.title("Bitwise OR")
plt.imshow(newTemp2, cmap = plt.get_cmap('gray'))
f.add_subplot(3,2, 6)
plt.title("Bitwise XOR")
plt.imshow(newTemp3, cmap = plt.get_cmap('gray'))
# plt.show()