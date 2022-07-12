"""    Este script funciona para obtener información de las redes wifi guardadas en el sistema de Windows
    ya que se utiliza el CMD el cual nos permite ejecutar un código para obtener las redes guardadas y otras
  para obtener información de la red que elijamos lo que podemos obtener es tipo de red incluido la contraseña
"""
# Importando librerias
import os
from colorama import Fore
from time import localtime, asctime, sleep
# -----------------Baner------------------
print(Fore.GREEN+':::       ::: ::::::::::: :::::::::: ::::::::::: ')
print(':+:       :+:     :+:     :+:            :+:     ')
print('+:+       +:+     +:+     +:+            +:+     ')
print('+#+  +:+  +#+     +#+     :#::+::#       +#+     ')
print('+#+ +#+#+ +#+     +#+     +#+            +#+     ')
print(' #+#+# #+#+#      #+#     #+#            #+#     ')
print('  ###   ###   ########### ###        ########### '+Fore.RESET)
print(Fore.RED+'         ### Wifi Information V.1.0 ###')
print('Autor: ZIX :D')
print('IG: zixk.6'+Fore.RESET)
# Codigo
sleep(2)
print(Fore.BLUE+'-------------------------------------------------')
print(asctime(localtime()))
# Instrucciones para el CMD
cmd = "netsh wlan show profile"
resultado = os.popen(cmd)
print(resultado.read())
# El resultado Guardado en un archivo TXT
archivo = open('wifi.txt','a')
# Llamamos la red la cual quiere la informacion
red = input("Ingrese el nombre de la red: ")
# Intrucciones del CMD para obtener la informacion de la red
cmd2 = "netsh wlan show profile " +red+" key=clear"
resultado2 = os.popen(cmd2)
archivo.write(resultado2.read())
# Fin del Codigo
print('La red a sido vulnerada con exito xD'+Fore.RESET)
print(Fore.CYAN+'"Informacion guardada en el archivo wifi.txt"')