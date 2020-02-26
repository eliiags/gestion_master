#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 00:52:36 2020

@author: Elianni Aguero, Angelica Guerrero, Cinthya Quintana
"""


# Generar numero aleatorio
import random
# Ocultar el numero que escribe el JUGADOR 1
import getpass



# Modulo creado para hacer comprobaciones del usuario
import Comprobaciones
import NivelJuego



# Variables globales
# Numero de intentos por nivel 
INT_FACIL   = 20
INT_MEDIO   = 12
INT_DIFICIL = 5
# Rango máximo y minimo de numeros a adivinar
MAXIMO      = 1000
MINIMO      = 1 



"""    
"""
class ModoJuego():
    
    def __init__(self, nivel):
        # Para comprobar si el jugador ha ganado el juego o no
        # Se inicializa a False
        self._ha_ganado = False
        # En caso de ganar en cuantos intentos
        self._intentos = 0
        
        # Si el nivel es FACIL
        if (self._nivel == 1):
            self._nivelJuego = NivelJuego.Facil(MAXIMO, MINIMO, INT_FACIL)
        # Si el nivel es MEDIO
        elif (self._nivel == 2):
            self._nivelJuego = NivelJuego.Medio(MAXIMO, MINIMO, INT_MEDIO)
        # Si el nivel es DIFICIL
        else:
            self._nivelJuego = NivelJuego.Dificil(MAXIMO, MINIMO, INT_DIFICIL)
    
    
    # Método jugar(). Este método será sobreescrito
    # Cada modo de juego funciona de forma distinta
    def jugar(self):
        pass

    # Método getNumero(). Este método será sobreescrito
    # Devuelve el numero que habia que adivinar
    def getNumero(self):
        pass

    # Devuelve si el jugador ha ganado o no 
    def haGanado(self):
        return self._ha_ganado
    
    # Devuelve el numero de intentos que el jugador ha realizado
    def getNumeroIntentos(self):
        return self._intentos
    
    

"""
"""
class Solitario(ModoJuego):
    
    def __init__(self, nivel):
        ModoJuego.__init__(self, nivel)
        # Genera un numero aleatorio, es el numero que se va a adivinar
        self._aleatorio = random.randint(self._nivelJuego.getMIN(), self._nivelJuego.getMAX())

    # Método sobreescrito 
    def jugar(self):
        print("He pensado en un número que esta entre " + str(self._nivelJuego.getMIN()) + 
              " y " + str(self._nivelJuego.getMAX()) + ". ¿Podrías adivinarlo en " 
              + str(self._nivelJuego.getIntentos()) + " intentos? \n")
        
        # Bucle que se repite tantas veces como intentos tenga el jugador
        # Depende de la dificultad del nivel 
        while (self._intentos < self._nivelJuego.getIntentos()):
            # Incrementa el numero de iteraciones (intentos)
            self._intentos+=1
            print(" --- Intento nº " + str(self._intentos) + " --- \n")
            aux = input("Escribe un número: ") # El usuario escribe un numero
            # Utiliza el modulo comprobaciones donde se hace una comprobacion del 
            # valor introducido por el usuario. Es decir, si el valor introducido
            # es un numero y si, ademas, esta en el intervalo correcto.
            # Además se le añade el parámetro False o True para saber si es un número 
            # oculto o no
            # Esta funcion compruebaNumero devuelve el numero correcto
            numero = Comprobaciones.compruebaNumero(self._nivelJuego.getMIN(), 
                                                    self._nivelJuego.getMAX(), 
                                                    aux, 
                                                    False)
            
            
            # Si el numero escrito es igual el numero pensado (aleatorio)
            if (numero == self._aleatorio):
                # El jugador ha ganado
                self._ha_ganado = True
                # Se sale del bucle
                break
            # Si el numero escrito es mayor que el numero pensado (aleatorio)
            elif(numero > self._aleatorio):
                print("Uy :( Has escrito un número mayor que el que he pensado. ", end="")
            # Si el numero escrito es menor que el numero pensado (aleatorio)
            else:
                print("Uy :( Has escrito un número menor que el que he pensado. ", end="")
         
        
            # Si aun quedan intentos se le pide al jugador que lo intente una vez mas
            if (self._intentos < self._nivelJuego.getIntentos()):
                print("Inténtalo de nuevo! \n")
        
        
        # Una vez fuera del bucle se comprueba si el usuario ha ganado o no
        # Si ha ganado
        if (self._ha_ganado):
            # Se le felicita
            print("\nENHORABUENA! Has ganado! :D")
        # Si no ha ganado
        else:
            # Se le muestra al jugador el numero aleatorio que tenia que adivinar
            print("\nLo siento. Has agotado todos los intentos :(")
            print("El número que tenías que adivinar era: " + str(self._aleatorio))
            print("Más suerte en la próxima vez")
        
    
    # Se sobreescribe
    def getNumero(self):
        return self._aleatorio
    



"""
"""
class MultiJugador(ModoJuego):
    
    def __init__(self, nivel):
        ModoJuego.__init__(self, nivel)
        # Numero que ha de adivinarse
        self._adivinar = 0
    
    
    # Se sobreescribe
    def jugar(self):
        
        print("JUGADOR Nº1: ")
        # El primer jugador escribe el numero
        aux = getpass.getpass("Introduce un número entre " + str(self._nivelJuego.getMIN()) + 
              " y " + str(self._nivelJuego.getMAX()) + ".\n Nota: El número que vas a introducir no " +
              "se mostrará por pantalla, así tu contrincante no podrá verlo :) ")
        # Se comprueba que el numero introducido es correcto. Es decir, si el valor 
        # introducido es un numero y si, ademas, esta en el intervalo correcto.
        # Además se le añade el parámetro False o True para saber si es un número 
        # oculto o no
        # Esta funcion compruebaNumero devuelve el numero correcto
        self._adivinar = Comprobaciones.compruebaNumero(self._nivelJuego.getMIN(), 
                                                        self._nivelJuego.getMAX(), 
                                                        aux,
                                                        True)
        print("Muy bien! Vamos a ver si el JUGADOR 2 puede adivinarlo :D \n")
        
        print("*-*-*-*-*-*-*-*-*-*-* \n")

        print("JUGADOR Nº2:")
        print("El JUGADOR Nº1 ha pensado en un número entre " + str(self._nivelJuego.getMIN()) + 
              " y " + str(self._nivelJuego.getMAX()) +  "¿Podrías adivinarlo en " 
              + str(self._nivelJuego.getIntentos()) + " intentos?")

        # Bucle que se repite tantas veces como intentos tenga el jugador
        # Depende de la dificultad del nivel 
        while (self._intentos < self._nivelJuego.getIntentos()):
            # Incrementa el numero de iteraciones
            self._intentos+=1
            print(" --- Intento nº " + str(self._intentos) + " ---\n")
            # El usuario escribe un numero
            aux = input("Escribe un número: ")
            # Utiliza el modulo comprobaciones donde se hace una comprobacion del 
            # valor introducido por el usuario. Es decir, si el valor introducido
            # es un numero y si, ademas, esta en el intervalo correcto.
            # Además se le añade el parámetro False o True para saber si es un número 
            # oculto o no
            # Esta funcion compruebaNumero devuelve el numero correcto
            numero = Comprobaciones.compruebaNumero(self._nivelJuego.getMIN(), 
                                                        self._nivelJuego.getMAX(), 
                                                        aux,
                                                        False)
            
            # Si el numero escrito es igual el numero pensado (aleatorio)
            if (numero == self._adivinar):
                # El jugador gana
                self._ha_ganado = True
                # Se sale del bucle
                break
            # SI el numero escrito es mayor que el numero pensado (aleatorio)
            elif(numero > self._adivinar):
                print("Uy :( Has escrito un número mayor que el que he pensado. ", end="")
            # Si el numero escrito es menor que el numero pensado (aleatorio)
            else:
                print("Uy :( Has escrito un número menor que el que he pensado. ", end="")
            
            
            # Si aun quedan intentos se le pide al usuario que lo intente una vez más
            if (self._intentos < self._nivelJuego.getIntentos()):
                print("Inténtalo de nuevo! \n")
        
        # Una vez fuera del bucle se comprueba si el usuario ha ganado o no
        # Si ha ganado
        if (self._ha_ganado):
            print("\nENHORABUENA! Has ganado!\n")
        # Si no ha ganado
        else:
            # Se le muestra al jugador el numero aleatorio que tenia que adivinar
            print("\nLo siento. Has agotado todos los intentos :(")
            print("El número que tenías que adivinar era: " + str(self._adivinar))
            print("Más suerte en la próxima vez\n")
    
    
    # Se sobreescribe      
    def getNumero(self):
        return self._adivinar
        
    
    
"""  FIN MODO JUEGO  """