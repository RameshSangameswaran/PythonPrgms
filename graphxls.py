import xlrd
import numpy as np
import matplotlib.pyplot as plt
file_location = "/home/user/Desktop/graph.xlsx"
workbook = xlrd.open_workbook(file_location)
first_sheet = workbook.sheet_by_index(0)
x = [first_sheet.cell_value(i, 0) for i in range(first_sheet.nrows)]
y = [first_sheet.cell_value(i, 1) for i in range(first_sheet.nrows)]
plt.xlabel("39;39;")
plt.ylabel("39;Ph39;")
plt.title("39;vol vs ph curve 39;")
plt.ylim(0,15)
plt.xlim(0,30)
plt.plot(x,y)
plt.show()
