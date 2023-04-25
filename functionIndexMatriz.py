import xlrd

book = xlrd.open_workbook('pagina.xls')
number_sheets = book.nsheets  # Numero de hojas que tiene el libro de excel


def obtain_row_index(rowi, page):
    sheet = book.sheet_by_index(page)
    indexRow = [num for num in range(sheet.ncols+1)]
    listaRow = sheet.row_values(rowi)
    matriz = []
    matriz.append(indexRow)
    matriz.append(listaRow)
    return matriz


print(obtain_row_index(0, 1))
