from ast import Return
import tkinter as tk
from tkinter import messagebox
import mysql.connector

# CONFIGURACIÓN DE LA BASE DE DATOS
db_config = {
    "user": "root",
    "password": "admin",
    "host": "127.0.0.1", 
    "port": 3306,
    "database": "trabajo",
    # EN CASO DE HABER UN PROBLEMA O ADVERTENCIA LA EJECUCIÓN SE DETIENE
    "raise_on_warnings": True,
}


def create_table():
    conn = mysql.connector.connect(**db_config)
    cur = conn.cursor()
    cur.execute("SHOW TABLES LIKE 'empleados'")
    result = cur.fetchone()
    if not result:
        cur.execute(
            """
        CREATE TABLE empleados (
            id INT AUTO_INCREMENT PRIMARY KEY,
            documento INT,
            nombres VARCHAR(255),
            apellidos VARCHAR(255),
            correo VARCHAR(255),
            telefono VARCHAR(255),
            empresa VARCHAR(255),
            salario FLOAT,
            direccion VARCHAR(255),
            estrato INT
        );
        """
        )
        conn.commit()
    conn.close()


# Función para insertar datos en la tabla 'empleados'
def insert_data(
    documento,
    nombres,
    apellidos,
    correo,
    telefono,
    empresa,
    salario,
    direccion,
    estrato,
):
    conn = mysql.connector.connect(**db_config)
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO empleados (documento, nombres, apellidos, correo, telefono, empresa, salario, direccion, estrato) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
        (
            documento,
            nombres,
            apellidos,
            correo,
            telefono,
            empresa,
            salario,
            direccion,
            estrato,
        ),
    )
    conn.commit()
    conn.close()


# Función para buscar datos en la tabla 'empleados' usando el documento
def search_data(documento):
    conn = mysql.connector.connect(**db_config)
    cur = conn.cursor()
    cur.execute("SELECT * FROM empleados WHERE documento=%s", (documento,))
    rows = cur.fetchall()
    conn.close()
    return rows


# Función para modificar datos en la tabla 'empleados'
def update_data(
    id,
    documento,
    nombres,
    apellidos,
    correo,
    telefono,
    empresa,
    salario,
    direccion,
    estrato,
):
    conn = mysql.connector.connect(**db_config)
    cur = conn.cursor()
    cur.execute(
        "UPDATE empleados SET documento=%s, nombres=%s, apellidos=%s, correo=%s, telefono=%s, empresa=%s, salario=%s, direccion=%s, estrato=%s WHERE id=%s",
        (
            documento,
            nombres,
            apellidos,
            correo,
            telefono,
            empresa,
            salario,
            direccion,
            estrato,
            id,
        ),
    )
    conn.commit()
    conn.close()


# Función para eliminar datos en la tabla 'empleados' usando el id
def delete_data(id):
    conn = mysql.connector.connect(**db_config)
    cur = conn.cursor()
    cur.execute("DELETE FROM empleados WHERE id=%s", (id,))
    conn.commit()
    conn.close()


