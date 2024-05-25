class Series:
    # Nombre,Genero,Temporadas,Capitulos,Duracion_Capitulo(min),Creador,Puntuacion_Estrellas,Plataforma,Tendencia
    def __init__(self,nombre,genero,temporadas,puntuacion_estrellas,tendencia):
        self.nombre = nombre
        self.genero = genero
        self.temporada = temporadas
        self.puntuacion_estrellas = puntuacion_estrellas
        self.tendencia = tendencia

    def __str__(self):
        return self.nombre, self.genero, self.temporada,self.puntuacion_estrellas,self.tendencia
    def __repr__(self):
        return self.nombre, self.genero,self.temporada, self.puntuacion_estrellas,self.tendencia