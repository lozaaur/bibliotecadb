
# ==================================================
# ======== CÓDIGO ORIGINAL EN CONSOLA (COMENTADO)
# ==================================================

"""
def login():
    print("====LOGIN====")
    usuario = input("Usuario: ")
    contraseña = input("Contraseña: ")

    if usuario == "admin" and contraseña == "1234":
        print("Acceso permitido")
        menu()
    else:
        print("Acceso denegado")
"""

"""
def menu():
    while True:
        print("1. ver_libros")
        print("2. libros")
        print("3. clientes")
        print("4. prestamos_libros")
        print("5. ver_prestamoslibros")
        print("6. salir")
"""

"""
def ver_libros():
    cursor.execute("SELECT * FROM libros")
    for libro in cursor.fetchall():
        print(libro)
"""

"""
def libros():
    id_libros = int(input("ID: "))
    titulo = input("Titulo: ")
"""

"""
def clientes():
    id_clientes = int(input("ID cliente: "))
"""

"""
def prestamos_libros():
    fecha_entrega = input("Fecha entrega: ")
"""

"""
def ver_prestamoslibros():
    cursor.execute("SELECT * FROM prestamos_libros")
"""



import sqlite3
import tkinter as tk
from tkinter import messagebox

# =========================
# CONEXIÓN A LA BASE DE DATOS
# =========================
conexion = sqlite3.connect("biblioteca.db")
cursor = conexion.cursor()


# ==================================================
# =============== TKINTER (INTERFAZ GRÁFICA)
# ==================================================

# -------- LOGIN ----------
def login_gui():
    usuario = entry_usuario.get()
    contraseña = entry_contraseña.get()

    if usuario == "admin" and contraseña == "1234":
        messagebox.showinfo("Login", "Acceso permitido")
        ventana_login.destroy()
        menu_gui()
    else:
        messagebox.showerror("Error", "Acceso denegado")


# -------- MENÚ ----------
def menu_gui():
    ventana_menu = tk.Tk()
    ventana_menu.title("Sistema Biblioteca")
    ventana_menu.geometry("300x350")

    tk.Button(ventana_menu, text="Ver libros", command=ver_libros_gui).pack(pady=5)
    tk.Button(ventana_menu, text="Agregar libro", command=libros_gui).pack(pady=5)
    tk.Button(ventana_menu, text="Clientes", command=clientes_gui).pack(pady=5)
    tk.Button(ventana_menu, text="Préstamos", command=prestamos_gui).pack(pady=5)
    tk.Button(ventana_menu, text="Ver préstamos", command=ver_prestamos_gui).pack(pady=5)
    tk.Button(ventana_menu, text="Salir", command=ventana_menu.destroy).pack(pady=10)

    ventana_menu.mainloop()


# -------- VER LIBROS ----------
def ver_libros_gui():
    v = tk.Toplevel()
    v.title("Libros")

    texto = tk.Text(v, width=60, height=15)
    texto.pack()

    cursor.execute("SELECT * FROM libros")
    for libro in cursor.fetchall():
        texto.insert(tk.END, str(libro) + "\n")


# -------- AGREGAR LIBRO ----------
def libros_gui():
    v = tk.Toplevel()
    v.title("Agregar libro")

    entradas = []
    campos = ["ID", "Título", "Autor", "Año", "Cantidad", "Disponibles"]

    for campo in campos:
        tk.Label(v, text=campo).pack()
        e = tk.Entry(v)
        e.pack()
        entradas.append(e)

    def guardar():
        cursor.execute("""
        INSERT INTO libros ("id-libros","titulo-libro","autor-libro",
        "anio-de-publicacion","cantidad-de-libro","libros-disponible")
        VALUES (?, ?, ?, ?, ?, ?)
        """, tuple(e.get() for e in entradas))
        conexion.commit()
        messagebox.showinfo("OK", "Libro guardado")

    tk.Button(v, text="Guardar", command=guardar).pack(pady=10)


# -------- CLIENTES ----------
def clientes_gui():
    v = tk.Toplevel()
    v.title("Clientes")

    campos = ["ID", "Nombre", "Teléfono", "Tipo", "Correo"]
    entradas = []

    for campo in campos:
        tk.Label(v, text=campo).pack()
        e = tk.Entry(v)
        e.pack()
        entradas.append(e)

    def guardar():
        cursor.execute("""
        INSERT INTO clientes ("id-clientes","nombre-cliente",
        "telefono-cliente","tipo-cliente","correo")
        VALUES (?, ?, ?, ?, ?)
        """, tuple(e.get() for e in entradas))
        conexion.commit()
        messagebox.showinfo("OK", "Cliente guardado")

    tk.Button(v, text="Guardar", command=guardar).pack(pady=10)


# -------- PRÉSTAMOS ----------
def prestamos_gui():
    v = tk.Toplevel()
    v.title("Préstamos")

    campos = ["Fecha préstamo", "Fecha entrega", "ID Libro", "ID Cliente"]
    entradas = []

    for campo in campos:
        tk.Label(v, text=campo).pack()
        e = tk.Entry(v)
        e.pack()
        entradas.append(e)

    def prestar():
        cursor.execute("""
        INSERT INTO prestamos_libros ("fecha-prestamo","fecha-entrega",
        "id-libros","id-clientes")
        VALUES (?, ?, ?, ?)
        """, tuple(e.get() for e in entradas))

        cursor.execute("""
        UPDATE libros SET "libros-disponible" = "libros-disponible" - 1
        WHERE "id-libros" = ?
        """, (entradas[2].get(),))

        conexion.commit()
        messagebox.showinfo("OK", "Préstamo realizado")

    tk.Button(v, text="Prestar", command=prestar).pack(pady=10)


# -------- VER PRÉSTAMOS ----------
def ver_prestamos_gui():
    v = tk.Toplevel()
    v.title("Préstamos")

    texto = tk.Text(v, width=60, height=15)
    texto.pack()

    cursor.execute("SELECT * FROM prestamos_libros")
    for p in cursor.fetchall():
        texto.insert(tk.END, str(p) + "\n")


# =========================
# ===== VENTANA LOGIN =====
# =========================
ventana_login = tk.Tk()
ventana_login.title("Login Biblioteca")
ventana_login.geometry("300x200")

tk.Label(ventana_login, text="Usuario").pack()
entry_usuario = tk.Entry(ventana_login)
entry_usuario.pack()

tk.Label(ventana_login, text="Contraseña").pack()
entry_contraseña = tk.Entry(ventana_login, show="*")
entry_contraseña.pack()

tk.Button(ventana_login, text="Ingresar", command=login_gui).pack(pady=10)

ventana_login.mainloop()

conexion.close()

