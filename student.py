import numpy as np
import pandas as pd
import cv2
import student_infor
import answer_student

arr = []
for x in range(len(student_infor.sheet_lst)):
    arr.append('Data folder/{student_infor.sheet_lst[sheet]}.jpg')

id_student =[]
grading = []
status = []

for x in range(len(arr)):
    image_width = 950
    image_height = 950
    arr_answer = answer_student.my_answer_list

    image = cv2.imread(arr[sheet])
    image = cv2.resize(image, (image_width, image_height))

    roll1 = image[132:816, 150:365]
    roll2 = image[132:816, 532:747]

    roll1 = cv2.cvtColor(roll1, cv2.COLOR_BGR2GRAY)
    roll2 = cv2.cvtColor(roll2, cv2.COLOR_BGR2GRAY)
    roll1_thresh = cv2.threshold(roll1, 150, 255, cv2.THRESH_BINARY_INV)[1]
    roll2_thresh = cv2.threshold(roll2, 150, 255, cv2.THRESH_BINARY_INV)[1]

    cell1 = answer_student.cells(roll1_thresh)
    cell2 = answer_student.cells(roll2_thresh)

    pixel_arr = np.zeros((72,5))

    answer_student.boxes(cell1, 0, 0, pixel_arr)
    answer_student.boxes(cell2, 0, 36, pixel_arr)


    id = student_infor.df.loc[sheet, ['Student_ID']].tolist()
    id = ' '.join(id)
    id_student.append(id)

    answer = {'0': 'A', '1': 'B', '2': 'C', '3': 'D', '4': 'E'}
    student_answer = []
    letter = []
    for y in range(0, 72):
        array = pixel_arr[x]
        list_value = np.where(array == np.amax(array))
        student_answer.append(list_value[0][0])

    for y in student_answer:
        letter.append(answer[f'{x}'])



# Question 7:
df = pd.read_csv("student.csv")
df['Pass/Fail'] = None
df2 = pd.read_csv("grading.csv")

for i in range(0,len(df)):
    if df2.loc[i,'Grading'] > 30 :
        df.loc[i,'Pass/Fail'] = "Pass"
    else:
        df.loc[i,'Pass/Fail'] = 'Fail'
df.to_csv('student.csv')


