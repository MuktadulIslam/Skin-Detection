import cv2

T = 0.4
detection_accuracy = []
roundNumber = 10

for i in range(roundNumber):
    training_image_data = [[[0 for k in range(256)] for j in range(256)] for i in range(256)]
    # Reading from values from file
    file = open("training_value" + str(i + 1) + ".txt", "r")
    statingImageNo = (int(file.readline()) + 555 - 55) % 555
    for x in range(256):
        for y in range(256):
            for z in range(256):
                training_image_data[x][y][z] = float(file.readline())

    false_positive = 0
    false_negative = 0
    true_positive = 0
    true_negative = 0

    for j in range(55):
        # print("Testing no ", i, "   image on", j)

        # Filling the image path
        nonSkinImageName = "/home/muktadul/Documents/Python Programes/myTest/DBMS-2/skin_detection/ibtd/nonSkin/" + str(
            (j + statingImageNo) % 555).zfill(4) + ".jpg"
        skinImageName = "/home/muktadul/Documents/Python Programes/myTest/DBMS-2/skin_detection/ibtd/skin/" + str(
            (j + statingImageNo) % 555).zfill(4) + ".bmp"

        test_image = cv2.imread(nonSkinImageName)
        actualSkinImage = cv2.imread(skinImageName)

        # Finding the skin part from test value
        height, width, channel = test_image.shape
        r1, g1, b1, r2, g2, b2 = 0, 0, 0, 0, 0, 0

        for x in range(height):
            for y in range(width):
                r1 = test_image[x][y][0]
                g1 = test_image[x][y][1]
                b1 = test_image[x][y][2]

                r2 = actualSkinImage[x][y][0]
                g2 = actualSkinImage[x][y][1]
                b2 = actualSkinImage[x][y][2]

                if abs(training_image_data[r1][g1][b1]) < T:
                    if r2 <= 250 and g2 <= 250 and b2 <= 250:
                        false_negative += 1
                    else:
                        true_negative += 1

                else:
                    if r2 > 250 and g2 > 250 and b2 > 250:
                        false_positive += 1
                    else:
                        true_positive += 1

    accuracy = (true_positive + true_negative) / (false_positive + false_negative + true_negative + true_positive) * 100
    print("Accuracy for " + str(i + 1) + " round= ",accuracy, "%")
    detection_accuracy.append(accuracy)

print("Final Accuracy = " + str(sum(detection_accuracy) / roundNumber));
