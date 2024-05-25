class Pelicula:
    def __init__(self,nombre,genero,duracion,calificacion,tendencia):
        self.nombre = nombre
        self.genero = genero
        self.duracion = duracion
        self.calificacion = calificacion
        self.tendencia = tendencia

    def __str__(self):
        return self.nombre, self.genero, self.duracion,self.calificacion,self.tendencia
    def __repr__(self):
        return self.nombre, self.genero,self.duracion, self.calificacion,self.tendencia
