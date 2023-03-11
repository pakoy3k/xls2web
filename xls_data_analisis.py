'''
Library_xlrd documentation IS DEPRECATED
https://xlrd.readthedocs.io/en/latest/genindex.html
'''
import xlrd

book = xlrd.open_workbook('pagina.xls')
number_sheets = book.nsheets  # Numero de hojas que tiene el libro de excel

'''
method to return column id and return id_index
'''


def find_column(id, page):
    try:
        sheet = book.sheet_by_index(page)  # load 0 page
        # busca el indice de la columna id
        id_index = sheet.row_values(0).index("id")
        # En caso de no estar la palabra id en la fila retorna una lista vacia.
        # Busca que el id esté en los valores de la columna si no está retorna una
        # lista vacía, si está retorna el valor de la columna donde se escuentra.
        if id in sheet.col_values(id_index):
            print("Id encontrada en hoja\t", sheet)
            # print("-----------------------\n")
            return id_index, True
        else:
            print("Id en columna: NO Encontrado", sheet)
            return 0, False
        # elif id_index.type
    except ValueError as e:
        print('Error type: ', type(e))
        print("-----------------------\n")


def next_aproved(row, column, page):
    actual_page = book.sheet_by_index(page)  # load 0 page
    # Primero comprobar que el valor de la siguiente columna sea booleano.
    if actual_page.ncols > 1:
        its_boolean = str(actual_page.cell(row, column+1).value)
        # revisar a atras y adelante
        if its_boolean.lower() == "true":
            return True
        elif its_boolean.lower() == "false":
            # print("Valor booleano:", its_boolean)
            return False
        else:
            print("Busca el valor true o false en otra columna :)\n")
            return "No booleano"
    else:
        print("No existe columnas por revisar")


def load_XLRD(id_search):
    try:
        # recorre la cantidad total de paginas
        for index_page in range(number_sheets):  # recorre cada pagina
            actual_page = book.sheet_by_index(index_page)
            # Busca la columna que contene el id
            index_id, find = find_column(id_search, index_page)
            if find:  # Si se encontró el id prosigue
                row_index = actual_page.col_values(index_id).index(id_search)
                print("Se en encuentra en la fila: ", row_index)
                print("Y en la columna: ", index_id)
                print("-----------------------\n")
                # Si tiene su evaluador booleano prosigue
                if next_aproved(row_index, index_id, index_page) == "No booleano":
                    print("-----------------------\n")
                elif next_aproved(row_index, index_id, index_page):
                    print("DATOS DE: ", actual_page.row_values(row_index), "\n")
                    print("-----------------------\n")
            else:
                print("-----------------------\n")
    except ValueError as e:
        print('Error type: ', type(e))


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
