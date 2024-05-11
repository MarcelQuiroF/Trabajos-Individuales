import tkinter as tk

def registro_de_gastos():
    gastos = []

    def agregar():
        fecha = entrada_fecha.get()
        monto = int(entrada_gasto.get())
        gastos.append(monto)
        lista_gasto.insert(tk.END, f"{fecha} - {monto}")
        
    def eliminar():
        seleccion = lista_gasto.curselection()
        if seleccion:
            indice = seleccion[0]
            del gastos[indice]
            lista_gasto.delete(indice)
            
    def reiniciar():
        global gastos
        gastos = []
        lista_gasto.delete(0, tk.END)
        
    def monto_total():
        global monto
        monto = 0
        for i in gastos:
            monto += i
        gasto = tk.Label(ventana, text=f"""El monto es:
{monto}""", font=("Arial", 10))
        gasto.place(relx=0.68, rely=0.85)

    ventana = tk.Tk()
    ventana.geometry("300x400")
    ventana.title("Gestor de gastos")

    fecha = tk.Label(ventana, text="""FECHA
(dd/mm)""", font=("Arial", 10))
    fecha.place(relx=0.15, rely=0.05)

    gasto = tk.Label(ventana, text="GASTO", font=("Arial", 10))
    gasto.place(relx=0.15, rely=0.17)

    gasto_mensual = tk.Label(ventana, text="LISTA DE GASTOS", font=("Arial", 10))
    gasto_mensual.place(relx=0.15, rely=0.35)

    entrada_gasto = tk.Entry(ventana, font=("Arial", 10), justify="left")
    entrada_gasto.place(relx=0.40, rely=0.173, relwidth=0.4, relheight=0.05)

    entrada_fecha = tk.Entry(ventana, font=("Arial", 10), justify="left")
    entrada_fecha.place(relx=0.40, rely=0.073, relwidth=0.4, relheight=0.05)

    boton_agregar= tk.Button(ventana, text="Agregar", command=agregar)
    boton_agregar.place(relx=0.45, rely=0.27, relwidth=0.3, relheight=0.05)

    boton_agregar= tk.Button(ventana, text="Monto total", command=monto_total)
    boton_agregar.place(relx=0.65, rely=0.7, relwidth=0.3, relheight=0.05)

    boton_agregar= tk.Button(ventana, text="Eliminar", command=eliminar)
    boton_agregar.place(relx=0.65, rely=0.45, relwidth=0.3, relheight=0.05)

    boton_agregar= tk.Button(ventana, text="Reiniciar", command=reiniciar)
    boton_agregar.place(relx=0.65, rely=0.55, relwidth=0.3, relheight=0.05)

    lista_gasto = tk.Listbox(ventana)
    lista_gasto.place(relx=0.1, rely=0.41, relwidth=0.5, relheight=0.5)

    ventana.mainloop()

def gestion_de_contraseñas():
    def eliminar():
        seleccionado = lista_contraseña.curselection()
        if seleccionado:
            indice = seleccionado[0]
            lista_contraseña.delete(indice)
        
    def agregar():
        contraseña = entrada_contraseña.get()
        lista_contraseña.insert(tk.END, contraseña)
        
    def editar():
        seleccionado = lista_contraseña.curselection()
        if seleccionado:
            indice = seleccionado[0]
            lista_contraseña.delete(indice)
            lista_contraseña.insert(indice, editar_contraseña.get())

    ventana = tk.Tk()
    ventana.geometry("500x350")
    ventana.title("Gestor de contraseñas")

    contraseña = tk.Label(ventana, text="Contraseña", font=("Arial", 10))
    contraseña.place(relx=0.07, rely=0.07)

    entrada_contraseña = tk.Entry(ventana, font=("Arial", 10), justify="left")
    entrada_contraseña.place(relx=0.23, rely=0.06, relwidth=0.5, relheight=0.1)

    editar_contraseña = tk.Entry(ventana, font=("Arial", 10), justify="left")
    editar_contraseña.place(relx=0.65, rely=0.3, relwidth=0.30, relheight=0.1)

    boton_añadir= tk.Button(ventana, text="Agregar", command=agregar)
    boton_añadir.place(relx=0.75, rely=0.05, relwidth=0.2, relheight=0.12)

    boton_eliminar= tk.Button(ventana, text="Eliminar", command=eliminar)
    boton_eliminar.place(relx=0.7, rely=0.7, relwidth=0.2, relheight=0.12)

    boton_editar= tk.Button(ventana, text="Editar", command=editar)
    boton_editar.place(relx=0.7, rely=0.45, relwidth=0.2, relheight=0.12)

    lista_contraseña = tk.Listbox(ventana)
    lista_contraseña.place(relx=0.1, rely=0.27, relwidth=0.5, relheight=0.6)

    ventana.mainloop()

