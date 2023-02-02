# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 09:57:13 2023

@author: josuv
"""


def crear_diccionario()-> dict:
    diccionario={
        "robot_r": "Inicio",
        "(": "PARENTESIS",
        "VARS" : "Variable"
        
        }    
    return diccionario

def leer_archivo(ruta)->None:
    archivo = open(ruta)
    linea= ""
    for linea in archivo:
        print(linea)
        diccionario = crear_diccionario()
        palabracreada=""
        lexer = ""
        for letra in linea :
                
                if((letra == " ") or (letra == "\n") or(letra == "(")) :
                    if (palabracreada != "\n"):
                        palabracreada = palabracreada.lower()
                        if(palabracreada in diccionario):               
                            lexer = lexer + " " + diccionario[palabracreada] 
                        else:
                            lexer = lexer + " var"
                        if(letra == "("):
                            lexer = lexer + " " + diccionario[letra] 
                    # hacer que escriba en un archivo lo que dice el lexer
                    palabracreada = ""
                else:
                    palabracreada = palabracreada + letra
        print(lexer)
    pass
print(leer_archivo("programa.txt"))
    
