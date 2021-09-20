import cv2
import numpy as np

path = 'Answer folder/3A.jpg'
image_width = 950
image_height = 950

image = cv2.imread(path)

image = cv2.resize(image, (image_width, image_height))

roll1 = image[132:816, 150:365]
roll2 = image[132:816, 532:747]

def cells(image):
    row1 = np.vsplit(image, 36)
    cells = []
    for a in row1:
        col = np.hsplit(a, 5)
        for cell1 in col:
            cells.append(cell1)
    return cells


def boxes(cells, count_col, count_row, pixel_array):
    for box in cells:
        pixels = cv2.countNonZero(box)
        pixel_array[count_row][count_col] = pixels
        count_col += 1
        if count_col == 5:
            count_row += 1
            count_col = 0

roi1 = cv2.cvtColor(roll1, cv2.COLOR_BGR2GRAY)
roi2 = cv2.cvtColor(roll2, cv2.COLOR_BGR2GRAY)
roi1_thresh = cv2.threshold(roi1, 150, 255, cv2.THRESH_BINARY_INV)[1]
roi2_thresh = cv2.threshold(roi2, 150, 255, cv2.THRESH_BINARY_INV)[1]

cells1 = cells(roi1_thresh)
cells2 = cells(roi2_thresh)

pixel_array1 = np.zeros((72, 5))

boxes(cells1, 0, 0, pixel_array1)
boxes(cells2, 0, 36, pixel_array1)

print(pixel_array1)

my_answer_list = []
for x in range(0, 72):
    array = pixel_array1[x]
    list_value = np.where(array == np.amax(array))
    my_answer_list.append(list_value[0][0])

cv2.waitKey(0)