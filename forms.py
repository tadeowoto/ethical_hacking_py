import requests
from bs4 import BeautifulSoup

def buscar_forms(url):
    print(f'buscando forms en {url}')
    # enviar una solicitud GET a la URL
    res = requests.get(url)
    # objeto BeautifulSoup para parsear el contenido HTML
    soup = BeautifulSoup(res.text, 'html.parser')
    # encontrar todos los formularios en la página
    formularios = soup.find_all('form')
    print(f"Fornularios encontrados: {len(formularios)}")
    
    # iterar sobre los formularios encontrados y guardamos todos sus atributos.
    for i, form in enumerate(formularios, 1):
        action = form.attrs.get('action').lower()
        method = form.get("method", "GET").upper()
        inputs = form.find_all("input")
        print(f"Formulario {i}")
        print(f"Action: {action}")
        print(f"Method: {method}")
        print("inputs:")
        for input_tag in inputs:
            tipo = input_tag.attrs.get("type", "text")
            nombre = input_tag.attrs.get("name")
            print(f"\tInput: tipo={tipo}, nombre={nombre}")


buscar_forms("https://httpbin.org/forms/post")
