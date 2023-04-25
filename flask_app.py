""" importación del modulo de flask y de xls_data_analisis como excel """

import xls_data_analisis as excel

from flask_jwt_extended import (
    create_access_token, get_jwt_identity, jwt_required, JWTManager)
from flask import (Flask, jsonify, render_template, request)

app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = "secret-malevical"
jwt = JWTManager(app)


@app.route("/login", methods=["POST"])
def login():
    """
    Función que permite iniciar sesión en la aplicación.

    Parameters:
        None

    Returns:
        jsonify(acces_token = acces_token): Retorna un objeto json con el token de acceso generado.
    """
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if username != "test" or password != "test":
        return jsonify({"msg": "Bad usename or password"}), 401
    acces_token = create_access_token(identity=username)
    return jsonify(acces_token=acces_token)


@app.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    """
    Función que protege la ruta "/protected" mediante la autenticación con token JWT.

    Parameters:
        None

    Returns:
        jsonify(logged_in_as = current_user): Retorna un objeto json con el usuario autenticado.
    """
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200


@app.route("/")
def home():
    """
    Función que renderiza la plantilla "index.html" en la ruta raíz.

    Parameters:
        None

    Returns:
        render_template('index.html'): Retorna la plantilla "index.html" renderizada.
    """
    return render_template('index.html')


@app.route("/about")
def about():
    """
    Función que retorna un mensaje en la ruta "/about".

    Parameters:
        None

    Returns:
        "que onda man como estás": Retorna un mensaje en forma de cadena de texto.
    """
    return "que onda man como estás"


@app.route("/numero_de_hoja/<file>")
def pages(file):
    """
    Función que retorna el número de hojas que contiene un 
    libro de excel en la ruta "/numero_de_hoja/<file>".

    Parameters:
        file (str): Nombre del archivo de excel.

    Returns:
        jsonify({"Hojas en el libro: ": excel.num_hojas(file)}): Retorna un objeto json con el 
        número de hojas que contiene el libro de excel.
    """
    return jsonify({"Hojas en el libro: ": excel.num_hojas(file)})


@app.route("/filas_columnas/<file>/<int:page>")
def cols_rows(file, page):
    """
    Función que retorna el número de filas y columnas que tiene una hoja 
    de un libro de excel en la ruta "/filas_columnas/<file>/<int:page>".

    Parameters:
        file (str): Nombre del archivo de excel.
        page (int): Número de página (hoja) del libro de excel.

    Returns:
        jsonify({"Filas: ": rows, "Columnas": cols}): Retorna un objeto json con el 
        número de filas y columnas que tiene la hoja del libro de excel.
    """
    rows, cols = excel.filas_column(file, page)
    return jsonify({"Filas: ": rows, "Columnas": cols})


@app.route("/celda/<file>/<int:page>/<int:row>/<int:col>")
def cell_info(file, page, row, col):
    """
    Retorna la información de la celda en una hoja de Excel específica.

    :param file: Nombre del archivo de Excel.
    :type file: str.
    :param page: Número de página en el libro de Excel.
    :type page: int.
    :param row: Número de fila de la celda.
    :type row: int.
    :param col: Número de columna de la celda.
    :type col: int.
    :return: Información de la celda.
    :rtype: dict.
    """
    return jsonify({"Celda: ": excel.cell_info(file, page, row, col)})


@app.route("/columna/<file>/<int:page>/<int:col>")
def col_info(file, page, col):
    """
    Retorna la información de una columna en una hoja de Excel específica.

    :param file: Nombre del archivo de Excel.
    :type file: str.
    :param page: Número de página en el libro de Excel.
    :type page: int.
    :param col: Número de columna.
    :type col: int.
    :return: Información de la columna.
    :rtype: dict.
    """
    return jsonify({"Columna: ": excel.col_info(file, page, col)})


@app.route("/findId/<file>/<int:page>/<int:id>")
def id_find(file, page, id_find):
    """
    Encuentra una fila en una hoja de Excel específica con un ID específico.

    :param file: Nombre del archivo de Excel.
    :type file: str.
    :param page: Número de página en el libro de Excel.
    :type page: int.
    :param id_find: Valor del ID a buscar.
    :type id_find: int.
    :return: Información de la fila con el ID.
    :rtype: dict.
    """
    return jsonify({"Fund: ": excel.id_find_xls(file, page, id_find)})


@app.route("/valuesCols/<file>/<int:page>/<cols>")
def values_cols(file, page, cols):
    """
    Retorna los valores de las columnas específicas de una hoja de Excel.

    :param file: Nombre del archivo de Excel.
    :type file: str.
    :param page: Número de página en el libro de Excel.
    :type page: int.
    :param cols: Números de las columnas separados por comas.
    :type cols: str.
    :return: Valores de las columnas específicas.
    :rtype: dict.
    """
    return jsonify({"Cols: ": excel.show_cols(file, page, cols)})


@app.route("/matrizSheet/<file>/<int:page>")
def matrix(file, page):
    """
    Retorna una matriz de una hoja de Excel específica.

    :param file: Nombre del archivo de Excel.
    :type file: str.
    :param page: Número de página en el libro de Excel.
    :type page: int.
    :return: Matriz de la hoja de Excel.
    :rtype: dict.
    """
    return jsonify({"Matrix: ": excel.matriz_sheet(file, page)})


if __name__ == "__main__":
    app.run()

    # app.run(debug = True, port = 3000, host = "0.0.0.0")   #EJEMPLO PARA
