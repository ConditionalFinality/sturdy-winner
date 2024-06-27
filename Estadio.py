class Estadio:
    def __init__(self, stadium_id, nombre, ubicacion):
            self.stadium_id = stadium_id
            self.nombre = nombre
            self.ubicacion = ubicacion

    def mostrar(self):
          return f'Nombre: {self.nombre}, Ubicación: {self.ubicacion}'