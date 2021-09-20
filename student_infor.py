import os
import numpy as np
import re
import pandas as pd

path = 'D:\learn-git\Data folder'
data = os.listdir(path)
sheet_lst = []

# Split .jpg
for file in data:
    extension = os.path.splitext(file)
    sheet_lst.append(extension[0])

sheet_data = {'Student_ID': [], 'Surname': [], 'Firstname': [], 'Code': []}
for name in sheet_lst:
    filename = name.split('_')

    sheet_data['Student_ID'].append(filename[0])

    sheet_data['Surname'].append(filename[1])
    sheet_data['Firstname'].append(filename[1])
    sheet_data['Code'].append(filename[2])

df = pd.DataFrame(sheet_data, columns=['Student_ID', 'Surname', 'Firstname', 'Code'])

# df.to_csv('D:\learn-git\student.csv')


