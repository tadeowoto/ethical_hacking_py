import requests

def fingerprint(url):
    try:
        print(f"🔍 Escaneando: {url}\n")
        res = requests.get(url, timeout=5)
        headers = res.headers
        
        print("📋 Headers encontrados:")
        print("-" * 50)
        for key, value in headers.items():
            print(f"  {key}: {value}")
        print("-" * 50)
        
        print('\n🔎 Posibles tecnologías utilizadas:')
        print("-" * 50)
        tech = []
        if 'X-Powered-By' in headers:
            tech.append(headers['X-Powered-By'])
        if 'Server' in headers:
            tech.append(headers['Server'])
            
        html = res.text.lower()

        # Check for common technologies
        technologies = {
            "wp-content": "WordPress",
            "joomla": "Joomla",
            "drupal": "Drupal",
            "magento": "Magento",
            "reactjs": "ReactJS",
            "vue.js": "Vue.js",
            "angular": "Angular",
            "laravel": "Laravel",
            "codeigniter": "CodeIgniter"
        }
        
        for keyword, technology in technologies.items():
            if keyword in html:
                tech.append(technology)
        
        print()
        if tech:
            print(f"✨ Tecnologías encontradas: {', '.join(tech)}")
        else:
            print("❌ No se encontraron tecnologías")
        print("-" * 50)
    
    except Exception as e:
        print(f"⚠️  Error al escanear {url}: {e}")    

print('Ingrese la url a escanear')
url = input()
print('Espere un momento...')
fingerprint(url)
