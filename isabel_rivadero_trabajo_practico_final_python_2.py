#Trabajo Practico Final Python2
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import scrolledtext as st   # es para que abra la ventanita de texto
import conexionDB as cdb
from datetime import datetime
import crearTablas

class biblioteca:
    def __init__(self):
        crearTablas.crea_tabla()  #llamo a crearTablas y uso la funcion cre_tabla que esta ahi dentro
        self.conexion = cdb.ConexionDB()   #para usar interactuar con la base de datos 
        self.ventana1=tk.Tk()
        self.ventana1.title("Gestor de Bibliotecas")  # titulo principal de la ventana
        self.cuaderno1 = ttk.Notebook(self.ventana1)   
        #funcionalidades de libro     
        self.dar_de_alta()
        self.modificar_datos_de_libro()
        self.dar_de_baja_libro()
        self.consultar_libro_por_nombre()
        self.mostrar_todos_los_libros_cargados()
        #funcionalidades de prestamo
        self.registrar_un_prestamo()
        self.prestamo_devuelto()   #da por terminado el prestaamo 
        self.reclamar_prestamo()  #se da cuando el usuario controla los prestamos vigentes y el programa detecta que hay prestamos que no se devolvieron
        #genera la ventana
        self.cuaderno1.grid(column=0, row=0, padx=10, pady=10)
        self.ventana1.mainloop()

