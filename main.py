import argparse
import logging
from config import configurar_logging
from src.pipeline import filtrar_empleados
from src.report import generar_reporte, guardar_reporte


def configurar_cli():
    parser = argparse.ArgumentParser(
        description="Procesador de empleados con filtros y generación de reportes"
    )

    parser.add_argument(
        "--input",
        required=True,
        help="Ruta del archivo CSV de entrada"
    )

    parser.add_argument(
        "--output",
        default="output/reporte.txt",
        help="Ruta del archivo de salida"
    )

    parser.add_argument(
        "--min_salario",
        type=float,
        default=1500,
        help="Salario mínimo para filtrar"
    )

    parser.add_argument(
        "--solo_activos",
        action="store_true",
        help="Filtrar solo empleados activos"
    )

    return parser.parse_args()


def main():
    # 🔧 Configurar logging
    configurar_logging()

    try:
        args = configurar_cli()

        logging.info("🚀 Inicio del proceso")
        logging.info(f"Archivo entrada: {args.input}")
        logging.info(f"Archivo salida: {args.output}")
        logging.info(f"Salario mínimo: {args.min_salario}")
        logging.info(f"Solo activos: {args.solo_activos}")

        # 🔹 Pipeline
        empleados = filtrar_empleados(
            args.input,
            args.min_salario,
            solo_activos=args.solo_activos
        )

        # 🔹 Generar reporte
        grupos = generar_reporte(empleados)

        # 🔹 Guardar resultado
        guardar_reporte(grupos, args.output)

        logging.info("✅ Proceso finalizado correctamente")

    except FileNotFoundError as e:
        logging.error(f"❌ Archivo no encontrado: {e}")

    except Exception as e:
        logging.exception("❌ Error inesperado durante la ejecución")


if __name__ == "__main__":
    main()