import requests
import json

class obtenerProcesos:

  if __name__ == '__main__': 
    url = 'http://api2.psicoalianza.com/api/procesos'
    headers = {
      'Token' : 'uWJX7TwS68Ede2OyN43ISjbGU10T1OFF',
      'Authorization' : 'Basic eWhleXNvbi5ndWV2YXJhOlBzaWNvYWxpYW56YTIk',
      
    }
    
    arg = {
      'id_proceso': 220,
      'proceso_nombre': 'Proceso de selección',
      'id_empresa': 1,
      'fecha_cierre': '2019-06-13',
      'numero_vacantes': 1,
      'verificacion_identidad': 1,
      'estado': 0,
      'created_at': '2019-06-13T22:08:12',
      'updated_at': '2019-06-13T22:08:12'
    }

    response =requests.get(url, params=arg, headers=headers)
    print(response)
    if response.status_code  == 200:
      print("Exito")
    else:
      print("mal")