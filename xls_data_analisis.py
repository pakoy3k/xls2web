'''
Library_xlrd documentation IS DEPRECATED
https://xlrd.readthedocs.io/en/latest/genindex.html
'''
import xlrd

book = xlrd.open_workbook('pagina.xls')
number_sheets = book.nsheets  # Numero de hojas que tiene el libro de excel


def find_column(id, page):
    try:
        sheet = book.sheet_by_index(page)  # load 0 page
        # vector.index("VALOR BUSCADO")
        id_index = sheet.row_values(0).index("id")
        # print("ESTE ES EL ID INDEX: O SEA LA COLUMNA ID", id_index)
        if id_index is None:
            return []
        if id in sheet.col_values(id_index):
            print("Columna Id encontrada en hoja\t", sheet)
            # print("-----------------------\n")
            return id_index
        # elif id_index.type
    except ValueError as e:
        print('Error type: ', type(e))
        print("-----------------------\n")
    finally:
        return 0


def load_XLRD(id_search):
    # try:
    # recorre la cantidad total de paginas
    for index_page in range(number_sheets):
        actual_page = book.sheet_by_index(index_page)  # load 0 page
        # Busca que tenga en la fila 0 la palabra id para encontrar el valor de su columna
        index_id = find_column(id_search, index_page)
        if id_search in actual_page.col_values(index_id):
            print("Id en columna: Encontrado")
            row_index = actual_page.col_values(index_id).index(id_search)
            print("Se en encuentra en la fila: ", row_index)
            print("Y en la columna: ", index_id)
            print("-----------------------\n")
            # if
            print(actual_page.row_values(row_index), "\n")
        else:
            print("Id en columna: NO Encontrado")
            print("-----------------------\n")
    # except TypeError:
    #     print("Error: El valor no está en la pagina")
    # index_page = index_page+1


load_XLRD(3)


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
