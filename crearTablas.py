import sqlite3

def crea_tabla():    #programa que crea las tablas
    #Establecemos una conexión con la base de datos.
    conexion = sqlite3.connect('BaseDeDatos.db') #conecta con la base de datos 
    
    #Creamos una tabla.
    try:                    
        conexion.execute("""create table prestamos (  
                                  Codigo integer primary key AUTOINCREMENT,
                                  Nombre text,
                                  Telefono text, 
                                  Mail text,
                                  FechaPrestamo  datetime,
                                  FechaDevolucion  datetime,
                                  Devuelto bool,
                                  CodigoLibro text
                            )""")
        print("se creo la tabla prestamos")
    except sqlite3.OperationalError:      #salvo que ocurra determinado error
        print("La tabla prestamos ya existe")
    
    try:
        conexion.execute("""create table libros (
            Codigo integer primary key AUTOINCREMENT,
            Titulo text,
            Autor text, 
            Edicion int,
            LugarDeImpresion text, 
            Editorial text,
            Traduccion bool,
            CantidadDePaginas int,
            Condicion bool
            )""")
        print("se creo la tabla libros")                        
    except sqlite3.OperationalError: 
        print("La tabla libros ya existe")
    
    #Cerramos la conexión con la base de datos.
    conexion.close()
