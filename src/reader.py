from dataclasses import dataclass
import os

@dataclass
class Empleado:
    nombre: str
    rol: str
    salario: float
    activo: bool


def parsear_linea(linea: str) -> Empleado:
    nombre, rol, salario, activo = linea.strip().split(",")

    return Empleado(
        nombre=nombre,
        rol=rol,
        salario=float(salario),
        activo=activo == "True" 
    )


def leer_empleados(ruta):
    if not os.path.exists(ruta):
        raise FileNotFoundError(f"No existe el archivo: {ruta}")

    with open(ruta, "r") as f:
        next(f)
        for linea in f:
            if linea.strip():
                yield parsear_linea(linea)