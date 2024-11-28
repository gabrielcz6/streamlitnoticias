import requests

# URL de tu API de Django (ajusta la URL según corresponda)
url = "http://localhost:8001/api/procesador/cargar_excel/"

# Ruta al archivo Excel que deseas subir
archivo = {'archivo': open('Book1.xlsx', 'rb')}

# Token de autenticación (sustituye con el token real que tienes)
token = '6e8acbc0c4f057e11f594f34c1710f9b4853ebac'

# Agregar el token al encabezado 'Authorization'
headers = {
    'Authorization': f'Token {token}'  # Agrega el prefijo 'Bearer' para tokens tipo JWT
}

# Hacer la solicitud POST con el archivo y el encabezado
response = requests.post(url, files=archivo, headers=headers)

# Verificar la respuesta
if response.status_code == 201:
    print("Archivo cargado exitosamente!")
    print("Respuesta:", response.json())  # Muestra la respuesta del servidor (si la hay)
else:
    print("Error al cargar el archivo. Código de estado:", response.status_code)
    print("Mensaje de error:", response.json())