#Libro    
    '''Método que se encarga de la configuración de los componentes gráficos del primer Frame (pagina): carga de articulos'''
    def dar_de_alta(self):      #corresponde a la pestaña: carga de libros
        self.pagina1 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1, text="Carga de libros")    #Frame: pagina 1
        self.labelframe1=ttk.LabelFrame(self.pagina1, text="Cargar")   #labelFrame: recuadro     
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)

        self.label1=ttk.Label(self.labelframe1, text="Titulo: ")  # label :labelframe(espacios)
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.titulocarga=tk.StringVar()
        self.entrytitulo=ttk.Entry(self.labelframe1, textvariable=self.titulocarga)
        self.entrytitulo.grid(column=1, row=0, padx=4, pady=4)

        self.label2=ttk.Label(self.labelframe1, text="Autor: ")        
        self.label2.grid(column=0, row=2, padx=4, pady=4)
        self.autorcarga=tk.StringVar()
        self.entryautor=ttk.Entry(self.labelframe1, textvariable=self.autorcarga)
        self.entryautor.grid(column=1, row=2, padx=4, pady=4)

        self.label3=ttk.Label(self.labelframe1, text="Edicion: ")        
        self.label3.grid(column=0, row=3, padx=4, pady=4)
        self.edicioncarga=tk.StringVar()
        self.entryedicion=ttk.Entry(self.labelframe1, textvariable=self.edicioncarga)
        self.entryedicion.grid(column=1, row=3, padx=4, pady=4)

        self.label4=ttk.Label(self.labelframe1, text="Lugar de Impresion:")        
        self.label4.grid(column=0, row=4, padx=4, pady=4)
        self.lugardeimpresioncarga=tk.StringVar()
        self.entrylugardeimpresion=ttk.Entry(self.labelframe1, textvariable=self.lugardeimpresioncarga)
        self.entrylugardeimpresion.grid(column=1, row=4, padx=4, pady=4)

        self.label2=ttk.Label(self.labelframe1, text="Editorial:")        
        self.label2.grid(column=0, row=5, padx=4, pady=4)
        self.editorialcarga=tk.StringVar()
        self.entryeditorial=ttk.Entry(self.labelframe1, textvariable=self.editorialcarga)
        self.entryeditorial.grid(column=1, row=5, padx=4, pady=4)

        self.label2=ttk.Label(self.labelframe1, text="Traducido: ")     #radiobutton para marcar las opciones     
        self.label2.grid(column=0, row=6, padx=4, pady=4)
        self.traducidocarga=tk.StringVar()
        self.traducidocarga.set(2)
        self.radio_1=tk.Radiobutton(self.labelframe1, text = 'Verdadero', variable = self.traducidocarga, value='Verdadero')
        self.radio_1.grid(column=1, row=6)
        self.radio_2=tk.Radiobutton(self.labelframe1, text ='Falso', variable = self.traducidocarga, value='Falso')
        self.radio_2.grid(column=1, row=7)
        

        self.label2=ttk.Label(self.labelframe1, text="Cantidad de Paginas:")        
        self.label2.grid(column=0, row=8, padx=4, pady=5)
        self.cantidaddepaginascarga=tk.StringVar()
        self.entrycantidaddepaginas=ttk.Entry(self.labelframe1, textvariable=self.cantidaddepaginascarga)
        self.entrycantidaddepaginas.grid(column=1, row=8, padx=4, pady=4)

        self.label2=ttk.Label(self.labelframe1, text="Condicion:")        
        self.label2.grid(column=0, row=9, padx=4, pady=4)
        self.condicioncarga = tk.StringVar()
        self.condicioncarga.set(4)
        self.radio_1=tk.Radiobutton(self.labelframe1, text = 'Prestamo en proceso', variable = self.condicioncarga, value='Prestamo en proceso')
        self.radio_1.grid(column=1, row=9)
        self.radio_2=tk.Radiobutton(self.labelframe1, text = 'Disponible ', variable = self.condicioncarga, value='Disponible ')
        self.radio_2.grid(column=1, row=10)
        self.radio_3=tk.Radiobutton(self.labelframe1, text = 'Retrazo [No devuelto]', variable = self.condicioncarga, value='Retrazo [No devuelto]')
        self.radio_3.grid(column=1, row=11)
        self.radio_4=tk.Radiobutton(self.labelframe1, text ='En restauracion', variable = self.condicioncarga, value='En restauracion')
        self.radio_4.grid(column=1, row=12)
        
        self.boton1=ttk.Button(self.labelframe1, text="Confirmar", command=self.agregar)
        self.boton1.grid(column=1, row=13, padx=4, pady=4)


    def modificar_datos_de_libro(self):   #Corresponde a la pestaña modificar datos
        self.pagina2 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina2, text="Modificar datos")

        self.labelframe1=ttk.LabelFrame(self.pagina2, text="Modificar")
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)

        self.label1=ttk.Label(self.labelframe1, text="Código:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.codigomodificar=tk.StringVar()
        self.entrycodigo=ttk.Entry(self.labelframe1, textvariable=self.codigomodificar)
        self.entrycodigo.grid(column=1, row=0, padx=4, pady=4)

        self.label2=ttk.Label(self.labelframe1, text="Titulo:")        
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.titulomodificar=tk.StringVar()
        self.entrytitulo=ttk.Entry(self.labelframe1, textvariable=self.titulomodificar)
        self.entrytitulo.grid(column=1, row=1, padx=4, pady=4)

        self.label3=ttk.Label(self.labelframe1, text="Autor:")        
        self.label3.grid(column=0, row=2, padx=4, pady=4)
        self.autormodificar=tk.StringVar()
        self.entryautor=ttk.Entry(self.labelframe1, textvariable=self.autormodificar)
        self.entryautor.grid(column=1, row=2, padx=4, pady=4)

        self.label4=ttk.Label(self.labelframe1, text="Edicion:")        
        self.label4.grid(column=0, row=3, padx=4, pady=4)
        self.edicionmodificar=tk.StringVar()
        self.entryedicion=ttk.Entry(self.labelframe1, textvariable=self.edicionmodificar)
        self.entryedicion.grid(column=1, row=3, padx=4, pady=4)

        self.label5=ttk.Label(self.labelframe1, text="Lugar de Impresion:")        
        self.label5.grid(column=0, row=4, padx=4, pady=4)
        self.lugardeimpresionmodificar=tk.StringVar()
        self.entrylugardeimpresion=ttk.Entry(self.labelframe1, textvariable=self.lugardeimpresionmodificar)
        self.entrylugardeimpresion.grid(column=1, row=4, padx=4, pady=4)

        self.label6=ttk.Label(self.labelframe1, text="Editorial:")        
        self.label6.grid(column=0, row=5, padx=4, pady=4)
        self.editorialmodificar=tk.StringVar()
        self.entryeditorial=ttk.Entry(self.labelframe1, textvariable=self.editorialmodificar)
        self.entryeditorial.grid(column=1, row=5, padx=4, pady=4)

        self.label7=ttk.Label(self.labelframe1, text="Traducido: ")        
        self.label7.grid(column=0, row=6, padx=4, pady=4)
        self.traducidomodificar=tk.StringVar()
        self.traducidomodificar.set(2)
        self.radio_1=tk.Radiobutton(self.labelframe1, text = 'Verdadero', variable = self.traducidomodificar, value='Verdadero')
        self.radio_1.grid(column=1, row=6)
        self.radio_2=tk.Radiobutton(self.labelframe1, text ='Falso', variable = self.traducidomodificar, value='Falso')
        self.radio_2.grid(column=1, row=7)

        self.label8=ttk.Label(self.labelframe1, text="Cantidad de Paginas:")        
        self.label8.grid(column=0, row=8, padx=4, pady=5)
        self.cantidaddepaginasmodificar=tk.StringVar()
        self.entrycantidaddepaginas=ttk.Entry(self.labelframe1, textvariable=self.cantidaddepaginasmodificar)
        self.entrycantidaddepaginas.grid(column=1, row=8, padx=4, pady=4)

        self.label9=ttk.Label(self.labelframe1, text="Condicion:")        
        self.label9.grid(column=0, row=9, padx=4, pady=4)
        self.condicionmodificar=tk.StringVar()
        self.condicionmodificar.set(4)
        self.radio_1=tk.Radiobutton(self.labelframe1, text = 'Prestamo en proceso', variable = self.condicionmodificar, value='Prestamo en proceso')
        self.radio_1.grid(column=1, row=9)
        self.radio_2=tk.Radiobutton(self.labelframe1, text = 'Disponible ', variable = self.condicionmodificar, value='Disponible ')
        self.radio_2.grid(column=1, row=10)
        self.radio_3=tk.Radiobutton(self.labelframe1, text = 'Retrazo [No devuelto]', variable = self.condicionmodificar, value='Retrazo [No devuelto]')
        self.radio_3.grid(column=1, row=11)
        self.radio_4=tk.Radiobutton(self.labelframe1, text ='En restauracion', variable = self.condicionmodificar, value='En restauracion')
        self.radio_4.grid(column=1, row=12)


        self.boton5=ttk.Button(self.labelframe1, text="Consultar", command=self.consultar_mod)
        self.boton5.grid(column=1, row=13, padx=4, pady=4)
        self.boton6=ttk.Button(self.labelframe1, text="Modificar", command=self.modifica)
        self.boton6.grid(column=1, row=14, padx=4, pady=4)
    
    '''
       Método que se encarga de la configuración de los componentes gráficos del tercer Frame: borrar libros
    '''
    def dar_de_baja_libro(self):       #corresponde a la pestaña-pagina Borrar libros
        self.pagina3 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina3, text="Borrar libros")
        self.labelframe1=ttk.LabelFrame(self.pagina3, text="Libro")        
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)
        self.label1=ttk.Label(self.labelframe1, text="Código:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.codigoborra=tk.StringVar()
        self.entryborra=ttk.Entry(self.labelframe1, textvariable=self.codigoborra)
        self.entryborra.grid(column=1, row=0, padx=4, pady=4)
        self.boton1=ttk.Button(self.labelframe1, text="Borrar", command=self.borrar)
        self.boton1.grid(column=1, row=1, padx=4, pady=4)

    '''
       Método que se encarga de la configuración de los componentes gráficos del cuarto Frame: consulta por nombre 
    '''
    def consultar_libro_por_nombre(self):   #corresponde a la pestaña Consulta por nombre correspondiente a la seccion libros 
        self.pagina4 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina4, text="Consulta por nombre ")
        self.labelframe1=ttk.LabelFrame(self.pagina4, text="Libro ")
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)

        self.label1=ttk.Label(self.labelframe1, text="Titulo: ")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.titulo=tk.StringVar()
        self.entrytitulo=ttk.Entry(self.labelframe1, textvariable=self.titulo)
        self.entrytitulo.grid(column=1, row=0, padx=4, pady=4)

        self.boton1=ttk.Button(self.labelframe1, text="Consultar", command=self.consultar)
        self.boton1.grid(column=1, row=3, padx=4, pady=4)
        self.scrolledtext1=st.ScrolledText(self.labelframe1, width=30, height=10)
        self.scrolledtext1.grid(column=1,row=2, padx=10, pady=10)

    '''
       Método que se encarga de la configuración de los componentes gráficos del quinto Frame: listado de todos los libros
    '''
    def mostrar_todos_los_libros_cargados(self):    #corresponde a la pestaña listado completo
        self.pagina5 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina5, text="Listado completo")
        self.labelframe1=ttk.LabelFrame(self.pagina5, text="Libros ")
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)
        self.boton1=ttk.Button(self.labelframe1, text="Listado completo", command=self.listar)
        self.boton1.grid(column=0, row=0, padx=4, pady=4)
        self.scrolledtext2=st.ScrolledText(self.labelframe1, width=30, height=10)  #deja un cuadrado de espacio para completar
        self.scrolledtext2.grid(column=0,row=1, padx=10, pady=10)


