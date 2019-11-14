import openpyxl

workbook = openpyxl.load_workbook("C:\\Users\\zhao xiao hui\\Desktop\\成绩.xlsx")
worksheet = workbook.worksheets[0]

no = {}
name = {}
nom = {}
i = 0
np = {}
for row in worksheet.rows:
    no[row[0].value[-4:]] = i
    np[row[0].value[-4:]] = row[1].value
    nom[row[0].value] = i
    name[row[1].value] = i
    i += 1

while (1):
    xh4 = input('输入学号后四位：')
    if xh4 not in np:
        print('重新输入学号后四位')
        continue
    cj = int(input('输入成绩：'))
    syno = int(input('输入实验编号：'))
    print('确认信息,姓名', np[xh4], '成绩', cj, '实验', syno)

    choice = int(input('0 确认  1 修改'))

    if choice == 1:
        continue

    worksheet.cell(no[xh4] + 1, syno - 2, cj)
    choice = int(input('0 继续  1 保存并退出'))

    if choice == 1:
        break

workbook.save(filename='C:\\Users\\zhao xiao hui\\Desktop\\成绩.xlsx')
