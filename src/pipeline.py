from src.reader import leer_empleados


def filtrar_empleados(ruta, minimo, solo_activos=False):
    empleados = leer_empleados(ruta)

    return (
        e for e in empleados
        if e.salario >= minimo and (e.activo if solo_activos else True)
    )