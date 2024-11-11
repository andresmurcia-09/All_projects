from flask import Flask
from flask import render_template, request, redirect
from flask_mysqldb import MySQL
#
app = Flask(__name__)

# Crear conexión a la base de datos
mysql = MySQL()
app.config["MYSQL_DATABASE_HOST"] = "localhost"
app.config["MYSQL_DATABASE_USER"] = "root"
app.config["MYSQL_DATABASE_PASSWORD"] = ""
app.config["MYSQL_DATABASE_DB"] = "flask"

# Iniciar la conexión
mysql.init_app(app)


@app.route("/")
def inicio():
    conexion = mysql.connect()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM datos")
    usuario = cursor.fetchall()
    conexion.commit()
    return render_template("sitio/index.html", usuario=usuario)


@app.route("/sitio/eliminar", methods=["post"])
def eliminar():
    codigo = request.form["codigo"]
    conexion = mysql.connect()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM datos WHERE codigo=%s", (codigo))
    conexion.commit()
    return redirect("/")


@app.route("/sitio/guardar", methods=["post"])
def guardar():
    nombres = request.form["nombres"]
    telefono = request.form["telefono"]
    email = request.form["email"]

    # Insertar información
    sql = "INSERT INTO datos (nombres, telefono, email) VALUES (%s,%s,%s)"
    datos = (nombres, telefono, email)
    conexion = mysql.connect()

    # Declarar un cursor
    cursor = conexion.cursor()
    cursor.execute(sql, datos)
    conexion.commit()
    return redirect("/")

@app.route("/sitio/actualizar", methods=["post"])
def actualizar():
    codigo = request.form['codigo']
    conexion = mysql.connect()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM datos WHERE codigo=%s", (codigo))
    conexion.commit()
    usuario = cursor.fetchall()
    return render_template('/sitio/editar.html', dato=usuario[0])


if __name__ == "__main__":
    app.run(debug=True)
