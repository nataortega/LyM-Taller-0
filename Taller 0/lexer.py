# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 09:57:13 2023

@author: josuv
"""





def crear_diccionario()-> dict:
    diccionario={
        "robot_r": "Inicio",
       "(": "PARENTESISABIERTO",
       ";": "POINTCOME",
       ",": "COME",
       ":":"dospuntos",
       "[": "SQPARENTESISABIERTO",
       "]": "SQPARENTESISCERRADO",
       "|": "OR",
       #PALABRAS RESERVADAS
       "vars" : "DECLVAR",
       "procs": "PROCEDIMIENTOS",
       'if'       : 'IF',
       'else'     : 'ELSE',
       'while'    : 'WHILE',
       'break'    : 'BREAK',
       'continue' : 'CONTINUE',
       "repeat" : "REPEAT",
       "do": "DO",
       #INSTRUCCIONES
       "put":"PUT",
       "assignto":"ASSIGNTO",
       "goto": "GOTO",
       "move": "CANMOVETOTHE",
       "turn": "CANMOVETOTHE",
       "face": "CANMOVETOTHE",
       "pick": "CANMOVETOTHE",
       "movetothe": "MOVETOTHE",
       "moveindir": "MOVEINDIR",
       "jumptothe": "JUMPTOTHE",
       "jumpindir": "JUMPINDIR",
       "chips": "CHIPS",
       "balloons": "BALLOONS",
       "left": "IZQUIERDA",
       "right": "DERECHA",
       "front": "ADELANTE",
       "back": "ATRAS",
       "west": "OESTE",
       "south": "SUR",
       "north": "NORTE",
       "south": "SUR",
       "east": "ESTE",


       
       
       #condiciones
       "facing": "FACING",
       "canput": "CANPUT",
       "canpick": "CANPICK",
       "canmoveindir": "CANMOVEINDIR",
       "canjumpindir": "CANJUMPINDIR",
       "canmovetothe": "CANMOVETOTHE",
       "canjumptothe": "CANJUMPTOTHE",
       
       
       
        
        }    
    return diccionario



def crear_lista():
    lista = [
        "[","]","(",")",";",",",":","|"," ", ",","\n"]
    return lista

def listanumeros():
    lista = [
        "1","2","3","4","5","6","7","8","9","0"]
    return lista

def leer_archivo(ruta)->None:
    archivo = open(ruta)
    lexer =""
    palabracreada = ""
    lista = crear_lista()
    listanum = listanumeros()
    diccionario = crear_diccionario()
    for linea in archivo :
        linea = " " + linea + " " 
    
    
        for letra in linea :
                    
            if(letra in lista) or (letra in listanum):
                palabracreada = palabracreada.lower()
                if (letra == "[") and ("PROCEDIMIENTOS" in lexer):
                    lexer = lexer + " " + "FUNCTION"
                    lexer = lexer + " " + diccionario[letra]
                    palabracreada = ""
                    
                    
                    
                elif (palabracreada in diccionario) or (letra in diccionario) or (letra in listanum):
                    print(palabracreada)
                    if(palabracreada in diccionario):         
                        lexer = lexer + " " + diccionario[palabracreada] 
                    elif(palabracreada != ""):
                            if(palabracreada in listanum):
                                lexer = lexer + " " + "INT"
                            else:   
                                 lexer = lexer + " " + "var"
                    if letra in listanum:
                        lexer = lexer + " " + "INT"
                    
                    if letra in diccionario:
                        lexer = lexer + " " + diccionario[letra] 
                        # hacer que escriba en un archivo lo que dice el lexer
                    
                    palabracreada = ""
            else:
            
                palabracreada = palabracreada + letra
               
    print(lexer)
    pass



print(leer_archivo("programa.txt"))