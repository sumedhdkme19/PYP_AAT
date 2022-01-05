import pandas as pd
import os
import random
import shutil

from pandas.io.parsers import read_csv

if(os.path.isdir("QP_Repository")):
    pass
else:
    os.mkdir("QP_Repository")

def read_excel_file(path, sheetname, n, m):
    lst = []
    df = pd.read_excel(path, sheet_name = sheetname)
    for j in range(m):
        lst.append([a for a in [df.iloc[i,j] for i in range(n)]])
    return lst
    

def write_into(string, i):
    file_name = f'SOM_CIE_{i}'
    file_path = ''

    with open(file_name, 'a') as f:
        f.write('\n\n')
        f.write('Q1. '+string)
    


if __name__ == '__main__' :
        path = 'ATT_Sample_Question.xlsx'
        lst = read_excel_file(path, "Sheet2", 4, 5)
        c = 1
        p1, p2, p3, p4, p5, p6 = lst
        for i in p1:
            for j in p2:
                for k in p3:
                    for l in p4:
                        for o in p5:
                            for p in p6:
                                string = ' '.join([i, j, k, l, o, p])
                                write_into(string, c)
                                c += 1

        print("SUCCESS!")

    
    
    

