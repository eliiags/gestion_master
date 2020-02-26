#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 01:57:35 2020

@author: Elianni Aguero, Angelica Guerrero, Cinthya Quintana
"""

# Para ocultar el numero 
import getpass


""" 
    Hace comprobaciones del numero num
    Se asegura que sea tipo entero y que este dentro del intervalo [MIN, MAX]
    oculto: para saber si el numero es oculto o no, es decir si puede mostrarse 
            o no por pantalla
    
    Hasta que el usuario no escriba un numero correcto acaba la funcion
    Devuelve el numero introducido por el usuario
"""
def compruebaNumero(MIN, MAX, num, oculto):
    # Bucle "infinito"
    while (True):
        
        try:
            print("")
            # Nos aseguramos de que sea una variable tipo entero
            num = int(num)
            # Si el valor está dentro del intervalo esablecido
            if (num >= MIN and num <= MAX):
                # El valor es correcto y sale del bucle
                break
            # Si el valor no esta dentro del intervalo
            else:
                print("Uy, has introducido un valor incorrecto.")
                print("Recuerda que tiene que ser un número entre " + str(MIN) + " y " + str(MAX))
                # Si hay que ocultar el numero
                if (oculto):
                    num = getpass.getpass("Inténtalo otra vez :) ")
                # Si no hay que ocultarlo            
                else:
                    num = input("Inténtalo otra vez :) ")
        # Si el valor introducido no es un numero
        except:
            print("Uy, el valor que has introducido no es un número. Inténtalo otra vez :) ")
            if (oculto):
                num = getpass.getpass("Escribe un número entre " + str(MIN) + " y " + str(MAX) + ": ")
            else:
                num = input("Escribe un número entre " + str(MIN) + " y " + str(MAX) + ": ")


    return num # Devuelve el valor correcto


"""  FIN COMPROBACIONES  """
