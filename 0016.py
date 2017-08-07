import xlwt
import json

def load_data(filepath):
    with open(filepath,"r") as fp:
        temp = json.load(fp)
        return temp

def write_data_to_xls(data):
    new_workboot = xlwt.Workbook(encoding='utf-8')
    sheet = new_workboot.add_sheet("student")
    for i in range(len(data)):
        #write(行，列，value)
        for j in range(len(data[i])):
            sheet.write(i, j, data[i][j])
            new_workboot.save('student.xls')
    print("write success")
    
if __name__ == '__main__':
    data = load_data("student.txt")
    write_data_to_xls(data)

