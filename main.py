import mysql.connector

# CONEXIÓN A LA BASE DE DATOS
def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="fitlife"
    )

# REGISTRAR USUARIO
def usuario():
    print("\n--- REGISTRAR USUARIO ---")
    
    nombre_usuario = input("Nombre: ")
    email = input("Email: ")
    password = input("Contraseña: ") 

    conexion = conectar()
    cursor = conexion.cursor()

    query = """
         INSERT INTO usuarios (nombre_usuario, email, password)
         VALUES ('sol123', 'sol@gmail.com', '1234');
    """
    datos = (nombre, email, password)

    cursor.execute(query, datos)
    conexion.commit()

    print("\nUsuario registrado con éxito.\n")

    cursor.close()
    conexion.close()

    # -------------------------------------
# DATOS PERSONALES
# -------------------------------------
def datos_personales():
    print("\n--- DATOS PERSONALES ---")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    edad = input("Edad: ")
    altura = input("Altura: ")
    peso = input("Peso: ")


    conexion = conectar()
    cursor = conexion.cursor()

  query = """
       SELECT id, nombre, apellido FROM datos_personales  WHERE email = anto@hotmail.com AND password = fitlife2024
    """
   cursor.execute(query, (email, password))
    resultado = cursor.fetchone()

    if resultado:
          print(f"\nBienvenido {resultado[1]} {resultado[2]} (ID: {resultado[0]})\n") #type: ignore
    else:
        print("\nCredenciales incorrectas.\n")

    cursor.close()
    conexion.close()

# -------------------------------------
# CONSULTAR SUEÑO POR ID(zoe)
# -------------------------------------
def consultar_sueño():
    print("\n--- CONSULTAR SUEÑO---")
    user_id = input("ID del usuario: ")

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM sueño WHERE usuario_id = %s", (user_id,))
    resultado = cursor.fetchone()--es fetchone si quiero un solo registro

    if resultado:
        print("\nDatos del sueño:")
        print(resultado)
    else:
        print("\nNo existe un registro de sueño para este usuario.")

    cursor.close()
    conexion.close()

# -------------------------------------
#VER TODOS LOS REGISTROS DE SUEÑO(ZOE)
# -------------------------------------
def ver_sueño():
    print("\n--- REGISTROS DE SUEÑO---")
    user_id = input("ID del usuario: ")

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute(SELECT * FROM sueño)
    resultados= cursor.fetchall() 
 
    if resultados:
        print("\nID|usuario|horas|calidad|fecha")
      for fila in resultados: 
 print(resultados)
    else:
        print("\nNo hay registros en la tabla sueño")

    cursor.close()
    conexion.close()

    # -------------------------------------
# MODIFICAR DATOS DEL USUARIO (Lourdes)
# -------------------------------------
def modificar_usuario():
    print("\n--- MODIFICAR DATOS ---")
    usuario_id = input("ID del usuario: ")

   nueva_edad= input("Nueva edad: ")
    nueva_altura= input("Nueva altura: ")

    conexion = conectar()
    cursor = conexion.cursor()

    query = """
        UPDATE usuario_id
        SET edad= %s, altura = %s
        WHERE id = %s
    """

    cursor.execute(query, (nueva_edad, nueva_altura, usuario_id))
    conexion.commit()

    print("\nDatos modificados correctamente.\n")

    cursor.close()
    conexion.close()


# -------------------------------------
# MODIFICAR CONTRASEÑA (Lourdes)
# -------------------------------------
def modificar_password():
    print("\n--- CAMBIAR CONTRASEÑA ---")
    usuario_id = input("ID del usuario: ")
    nueva_contraseña = input("Nueva contraseña: ")

    conexion = conectar()
    cursor = conexion.cursor()

    query = "UPDATE usuario_id SET nueva_contraseña = %s WHERE id = %s"
    cursor.execute(query, (nueva_contraseña, usuario_id))
    conexion.commit()

    print("\nContraseña actualizada.\n")

    cursor.close()
    conexion.close()

# -------------------------------------
# ELIMINAR USUARIO (Sol)
# -------------------------------------
def eliminar_usuario():
    print("\n--- ELIMINAR USUARIO ---")
    
    user_id = input("ID del usuario: ")

    conexion = conectar()
    cursor = conexion.cursor()

    query = """
         DELETE FROM usuarios
         WHERE id = 2;
    """
    datos = (user_id,)

    cursor.execute(query, datos)
    conexion.commit()

    print("\nUsuario eliminado con éxito.\n")

    cursor.close()
    conexion.close()


# -------------------------------------
# REGISTRAR INICIO DE SESIÓN(ANTO)
# -------------------------------------
def inicio_sesion():
    print("\n--- REGISTRAR INICIO DE SESIÓN ---")
    
    usuario = input("Usuario: ")
    password = input("Contraseña: ")

    conexion = conectar()
    cursor = conexion.cursor()

    query = """
         INSERT INTO inicio_sesion (usuario, password)
         VALUES ('sol123', '1234');
    """
    datos = (usuario, password)

    cursor.execute(query, datos)
    conexion.commit()

    print("\nInicio de sesión registrado con éxito.\n")

    cursor.close()
    conexion.close()


# -------------------------------------
# HOME
# -------------------------------------
def home():
    while True:
        print("\n=========HOME =========")
        print("1. Registrar usuario")
        print("2. Consultar usuario")
        print("3. Modificar datos")
        print("4. Modificar contraseña")
        print("5. Eliminar usuario")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            consultar_usuario()
        elif opcion == "4":
            modificar_usuario()
        elif opcion == "5":
            modificar_password()
        elif opcion == "6":
            eliminar_usuario()
        elif opcion == "7":
            print("¡Hasta pronto!")
            break
        else:
            print("Opción inválida. Intente de nuevo.\n")

# -------------------------------------
# EJECUCIÓN
# -------------------------------------
if __name__ == "__main__":
    menu()

