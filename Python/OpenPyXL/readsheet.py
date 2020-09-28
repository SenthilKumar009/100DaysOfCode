import openpyxl

wb = openpyxl.load_workbook('example.xlsx')

#Method to read all the sheet names from the workbook
print(wb.sheetnames)
#['Sheet1', 'Sheet2']

# Get the sheet name by passing the name of the sheet
sheet = wb['Sheet2']
print(sheet)
# <Worksheet "Sheet3">

print(type(sheet))
#<class 'openpyxl.worksheet.worksheet.Worksheet'>

print(sheet.title)
#'Sheet3'

anotherSheet = wb.get_active_sheet()
print(anotherSheet)
#<Worksheet "Sheet1">