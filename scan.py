import socket

def scan_ports(ip, puertos):
    #EL IFNET INDICA EL TIPO DE IP EN ESTE CASO ES IPV4
    #EL SOCK_STREAM INDICA EL TIPO DE CONEXION QUE SE VA A REALIZAR EN ESTE CASO ES TCP
    for puerto in puertos:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        rtdo = sock.connect_ex((ip, puerto))
        if rtdo == 0:
            print(f" Puerto abiertos: {puerto}")
        else:
            print(f"Puerto cerrado: {puerto}")
        sock.close()

# scanme nmap org es una pagina de prueba de nmap
ip_obj = "scanme.nmap.org"
#
#PUERTOS A ESACANEAR
# 21: FTP
# 22: SSH
# 80: HTTP
# 443: HTTPS
# 8080: HTTP alternativo
#
puertos_a_escanear = [21, 22, 80, 443, 8080, 8000]    

scan_ports(ip_obj, puertos_a_escanear)