def gestor_tareas():
    global indice, posicionY, tareas
    indice = 0
    posicionY = 0.1
    tareas = {}

    def agregar_tarea():
        global indice, posicionY
        estado_tarea = tk.BooleanVar()
        estado_tarea.set(False)
        
        tarea_nombre = entrada.get()
        tareas[tarea_nombre] = estado_tarea
        
        tarea = tk.Checkbutton(ventana, text=tarea_nombre, var=estado_tarea, font=("Arial", 14))
        
        if indice <= 7:
            tarea.place(relx=0.02, rely=posicionY)
            if indice == 7:
               posicionY = 0.0
        elif indice <= 15:
            tarea.place(relx=0.42, rely=posicionY)
        else:
            aviso = tk.Label(ventana, text="El numero maximo de tareas es 16", font=("Arial", 14))
            aviso.place(relx=0.02, rely=0.90)
            indice -= 1
        indice += 1
        posicionY += 0.1


    def renovar_lista():
        for widget in ventana.winfo_children():
            if isinstance(widget, tk.Label):
                widget.destroy()

    def renovar_tareas():
        global indice, posicionY, tareas
        for widget in ventana.winfo_children():
            if isinstance(widget, tk.Checkbutton):
                widget.destroy()
        indice = 0
        posicionY = 0.1
        tareas = {}


    def filtrar_completas():
        posicion_completas = 0.15
        for tarea in tareas:
            if tareas[tarea].get():
                tarea_completa = tk.Label(ventana, text=tarea, font=("Arial", 10))
                tarea_completa.place(relx=0.75, rely=posicion_completas)
                posicion_completas += 0.05
                
    def filtrar_incompletas():
        posicion_incompletas = 0.15
        for tarea in tareas:
            if not tareas[tarea].get():
                tarea_completa = tk.Label(ventana, text=tarea, font=("Arial", 10))
                tarea_completa.place(relx=0.75, rely=posicion_incompletas)
                posicion_incompletas += 0.05


    ventana = tk.Tk()
    ventana.geometry("700x500")
    ventana.title("Gestor de tareas")

    entrada = tk.Entry(ventana, font=("Arial", 20), justify="left")
    entrada.place(relx=0.3, rely=0.01, relwidth=0.3, relheight=0.05)

    boton_agregar = tk.Button(ventana, text="Ingresar", command=agregar_tarea)
    boton_agregar.place(relx=0.62, rely=0.01, relwidth=0.1, relheight=0.05)

    boton_filtrar_completas = tk.Button(ventana, text="Completas", command=filtrar_completas)
    boton_filtrar_completas.place(relx=0.75, rely=0.1, relwidth=0.1, relheight=0.05)

    boton_filtrar_incompletas = tk.Button(ventana, text="Incompletas", command=filtrar_incompletas)
    boton_filtrar_incompletas.place(relx=0.87, rely=0.1, relwidth=0.1, relheight=0.05)

    boton_renovar = tk.Button(ventana, text="Vaciar lista", command=renovar_lista)
    boton_renovar.place(relx=0.87, rely=0.9, relwidth=0.1, relheight=0.05)

    boton_vaciar = boton_renovar = tk.Button(ventana, text="Vaciar tareas", command=renovar_tareas)
    boton_renovar.place(relx=0.75, rely=0.9, relwidth=0.1, relheight=0.05)

    ventana.mainloop()
    
def calculadora_propinas():
    def calcular_propina():
        porcentaje = int(entrada_propina.get())
        monto = int(entrada_monto.get())
        propina = monto*(porcentaje/100)
        monto = tk.Label(ventana, text=f"""La propina es 
{propina}""", font=("Arial", 10))
        monto.place(relx=0.15, rely=0.68, relwidth=0.70, relheight=0.3)


    ventana = tk.Tk()
    ventana.geometry("220x300")
    ventana.title("Calculador De Propina")


    entrada_monto = tk.Entry(ventana, font=("Arial", 10), justify="left")
    entrada_monto.place(relx=0.242, rely=0.15, relwidth=0.5, relheight=0.1)

    entrada_propina = tk.Entry(ventana, font=("Arial", 10), justify="left")
    entrada_propina.place(relx=0.242, rely=0.40, relwidth=0.5, relheight=0.1)

    monto = tk.Label(ventana, text="MONTO", font=("Arial", 10))
    monto.place(relx=0.38, rely=0.05)

    propina = tk.Label(ventana, text="PORCENTAJE DE PROPINA", font=("Arial", 10))
    propina.place(relx=0.1, rely=0.30)


    porcentaje = tk.Label(ventana, text="%", font=("Arial", 10))
    porcentaje.place(relx=0.79, rely=0.42)


    boton_calcular = tk.Button(ventana, text="Calcular", command=calcular_propina)
    boton_calcular.place(relx=0.38, rely=0.6)


    ventana.mainloop()
    
