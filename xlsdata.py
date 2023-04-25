import xlrd

book = xlrd.open_workbook('pagina.xls')
sheet = book.sheet_by_index(0)
number_sheets = book.nsheets  # Numero de hojas que tiene el libro de excel


def loadXLS():
    # print (book.nsheets)
    row = 0
    col = 0
    sheets = book.nsheets

    for hoja in range(sheets):

        sheet = book.sheet_by_index(hoja)
        num_rows = sheet.nrows
        num_col = sheet.ncols
        for row in range(num_rows):
            for col in range(num_col):
                cell = sheet.cell(row, col)
                # cell2 = sheet.cell(i,col+1)
                print(str(cell.value)+"\t", end="")
    print(num_rows)
    print(num_col)
    sheets = book.sheet_names()
    cur_sheet = book.sheet_by_name(sheets[0])
    print(cur_sheet)


def findd_page(id, page):
    sheet = book.sheet_by_index(page)
    num_rows = sheet.nrows
    num_col = sheet.ncols
    for col in range(num_col):
        cell = sheet.cell(0, col)
        if cell.value == "id":
            print("")
            for row in range(num_rows):
                cell = sheet.cell(row, col)
                rows_cell = sheet.row_values(row)
                # print(rows_cell)
                if id == rows_cell[0] and rows_cell[1] == 1:
                    print(rows_cell[0], "-", rows_cell[2], "-", rows_cell[3])


def x_function():
    # Nombre de archivo que se desea abrir
    print(number_sheets)
    sheet = book.sheet_by_index(0)  # Primera hoja
    id_temp = "3.0"  # id que se busca
    index_info_id = 0  # indice de la columna donde se encuentra los id's
    num_row = sheet.nrows  # Cuantas filas tiene la hoja 2
    # num_col = sheet.ncols #Cuantas columnas cuenta la primera hoja
    for row in range(num_row):
        # Va recorriendo de fila en fila por la columna <index_info_id>
        cell = sheet.cell(row, index_info_id)
        next_cell = sheet.cell(row, index_info_id+1)
        print("->"+id_temp + "\t" + str(cell.value),
              next_cell.value == "true")  # Debug jajaja
        # Si <id_temp> es igual al valor de la celda y la siguiente celda es igual a true
        if id_temp == str(cell.value) and next_cell.value == "true":
            print(sheet.row_values(row))


def getTitle():
    book = xlrd.open_workbook('pagina.xls')
    sheet = book.sheet_by_index(0)
    cell = sheet.cell(0, 1)
    return cell.value


def getAboutImg():
    book = xlrd.open_workbook('pagina.xls')
    sheet = book.sheet_by_index(0)
    cell = sheet.cell(1, 1)
    return cell.value


def getAboutText():
    book = xlrd.open_workbook('pagina.xls')
    sheet = book.sheet_by_index(0)
    cell = sheet.cell(2, 1)
    return cell.value


loadXLS()
print("Loading data for web")
