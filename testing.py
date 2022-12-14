import cv2

T = 0.4
training_image_data = [[[0 for k in range(256)] for j in range(256)] for i in range(256)]
# Reading from values from file
file = open("training_value.txt", "r")
for x in range(256):
    for y in range(256):
        for z in range(256):
            training_image_data[x][y][z] = float(file.readline())


test_image = cv2.imread("testingImg.jpg")


height, width, channel = test_image.shape
print("height = ", height , "  width = ", width , "   channel = ", channel)
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

cv2.imwrite("testingSkinImg.jpg", test_image)

print('Testing successfully done and the skin image is saved in "testingSkinImg.jpg" ')
