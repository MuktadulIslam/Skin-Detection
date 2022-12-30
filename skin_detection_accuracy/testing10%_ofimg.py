import cv2

T = 0.4
detection_accuracy = []
for i in range(10):
    training_image_data = [[[0 for k in range(256)] for j in range(256)] for i in range(256)]
    # Reading from values from file
    file = open("training_value" + str(i+1) + ".txt", "r")
    statingImageNo = (int(file.readline()) + 555 - 55) % 555
    for x in range(256):
        for y in range(256):
            for z in range(256):
                training_image_data[x][y][z] = float(file.readline())

    accuracyNumber = 0
    totalPixel = 0
    for j in range(55):
        # print("Testing no ", i, "   image on", j)

        # Filling the image path
        nonSkinImageName = "/home/muktadul/Documents/Python Programes/myTest/DBMS-2/skin_detection/ibtd/nonSkin/" + str((j + statingImageNo) % 555).zfill(4) + ".jpg"
        skinImageName = "/home/muktadul/Documents/Python Programes/myTest/DBMS-2/skin_detection/ibtd/skin/" + str((j + statingImageNo) % 555).zfill(4) + ".bmp"

        test_image = cv2.imread(nonSkinImageName)
        actualSkinImage = cv2.imread(skinImageName)

        # Finding the skin part from test value
        height, width, channel = test_image.shape
        r, g, b = 0, 0, 0

        for x in range(height):
            for y in range(width):
                r = test_image[x][y][0]
                g = test_image[x][y][1]
                b = test_image[x][y][2]

                if abs(training_image_data[r][g][b]) < T:
                    test_image[x][y][0] = 255
                    test_image[x][y][1] = 255
                    test_image[x][y][2] = 255

        totalPixel += height*width
        for x in range(height):
            for y in range(width):
                if test_image[x][y][0] == actualSkinImage[x][y][0] and test_image[x][y][1] == actualSkinImage[x][y][1] and test_image[x][y][2] == actualSkinImage[x][y][2]:
                    accuracyNumber += 1

    print("Accuracy for " + str(i+1) + " round= ", accuracyNumber / totalPixel)
    detection_accuracy.append(accuracyNumber / totalPixel)

print("Final Accuracy = " + str(sum(detection_accuracy)/10));