def generar_reporte(empleados):
    grupos = {}

    for e in empleados:
        if e.rol not in grupos:
            grupos[e.rol] = {"total": 0, "cantidad": 0}

        grupos[e.rol]["total"] += e.salario
        grupos[e.rol]["cantidad"] += 1

    return grupos


def guardar_reporte(grupos, ruta_salida):
    with open(ruta_salida, "w") as f:
        for rol, data in grupos.items():
            promedio = data["total"] / data["cantidad"]

            f.write(f"Rol: {rol}\n")
            f.write(f"Cantidad: {data['cantidad']}\n")
            f.write(f"Promedio Salario: {promedio:.2f}\n\n")