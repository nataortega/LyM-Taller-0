"""
Reglas:
1) Primera palabra debe ser ROBOT_R
2) Declaracion d variables con VARS
3) Variables separadas por coma, terminada la declaracion punto y coma
4) Declaracion de procedimientos con PROCS
5) Despues del nombre del procedimiento [ y para cerrarlo ]
6) Cada procedimiento separado por ;
7) Variables de un procedimieto entre||
8) asignTo: parametro int,var
9) goTo: parametros int o var,int o var
10) move: parametro int o variable
11) turn: parametro left right o around
12) face: parametro norte sur este o oeste
13) put: parametros int o var, balloons o chips
14) pick: parametros int o var, balloons o chips
15) moveToThe: parametros int o var, front o right o left o back
16) moveInDir: parametros int o var, norte sur este o oeste
17) jumpToThe: parametros int o var, front o right o left o back
18) jumpInDir: parametros int o var, norte sur este o oeste
19) nop no tiene restriccion
20) Para iniciar un procedimiento se colocan : y los parametros estan separados por ,
21) if : condicion then: [procedimiento] else: [procedimiento] (a menos de que se nop)
22) while: condicion do: [procedimiento]
23) repeat: itt o var [procedimiento]
Condiciones
24) facing: parametro norte sur este o oeste
25) canPut: parametros int o var, chips o balloons
26) canPick: parametros int o var, chips o balloons
27) canMoveToThe: parametros int o var, front o right o left o back
28) canMoveInDir: parametros int o var, norte sur este o oeste
29) canJumpToThe: parametros int o var, front o right o left o back
30) canJumpInDir: parametros int o var, norte sur este o oeste
31) not condicion
"""

import lexer

def parcer(traduccion):
    lista =traduccion.lstrip().split(" ")
    
    print(lista )

def asignTo(lista):
    
    respuesta=False
    if lista[0]=="dospuntos" and  lista[1]=="INT" and lista[3]=="var" and lista[2]=="COME":
        respuesta=True
        
    return(respuesta)

def goTo(lista):
    
    respuesta=False
    if lista[0]=="dospuntos" and (lista[1]=="var" or lista[1]=="INT") and (lista[3]=="var" or lista[3]=="INT") and lista[2]=="COME":
        respuesta=True
        
    return(respuesta)

def move(lista):
    
    respuesta=False
    if lista[0]=="dospuntos" and (lista[1]=="var" or lista[1]=="INT") :
        respuesta=True
        
    return(respuesta)

def turn(lista):
    
    respuesta=False
    if lista[0]=="dospuntos" and (lista[1]=="left" or lista[1]=="right" or lista[1]=="around"):
        respuesta=True
        
    return(respuesta)

def face(lista):
    
    respuesta=False
    if lista[0]=="dospuntos" and (lista[1]=="norte" or lista[1]=="sur" or lista[1]=="este" or lista[1]=="oeste"):
        respuesta=True
        
    return(respuesta)

def put(lista):
    
    respuesta=False
    if lista[0]=="dospuntos" and (lista[1]=="var" or lista[1]=="INT") and (lista[3]=="balloons" or lista[3]=="chips") and lista[2]=="COME":
        respuesta=True
        
    return(respuesta)

def pick(lista):
    
    respuesta=False
    if lista[0]=="dospuntos" and (lista[1]=="var" or lista[1]=="INT") and (lista[3]=="balloons" or lista[3]=="chips") and lista[2]=="COME":
        respuesta=True
        
    return(respuesta)

def moveToThe(lista):
    
    respuesta=False
    if lista[0]=="dospuntos" and (lista[1]=="var" or lista[1]=="INT") and (lista[3]=="front" or lista[3]=="right" or lista[3]=="left" or lista[3]=="back") and lista[2]=="COME":
        respuesta=True
        
    return(respuesta)

def moveInDir(lista):
    
    respuesta=False
    if lista[0]=="dospuntos" and (lista[1]=="var" or lista[1]=="INT") and (lista[3]=="norte" or lista[3]=="sur" or lista[3]=="este" or lista[3]=="oeste") and lista[2]=="COME":
        respuesta=True
        
    return(respuesta)

def jumpToThe(lista):
    
    respuesta=False
    if lista[0]=="dospuntos" and (lista[1]=="var" or lista[1]=="INT") and (lista[3]=="front" or lista[3]=="right" or lista[3]=="left" or lista[3]=="back") and lista[2]=="COME":
        respuesta=True
        
    return(respuesta)

def jumpInDir(lista):
    
    respuesta=False
    if lista[0]=="dospuntos" and (lista[1]=="var" or lista[1]=="INT") and (lista[3]=="norte" or lista[3]=="sur" or lista[3]=="este" or lista[3]=="oeste") and lista[2]=="COME":
        respuesta=True
        
    return(respuesta)

#print(parcer(lexer.leer_archivo("programa.txt")))
print(parcer(lexer.leer_archivo("programa.txt")))