# Clase principal para la aplicación de empleados
class EmpleadosApp(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    # Función para limpiar las entradas del formulario
    def clear_entries(self):
        self.documento_entry.delete(0, tk.END)
        self.nombres_entry.delete(0, tk.END)
        self.apellidos_entry.delete(0, tk.END)
        self.correo_entry.delete(0, tk.END)
        self.telefono_entry.delete(0, tk.END)
        self.empresa_entry.delete(0, tk.END)
        self.salario_entry.delete(0, tk.END)
        self.direccion_entry.delete(0, tk.END)
        self.estrato_entry.delete(0, tk.END)

    # Crear y colocar los widgets en la ventana
    def create_widgets(self):
        # Widgets para Limpiar
        self.clear_button = tk.Button(self, text="Limpiar", command=self.clear_entries)
        self.clear_button.grid(row=10, column=2, padx=10, pady=10)

        # Widgets para el documento
        self.documento_label = tk.Label(self, text="Documento:")
        self.documento_label.grid(row=0, column=0, padx=10, pady=10)
        self.documento_entry = tk.Entry(self)
        self.documento_entry.grid(row=0, column=1, padx=10, pady=10)
        # Widgets para nombres
        self.nombres_label = tk.Label(self, text="Nombres:")
        self.nombres_label.grid(row=1, column=0, padx=10, pady=10)
        self.nombres_entry = tk.Entry(self)
        self.nombres_entry.grid(row=1, column=1, padx=10, pady=10)
        # Widgets para apellidos
        self.apellidos_label = tk.Label(self, text="Apellidos:")
        self.apellidos_label.grid(row=2, column=0, padx=10, pady=10)
        self.apellidos_entry = tk.Entry(self)
        self.apellidos_entry.grid(row=2, column=1, padx=10, pady=10)
        # Widgets para correo
        self.correo_label = tk.Label(self, text="Correo:")
        self.correo_label.grid(row=3, column=0, padx=10, pady=10)
        self.correo_entry = tk.Entry(self)
        self.correo_entry.grid(row=3, column=1, padx=10, pady=10)
        # Widgets para teléfono
        self.telefono_label = tk.Label(self, text="Teléfono:")
        self.telefono_label.grid(row=4, column=0, padx=10, pady=10)
        self.telefono_entry = tk.Entry(self)
        self.telefono_entry.grid(row=4, column=1, padx=10, pady=10)
        # Widgets para empresa
        self.empresa_label = tk.Label(self, text="Empresa:")
        self.empresa_label.grid(row=5, column=0, padx=10, pady=10)
        self.empresa_entry = tk.Entry(self)
        self.empresa_entry.grid(row=5, column=1, padx=10, pady=10)
        # Widgets para salario
        self.salario_label = tk.Label(self, text="Salario:")
        self.salario_label.grid(row=6, column=0, padx=10, pady=10)
        self.salario_entry = tk.Entry(self)
        self.salario_entry.grid(row=6, column=1, padx=10, pady=10)
        # Widgets para dirección
        self.direccion_label = tk.Label(self, text="Dirección:")
        self.direccion_label.grid(row=7, column=0, padx=10, pady=10)
        self.direccion_entry = tk.Entry(self)
        self.direccion_entry.grid(row=7, column=1, padx=10, pady=10)

        # Widgets para estrato
        self.estrato_label = tk.Label(self, text="Estrato:")
        self.estrato_label.grid(row=8, column=0, padx=10, pady=10)
        self.estrato_entry = tk.Entry(self)
        self.estrato_entry.grid(row=8, column=1, padx=10, pady=10)
        # Botón para agregar el formulario
        self.submit_button = tk.Button(self, text="Agregar", command=self.submit_form)
        self.submit_button.grid(row=9, column=0, padx=10, pady=10)
        # Botón para buscar el formulario
        self.search_button = tk.Button(
            self, text="Buscar", command=self.search_employee
        )
        self.search_button.grid(row=9, column=1, padx=10, pady=10)
        # Botón para modificar el formulario
        self.update_button = tk.Button(
            self, text="Modificar", command=self.update_employee
        )
        self.update_button.grid(row=9, column=2, padx=10, pady=10)
        # Botón para eliminar el formulario
        self.delete_button = tk.Button(
            self, text="Eliminar", command=self.delete_employee
        )
        self.delete_button.grid(row=9, column=3, padx=10, pady=10)

    # Función para enviar el formulario y guardar los datos en la base de datos
    def submit_form(self):
        documento = self.documento_entry.get()
        nombres = self.nombres_entry.get()
        apellidos = self.apellidos_entry.get()
        correo = self.correo_entry.get()
        telefono = self.telefono_entry.get()
        empresa = self.empresa_entry.get()
        salario = self.salario_entry.get()
        direccion = self.direccion_entry.get()
        estrato = self.estrato_entry.get()
        # Validación de datos
        if not (
            documento
            and nombres
            and apellidos
            and correo
            and telefono
            and empresa
            and salario
            and direccion
            and estrato
        ):
            messagebox.showerror("Error", "Todos los campos deben estar llenos.")
            Return

        # Insertar datos en la base de datos
        insert_data(
            documento,
            nombres,
            apellidos,
            correo,
            telefono,
            empresa,
            salario,
            direccion,
            estrato,
        )
        messagebox.showinfo("Éxito", "Datos agregados correctamente.")
        self.clear_entries()

    # Función para buscar los datos en la base de datos
    def search_employee(self):
        documento = self.documento_entry.get()
        result = search_data(documento)
        if result:
            empleado = result[0]
            self.nombres_entry.delete(0, tk.END)
            self.nombres_entry.insert(tk.END, empleado[2])
            self.apellidos_entry.delete(0, tk.END)
            self.apellidos_entry.insert(tk.END, empleado[3])
            self.correo_entry.delete(0, tk.END)
            self.correo_entry.insert(tk.END, empleado[4])
            self.telefono_entry.delete(0, tk.END)
            self.telefono_entry.insert(tk.END, empleado[5])
            self.empresa_entry.delete(0, tk.END)
            self.empresa_entry.insert(tk.END, empleado[6])
            self.salario_entry.delete(0, tk.END)
            self.salario_entry.insert(tk.END, empleado[7])
            self.direccion_entry.delete(0, tk.END)
            self.direccion_entry.insert(tk.END, empleado[8])
            self.estrato_entry.delete(0, tk.END)
            self.estrato_entry.insert(tk.END, empleado[9])
        else:
            messagebox.showerror("Error", "Datos no encontrados.")

    # Función para modificar los datos en la base de datos
    def update_employee(self):
        documento = self.documento_entry.get()
        result = search_data(documento)
        if result:
            empleado = result[0]
            id = empleado[0]
            update_data(
                id,
                self.documento_entry.get(),
                self.nombres_entry.get(),
                self.apellidos_entry.get(),
                self.correo_entry.get(),
                self.telefono_entry.get(),
                self.empresa_entry.get(),
                self.salario_entry.get(),
                self.direccion_entry.get(),
                self.estrato_entry.get(),
            )
            messagebox.showinfo("Éxito", "Datos modificados correctamente.")
        else:
            messagebox.showerror("Error", "Datos no encontrados.")

    # Función para borrar los datos en la base de datos
    def delete_employee(self):
        documento = self.documento_entry.get()
        result = search_data(documento)
        if result:
            empleado = result[0]
            id = empleado[0]
            delete_data(id)
            messagebox.showinfo("Éxito", "Datos eliminados correctamente.")
            self.documento_entry.delete(0, tk.END)
            self.nombres_entry.delete(0, tk.END)
            self.apellidos_entry.delete(0, tk.END)
            self.correo_entry.delete(0, tk.END)
            self.telefono_entry.delete(0, tk.END)
            self.empresa_entry.delete(0, tk.END)
            self.salario_entry.delete(0, tk.END)
            self.direccion_entry.delete(0, tk.END)
            self.estrato_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Datos no encontrados.")


# Crear y ejecutar la ventana principal de la aplicación
create_table()
root = tk.Tk()
root.title("DB")
app = EmpleadosApp(master=root)
app.mainloop()
