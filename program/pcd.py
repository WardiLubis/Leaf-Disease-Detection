import numpy as np

def rgb2Gray(img):
    r = img[:,:,0]
    g = img[:,:,1]
    b = img[:,:,2]
    gray = 0.21 * r + 0.71 * g + 0.07 *b
    return np.uint8(gray);

def negative(img):
    L = np.max(img)
    neg = L - img
    return neg

def logTransformations(img, c):
    img = img / 255
    S = c * np.log(1 + img)
    S = np.uint8(S*255)
    return S

def powerLawTransformation(img, c, y):
    img = img/255
    hasil = c * (np.power(img,y))
    return hasil

def contrastStretching(img, x1, y1, x2, y2):

    image = rgb2Gray(img)

    m1 = (y1/x1)
    m2 = (y2-y1)/(x2-x1)
    m3 = (255-y2) / (255-x2)

    c1 = y1 - m2*x1
    c2 = y2 - m3*x2

    [m,n] = np.shape(image)

    for i in range(0, m):
        for j in range(0,n):
            if (np.logical_and(image[i,j] > 0, image[i,j] < x1)):
                image[i, j] = m1 * image[i,j]
            elif (np.logical_and(image[i,j]  > x1, image[i,j]  < x2)):
                image[i, j] = m2 * image[i,j] + c1
            elif (np.logical_and(image[i,j]  > x2, image[i,j]  < 255)):
                image[i, j] = m3 * image[i,j] + c2

    return image

def biner(img, x):
    image = img
    [m, n] = np.shape(image)

    for i in range(0, m):
        for j in range(0, n):
            if image[i, j] <= x:
                image[i, j] = 0
            else:
                image[i, j] = 255
    return image

def grayLevelSlicing(img):
    img = rgb2Gray(img)
    [m, n] = np.shape(img)
    for i in range(0, m):
        for j in range(0, n):
            if img[i,j] >= 128 :
                img[i,j] = 255
            else:
                img[i,j] = 0
    return img

def substraction(img1, img2):
    new = np.subtract(img1, img2)
    return new

def bitwiseAnd(img1, img2):
    new = np.bitwise_and(img1, img2)
    return new

def bitwiseOr(img1, img2):
    new = np.bitwise_or(img1, img2)
    return new

def bitwiseXOR(img1, img2):
    new = np.bitwise_xor(img1, img2)
    return new

def bitPlaneSlicing(img, plane):

    plane = 7 - plane

    [m, n] = np.shape(img)

    new = np.zeros((m,n))

    for i in range(0, m):
        for j in range(0,n):
            a1 = np.unpackbits(img[i,j])
            a1 = np.take(a1, plane)
            if(a1 == 0):
                new[i, j] = 0
            else:
                new[i, j] = 255
    return new;

def dilation (img, num):
    disk = np.shape(se(num))[0]

    [m, n] = np.shape(img)
    new = np.zeros((m,n))

    temp = np.zeros((m+(num*2), n+(num*2)))
    temp[num:-num, num:-num] = img

    [a, b] = np.shape(temp)

    temp[num:-num, 0:num-1] = img[:, 0:num-1]
    temp[0:num-1, num:-num] = img[0:num-1, :]
    temp[num:-num, b-num] = img[:, n-1]
    temp[a-num, num:-num] = img[m-1, :]

    for i in range(0, m):
        for j in range(0, n):
            new[i,j] = hit(temp[i:i+disk, j:j+disk], num)
    return new;


def erotion (img, num):
    disk = np.shape(se(num))[0]

    [m, n] = np.shape(img)
    new = np.zeros((m, n))

    temp = np.zeros((m + (num * 2), n + (num * 2)))
    temp[num:-num, num:-num] = img

    [a, b] = np.shape(temp)

    temp[num:-num, 0:num - 1] = img[:, 0:num - 1]
    temp[0:num - 1, num:-num] = img[0:num - 1, :]
    temp[num:-num, b - num] = img[:, n - 1]
    temp[a - num, num:-num] = img[m - 1, :]

    for i in range(0, m):
        for j in range(0, n):
            new[i, j] = fit(temp[i:i + disk, j:j + disk], num)
    return new;

def hit (img, num):
    kernel = se(num)
    out = 0

    temp = kernel + img
    if (np.max(temp) == 510):
        out = 255
    return out

def fit (img, num):
    kernel = se(num)
    out = 0

    temp = kernel + img
    if (np.min(temp) == 255):
        out = 255
    return out

def se(radius):
    L = np.arange(-radius, radius + 1)
    X, Y = np.meshgrid(L, L)

    [m, n] = np.shape(X)
    new = np.zeros((m, n))

    for i in range (0, m):
        for j in range (0, n):
            if((X[i, j] ** 2 + Y[i, j] ** 2) <= radius ** 2):
                new[i, j] = 255

    return new