import base64

# String Base64 del contenido del archivo PDF
base64_pdf = """
#---aqui poner el texto base64
"""

# Decodificar el string Base64
pdf_data = base64.b64decode(base64_pdf)

# Escribir los datos decodificados a un archivo PDF
Nombre_archivo = "NombreDelArchivo.pdf"
with open(Nombre_archivo, 'wb') as pdf_file:
    pdf_file.write(pdf_data)

print(f"El archivo PDF ha sido guardado como {Nombre_archivo}")
