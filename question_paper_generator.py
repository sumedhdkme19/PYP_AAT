def read_csv_file(path):
    pass

def write_questions(l1, l2, l3):
    try:
        if(len(l1) !=0 and len(l2) !=0 and len(l3)!=0):
            return "Success!"
    except:
        return "Failed"

if __name__ == '__main__':
    path = ''
    l1, l2, l3 = read_csv_file(path)
    result = write_questions(l1, l2, l3)
    print(result)

    

