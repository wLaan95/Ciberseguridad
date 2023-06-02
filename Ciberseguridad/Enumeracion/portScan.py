#!/bin/bash

# Importamos los modulos necesarios
import os
import ipaddress
import socket
from termcolor import colored

try:
    while True:
        try:  
            lista_puertos = list()

            # Pedimos la información al usuario
            puerto_inicial = int(input("Introduzca el puerto de inicio: "))
            puerto_final = int(input("Introduzca el puerto final: "))
            host = input("Introduce la IP donde escanear los puertos: ")
            
            print(colored("\n[*] Comenzando el escaneo de puertos...", "yellow"))
            
            # Recorremos todo el rango de puertos
            for puerto in range(puerto_inicial, puerto_final+1):
                # Creamos el socket para conectarnos
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(0.1)

                #print(colored(f"[*] Conectando con el puerto {puerto}...", "cyan"))
                respuesta = s.connect_ex((host, puerto))
                # Comprobamos el resultado de la conexión
                if respuesta == 0:
                    # Conexión aceptada
                    print(colored(f"[*] Puerto {puerto} abierto", "green"))
                    lista_puertos.append(puerto)
                s.close()
            
            if len(lista_puertos) > 0:
                print(colored(f"\n[*] Se han encontrado {len(lista_puertos)} puertos abiertos en {host}", "green"))
            else:
                print(colored(f"\n[*] No se han encontrado puertos abiertos en {host}", "cyan"))
            
            # Fin de while True
            break
        except ValueError: 
            print(colored("\n[!] ERROR: Los puertos deben ser un número válido", "red"))
        except KeyboardInterrupt:
            if len(lista_puertos) > 0:
                print(colored(f"[*] Se han encontrado {len(lista_puertos)} puertos abiertos en {host}", "green"))
            else:
                print(colored("\n[!] ERROR: Saliendo del programa...", "colored"))
                exit()
except Exception as e:
    print(colored(f"\n[!] ERROR: Saliendo del programa...", "red"))
    exit()
