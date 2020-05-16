#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Elianni Aguero, Angelica Guerrero, Cynthia Quintana
"""


# Ocultar el numero que escribe el JUGADOR 1
import getpass


# Modulo creado para hacer comprobaciones del usuario
import Utiles
import Nivel



"""    
"""
class ModoJuego():
    
    def __init__(self, MINIMO, MAXIMO, intentos):
        # Para comprobar si el jugador ha ganado el juego o no
        # Se inicializa a False
        self._ha_ganado = False
        # En caso de ganar en cuantos intentos
        self._intentos = 0
        
        # Creamos el nivel del juego
        self._nivelJuego = Nivel.Nivel(MINIMO, MAXIMO, intentos)
    
    
    # Método jugar(). Este método será sobreescrito
    # Cada modo de juego funciona de forma distinta
    def jugar(self):
        num = self.inicializarJuego()
        
        intentos = self._nivelJuego.getIntentos()
        
        # Bucle que se repite tantas veces como intentos tenga el jugador
        # Depende de la dificultad del nivel 
        while (intentos > 0):
            # Numero de iteraciones (intentos)
            intentos-=1
            self._intentos = self._nivelJuego.getIntentos() - intentos
            print(" --- Intento nº " + str(self._intentos) + " --- \n")
            
            if (intentos == 0):
                print("Te queda un intento. ¿Quieres que te demos una pista? ")
                p = input("Escribe 'SI' si quieres la pista y 'NO' en caso contrario: ")
                
                if (Utiles.compruebaString(p, "SI", "NO")):
                    print(self.darPista(num))
                
           
            
            aux = input("Escribe un número: ") # El usuario escribe un numero
            # Utiliza el modulo comprobaciones donde se hace una comprobacion del 
            # valor introducido por el usuario. Es decir, si el valor introducido
            # es un numero y si, ademas, esta en el intervalo correcto.
            # Además se le añade el parámetro False o True para saber si es un número 
            # oculto o no
            # Esta funcion compruebaNumero devuelve el numero correcto
            numero = Utiles.compruebaNumero(self._nivelJuego.getMIN(), 
                                            self._nivelJuego.getMAX(), 
                                            aux, 
                                            False)
            
            
            # Si el numero escrito es igual el numero pensado (aleatorio)
            if (numero == num):
                # El jugador ha ganado
                self._ha_ganado = True
                # Se sale del bucle
                break
            
            # Si el numero escrito es mayor que el numero pensado (aleatorio)
            if (numero > num):
                print("Uy :( Has escrito un número mayor que el que he pensado. ", end="")
            # Si el numero escrito es menor que el numero pensado (aleatorio)
            else:
                print("Uy :( Has escrito un número menor que el que he pensado. ", end="")
         
        
            # Si aun quedan intentos se le pide al jugador que lo intente una vez mas
            if (intentos > 0):
                print("Inténtalo de nuevo! \n")
        
        
        # Una vez fuera del bucle se comprueba si el usuario ha ganado o no
        # Si ha ganado
        if (self._ha_ganado):
            # Se le felicita
            print("\nENHORABUENA! Has ganado! :D")
        # Si no ha ganado
        else:
            # Se le muestra al jugador el numero aleatorio que tenia que adivinar
            print("\n\nLo siento. Has agotado todos los intentos :(")
            print("El número que tenías que adivinar era: " + str(num))
            print("Más suerte en la próxima vez")        
        

    def inicializarJuego(self):
        raise NotImplementedError('Tienes que definir el método')


    def darPista(self, num):
        
        aleatorio = Utiles.dameNumAleatorio(1, 3)
        
        if (aleatorio == 1):
            if (num % 3 == 0):
                return "El número es múltiplo de 3\n"
            elif (num % 5 == 0):
                return "El número es múltiplo de 5\n"
            else:
                return "El número no es ni múltiplo de 3 ni de 5\n"
        elif (aleatorio == 2):
            if (num % 2 == 0):
                return "El número es par\n"
            else:
                return "El número es impar\n"
        else:
            return "El número termina en " + str(num % 10) + "\n"
        

    # Devuelve si el jugador ha ganado o no 
    def haGanado(self):
        return self._ha_ganado
    
    # Devuelve el numero de intentos que el jugador ha realizado
    def getNumeroIntentos(self):
        return self._intentos
    
    def getInfoJugadores(self):
        raise NotImplementedError('Método no implementado')
        
        
        
"""
"""
class Solitario(ModoJuego):
    
    def __init__(self, MAX, MIN, nivel):
        ModoJuego.__init__(self, MAX, MIN, nivel)
        # Genera un numero aleatorio, es el numero que se va a adivinar
        self._aleatorio = Utiles.dameNumAleatorio(self._nivelJuego.getMIN(), self._nivelJuego.getMAX())


    def inicializarJuego(self):
        print("He pensado en un número que está entre " + str(self._nivelJuego.getMIN()) + 
              " y " + str(self._nivelJuego.getMAX()) + ". ¿Podrías adivinarlo en " 
              + str(self._nivelJuego.getIntentos()) + " intentos? \n")  
        
        return self._aleatorio

    def getInfoJugadores(self):
        lista = []
        lista.append(Utiles.noCadenaVacia(input("\nEscribe tu nombre: ")).upper())
        return lista

"""
"""
class MultiJugador(ModoJuego):
    
    def __init__(self, MAX, MIN, nivel):
        ModoJuego.__init__(self, MAX, MIN, nivel)


    def inicializarJuego(self):
        print("En esta opción juegan Dos Jugadores. El JUGADOR Nº1 tendrá que introducir "
              + "un número entre " + str(self._nivelJuego.getMIN()) + " y " 
              + str(self._nivelJuego.getMAX()) + ", y el JUGADOR Nº2 tendrá que adivinarlo \n"
              + "Así que allá vamos :)\n")
        print("Turno para el JUGADOR Nº1: ")
        # El primer jugador escribe el numero
        aux = getpass.getpass("Introduce un número entre " + str(self._nivelJuego.getMIN()) + 
              " y " + str(self._nivelJuego.getMAX()) + ".\nNota: El número que vas a introducir no " +
              "se mostrará por pantalla, así tu contrincante no podrá verlo :) ")
        # Se comprueba que el numero introducido es correcto. Es decir, si el valor 
        # introducido es un numero y si, ademas, esta en el intervalo correcto.
        # Además se le añade el parámetro False o True para saber si es un número 
        # oculto o no
        # Esta funcion compruebaNumero devuelve el numero correcto
        num = Utiles.compruebaNumero(self._nivelJuego.getMIN(), 
                                                        self._nivelJuego.getMAX(), 
                                                        aux,
                                                        True)
        print("Muy bien! Vamos a ver si el JUGADOR 2 puede adivinarlo :D \n")
        
        print("---*-*-*-*-*-*-*-*-*-*-*-*-*-*-*--- \n")

        print("Turno para el JUGADOR Nº2: ")
        print("El JUGADOR Nº1 ha pensado en un número entre " + str(self._nivelJuego.getMIN()) + 
              " y " + str(self._nivelJuego.getMAX()) +  " ¿Podrías adivinarlo en " 
              + str(self._nivelJuego.getIntentos()) + " intentos?")

        return num



    def getInfoJugadores(self):
        lista = []
        # Preguntamos el nombre del jugador 1
        # j1 = input("\nJUGADOR Nº1, escribe tu nombre: ").upper()
        j1 = Utiles.noCadenaVacia(input("\nJUGADOR Nº1, escribe tu nombre: ")).upper()
        j2 = Utiles.noCadenaVacia(input("\nJUGADOR Nº2, escribe tu nombre: ")).upper()
        # Guardamos el nombre del jugador 2
        lista.append(j2)
        # Guardamos el nombre del jugador 1
        lista.append(j1)
        return lista

    
    
"""  FIN MODO JUEGO  """
