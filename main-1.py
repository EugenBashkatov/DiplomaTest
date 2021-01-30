<<<<<<< HEAD
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pandas as pd
import numpy as np
import  xlsxwriter


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# ['Num','Date','MinTemp','RayFrom','RayTo','dx','dy','K','B','FLiine']
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

df = pd.read_csv('daily-min-temperatures-02.csv',
                 names=['Date', 'MinTemp', 'RayFrom', 'RayTo', 'dx', 'dy', 'K', 'B', 'FLiine'])
data_list = df.to_numpy()


# Cov = pd.read_csv("path/to/file.txt",
#                 sep='\t',
#                names=["Sequence", "Start", "End", "Coverage"])
def line(x0, x1, x):
    y0 = data_list[0][1]
    y1 = data_list[1][1]

    k = (y1 - y0) / (x1 - x0)
    B = (x1 * y0 - x0 * y1) / (x1 - x0)
    print("****** Line from x0 = {0} to x1 = {1}, k = {2}, B = {3}".format(x0, x1, k, B))
    return k * x + B


graph_array = np.eye(9)

x1 = 1
Epsilon = 1.e-3
for x0 in range(0, 8):

    for x1 in range(x0+2, 8):
        graph_array[x0][x1-1] = 1
        graph_array[x1-1][x0] = 1

        for cur_x in range(x1+1, 8):
            par_line = line(x0, x1, cur_x)
            par_y = data_list[cur_x][1]

            print("x0 = ", x0, " x1= ", x1, " cur_x = ", cur_x, " par_line = ", par_line, " par_y = ", par_y, "abs = ")

            if par_line <= par_y:
                print("Видно ", cur_x)
                x1 = cur_x
                graph_array[x0][cur_x] = 1
                # graph_array[x0][cur_x-1] = 1
                graph_array[cur_x][x0] = 1


                # graph_array[cur_x-1][x0] = 1
            # print(cur_x)



print(graph_array)
# print(graph_array[362])
# print(graph_array[325])

eOutput = pd.DataFrame(graph_array)
writer = pd.ExcelWriter('ArrayFromPycharm2.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
eOutput.to_excel(writer, sheet_name='Sheet1', index=False)

# Close the Pandas Excel writer and output the Excel file.
=======
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pandas as pd
import numpy as np
import  xlsxwriter


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# ['Num','Date','MinTemp','RayFrom','RayTo','dx','dy','K','B','FLiine']
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

df = pd.read_csv('daily-min-temperatures-02.csv',
                 names=['Date', 'MinTemp', 'RayFrom', 'RayTo', 'dx', 'dy', 'K', 'B', 'FLiine'])
data_list = df.to_numpy()


# Cov = pd.read_csv("path/to/file.txt",
#                 sep='\t',
#                names=["Sequence", "Start", "End", "Coverage"])
def line(x0, x1, x):
    y0 = data_list[0][1]
    y1 = data_list[1][1]

    k = (y1 - y0) / (x1 - x0)
    B = (x1 * y0 - x0 * y1) / (x1 - x0)
    print("Line from x0 = {0} to x1 = {1}, k = {2}, B = {3}".format(x0, x1, k, B))
    return k * x + B


graph_array = np.eye(9)

x1 = 1
Epsilon = 1.e-3
for x0 in range(0, 8):

    for x1 in range(x0+2, 8):
        graph_array[x0][x1-1] = 1
        graph_array[x1-1][x0] = 1

        for cur_x in range(x1+1,8):
            par_line = line(x0, x1, cur_x)
            par_y = data_list[cur_x][1]
            # crit = abs(par_line - par_y)
            print("x0 = ", x0, " x1= ", x1, " cur_x = ", cur_x, " par_line = ", par_line, " par_y = ", par_y, "abs = ")

            if par_line <= par_y:
                print("Видно ", cur_x)
                x1 = cur_x
                graph_array[x0][cur_x] = 1
                # graph_array[x0][cur_x-1] = 1
                graph_array[cur_x][x0] = 1


                # graph_array[cur_x-1][x0] = 1
            # print(cur_x)



print(graph_array)
# print(graph_array[362])
# print(graph_array[325])

eOutput = pd.DataFrame(graph_array)
writer = pd.ExcelWriter('ArrayFromPycharm2.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
eOutput.to_excel(writer, sheet_name='Sheet1', index=False)

# Close the Pandas Excel writer and output the Excel file.
>>>>>>> origin/master
writer.save()