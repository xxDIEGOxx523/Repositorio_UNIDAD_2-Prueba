class Usuario:
    # El constructor (inicializa los atributos del UML)
    def __init__(self, nombre: str, correo: str):
        self.nombre = nombre
        self.correo = correo

    # El método de negocio
    def presentarse(self) -> str:
        return f"Hola, mi nombre es {self.nombre} y mi correo es {self.correo}."