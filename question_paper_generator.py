import pandas as pd
import os
import random
import numpy as np

from pandas.io.parsers import read_csv

if(os.path.isdir("QP_Repository")):
    pass
else:
    os.mkdir("QP_Repository")

def read_excel_file(path, n, m):
    lst = []
    df = pd.read_excel(path)
    for j in range(m):
        lst.append([a for a in [df.iloc[i,j] for i in range(n)]])
    return lst
    

def write_into(string, i):
    file_name = f'SOM_CIE_{i}.doc'
    target = 'QP_Repository/'+file_name
    with open(target, 'w') as f:
        f.write(f'\n\n Q1. {string}')
    return file_name
    
def assign_question_papers(lst):
    df = pd.read_excel("./Section_List.xlsx")
    df.insert(3,"Question_Paper_Name",np.array(lst))
    df.drop(df.filter(regex="Unname"),axis=1, inplace=True)
    df.to_excel("./QP_Asigned_Section_List.xlsx",index=False)


if __name__ == '__main__' :
    qp_names = []
    assigned_order = []
    nos = int(input("Enter the number of students enrolled for this course: "))
    path = 'ATT_Sample_Question.xlsx'
    lst = read_excel_file(path, 2, 6)
    c = 1
    p1, p2, p3, p4, p5, p6 = lst
    for i in p1:
        for j in p2:
            for k in p3:
                for l in p4:
                    for o in p5:
                        for p in p6:
                            string = ' '.join([i, j, k, l, o, p])
                            name = write_into(string, c)
                            c += 1
                            qp_names.append(name)

    assigned_order = random.choices(qp_names, k = nos)
    assign_question_papers(assigned_order)
    print("SUCCESS!")

    
    
    

