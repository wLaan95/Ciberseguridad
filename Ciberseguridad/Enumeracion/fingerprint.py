#!/bin/bash

# Importamos los modulos necesarios
import requests
import os
from termcolor import colored

try:
    
    url = input("[*] Introduce una URL: ")
    response = requests.get(url)

    if response.status_code == 200:
        print(colored(f"\n[*] La url está online", "green"))
        
        for clave, valor in response.headers.items():
            print(colored(f"[*] {clave}: {valor}", "cyan"))

except Exception as e:
    print(colored("\n[!] ERROR: Saliendo del problema..."))
    exit()

