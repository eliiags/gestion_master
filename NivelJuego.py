#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 00:53:55 2020

@author: Elianni Aguero, Angelica Guerrero, Cinthya Quintana
"""


"""
Clase Nivel
 - Representa los niveles del juego
"""
class Nivel():
    def __init__(self, MAX, MIN, intentos):
        # Numero de intentos del nivel 
        self._n_intentos = intentos
        # Rango Maximo en el cual debe adivinarse el numero
        self._MAX = MAX
        # Rango minimo en el cual debe adivinarse el numero
        self._MIN = MIN
    
    
    # Devuelve el total de intentos del nivel
    def getIntentos(self):
        return self._n_intentos
    
    def setIntentos(self, intentos):
        self._n_intentos = intentos
    
    # Devuelve el rango maximo del numero que ha de adivinarse
    def getMAX(self):
        return self._MAX
    
    def setMAX(self, MAX):
        self._MAX = MAX
    
    # Devuelve el rango minimo del numero que ha de adivinarse
    def getMIN(self):
        return self._MIN 
    
    def setMIN(self, MIN):
        self._MIN = MIN

        

class Facil(Nivel):
    def __init__(self, MAX, MIN, intentos):
        super().__init__(MAX, MIN, intentos)

class Medio(Nivel):
    def __init__(self, MAX, MIN, intentos):
        super().__init__(MAX, MIN, intentos)

class Dificil(Nivel):
    def __init__(self, MAX, MIN, intentos):
        super().__init__(MAX, MIN, intentos)


"""  FIN NIVEL JUEGO  """