def lista_compras():
    productos = {}

    def agregar_producto():
        producto = entrada_producto.get()
        costo = entrada_costo.get()
        productos[producto] = costo
        lista_sin_comprar.insert(tk.END, producto)
        
    def eliminar_sin_comprar():
        seleccionado = lista_sin_comprar.curselection()
        if seleccionado:
            indice = seleccionado[0]
            lista_sin_comprar.delete(indice)
            
    def eliminar_comprado():
        seleccionado = lista_comprado.curselection()
        if seleccionado:
            indice = seleccionado[0]
            lista_comprado.delete(indice)
            
    def agregar_comprado():
        seleccionado = lista_sin_comprar.curselection()
        if seleccionado:
            indice = seleccionado[0]
            seleccionado = lista_sin_comprar.get(indice)
            lista_sin_comprar.delete(indice)
            lista_comprado.insert(tk.END, seleccionado)
            
    def costo_total():
        precio = 0
        for i in range(lista_comprado.size()):
            producto = lista_comprado.get(i)
            precio += int(productos[producto])
        etiqueta_precio = tk.Label(ventana, text=f"""El monto total es:
{precio}""", font=("Arial", 10))
        etiqueta_precio.place(relx=0.73, rely=0.85, relwidth=0.3, relheight=0.05)
        

    ventana = tk.Tk()
    ventana.geometry("800x600")
    ventana.title("Gestor de productos")


    producto = tk.Label(ventana, text="Producto", font=("Arial", 10))
    producto.place(relx=0.1, rely=0.07)

    costo = tk.Label(ventana, text="Costo", font=("Arial", 10))
    costo.place(relx=0.6, rely=0.07)

    entrada_producto = tk.Entry(ventana, font=("Arial", 10), justify="left")
    entrada_producto.place(relx=0.18, rely=0.06, relwidth=0.3, relheight=0.05)

    entrada_costo = tk.Entry(ventana, font=("Arial", 10), justify="left")
    entrada_costo.place(relx=0.66, rely=0.06, relwidth=0.1, relheight=0.05)
    entrada_costo.insert(0, 0)

    boton_agregar = tk.Button(ventana, text="Ingresar", command=agregar_producto)
    boton_agregar.place(relx=0.4, rely=0.16, relwidth=0.2, relheight=0.05)

    boton_eliminar_sin_comprar = tk.Button(ventana, text="Eliminar", command=eliminar_sin_comprar)
    boton_eliminar_sin_comprar.place(relx=0.12, rely=0.74, relwidth=0.1, relheight=0.05)

    boton_eliminar_comprado = tk.Button(ventana, text="Eliminar", command=eliminar_comprado)
    boton_eliminar_comprado.place(relx=0.62, rely=0.74, relwidth=0.1, relheight=0.05)

    boton_agregar_comprado = tk.Button(ventana, text="Añadir →", command=agregar_comprado)
    boton_agregar_comprado.place(relx=0.28, rely=0.74, relwidth=0.1, relheight=0.05)

    boton_costo = tk.Button(ventana, text="Costo", command=costo_total)
    boton_costo.place(relx=0.78, rely=0.74, relwidth=0.1, relheight=0.05)

    lista_sin_comprar = tk.Listbox(ventana)
    lista_sin_comprar.place(relx=0.1, rely=0.3, relwidth=0.3, relheight=0.4)

    lista_comprado = tk.Listbox(ventana)
    lista_comprado.place(relx=0.6, rely=0.3, relwidth=0.3, relheight=0.4)

    ventana.mainloop()


opcion = int(input("""Escriba el numero de ejercicio
1. Registro de gastos
2. Gestion de contraseñas
3. Gestor de Tareas Pendientes
4. Calculadora de Propinas
5. Lista de Compras
:"""))

if opcion == 1:
    registro_de_gastos()
elif opcion == 2:
    gestion_de_contraseñas()
elif opcion == 3:
    gestor_tareas()
elif opcion == 4:
    calculadora_propinas()
elif opcion == 5:
    lista_compras()