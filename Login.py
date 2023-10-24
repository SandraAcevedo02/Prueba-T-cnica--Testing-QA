import requests

def Login():
    url = 'http://api2.psicoalianza.com/api/procesos'
    headers = {
        'Token': 'uWJX7TwS68Ede2OyN43ISjbGU10T1OFF',
        'Authorization': 'Basic eWhleXNvbi5ndWV2YXJhOlBzaWNvYWxpYW56YTIk',
    }

    params = {
        'username': 'abdel1.cartagena',
        'password': 'Abdel1234',
        
    }

    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()  # Levanta una excepción si la solicitud no fue exitosa

        if response.status_code == 200:
            print("Ingreso exitoso")
        else:
            print("Error en la solicitud: Código", response.status_code)
    except requests.exceptions.RequestException as e:
        print("Error en la solicitud:", str(e))

if __name__ == '__main__':
    Login()