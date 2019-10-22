import xlrd
def loadXLS():
    book = xlrd.open_workbook('pagina.xls')
    print (book.nsheets)
    sheet = book.sheet_by_index(0)
    row = 0
    col = 0
    cell = sheet.cell(row,col)
    print (cell.value)
    num_rows = sheet.nrows
    num_col = sheet.ncols
    print (num_rows)
    print (num_col)
    sheets = book.sheet_names()
    cur_sheet = book.sheet_by_name(sheets[0])
    print (cur_sheet)

def getTitle():
    book = xlrd.open_workbook('pagina.xls')    
    sheet = book.sheet_by_index(0)
    cell = sheet.cell(0,1)
    return cell.value

def getAboutImg():
    book = xlrd.open_workbook('pagina.xls')    
    sheet = book.sheet_by_index(0)
    cell = sheet.cell(1,1)
    return cell.value

def getAboutText():
    book = xlrd.open_workbook('pagina.xls')    
    sheet = book.sheet_by_index(0)
    cell = sheet.cell(2,1)
    return cell.value

loadXLS()
print("Loading data for web")
