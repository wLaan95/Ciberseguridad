#!/bin/python3

# Importamos el modulo ipaddress
import ipaddress
import os
from termcolor import colored

try:
    while True:
        try:
            lista_ip = list()

            # Especificamos la red en formato CIDR
            red = input("Introduzca la red que quiere escanear en formato CIDR: ")
            print(colored(f"\n[*] Escaneando la red {red}...", "yellow"))

            # Recorremos las direcciones útiles de la red
            for host in ipaddress.IPv4Network(red).hosts():
                respuesta = os.system(f"ping -c 1 {host} > /dev/null")

                # Si respuesta es 0, el host ha respondido a nuestro ping
                if respuesta == 0:
                    print(colored(f"[*] Encontrado un live host en {host}", "green"))
                    lista_ip.append(host)

            if len(lista_ip) > 0:
                print(colored(f"[*] Se han encontrado {len(lista_ip)} live hosts", "cyan"))
            else:
                print(colored("[*] No se han encontrado live hosts", "cyan"))
            # Fin de while True
            break

        # Red con formato incorrecto
        except ipaddress.AddressValueError:
            print(colored("\n[!] ERROR: Formato CIDR incorrecto...", "red"))

# Ctrl + C
except KeyboardInterrupt:
    print(colored("\n[!] Saliendo del programa...", "red"))
    exit()

# Errores inesperados
except Exception as e:
    print(colored(f"\n[!] ERROR: Saliendo del programa...", "red"))
    exit()
