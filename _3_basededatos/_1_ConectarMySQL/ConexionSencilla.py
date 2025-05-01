import mariadb

def conectar_y_consultar():
    try:
        #Establecer conexion a la base de datos
        conexion = mariadb.connect(
            host="localhost",
            database="almacen",
            user="root",
            password="",
            port=3306 #Puerto preterminado de MariaDB
        )
        print(type(conexion))
        print("Conexion a la base de datos del servidor Ounus")

        cursor = conexion.cursor()
        consulta = "select * from usuarios"
        cursor.execute(consulta)

        resultados = cursor.fetchall()
        print("Resultado ", type(resultados))
        print("Datos en la tabla:")
        for fila in resultados:

            print(f"ID: {fila[0]}, Nombre completo: {fila[1]}, Nombre de usuario: {fila[2]}, Correo: {fila[3]}, contraseña: {fila[4]}, Id_Rol: {fila[5]} ")

    except mariadb.Error as e:
        print(f"Error al conectar con la base de datos: {e}")

    finally:

        #Cerrar la conexion y el cursor si estan abiertos
        if 'cursor' in locals() and cursor:
            cursor.close()
            print("Conexion cerrada.")

if __name__ == '__main__':
    conectar_y_consultar()