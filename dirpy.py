from pathlib import Path
from urllib.parse import urlparse
from os import system, name
import socket
import requests
import time
import sys
from colorama import Fore

lista = []
lista2 = []

heade = {
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64; rv:152.0) "
        "Gecko/20100101 Firefox/152.0"
    ),
    "Accept": (
        "text/html,application/xhtml+xml,application/xml;q=0.9,"
        "image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8"
    ),
    "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.7,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "DNT": "1",
    "Sec-GPC": "1"
}


def limpar():
    system("cls" if name == "nt" else "clear")

def grabb(url):

    req = requests.get(url, headers=heade, timeout=1)

    return req.headers.geYt("Server")

def url(url=str):
    while True:
        try:
            url = input('Url: ')
            if not url:
                print('URL VAZIA!')
                continue
            return url
        except ValueError:
                print('VARIAVEL NAO SUPORTADA')
                continue      

def select1(url1):
        
        try:
            final_url = ensure_scheme_probe(url1) 
            ip_url = ip(url1)
        except ValueError:
            print('O conteudo dever ser uma string!')
            sys.exit()
        except Exception as a:
            limpar()
            print('ERRO ao criar a URL')
            print('='*60)
            print(f'{a}')
            sys.exit()

        while True:
            caminhos = input('File name or path: ')
            if not caminhos:
                 print('PATH VAZIO!')
                 continue
            break

        resp = caminho(caminhos)

        limpar()

        print('*DIRPY 1.4')
        print('*Author Vortex')

        print('='*60)

        print('INFO ALVO')
        print(f'~ Site:{final_url} = [{ip_url}]')
        head = grabb(final_url)
        print(f"~ Server:[{head}]")
        print('='*60)
        print('METHOD GET')

        for itens in lista:
                resposta = scan(final_url, itens)
                if resposta == 200:
                    print(Fore.GREEN + f'[+] Directory found {itens}, status:', resposta )
                elif resposta in (301, 302, 307, 308):
                    print(Fore.BLUE + f'[~] Redirect page {itens}, status:', resposta)
                elif resposta in (403, 405, 501):
                    print(Fore.RED + f'Forbidden/Unauthorized (possible protected dir) {itens}, status:', resposta )
                elif resposta == 404:
                    print(Fore.YELLOW + f'[~] {final_url}{itens}:', resposta)
                else:
                    print(f'[~] {final_url}{itens}:', resposta)

        print('-'*60)

def montar(domain=str, itens=str):
    url = (itens + '.' + domain)
    return url

def caminho(caminho):
        
    base = Path(__file__).resolve().parent

    while True:
        try:

            arquivo = base / caminho
            print(arquivo)

            with open(arquivo, 'r', encoding='utf-8') as f:
                    for linha in f:
                        linha2 = linha.strip()
                        lista.append(linha2)
            return lista
        except FileNotFoundError:
            print('File Not Found')
            sys.exit()
        except ValueError:
            print('O conteudo dever ser uma string!')
            sys.exit()

def ip(url):
    ip = socket.gethostbyname(url)
    return ip

def scan(url=str, itens=str):
    resp = requests.get(url + itens, headers=heade, timeout=1)
    if resp.status_code is None:
        return "Falha na Conexão"
    return resp.status_code

def ensure_scheme_probe(url: str, timeout: float = 3.0) -> str:
    try:
        url = url.strip()
        if not url:
            print('URL VAZIA')
    except ValueError:
        print('Formato insuportavel use str')

    parsed = urlparse(url)
    if parsed.scheme in ("http", "https"):
        return url

    host_and_path = url
    https_url = f"https://{host_and_path}"
    http_url = f"http://{host_and_path}"

    try:
        resp = requests.head(https_url, allow_redirects=True, timeout=timeout, headers=heade)
        if resp.status_code >= 400:
            resp = requests.get(https_url, allow_redirects=True, timeout=timeout, headers=heade)
        final_scheme = urlparse(resp.url).scheme if resp else None

        if resp and resp.status_code < 400 and final_scheme == "https":
            return resp.url
        if resp and final_scheme == "http":
            return resp.url
    except requests.exceptions.SSLError:
        pass
    except requests.RequestException:
        pass

    try:
        resp = requests.head(http_url, allow_redirects=True, timeout=timeout)
        if resp.status_code >= 400:
            resp = requests.get(http_url, allow_redirects=True, timeout=timeout)
        if resp and resp.status_code < 400:
            return resp.url
    except requests.RequestException:
        pass

    return https_url

print(Fore.GREEN + r"""
888 88e   ,e,                           
888 888b   "  888,8, 888 88e  Y8b Y888P 
888 8888D 888 888 "  888 888b  Y8b Y8P  
888 888P  888 888    888 888P   Y8b Y   
888 88"   888 888    888 88"     888    
                     888         888    
                     888         888    
""")
print((Fore.WHITE + 'DIRPY >:D \n'))

try:
    while True:
        print('[1] dir scan')
        try:
            select = int(input(':'))
        except ValueError:
            print('1 OPTIONS ONLY')
            continue
        break

    if select == 1:
        limpar()
        url1 = url()
        select1(url1)
    else:
        print('OPTION NOT FOUND')

except KeyboardInterrupt:
    print('Intermediate process: KeyboardInterrupt')
