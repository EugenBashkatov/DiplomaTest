# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pandas as pd
import numpy as np


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# ['Num','Date','MinTemp','RayFrom','RayTo','dx','dy','K','B','FLiine']
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

df = pd.read_csv('daily-min-temperatures-01.csv',
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
    return k * x + B


graph_array = np.eye(364)

x1 = 1
for x0 in range(0, 364):
    # x0 = 0
    # print("X0=",x0)

    for cur_x in range(x1+1, 364):
        # print("xur_x=",)
        # par_line = line(x0, x1, cur_x)
        # par_y = data_list[cur_x][1]
        # print(par_line, " ", par_y)
        par_line = line(x0,x1,cur_x)
        par_y = data_list[cur_x][1]
        print("x0 = ",x0," x1= ",x1," c2ur_x = ", cur_x," par_line = ",par_line, " par_y = ",par_y)
        if par_line < par_y:
             print("Видно ", cur_x)
             x1 = cur_x
             graph_array[x0][cur_x] = 1
             graph_array[cur_x][x0] = 1
            # print(cur_x)

print(graph_array)
print(graph_array[362])
print(graph_array[325])
