"""
Generador de certificados en PDF
----------------------------------
Lee una lista de alumnos desde un archivo CSV y genera automáticamente
un certificado en PDF personalizado para cada uno.

Autora: Sabrina Soledad Roa
"""

import csv
import os
from datetime import date

from reportlab.lib.pagesizes import landscape, A4
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas

# ---------------------------------------------------------
# Configuración general
# ---------------------------------------------------------

ARCHIVO_ALUMNOS = "alumnos.csv"
CARPETA_SALIDA = "certificados_generados"
CURSO = "Introducción a la Programación"
FECHA_EMISION = date.today().strftime("%d/%m/%Y")

COLOR_TITULO = HexColor("#1F3864")
COLOR_TEXTO = HexColor("#333333")


# ---------------------------------------------------------
# Funciones
# ---------------------------------------------------------

def leer_alumnos(ruta_csv):
    """Lee los nombres de alumnos desde un CSV con columna 'nombre'."""
    with open(ruta_csv, newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        return [fila["nombre"].strip() for fila in lector if fila.get("nombre")]


def generar_certificado(nombre_alumno, curso, fecha, carpeta_salida):
    """Crea un PDF de certificado para un alumno y lo guarda en carpeta_salida."""
    nombre_archivo = nombre_alumno.lower().replace(" ", "_")
    ruta_pdf = os.path.join(carpeta_salida, f"certificado_{nombre_archivo}.pdf")

    ancho, alto = landscape(A4)
    c = canvas.Canvas(ruta_pdf, pagesize=landscape(A4))

    # Borde decorativo
    c.setStrokeColor(COLOR_TITULO)
    c.setLineWidth(3)
    c.rect(1.5 * cm, 1.5 * cm, ancho - 3 * cm, alto - 3 * cm)

    # Título
    c.setFillColor(COLOR_TITULO)
    c.setFont("Helvetica-Bold", 34)
    c.drawCentredString(ancho / 2, alto - 5 * cm, "CERTIFICADO DE FINALIZACIÓN")

    # Texto principal
    c.setFillColor(COLOR_TEXTO)
    c.setFont("Helvetica", 16)
    c.drawCentredString(ancho / 2, alto - 8 * cm, "Se certifica que")

    c.setFont("Helvetica-Bold", 26)
    c.setFillColor(COLOR_TITULO)
    c.drawCentredString(ancho / 2, alto - 9.5 * cm, nombre_alumno)

    c.setFont("Helvetica", 16)
    c.setFillColor(COLOR_TEXTO)
    c.drawCentredString(ancho / 2, alto - 11 * cm, "ha completado satisfactoriamente el curso")

    c.setFont("Helvetica-Bold", 20)
    c.drawCentredString(ancho / 2, alto - 12.5 * cm, curso)

    # Fecha
    c.setFont("Helvetica", 12)
    c.drawCentredString(ancho / 2, 3 * cm, f"Emitido el {fecha}")

    c.save()
    return ruta_pdf


def main():
    os.makedirs(CARPETA_SALIDA, exist_ok=True)

    alumnos = leer_alumnos(ARCHIVO_ALUMNOS)
    if not alumnos:
        print("No se encontraron alumnos en el archivo CSV.")
        return

    print(f"Generando {len(alumnos)} certificado(s)...\n")
    for nombre in alumnos:
        ruta = generar_certificado(nombre, CURSO, FECHA_EMISION, CARPETA_SALIDA)
        print(f"  ✅ {nombre} -> {ruta}")

    print(f"\nListo. Los certificados están en la carpeta '{CARPETA_SALIDA}/'.")


if __name__ == "__main__":
    main()
