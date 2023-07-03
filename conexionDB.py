import sqlite3

class ConexionDB:  # programa que interactua con las tablas
    
    def abrir(self):
        conexion=sqlite3.connect("BaseDeDatos.db")
        return conexion

# funciones que interactuan con la tabla libro
    def altaLibro(self, datos): #guarda el libro en la base de datos
        cone=self.abrir()   #abro conexion
        cursor=cone.cursor() #creo objeto cursor que despues voy a utilizar .algo
        sql="insert into libros (Titulo, Autor, Edicion, LugarDeImpresion, Editorial, Traduccion, CantidadDePaginas, Condicion) values (?,?,?,?,?,?,?,?)"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()

    def consultaLibro(self, datos): #consulto el libro en la base de datos a traves del nombre
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="select Codigo, Titulo, Autor, Edicion, LugarDeImpresion, Editorial, Traduccion, CantidadDePaginas, Condicion from libros where Titulo=?"
            cursor.execute(sql, datos)
            return cursor.fetchall()
        finally:
            cone.close()

    def consultaLibroCodigo(self, datos):  #consulto el libro en la base de datos a traves del codigo
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="select Titulo, Autor, Edicion, LugarDeImpresion, Editorial, Traduccion, CantidadDePaginas, Condicion from libros where Codigo=?"
            cursor.execute(sql, datos)
            return cursor.fetchall()
        finally:
            cone.close()

    def recuperar_todos_los_libros(self): #consulto todos los libros que tengo en la base de datos y lo muestra en una ventanita- relacionado con listado completo?
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="select Codigo, Titulo, Autor, Edicion, LugarDeImpresion, Editorial, Traduccion, CantidadDePaginas, Condicion from libros"
            cursor.execute(sql)
            return cursor.fetchall()
        finally:
            cone.close()

    def dar_baja_libros(self, datos): #doy de baja libros( los elimino de la base de datos) usando el codigo
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="delete from libros where Codigo=?"
            cursor.execute(sql, datos)
            cone.commit()
            return cursor.rowcount # retornamos la cantidad de filas borradas
        except:
            cone.close()
    
    def modificacion_datos_libros(self, datos): #modifico segun codigo la informacion de un libro en la tabla libro, porque es la forma de encontrar un unico libro
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="update libros set Titulo=?, Autor=?, Edicion=?, LugarDeImpresion=?, Editorial=?, Traduccion=?, CantidadDePaginas=?, Condicion=? where Codigo=?"
            cursor.execute(sql, datos)
            cone.commit()
            return cursor.rowcount # retornamos la cantidad de filas modificadas            
        except:
            cone.close()

#prestamo
    def altaPrestamo(self, datos):   # guarda en la base de datos el prestamo que se realizo
        cone=self.abrir()
        cursor=cone.cursor()
        sql="insert into prestamos(Nombre, Telefono, Mail, FechaPrestamo, FechaDevolucion, Devuelto, CodigoLibro) values (?,?,?,?,?,?,?)"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()

    def dar_baja_prestamo(self, datos):    #actualizo que un prestamo ha sido devuelto en la tabla de prestamo cambiando el valor de devuelto
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="update prestamos set Devuelto=? where Codigo=?"
            cursor.execute(sql, datos)
            cone.commit()
            return cursor.rowcount # retornamos la cantidad de filas borradas
        except:
            cone.close()

    def reclamar_prestamo(self):  #me devuelve toda la base de datos de prestamo
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="select Codigo, Nombre, Telefono, Mail, FechaPrestamo, FechaDevolucion, Devuelto, CodigoLibro from prestamos"
            cursor.execute(sql)
            return cursor.fetchall()
        finally:
            cone.close()

    def recuperar_todos_prestamo(self):   ###atentiiiii que este programa hace lo mismo que el anterior :reclamar_prestamo(self), pero el que estoy usando es este
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="select Codigo, Nombre, Telefono, Mail, FechaPrestamo, FechaDevolucion, Devuelto, CodigoLibro from prestamos"
            cursor.execute(sql)
            return cursor.fetchall()
        finally:
            cone.close()

    
    def consultaPrestamoCodigo(self, datos): #consulto los prestamos realizados segun el codigo del prestamo
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="select Nombre, Telefono, Mail, FechaPrestamo, FechaDevolucion, Devuelto, CodigoLibro from prestamos where Codigo=?"
            cursor.execute(sql, datos)
            return cursor.fetchall()
        finally:
            cone.close()

    def modificacion_datos_prestamo(self, datos):    #actualizar datos de prestamo en la tabla prestamo segun el codigoo
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="update prestamos set Nombre=?, Telefono=?, Mail=?, FechaPrestamo=?, FechaDevolucion=?, Devuelto=?, CodigoLibro=? where Codigo=?"
            cursor.execute(sql, datos)
            cone.commit()
            return cursor.rowcount # retornamos la cantidad de filas modificadas            
        except:
            cone.close()

