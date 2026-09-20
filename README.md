# 🎓 Generador de Certificados en PDF

Script en Python que lee una lista de alumnos desde un archivo CSV y genera automáticamente un certificado de finalización en PDF, personalizado para cada uno.

## ¿Qué hace?

- Lee los nombres de los alumnos desde `alumnos.csv`
- Genera un PDF individual por cada alumno con diseño prolijo (borde, título, nombre destacado y fecha)
- Guarda todos los PDFs en la carpeta `certificados_generados/`

## Tecnologías

- Python 3
- [ReportLab](https://www.reportlab.com/) para la generación de PDF
- Módulo `csv` de la librería estándar

## Cómo ejecutarlo

```bash
pip install reportlab
python generar_certificados.py
```

## Cómo personalizarlo

- Editá `alumnos.csv` y agregá o quitá nombres (una columna llamada `nombre`)
- Cambiá la variable `CURSO` dentro del script para usar otro nombre de curso
- Ajustá colores y textos en la función `generar_certificado()`

## Estructura del código

- `leer_alumnos()`: lee los nombres desde el CSV
- `generar_certificado()`: arma el diseño del PDF para un alumno
- `main()`: recorre la lista de alumnos y genera todos los certificados

## Contexto

Como Profesora en Educación Especial, este proyecto surge de una necesidad real: automatizar una tarea repetitiva (generar certificados uno por uno) que antes hacía manualmente.

## Posibles mejoras a futuro

- Agregar un logo institucional a los certificados
- Leer los datos desde un Excel en lugar de CSV
- Enviar los certificados por email automáticamente
