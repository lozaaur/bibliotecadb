import sqlite3
conexion = sqlite3.connect("biblioteca.db")
cursor =conexion.cursor()

def login ():
    print("====LOGIN====")
    usuario= input("Usuario: ")
    contraseña= input("Contraseña: ")

    if usuario == "admin" and contraseña == "1234":
     print ("Acceso permitido")
     menu()
    else:
     print("Acceso denegado")

def menu():
  while True:
    print("SISTEMA DE BIBLIOTECA")
    print("1. ver_libros")  
    print("2. libros") 
    print("3. clientes")
    print("4. prestamos_libros")  
    print("5. ver_pretamoslibros")
    print("6. Salir")

    opcion= input ( "seleccione una opción: ")

    if opcion == "1":
       ver_libros()
    elif opcion == "2":
       libros() 
    elif opcion == "3":
       clientes()      
    elif opcion == "4":
       prestamos_libros() 
    elif opcion == "5":
       ver_prestamoslibros() 
    elif opcion == "6":
       print("Saliendo del sistema")
       break
    else:
       print("opción inválida")

def ver_libros():
   cursor.execute("SELECT * FROM libros")
   libros = cursor.fetchall()

   print("===LIBROS==")
   for libro in libros:
      print(libro)
    
def libros():
     id_libros= int(input("Ingrese el ID del libro: "))
     titulo_libro= input("Ingrese el titulo del libro: ")
     autor_libro= input("Ingrese el nombre del autor: ")
     anio_de_publicacion=int(input("Ingrese el año de publicacion: "))
     cantidad_de_libro=int(input("Ingrese la cantidad de libros : "))
     libros_disponible=int(input("Ingrese cuantos libros disponibles: "))

     cursor.execute(  """INSERT INTO libros ("id-libros","titulo-libro", "autor-libro", "anio-de-publicacion", "cantidad-de-libro", "libros-disponible") VALUES (?, ?, ?, ?, ?, ?)""",
     (id_libros, titulo_libro, autor_libro, anio_de_publicacion, cantidad_de_libro , libros_disponible))
     conexion.commit()

def   clientes():
     id_clientes = int(input("Ingrese el ID del cliente: "))
     nombre_cliente= input("ingrese el nombre del cliente :")
     telefono_cliente= int(input("Ingrese el telefono del cliente: "))
     tipo_cliente= input("ingrese el tipo del cliente :")
     correo= input("Ingrese el correo del cliente: ")

     cursor.execute(  """INSERT INTO clientes ("id-clientes", "nombre-cliente", "telefono-cliente", "tipo-cliente", "correo") VALUES (?, ?, ?, ?, ?)""",
     (id_clientes, nombre_cliente, telefono_cliente, tipo_cliente, correo))
     conexion.commit()

def prestamos_libros():
    
    fecha_entrega=input("Ingrese fecha de entrega del libro: ")
    fecha_prestamo=input("Ingrese fecha que se presto el libro: ")
    id_libros= int(input("Ingrese el ID del libro: "))
    id_clientes= int(input("Ingrese el ID del cliente: "))

    cursor.execute(  """INSERT INTO prestamos_libros ( "fecha-entrega", "fecha-prestamo", "id-libros", "id-clientes") VALUES (?, ?, ?, ?)""",
    (fecha_entrega, fecha_prestamo, id_libros, id_clientes))
    

    cursor.execute(""" UPDATE libros SET "libros-disponible" = "libros-disponible" - 1 WHERE "id-libros" = ?""",
          (id_libros,))

    conexion.commit()
    print("Préstamo realizado")

def ver_prestamoslibros():
    cursor.execute("SELECT * FROM prestamos_libros")
    prestamos = cursor.fetchall()

    print("===PRESTAMOS===")
    for prestamo in prestamos:
      print(prestamo)


login()
conexion.close()


