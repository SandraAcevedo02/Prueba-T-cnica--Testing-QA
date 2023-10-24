import requests
import json

class obtenerProcesos:
    url = 'http://api2.psicoalianza.com/api/procesos'
    headers = {
       'token' : 'uWJX7TwS68Ede2OyN43ISjbGU10T1OFF',
        'Authorization' : 'Basic eWhleXNvbi5ndWV2YXJhOlBzaWNvYWxpYW56YTIk'
    }
    
    carga = {
'proceso_nombre': 'Pruebas creacion',
  'fecha_cierre': '202',
  'numero_vacantes': 5,
  'proceso_estado': True,
  'verificacion_identidad': True,
  'pruebas': [
    {
      'id_prueba': 1,
      'id_perfil': 18,
      'valor_porcentual': 100
    }
  ]
    }

    response = requests.post(url, headers=headers, json=carga)
    print(response)
    if response.status_code == 200:
        print("Solicitud GET exitosa")
        print(response.json())
    else:
        print(f"Error en la solicitud GET: {response.status_code}")