import tkinter as tk # importar libreria
from Pelicula import Pelicula # importar clase
from Series import Series

# crear listas para los objetos de clase
peliculas = []
series = []
opciones = ["Drama","Accion","Terror","Comedia","Aventura","Ciencia ficcion","Fantasia","Anime"]

# cargar datos en listas y clases del archivo peliculas
def cargarPelicula():
    try:
        with open("../pythonProject2/peliculas.txt", "r", encoding="utf-8") as file:
            lineas = file.readlines()
        for linea in lineas:
            nombre, genero, duracion_Minutos, valoracion_estrellas, tendencia = linea.strip().split(",")
            pelicula = Pelicula(nombre, genero, duracion_Minutos, valoracion_estrellas, tendencia)
            peliculas.append(pelicula)
    
    # excepcion si no exite el archivo
    except FileExistsError:
        error.config(text="El archivo no existe.")

# muestra todas las peliculas
def mostrarPelicula():
    listbox.delete(0, tk.END)
    for pelicula in peliculas:
        listbox.insert(tk.END, pelicula.nombre)  

def cargarSeries():
    try:
        with open("../pythonProject2/series.txt", "r", encoding="utf-8") as file:
            lineas = file.readlines()
        for linea in lineas:
            nombre,genero,temporadas,puntuacion_estrellas,tendencia = linea.strip().split(",")
            serie = Series(nombre,genero,temporadas,puntuacion_estrellas,tendencia)
            series.append(serie)

    except FileExistsError:
        error.config(text="El archivo no existe.")

def mostrarSeries():
    listbox.delete(0, tk.END)
    for serie in series:
        listbox.insert(tk.END, serie.nombre)

# filtrar por genero
def filtrarPeliculas():
    listbox.delete(0, tk.END)
    genero_seleccionado = entry.get().lower()
    for pelicula in peliculas:
        if genero_seleccionado == pelicula.genero.lower():
            listbox.insert(tk.END,f"Nombre: {pelicula.nombre},Duración: {pelicula.duracion}")

# filtrar por peliculas mas vistas
def topPeliculas():
    listbox.delete(0, tk.END)
    for pelicula in peliculas:
        if pelicula.tendencia == "1":
            listbox.insert(tk.END,f"Nombre: {pelicula.nombre},Duración: {pelicula.duracion}")

def filtrarSeries():
    listbox.delete(0, tk.END)
    genero_seleccionado = entry.get().lower()
    for serie in series:
        if genero_seleccionado == serie.genero.lower():
            listbox.insert(tk.END,f"Nombre: {serie.nombre},Duración: {serie.temporada}")

def topSeries():
    listbox.delete(0, tk.END)
    for serie in series:
        if serie.tendencia == "1":
            listbox.insert(tk.END,f"Nombre: {serie.nombre},Duración: {serie.temporada}")

# interfaz grafica
def main():
    # hacer global a la variable
    global listbox
    global entry
    global error

    # crear una ventana
    window = tk.Tk()
    # poner titulo
    window.title("Recomendador de series y películas")
    # acomodar la ventana a la pantalla
    ancho_pantalla = window.winfo_screenwidth()
    alto_pantalla = window.winfo_screenheight()
    window.geometry(f"{ancho_pantalla}x{alto_pantalla}")
    
    # llama a las funciones para cargar los archivos
    cargarSeries()
    cargarPelicula()

    # ingresamos un fondo 
    bg_image = tk.PhotoImage(file="../pythonProject2/Fondoimagen.png")

    # posicion de fondo
    bg_label = tk.Label(window, image=bg_image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1) 

    # crea un boton
    boton1 = tk.Button(window, text="Películas", bg="ghost white", width=14, height=3, font=("arial", 15),command=mostrarPelicula)
    boton1.place(x=200, y=130)

    boton2 = tk.Button(window, text="Series", bg="ghost white", width=14, height=3, font=("arial", 15), command=mostrarSeries)
    boton2.place(x=700, y=130)

    boton3 = tk.Button(window, text="Filtrar peliculas", bg="ghost white", width=14, height=3, font=("arial", 15),command=filtrarPeliculas)
    boton3.place(x=400, y=80)

    boton4 = tk.Button(window, text="Top peliculas", bg="ghost white", width=14, height=3, font=("arial", 15),command=topPeliculas)
    boton4.place(x=400, y=180)

    boton5 = tk.Button(window, text="Filtrar series", bg="ghost white", width=14, height=3, font=("arial", 15),command=filtrarSeries)
    boton5.place(x=900, y=80)

    boton6 = tk.Button(window, text="Top series", bg="ghost white", width=14, height=3, font=("arial", 15),command=topSeries)
    boton6.place(x=900, y=180)

    # etiqueta de error
    error = tk.Label(window,text="",font=16,fg="red")
    error.place(x=600,y=675)

    # valor predeterminado de opcion de genero
    variable_opcion = tk.StringVar(window)
    variable_opcion.set(opciones[0])

    # guardar la opcion elegida
    entry = tk.Entry(window,width=35,textvariable=variable_opcion,font=16)
    entry.place(x=500,y=340)

    # menu de opciones desplegable
    menu_desplegable = tk.OptionMenu(window, variable_opcion, *opciones)
    menu_desplegable.place(x=900,y=337)

    # lista los elementos de las listas
    listbox = tk.Listbox(window, width=100, height=14)
    listbox.place(x=300, y=400)

    # inicio de interfaz grafica
    window.mainloop()

if __name__ == "__main__":
    # llama a la funcion principal
    main() 