#Prestamo
    '''
       Método que se encarga de la configuración de los componentes gráficos del primer Frame: carga de libros
    '''
    def registrar_un_prestamo(self):   #corresponde a la pestaña prestamo
        self.pagina6 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina6, text="Prestamo")
        self.labelframe1=ttk.LabelFrame(self.pagina6, text="Registrar")        
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)

        self.label1=ttk.Label(self.labelframe1, text="Nombre Completo: ")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.nombrecompletocarga=tk.StringVar()
        self.entrynombrecompleto=ttk.Entry(self.labelframe1, textvariable=self.nombrecompletocarga)
        self.entrynombrecompleto.grid(column=1, row=0, padx=4, pady=4)

        self.label2=ttk.Label(self.labelframe1, text="Telefono: ")        
        self.label2.grid(column=0, row=2, padx=4, pady=4)
        self.telefonocarga=tk.StringVar()
        self.entrytelefono=ttk.Entry(self.labelframe1, textvariable=self.telefonocarga)
        self.entrytelefono.grid(column=1, row=2, padx=4, pady=4)

        self.label3=ttk.Label(self.labelframe1, text="Mail: ")        
        self.label3.grid(column=0, row=3, padx=4, pady=4)
        self.mailcarga=tk.StringVar()
        self.entrymail=ttk.Entry(self.labelframe1, textvariable=self.mailcarga)
        self.entrymail.grid(column=1, row=3, padx=4, pady=4)

        self.label4=ttk.Label(self.labelframe1, text="Fecha de Prestamo:")        
        self.label4.grid(column=0, row=4, padx=4, pady=4)
        self.fechadeprestamocarga=tk.StringVar()
        self.entryfechadeprestamo=ttk.Entry(self.labelframe1, textvariable=self.fechadeprestamocarga)
        self.entryfechadeprestamo.grid(column=1, row=4, padx=4, pady=4)

        self.label5=ttk.Label(self.labelframe1, text="Fecha de Devolucion:")        
        self.label5.grid(column=0, row=5, padx=4, pady=4)
        self.fechadedevolucioncarga=tk.StringVar()
        self.entryfechadedevolucion=ttk.Entry(self.labelframe1, textvariable=self.fechadedevolucioncarga)
        self.entryfechadedevolucion.grid(column=1, row=5, padx=4, pady=4)

        self.label6=ttk.Label(self.labelframe1, text="Devuelto:")        
        self.label6.grid(column=0, row=6, padx=4, pady=4)
        self.devueltocarga=tk.StringVar()
        self.devueltocarga.set(2)
        self.radio_1=tk.Radiobutton(self.labelframe1, text = 'Verdadero', variable = self.devueltocarga, value='Verdadero')
        self.radio_1.grid(column=1, row=6)
        self.radio_2=tk.Radiobutton(self.labelframe1, text = 'Falso', variable = self.devueltocarga, value='Falso')
        self.radio_2.grid(column=1, row=7)

        self.label7=ttk.Label(self.labelframe1, text="Libro a prestar [codigo]: ")        
        self.label7.grid(column=0, row=8, padx=4, pady=4)
        self.libroaprestarcarga=tk.StringVar()
        self.entrylibroaprestar=ttk.Entry(self.labelframe1, textvariable=self.libroaprestarcarga)
        self.entrylibroaprestar.grid(column=1, row=8, padx=4, pady=4)

        self.boton1=ttk.Button(self.labelframe1, text="Confirmar", command=self.agregarPrestamo)
        self.boton1.grid(column=1, row=9, padx=4, pady=4)

    '''
       Método que se encarga de la configuración de los componentes gráficos del segundo Frame: borrar un artículo
    '''
    def prestamo_devuelto(self):  #corresponde a la pestaña prestamodevuelto,para dar por terminado el prestamo 
        self.pagina7 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina7, text="Prestamo devuelto ")
        self.labelframe1=ttk.LabelFrame(self.pagina7, text="Modificar estado de prestamo")        
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)
        self.label1=ttk.Label(self.labelframe1, text="Código de Prestamo:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.codigocambiaprestamo=tk.StringVar()
        self.entrycambia=ttk.Entry(self.labelframe1, textvariable=self.codigocambiaprestamo)
        self.entrycambia.grid(column=1, row=0, padx=4, pady=4)
        
        self.label2=ttk.Label(self.labelframe1, text="Nombre Completo:")        
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.nombremodificar=tk.StringVar()
        self.entrynombremodificar=ttk.Entry(self.labelframe1, textvariable=self.nombremodificar)
        self.entrynombremodificar.grid(column=1, row=1, padx=4, pady=4)

        self.label3=ttk.Label(self.labelframe1, text="Telefono: ")        
        self.label3.grid(column=0, row=2, padx=4, pady=4)
        self.telefonomodificar=tk.StringVar()
        self.entrytelefonomodificar=ttk.Entry(self.labelframe1, textvariable=self.telefonomodificar)
        self.entrytelefonomodificar.grid(column=1, row=2, padx=4, pady=4)

        self.label4=ttk.Label(self.labelframe1, text="Mail: ")        
        self.label4.grid(column=0, row=3, padx=4, pady=4)
        self.mailmodificar=tk.StringVar()
        self.entrymailmodificar=ttk.Entry(self.labelframe1, textvariable=self.mailmodificar)
        self.entrymailmodificar.grid(column=1, row=3, padx=4, pady=4)

        self.label5=ttk.Label(self.labelframe1, text="Fecha de Prestamo:")        
        self.label5.grid(column=0, row=4, padx=4, pady=4)
        self.fechadeprestamomodificar=tk.StringVar()
        self.entryfechadeprestamomodificar=ttk.Entry(self.labelframe1, textvariable=self.fechadeprestamomodificar)
        self.entryfechadeprestamomodificar.grid(column=1, row=4, padx=4, pady=4)

        self.label6=ttk.Label(self.labelframe1, text="Fecha de Devolucion:")        
        self.label6.grid(column=0, row=5, padx=4, pady=4)
        self.fechadedevolucionmodificar=tk.StringVar()
        self.entryfechadedevolucionmodificar=ttk.Entry(self.labelframe1, textvariable=self.fechadedevolucionmodificar)
        self.entryfechadedevolucionmodificar.grid(column=1, row=5, padx=4, pady=4)

        self.label7=ttk.Label(self.labelframe1, text="Devuelto:")        
        self.label7.grid(column=0, row=6, padx=4, pady=4)
        self.devueltomodificar=tk.StringVar()
        self.devueltomodificar.set(2)
        self.radio_1=tk.Radiobutton(self.labelframe1, text = 'Verdadero', variable = self.devueltomodificar, value='Verdadero')
        self.radio_1.grid(column=1, row=6)
        self.radio_2=tk.Radiobutton(self.labelframe1, text = 'Falso', variable = self.devueltomodificar, value='Falso')
        self.radio_2.grid(column=1, row=7)

        self.label8=ttk.Label(self.labelframe1, text="Libro a prestar [codigo]: ")        
        self.label8.grid(column=0, row=8, padx=4, pady=4)
        self.libroaprestarmodificar=tk.StringVar()
        self.entrylibromodificar=ttk.Entry(self.labelframe1, textvariable=self.libroaprestarmodificar)
        self.entrylibromodificar.grid(column=1, row=8, padx=4, pady=4)

        self.boton1=ttk.Button(self.labelframe1, text="consultar", command=self.consultarPrestamo)
        self.boton1.grid(column=1, row=9, padx=4, pady=4)
        self.boton2=ttk.Button(self.labelframe1, text="Actualizar", command=self.cambiaPrestamo)
        self.boton2.grid(column=1, row=10, padx=4, pady=4)
    

    def reclamar_prestamo(self):    #se corresponde con la pagina(pestaña) Reclamar prestamo, pongo una fecha y dice todos los libros que debieron haberse devuelto eantes de esa fecha y no se devolvieron
        self.pagina8 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina8, text="Reclamar prestamo")
        self.labelframe1=ttk.LabelFrame(self.pagina8, text="prestamo pendiente ")
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)
        self.label1=ttk.Label(self.labelframe1, text="Fecha:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.fechaborrar=tk.StringVar()
        self.entryfecha=ttk.Entry(self.labelframe1, textvariable=self.fechaborrar)
        self.entryfecha.grid(column=1, row=0, padx=4, pady=4)
        self.boton1=ttk.Button(self.labelframe1, text="Aceptar", command=self.aceptar)
        self.boton1.grid(column=1, row=1, padx=4, pady=4)
        self.scrolledtext3=st.ScrolledText(self.labelframe1, width=30, height=10)  #deja un cuadrado de espacio para completar
        self.scrolledtext3.grid(column=1,row=2, padx=10, pady=10)



    #funcionalidades llamadas por botones
    #de libro
    '''Permite agregar un artículo a la base de datos. '''
    def agregar(self):   #lo que hace es que yo pueda cargar informacion
        datos=(self.titulocarga.get(), self.autorcarga.get(), self.edicioncarga.get(), self.lugardeimpresioncarga.get(), self.editorialcarga.get(), self.traducidocarga.get(), self.cantidaddepaginascarga.get(), self.condicioncarga.get())
        self.conexion.altaLibro(datos)
        mb.showinfo("Información", "Los datos fueron cargados")
        self.titulocarga.set("")
        self.autorcarga.set("")
        self.edicioncarga.set("")
        self.lugardeimpresioncarga.set("")
        self.editorialcarga.set("")
        self.traducidocarga.set("")
        self.cantidaddepaginascarga.set("")
        self.condicioncarga.set("")

    '''Permite borrar un artículo de la base de datos utilizando el código de dicho elemento.'''
    def borrar(self):  #borra informacion de la base de datos
        datos = (self.codigoborra.get(), )
        cantidad = self.conexion.dar_baja_libros(datos)
        if cantidad == 1:
            mb.showinfo("Información", "Se borró el artículo con dicho código")
        else:
            mb.showinfo("Información", "No existe un artículo con dicho código")


    '''Permite consultar los valores de un artículo buscándolo por su código.'''
    def consultar_mod(self):         #consulto valores en la base de datos por su codigo
        datos = (self.codigomodificar.get(), )
        respuesta = self.conexion.consultaLibroCodigo(datos)
        if len(respuesta) > 0:
            self.titulomodificar.set(respuesta[0][0])
            self.autormodificar.set(respuesta[0][1])
            self.edicionmodificar.set(respuesta[0][2])
            self.lugardeimpresionmodificar.set(respuesta[0][3])
            self.editorialmodificar.set(respuesta[0][4])
            self.traducidomodificar.set(respuesta[0][5])
            self.cantidaddepaginasmodificar.set(respuesta[0][6])
            self.condicionmodificar.set(respuesta[0][7])
        else:
            self.titulomodificar.set('')
            self.autormodificar.set('')
            self.edicionmodificar.set('')
            self.lugardeimpresionmodificar.set('')
            self.editorialmodificar.set('')
            self.traducidomodificar.set('')
            self.cantidaddepaginasmodificar.set('')
            self.condicionmodificar.set('')
            mb.showinfo("Información", "No existe un libro con dicho código")

    
    '''Permite modificar los valores de un artículo. '''
    def modifica(self):         #modifico valores de la base de datos segun el codigo
        datos = (self.titulomodificar.get(), self.autormodificar.get(), self.edicionmodificar.get(), self.lugardeimpresionmodificar.get(), self.editorialmodificar.get(), self.traducidomodificar.get(), self.cantidaddepaginasmodificar.get(), self.condicionmodificar.get(), self.codigomodificar.get())
        cantidad = self.conexion.modificacion_datos_libros(datos)
        if cantidad == 1:
            mb.showinfo("Información", "Se modificó el artículo")
        else:
            mb.showinfo("Información", "No existe un artículo con dicho código")
    
    
    def consultar(self):   #consulta tambien segun el titulo
        datos = (self.titulo.get(), )
        respuesta = self.conexion.consultaLibro(datos)
        self.scrolledtext1.delete("1.0", tk.END)        
        for fila in respuesta:
            self.scrolledtext1.insert(tk.END, "código:"+str(fila[0])+
                                              "\ntitulo:"+str(fila[1])+
                                              "\nautor:"+str(fila[2])+
                                              "\nedicion:"+str(fila[3])+
                                              "\nlugarde impresion:"+str(fila[4])+
                                              "\neditorial:"+str(fila[5])+
                                              "\ntraduccion:"+str(fila[6])+
                                              "\ncantidad de paginas:"+str(fila[7])+
                                              "\ncondicion:"+str(fila[8])+
                                              "\n\n")

    '''Muestra todos los artículos cargados. '''
    def listar(self):                 #lista todos los libros que hay en la base de datos
        respuesta=self.conexion.recuperar_todos_los_libros()
        self.scrolledtext2.delete("1.0", tk.END)        
        for fila in respuesta:
            self.scrolledtext2.insert(tk.END, "código:"+str(fila[0])+
                                              "\ntitulo:"+str(fila[1])+
                                              "\nautor:"+str(fila[2])+
                                              "\nedicion:"+str(fila[3])+
                                              "\nlugarde impresion:"+str(fila[4])+
                                              "\neditorial:"+str(fila[5])+
                                              "\ntraduccion:"+str(fila[6])+
                                              "\ncantidad de paginas:"+str(fila[7])+
                                              "\ncondicion:"+str(fila[8])+
                                              "\n\n")

    

    #prestamo
    def agregarPrestamo(self):      #agrega un prestamo con todos los datos corresponidientes a la tabla prestamo
        datos=(self.nombrecompletocarga.get(), self.telefonocarga.get(), self.mailcarga.get(), self.fechadeprestamocarga.get(), self.fechadedevolucioncarga.get(), self.devueltocarga.get(), self.libroaprestarcarga.get())
        #verificar si el libro esta disponible
        cod = (self.libroaprestarcarga.get(), )
        verif = self.conexion.consultaLibroCodigo(cod)
        if verif[0][7]=='Disponible ':    #si esta disponible lo puedo prestar
            self.conexion.altaPrestamo(datos)
            mb.showinfo("Información", "Los datos fueron cargados")
        else:                                     #en caso contrario: "el libro no esta disponible"
            mb.showinfo("Información", "el libro no esta disponible")   
        self.nombrecompletocarga.set("")
        self.telefonocarga.set("")
        self.mailcarga.set("")
        self.fechadeprestamocarga.set("")
        self.fechadedevolucioncarga.set("")
        self.devueltocarga.set("")
        self.libroaprestarcarga.set("")

    def borrarPrestamo(self):    #viene de prestamo devuelto, actualizar. borra la informacion de un prestamo de la tabla prestamo
        datos = (self.codigoborra.get(), )
        cantidad = self.conexion.baja(datos)
        if cantidad == 1:
            mb.showinfo("Información", "Se borró el artículo con dicho código")
        else:
            mb.showinfo("Información", "No existe un artículo con dicho código")

    def aceptar(self):          
        datos=(self.fechaborrar.get(),)
        respuesta=self.conexion.recuperar_todos_prestamo()
        self.scrolledtext3.delete("1.0", tk.END)        
        fechaActual=datetime.strptime(datos[0], '%d-%m-%Y') #strptime: de string a time
        for fila in respuesta:
            fechaDevolucion=datetime.strptime(fila[5], '%d-%m-%Y')
            if (fechaDevolucion < fechaActual)&(fila[6]=='Falso'):    #fila[6] es la fila 6 en recuperar_todos_prestamo(conexionDB)= Devuelto, si es false es que no fue devuelto
                self.scrolledtext3.insert(tk.END, "Codigo:"+str(fila[0])+     #scrolled text me va a mostrar todo en el cuadrito de texto, toda la informacion 
                                                "\nNombre:"+str(fila[1])+      #de un libro que no fue devuelto en el cuadrito de texto
                                                "\nTelefono:"+str(fila[2])+
                                                "\nMail:"+str(fila[3])+
                                                "\nFecha de Prestamo:"+str(fila[4])+
                                                "\nFecha de Devolucion:"+str(fila[5])+
                                                "\nDevuelto:"+str(fila[6])+
                                                "\nCodigo Libro:"+str(fila[7])+
                                                "\n\n")

    def consultarPrestamo(self):        #consultas en la pestaña: prestamo devuelto, segun el codigo 
        datos = (self.codigocambiaprestamo.get(), )
        respuesta = self.conexion.consultaPrestamoCodigo(datos)
        if len(respuesta) > 0:
            self.nombremodificar.set(respuesta[0][0])
            self.telefonomodificar.set(respuesta[0][1])
            self.mailmodificar.set(respuesta[0][2])
            self.fechadeprestamomodificar.set(respuesta[0][3])
            self.fechadedevolucionmodificar.set(respuesta[0][4])
            self.devueltomodificar.set(respuesta[0][5])
            self.libroaprestarmodificar.set(respuesta[0][6])
        
        else:
            self.nombremodificar.set('')
            self.telefonomodificar.set('')
            self.mailmodificar.set('')
            self.fechadeprestamomodificar.set('')
            self.fechadedevolucionmodificar.set('')
            self.devueltomodificar.set('')
            self.libroaprestarmodificar.set('')
            mb.showinfo("Información", "No existe un prestamo con dicho código")     

    def cambiaPrestamo(self):   #en la pestaña prestamo devuelto, tengo la posibilidad de actualizar que esta relacionada a esta funcion: cambia prestamo
        datos = (self.nombremodificar.get(), self.telefonomodificar.get(), self.mailmodificar.get(), self.fechadeprestamomodificar.get(), self.fechadedevolucionmodificar.get(), self.devueltomodificar.get(), self.libroaprestarmodificar.get(), self.codigocambiaprestamo.get() )
        cantidad = self.conexion.modificacion_datos_prestamo(datos)
        if cantidad == 1:
            mb.showinfo("Información", "Se modificó el prestamo")      #cartelito que salta diciendo que se modifico el prestamo
        else:
            mb.showinfo("Información", "No existe un prestamo con dicho código")                                      
        

aplicacion1 = biblioteca()