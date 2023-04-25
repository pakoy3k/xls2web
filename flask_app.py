# importanción del modulo de flask la clase flask
import xls_data_analisis as excel

from flask import (Flask, jsonify, render_template, request)
from flask_jwt_extended import (create_access_token , get_jwt_identity, jwt_required, JWTManager)

app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = "secret-malevical" 
jwt = JWTManager(app)

@app.route("/login", methods = ["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if username != "test" or password != "test":
        return jsonify({"msg": "Bad usename or password"}), 401
    acces_token = create_access_token(identity=username)
    return jsonify(acces_token = acces_token)

@app.route("/protected", methods=["GET"])
@jwt_required() # se
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as = current_user), 200

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/about")
def about():
    return "que onda man como estás"


@app.route("/numero_de_hoja/<file>")
def pages(file):
    return jsonify({"Hojas en el libro: ": excel.num_hojas(file)})


@app.route("/filas_columnas/<file>/<int:page>")
def cols_rows(file, page):
    rows, cols = excel.filas_column(file, page)
    return jsonify({"Filas: ": rows, "Columnas": cols})


@app.route("/celda/<file>/<int:page>/<int:row>/<int:col>")
def cell_info(file, page, row, col):
    return jsonify({"Celda: ": excel.cell_info(file, page, row, col)})


@app.route("/columna/<file>/<int:page>/<int:col>")
def col_info(file, page, col):
    return jsonify({"Columna: ": excel.col_info(file, page, col)})


@app.route("/findId/<file>/<int:page>/<int:id>")
def id_find(file, page, id):
    return jsonify({"Fund: ": excel.id_find_xls(file, page, id)})


@app.route("/valuesCols/<file>/<int:page>/<cols>")
def values_cols(file, page, cols):
    # print(cols)
    return jsonify({"Cols: ": excel.show_cols(file, page, cols)})


@app.route("/matrizSheet/<file>/<int:page>")
def matrix(file, page):
    return jsonify({"Matrix: ": excel.matriz_sheet(file, page)})


if __name__ == "__main__":
    app.run()

    # app.run(debug = True, port = 3000, host = "0.0.0.0")   #EJEMPLO PARA
