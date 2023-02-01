# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 09:57:13 2023

@author: josuv
"""





def crear_diccionario()-> dict:
    diccionario={
        "robot_r": "Inicio"
        }    
    return diccionario

def leer_archivo(ruta)->None:
    archivo = open(ruta)
    linea = " "
    while(linea != None):
        linea = archivo.readline()
    
        lista_palabras = linea.split(" ")
        diccionario = crear_diccionario()
        for palabra in lista_palabras :
            palabra = palabra.lower()
            if palabra in diccionario:
                t = diccionario[palabra]
            else:
                t = "NO"
        print(t)
    pass

print(leer_archivo("programa.txt"))
    
