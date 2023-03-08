'''
Library_xlrd documentation IS DEPRECATED
https://xlrd.readthedocs.io/en/latest/genindex.html
'''
import xlrd

book = xlrd.open_workbook('pagina.xls')


def loadXLS():
    # Nombre de archivo que se desea abrir
    # number_sheets = book.nsheets  # Numero de hojas que tiene el libro de excel
    sheet = book.sheet_by_index(1)  # Primera hoja
    sheet_2 = book.sheet_by_index(2)  # Primera hoja
    id_temp = "3.0"  # id que se busca
    index_info_id = 0  # indice de la columna donde se encuentra los id's
    num_row = sheet_2.nrows  # Cuantas filas tiene la hoja 2
    # num_col = sheet.ncols #Cuantas columnas cuenta la primera hoja
    for row in range(num_row):
        # Va recorriendo de fila en fila por la columna <index_info_id>
        cell = sheet_2.cell(row, index_info_id)
        next_cell = sheet_2.cell(row, index_info_id+1)
        print("->"+id_temp + "\t" + str(cell.value),
              next_cell.value == "true")  # Debug jajaja
        # Si <id_temp> es igual al valor de la celda y la siguiente celda es igual a true
        if id_temp == str(cell.value) and next_cell.value == "true":
            print(sheet_2.row_values(row))


def find_id_col(id, page):
    sheet = book.sheet_by_index(page)
    num_rows = sheet.nrows
    num_col = sheet.ncols
    cell = sheet.cell(0, 1)
    for col in range(num_col):
        cell = sheet.cell(0, col)
        if cell.value == "id":
            print("")
        for row in range(num_rows):
            cell = sheet.cell(row, col)
            if id == cell.value:
                # cell2 = sheet.cell(i,col+1)
                print(str(cell.value)+"\t", end="")
                gps = sheet.cell(row, 1)
                print(gps.value)


loadXLS()
find_id_col(3, 2)
