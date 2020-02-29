#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Elianni Aguero, Angelica Guerrero, Cynthia Quintana
"""


"""
Clase Nivel
 - Representa los niveles del juego
"""
class Nivel():
    def __init__(self, MIN, MAX, intentos):
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

        

"""  FIN NIVEL JUEGO  """
