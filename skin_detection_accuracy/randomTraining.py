import cv2
import random

for j in range(1):
    skinArray = [[[0 for k in range(256)] for j in range(256)] for i in range(256)]
    nonSkinArray = [[[0 for k in range(256)] for j in range(256)] for i in range(256)]
    totalRGBinSkin = 0;
    totalRGBinNonSkin = 0;
    r, g, b = 0, 0, 0

    statingImageNo = random.randint(0, 554)
    for i in range(500):
        print("Training no ", j, "   image on", i)
        nonSkinImageName = "/home/muktadul/Documents/Python Programes/myTest/DBMS-2/skin_detection/ibtd/nonSkin/" + str((i + statingImageNo) % 555).zfill(4) + ".jpg"
        skinImageName = "/home/muktadul/Documents/Python Programes/myTest/DBMS-2/skin_detection/ibtd/skin/" + str((i + statingImageNo) % 555).zfill(4) + ".bmp"

        nonSkinImage = cv2.imread(nonSkinImageName)
        skinImage = cv2.imread(skinImageName)

        height, width, channel = skinImage.shape

        for x in range(height):
            for y in range(width):
                r = skinImage[x][y][0]
                g = skinImage[x][y][1]
                b = skinImage[x][y][2]

                if r <= 250 and g <= 250 and b <= 250:
                    skinArray[r][g][b] += 1
                    totalRGBinSkin += 1
                else:
                    r = nonSkinImage[x][y][0]
                    g = nonSkinImage[x][y][1]
                    b = nonSkinImage[x][y][2]
                    nonSkinArray[r][g][b] += 1
                    totalRGBinNonSkin += 1

    fileName = "training_value" + str(j + 1) + ".txt"
    file = open(fileName, "w")
    file.write(str(statingImageNo) + "\n")
    print(totalRGBinSkin)
    print(totalRGBinNonSkin)
    a = 0.0
    b = 0.0
    for x in range(256):
        for y in range(256):
            for z in range(256):
                a = (skinArray[x][y][z] / totalRGBinSkin)
                b = (nonSkinArray[x][y][z] / totalRGBinNonSkin)

                if b != 0:
                    file.write(str(a / b) + "\n")
                else:
                    file.write("1.0\n")
    file.close()

print("Training successfully done!!!")
print('And training value is record in "training_value(1-10).txt"')
