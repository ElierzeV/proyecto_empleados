from src.pipeline import filtrar_empleados
from src.reader import Empleado


def test_filtrar_salario():
    empleados = [
        Empleado("A", "IT", 2000, True),
        Empleado("B", "IT", 1000, True),
    ]

    resultado = [
        e for e in empleados
        if e.salario >= 1500
    ]

    assert len(resultado) == 1