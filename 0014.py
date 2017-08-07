import xlwt
import json

def load_data(filepath):
    with open(filepath, "r") as fp:
        return json.load(fp)

def write_data_to_xls(data):
    new_workboot = xlwt.Workbook(encoding='utf-8')
    sheet = new_workboot.add_sheet("student")
    for i in range(len(data)):
        sheet.write(i, 0, i+1)
        json_data = data[str(i+1)]
        for j in range(len(json_data)):
            sheet.write(i, j+1, json_data[j])
    new_workboot.save('student.xls')

if __name__ == '__main__':
    data = load_data("student.txt")
    write_data_to_xls(data)