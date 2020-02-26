#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 00:53:55 2020

@author: Elianni Aguero, Angelica Guerrero, Cinthya Quintana
"""


# Comprobar si el fichero existe
import os
# Para guardar los datos en EXCEL 
from openpyxl import Workbook
import openpyxl
# Graficos
#from IPython import get_ipython
#get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as grafico
# Para el abecedario 
from string import ascii_uppercase


import ModoJuego
import Comprobaciones


# Variables globales
# Ruta y nombre del fichero
FICHERO_PARTIDAS = '/home/eli/MASTER/DATOS/partidas.xlsx'




class Menu():
    def __init__(self):
        # Opcion modo juego
        self._opcionModo  = 0
        # Opcion nivel 
        self._opcionNivel = 0
        # Si el jugador ya existe en la BBDD
        self._existe = False
        self._pos    = 0
        # Se guardarán los datos del jugador para actualizarlos
        self._listaPuntos = ""


    # Mostramos el menu del modo del juego
    def muestraMenuModoJuego(self):
        print("\n¿Cómo quieres jugar?")
        print("1. Partida modo solitario")
        print("2. Partida 2 Jugadores")
        print("3. Estadística")
        print("4. Salir \n")


    # Mostramos el menu del nivel del juego (F, M, D)
    def muestraMenuNivelJuego(self):
        print("selecciona el nivel del juego")
        print("1. Fácil (20 intentos)")
        print("2. Medio (12 intentos)")
        print("3. Difícil (5 intentos) \n")
        
        
    # Comprobamos que la opcion seleccionada es valida
    # La variable "menu" contiene el indicador de si es menu de 
    # - 1 modo o 
    # - 2 nivel
    def opcionSeleccionada(self, n1, n2):
        opcion = input("Selecciona una de las opciones anteriores: ")
        # Se comprueba que el numero introducido es correcto. Es decir, si el valor 
        # introducido es un numero y si, ademas, esta en el intervalo correcto.
        # Además se le añade el parámetro False o True para saber si es un número 
        # oculto o no
        # Esta funcion compruebaNumero devuelve el numero correcto
        return Comprobaciones.compruebaNumero(n1, n2, opcion, False)
    
    
     
    # Accede al fichero excel y comprueba el nombre del jugador
    # Si el jugador existe recoge sus datos
    # Si no existe crea uno nuevo y pone toda la info a 0 
    def compruebaBBDD(self):
        # El usuario escribe su nombre
        nombre = input("\nEscribe tu nombre: ")
      
        fichero = ""
        # Comprueba si el fichero ya existe
        if os.path.exists(FICHERO_PARTIDAS):
            # Abrimos el fichero para comprobar si el jugador ya existe
            fichero = openpyxl.load_workbook(FICHERO_PARTIDAS)
            hoja    = fichero.active
            # Recorremos toda las filas comprobando si el usuario esta en la BBDD
            while (self._pos < hoja.max_row):
                self._pos+=1 # Incrementamos el contador
                # Si el jugador existe
                if (hoja['A%d' %(self._pos)].value == nombre.upper()):
                    # Se actualiza la variable
                    self._existe = True
                    # Salimos del bucle
                    break

        # Si el fichero no existe 
        else:
            # lo creamos
            wb = Workbook()
            # Lo guardamos
            wb.save(FICHERO_PARTIDAS)
        
        
        # Recogemos la informacion
        # Si el jugador existe
        if (self._existe):
            # Ultima letra del excel
            letra = ascii_uppercase[hoja.max_column-1]
            # Actualizamos la lista de info del usuario que esta en la posicion pos
            fila = hoja["A"+str(self._pos)+":"+str(letra)+str(self._pos)]
            self._listaPuntos = []
            for f in fila:
                for valor in f:
                    self._listaPuntos.append(valor.value)
        # Sino existe
        else:
            # Creamos las lista con valores iniciales
            # NOMBRE | GANADAS | PERDIDAS | FACIL | MEDIO | DIFICIL | 
            # MEJOR_F | MEJOR_M | MEJOR_D
            self._listaPuntos = [nombre.upper(), 0, 0, 0, 0, 0, "-", "-", "-"]


    # Se actualiza la info de la partida        
    def actualizaBBDD(self):
        
        # Abrimos el fichero 
        fichero = openpyxl.load_workbook(FICHERO_PARTIDAS)
        hoja    = fichero.active
      
        # SI el usuario existe
        if (self._existe):
            # Ultima letra del excel
            j=0
            for valor in self._listaPuntos:
                # Actualizamos la lista de info del usuario
                hoja[str(ascii_uppercase[j])+str(self._pos)].value = valor
                j+=1
            
        # Si el usuario no existe
        else:
            # Se anade al final de la lista
            hoja.append(self._listaPuntos)
            
        # Se guarda el fichero
        fichero.save(FICHERO_PARTIDAS)
    
    
    # Desarrollo del juego
    def empiezaElJuego(self):
        
        juego = ""
        # Segun la opcion crea el tipo de juego
        if (self._opcionModo == 1):
            # MODO SOLITARIO 
            # Se le pasa el nivel seleccionado por el usuario
            juego = ModoJuego.Solitario(int(self._opcionNivel))
        elif(self._opcionModo == 2):
            # MODO MULTIJUGADOR
            # Se le pasa el nivel seleccionado por el usuario
            juego = ModoJuego.MultiJugador(int(self._opcionNivel))
        
        
        # the game is on
        juego.jugar()
        
        # Cuando finaliza el juego
        # Comprobamos que si el jugador ya existe en la BBDD
        # Recogemos la informacion sobre el mismo 
        self.compruebaBBDD()
        
        
        # Se actualiza la informacion del jugador sea nuevo o no
        # SI HA GANADO
        if (juego.haGanado()):
            # Actualizamos la partida ganada
            aux = self._listaPuntos[1]
            self._listaPuntos[1] = aux + 1
           
            # Si ha sido un nivel FACIL
            if (self._opcionNivel == 1):
                aux = self._listaPuntos[3]
                self._listaPuntos[3] = aux + 1
                # Se actualiza el mejor numero de intentos
                if (self._listaPuntos[6] == "-" or
                    self._listaPuntos[6] > juego.getNumeroIntentos()):
                    self._listaPuntos[6] = juego.getNumeroIntentos()
                
            # Si ha sido un nivel MEDIO
            elif(self._opcionNivel == 2):
                aux = self._listaPuntos[4]
                self._listaPuntos[4] = aux + 1
                # Se actualiza el mejor numero de intentos
                if (self._listaPuntos[7] == "-" or
                    self._listaPuntos[7] > juego.getNumeroIntentos()):
                    self._listaPuntos[7] = juego.getNumeroIntentos()
          
            # Si ha sido un nivel DIFICIL
            else:
                aux = self._listaPuntos[5]
                self._listaPuntos[5] = aux + 1
                # Se actualiza el mejor numero de intentos
                if (self._listaPuntos[8] == "-" or
                    self._listaPuntos[8] > juego.getNumeroIntentos()):
                    self._listaPuntos[8] = juego.getNumeroIntentos()
        
        # SI HA PERDIDO
        else:
            # Actualizamos la partida perdida
            aux = self._listaPuntos[2]
            self._listaPuntos[2] = aux + 1
    
        
        ## Se actualiza la BBDD
        self.actualizaBBDD()
    
    
    
    # Muestra un gráfico con las estadísticas del usuario
    def mostrarEstadisticas(self):
        
        # Busca al usuario en la BBDD
        self.compruebaBBDD()
        
        # Si el jugador existe
        if (self._existe): 
        
            print("\nEstadísticas de: " + self._listaPuntos[0])
            
            x = ["Partidas ganadas","Partidas perdidas"]
            y = [self._listaPuntos[1], self._listaPuntos[2]]
            grafico.bar(x, y)
            grafico.title("Informacion del juego")
            grafico.show()
            
            print("\n")
            
            x = ["Fácil","Medio", "Difícil"]
            y = [self._listaPuntos[3], self._listaPuntos[4], self._listaPuntos[5]]
            grafico.bar(x, y)
            grafico.title("Partidas ganadas por dificultad del nivel")
            grafico.show()
        else:
            print("\nNunca has jugado a ADIVINA EL NUMERO, " + 
                  "por lo que no tenemos estadísticas para mostrarte. " +
                  "¿Te animas a jugar una partida?\n ")
    
    
    
    def menu(self):

        # Saludo de bienvenida
        print("Bienvenido a 'ADIVINA EL NÚMERO'")
        
        while(True):
            ### Muestra el menu del Modo de Juego ###
            self.muestraMenuModoJuego()
            # Actualiza la opcion del juego
            self._opcionModo = self.opcionSeleccionada(1, 4)
            
            # Opcion Estadistica
            if (self._opcionModo == 3):
                self.mostrarEstadisticas()
            # Salir del juego
            elif (self._opcionModo == 4):
                print("Hasta la próxima! :)")
                break
            # Modo jugar
            else:
                print("Muy bien! Has seleccionado la opción ", end="")
                if (self._opcionModo == 1):
                    print("Modo Solitario. Ahora ", end="")
                else:
                    print("Dos Jugadores. Ahora ", end="")
            
                # Muestra el menu del Nivel de Juego
                self.muestraMenuNivelJuego()
                # Actualiza la opcion nivel de juego
                self._opcionNivel = self.opcionSeleccionada(1, 3)
            
                # The game is on :)
                self.empiezaElJuego()
            
            # Volvemos a establecer los valores a predeterminados
            self._existe = False
            self._pos    = 0
            self._listaPuntos = ""
    
    
    
    
    
if __name__ == '__main__':
    juego = Menu()
    juego.menu()


