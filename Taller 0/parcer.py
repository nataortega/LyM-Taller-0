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
def reservadasPROCS ():
    diccionario ={
        #PROCEDIEMIENTOS
        "PUT":"PUT",
       "NOP": "NOP",
       "ASSIGNTO":"ASSIGNTO",
       "GOTO": "GOTO",
       "MOVE": "MOVE",
       "TURN": "TURN",
       "FACE": "FACE",
       "PICK": "PICK",
       "MOVETOTHE": "MOVETOTHE",
       "MOVEINDIR": "MOVEINDIR",
       "JUMPTOTHE": "JUMPTOTHE",
       "JUMPINDIR": "JUMPINDIR",

    }
    return diccionario

def reservadasCONDITIONS ():
    diccionario ={
       #CONDICIONES
       "facing": "FACING",
       "canput": "CANPUT",
       "canpick": "CANPICK",
       "canmoveindir": "CANMOVEINDIR",
       "canjumpindir": "CANJUMPINDIR",
       "canmovetothe": "CANMOVETOTHE",
       "canjumptothe": "CANJUMPTOTHE",
       "NOT": "NOT",   

    }
    return diccionario

def reservadasESTRUCTURAS ():
    diccionario ={
       #ESTRCTURA DE CONTROL
       'IF'       : 'IF',
       #'ELSE'     : 'ELSE',
       'WHILE'    : 'WHILE',
       ##'BREAK'    : 'BREAK',
       ##'CONTINUE' : 'CONTINUE',
       "REPEAT" : "REPEAT",
       #"DO": "DO",
       #"THEN" : "THEN",  

    }
    return diccionario

def asignacionESTRUCTURAS(palabra,lista,index):
    respuesta=True
    diccionario=reservadasCONDITIONS()
    otrodiccionario=reservadasPROCS()
    if palabra =="IF":
        
        todobien=True
        while todobien==True:
            if lista[0]!="IF" and lista[1]!="dospuntos":
                todobien=False
            elif lista[3] in diccionario:
                todobien,cont=asignacionCondiciones(lista[3],lista,3)
                index= 3+cont
            elif lista[index]!="THEN" and lista[index+1]!="dospuntos" and lista[index+2]!="SQPARENTESISABIERTO":
                todobien=False
                if lista[index+4] in otrodiccionario:
                    todobien,cont=asignacionPROCS(lista[index+4],lista,index+4)
                    index= index+4+cont
            elif lista[index]!="ELSE" and lista[index+1]!="dospuntos" and lista[index+2]!="SQPARENTESISABIERTO":
                todobien=False
                if lista[index+4] in otrodiccionario:
                    todobien,cont=asignacionPROCS(lista[index+4],lista,index+4)
                    index= index+4+cont
    elif palabra=="WHILE":
        todobien=True
        while todobien==True:
            if lista[0]!="WHILE" and lista[1]!="dospuntos":
                todobien=False
            elif lista[3] in diccionario:
                todobien,cont=asignacionCondiciones(lista[3],lista,3)
                index= 3+cont
            elif lista[index]!="DO" and lista[index+1]!="dospuntos" and lista[index+2]!="SQPARENTESISABIERTO":
                todobien=False
                if lista[index+4] in otrodiccionario:
                    todobien,cont=asignacionPROCS(lista[index+4],lista,index+4)
                    index= index+4+cont
    elif palabra=="REPEAT":
        todobien=True
        while todobien==True:
            if lista[0]!="REPEAT" and lista[1]!="dospuntos" and lista[2]!="INT" and lista[3]!="SQPARENTESISABIERTO":
                todobien=False
                if lista[4] in otrodiccionario:
                    todobien,cont=asignacionPROCS(lista[index+4],lista,index+4)
                    index= index+4+cont



            

def asignacionCondiciones(palabra,lista,index):
    respuesta=True
    if palabra == "FACING":
        nuevalista= []
        cont=1
        while cont <=3:
            nuevalista.append(lista[index])
            index +=1
            cont +=1
        respuesta= facing(nuevalista)
    elif palabra=="CANPUT":
        nuevalista= []
        cont=1
        while cont <=5:
            nuevalista.append(lista[index])
            index +=1
            cont +=1
        respuesta= canput(nuevalista)
    elif palabra=="CANPICK":
        nuevalista= []
        cont=1
        while cont <=5:
            nuevalista.append(lista[index])
            index +=1
            cont +=1
        respuesta= canpick(nuevalista)
    elif palabra=="CANMOVEINDIR":
        nuevalista= []
        cont=1
        while cont <=5:
            nuevalista.append(lista[index])
            index +=1
            cont +=1
        respuesta= canmoveindir(nuevalista)
    elif palabra=="CANJUMPINDIR":
        nuevalista= []
        cont=1
        while cont <=5:
            nuevalista.append(lista[index])
            index +=1
            cont +=1
        respuesta= canjumpindir(nuevalista)
    elif palabra=="CANMOVETOTHE":
        nuevalista= []
        cont=1
        while cont <=5:
            nuevalista.append(lista[index])
            index +=1
            cont +=1
        respuesta= canmovetothe(nuevalista)
    elif palabra=="CANJUMPTOTHE":
        nuevalista= []
        cont=1
        while cont <=5:
            nuevalista.append(lista[index])
            index +=1
            cont +=1
        respuesta= canjumptothe(nuevalista)
    elif palabra=="NOT":
        nuevalista= []
        cont=1
        while cont <=3:
            nuevalista.append(lista[index])
            index +=1
            cont +=1
        respuesta= condnot(nuevalista)
    return respuesta, cont

def asignacionPROCS(palabra,lista,index):
    respuesta=True
    if palabra == "PUT":
        nuevalista= []
        cont=1
        while cont <=6:
            nuevalista.append(lista[index])
            index +=1
            cont +=1
        respuesta= put(nuevalista)
    elif palabra=="NOP":
        nuevalista= []
        cont=1
        while cont <=3:
            nuevalista.append(lista[index])
            index +=1
            cont +=1
        respuesta= nop(nuevalista)
    elif palabra=="ASSIGNTO":
        nuevalista= []
        cont=1
        while cont <=6:
            nuevalista.append(lista[index])
            index +=1
            cont +=1
        respuesta= asignTo(nuevalista)
    elif palabra=="GOTO":
        nuevalista= []
        cont=1
        while cont <=6:
            nuevalista.append(lista[index])
            index +=1
            cont +=1
        respuesta= goTo(nuevalista)
    elif palabra=="MOVE":
        nuevalista= []
        cont=1
        while cont <=4:
            nuevalista.append(lista[index])
            index +=1
            cont +=1
        respuesta= move(nuevalista)
    elif palabra=="TURN":
        nuevalista= []
        cont=1
        while cont <=4:
            nuevalista.append(lista[index])
            index +=1
            cont +=1
        respuesta= turn(nuevalista)
    elif palabra=="FACE":
        nuevalista= []
        cont=1
        while cont <=4:
            nuevalista.append(lista[index])
            index +=1
            cont +=1
        respuesta= face(nuevalista)
    elif palabra=="PICK":
        nuevalista= []
        cont=1
        while cont <=6:
            nuevalista.append(lista[index])
            index +=1
            cont +=1
        respuesta= pick(nuevalista)
    elif palabra=="MOVETOTHE":
        nuevalista= []
        cont=1
        while cont <=6:
            nuevalista.append(lista[index])
            index +=1
            cont +=1
        respuesta= moveToThe(nuevalista)
    elif palabra=="MOVEINDIR":
        nuevalista= []
        cont=1
        while cont <=6:
            nuevalista.append(lista[index])
            index +=1
            cont +=1
        respuesta= moveInDir(nuevalista)
    elif palabra=="JUMPTOTHE":
        nuevalista= []
        cont=1
        while cont <=6:
            nuevalista.append(lista[index])
            index +=1
            cont +=1
        respuesta= jumpToThe(nuevalista)
    elif palabra=="JUMPINDIR":
        nuevalista= []
        cont=1
        while cont <=6:
            nuevalista.append(lista[index])
            index +=1
            cont +=1
        respuesta= jumpInDir(nuevalista)
    return(respuesta,cont)

    


def parcer(traduccion):
    lista =traduccion.lstrip().split(" ")
    diccionario = reservadasPROCS()
    index=0
    respuesta=True
    if lista[0]!="Inicio":
        respuesta=False
        index=len(lista)
    if lista.index("ERROR")!=0:
        respuesta=False
        index=len(lista)
    while index <= len(lista)-1:
        palabra = lista[index]
        
        if index == 1 and palabra =="DECLVAR":
            listica=[]
            #CASO EN EL QUE HAYA VARS (EN CASO DE QUE SI HAYA O NO PROCEDIMIENTOS)
            while lista[index]!="PROCEDIMIENTOS" or lista[index]!="SQPARENTESISABIERTO ":
                listica.append(lista[index])
                index+=1
            respuesta=declvar(listica)
            if respuesta==True:
                index=1+len(listica)
            else:
                index=len(lista)

        #CASO EN EL QUE EXISTE PROCEDIMIENTOS (CASO EN EL QUE HAYA DECLVAR O NO)
        elif palabra =="PROCEDIMIENTOS" and ((lista.index("DECLVAR")!=None and lista.index("DECLVAR")<index)or lista.index("DECLVAR")==None):
            otralistica=[]
            block=False
            while block==False:
                if lista[index]=="SQPARENTESISCERRADO" and lista[index+1]=="SQPARENTESISABIERTO":
                    otralistica.append(lista[index])
                    block=True
                else:
                    otralistica.append(lista[index])
                    index+=1
            respuesta=procs(otralistica)
            if respuesta==True:
                index=1+len(otralistica)
            else:
                index=len(lista)
        elif palabra=="SQPARENTESISABIERTO":
            laotralistica=[]
            block=False
            while block==False:
                if lista[index]=="SQPARENTESISCERRADO":
                    laotralistica.append(lista[index])
                    block=True
                else:
                    laotralistica.append(lista[index])
                    index+=1
            respuesta=procs(laotralistica)
            if respuesta==True:
                index=1+len(laotralistica)
            else:
                index=len(lista)
        elif index==len(lista) and lista[index]!="SQPARENTESISCERRADO":
            respuesta=False



        


    
    return respuesta


#VARS
def declvar(lista):
    respuesta=False
    entreaca=False
    i=1
    while i<=len(lista)-1:
        if i%2==0 and lista[i]=="COMMA":
            respuesta=True
        elif i%2!=0 and lista[i]=="var":
            respuesta=True
        elif i==len(lista)-1 and lista[i]=="SEMICOLON":
            respuesta=True
        else:
            entreaca=True
    if entreaca==True:
        respuesta=False
    return(respuesta)

def procs(lista):
    respuesta=False
    index=1
    procedimientos=[]
    #creacion de procedimientos
    while index<=len(lista):
        procedimiento=[]
        finarreglo=False
        while finarreglo==False:
            if lista[index]=="SQPARENTESISCERRADO" and lista[index+1] in lexer.otroDic:
                finarreglo=True
                procedimiento.append(lista[index])
            else:
                procedimiento.append(lista[index])
                index+=1
        procedimientos.append(procedimiento)
    otroindex=0
    while otroindex<len(procedimientos)-1:

        excepcion=validarProc(procedimientos[otroindex])
        if excepcion==False:
            otroindex=len(procedimientos)
            respuesta=False
        else:
            respuesta=True


    return(respuesta)


def validarProc(procedimiento):
    respuesta=True
    diccionarioestructura= reservadasESTRUCTURAS()
    diccionarioprocs=reservadasPROCS
    if procedimiento[0] not in lexer.otroDic or procedimiento[1]!="SQPARENTESISABIERTO" or procedimiento[2]!="OR":
        respuesta=False
    else:
        index=3
        while index<=len(procedimiento):
            if procedimiento[index]!="OR":
                if index%2==0 and procedimiento[index]!="COMMA":
                    respuesta=False
                    index=len(procedimiento)+1
                elif index%2!=0 and procedimiento[index]!="var":
                    respuesta=False
                    index=len(procedimiento)+1
            index+=1
    if respuesta==True:
        tareas=[]
        while index<=len(procedimiento):
            tarea=[]
            finarreglo=False
            esReservado=False
        
            while finarreglo==False:
                if procedimiento[index] not in diccionarioestructura and esReservado==False:
                    if procedimiento[index] != "SEMICOLON" or procedimiento[index]!="SQPARENTESISCERRADO":
                        tarea.append(procedimiento[index])
                        index+=1
                    else:
                        tarea.append(procedimiento[index])
                        finarreglo=True
                        index+=1        
                        
                else:
                    esReservado=True
                    if procedimiento[index] == "SQPARENTESISCERRADO" or procedimiento[index+1]!="SQPARENTESISCERRADO":
                        tarea.append(procedimiento[index])
                        index+=1
                    else:
                        tarea.append(procedimiento[index])
                        finarreglo=True
                        index+=1 
                       
            tareas.append(tarea)
        unindice=0
        while unindice<len(tareas):
            if tareas[unindice][0] in diccionarioprocs:
                respuesta,cont= asignacionPROCS(tareas[unindice][0],tareas[unindice],0)
            else:
                respuesta,cont=asignacionCondiciones(tareas[unindice][0],tareas[unindice],0)


    return respuesta

 

#PROCEDIMIENTOS
def asignTo(lista):
    
    respuesta=False
    if lista[0]=="ASIGNTO" and lista[1]=="dospuntos" and  lista[2]=="INT" and lista[3]=="COMMA" and lista[4]=="var" and (lista[5]=="SEMICOLON" or lista[5]=="SQPARENTESISCERRADO"):
        respuesta=True
        
    return(respuesta)

def goTo(lista):
    
    respuesta=False
    if lista[0]=="GOTO" and lista[1]=="dospuntos" and (lista[2]=="var" or lista[2]=="INT") and lista[3]=="COMMA" and (lista[4]=="var" or lista[4]=="INT") and (lista[5]=="SEMICOLON" or lista[5]=="SQPARENTESISCERRADO"):
        respuesta=True
        
    return(respuesta)

def move(lista):
    
    respuesta=False
    if lista[0]=="MOVE" and lista[1]=="dospuntos" and (lista[2]=="var" or lista[2]=="INT") and (lista[3]=="SEMICOLON" or lista[3]=="SQPARENTESISCERRADO") :
        respuesta=True
        
    return(respuesta)

def turn(lista):
    
    respuesta=False
    if lista[0]=="TURN" and lista[1]=="dospuntos" and (lista[2]=="IZQUIERA" or lista[2]=="DERECHA" or lista[2]=="AROUND")and (lista[3]=="SEMICOLON" or lista[3]=="SQPARENTESISCERRADO"):
        respuesta=True
        
    return(respuesta)

def face(lista):
    
    respuesta=False
    if lista[0]=="FACE" and lista[1]=="dospuntos" and (lista[2]=="NORTE" or lista[2]=="SUR" or lista[2]=="ESTE" or lista[2]=="OESTE") and (lista[3]=="SEMICOLON" or lista[3]=="SQPARENTESISCERRADO"):
        respuesta=True
        
    return(respuesta)

def put(lista):
    
    respuesta=False
    if lista[0]=="PUT" and lista[1]=="dospuntos" and (lista[2]=="var" or lista[2]=="INT") and lista[3]=="COMMA" and (lista[4]=="BALLOONS" or lista[4]=="CHIPS") and (lista[5]=="SEMICOLON" or lista[5]=="SQPARENTESISCERRADO"):
        respuesta=True
        
    return(respuesta)

def pick(lista):
    
    respuesta=False
    if lista[0]=="PICK" and lista[1]=="dospuntos" and (lista[2]=="var" or lista[2]=="INT")and lista[3]=="COMMA" and (lista[4]=="BALLOONS" or lista[4]=="CHIPS") and (lista[5]=="SEMICOLON" or lista[5]=="SQPARENTESISCERRADO"):
        respuesta=True
        
    return(respuesta)

def moveToThe(lista):
    
    respuesta=False
    if lista[0]=="MOVETOTHE" and lista[1]=="dospuntos" and (lista[2]=="var" or lista[2]=="INT") and lista[3]=="COMMA" and (lista[4]=="ADELANTE" or lista[4]=="DERECHA" or lista[4]=="IZQUIERDA" or lista[4]=="ATRAS") and (lista[5]=="SEMICOLON" or lista[5]=="SQPARENTESISCERRADO"):
        respuesta=True
        
    return(respuesta)

def moveInDir(lista):
    
    respuesta=False
    if lista[0]=="MOVEIDIR" and lista[1]=="dospuntos" and (lista[2]=="var" or lista[2]=="INT") and lista[3]=="COMMA" and (lista[4]=="NORTE" or lista[4]=="SUR" or lista[4]=="ESTE" or lista[4]=="OESTE") and (lista[5]=="SEMICOLON" or lista[5]=="SQPARENTESISCERRADO"):
        respuesta=True
        
    return(respuesta)

def jumpToThe(lista):
    
    respuesta=False
    if lista[0]=="JUMPTOTHE" and lista[1]=="dospuntos" and (lista[2]=="var" or lista[2]=="INT") and lista[3]=="COMMA" and (lista[4]=="ADELANTE" or lista[4]=="DERECHA" or lista[4]=="IZQUIERDA" or lista[4]=="ATRAS") and (lista[5]=="SEMICOLON" or lista[5]=="SQPARENTESISCERRADO"):
        respuesta=True
        
    return(respuesta)

def jumpInDir(lista):
    
    respuesta=False
    if lista[0]=="JUMPINDIR" and lista[1]=="dospuntos" and (lista[2]=="var" or lista[2]=="INT") and lista[3]=="COMMA" and(lista[4]=="NORTE" or lista[4]=="SUR" or lista[4]=="ESTE" or lista[4]=="OESTE") and (lista[5]=="SEMICOLON" or lista[5]=="SQPARENTESISCERRADO"):
        respuesta=True
        
    return(respuesta)

def nop(lista):
    respuesta=False
    if lista[0]=="NOP" and lista[1]=="dospuntos" and (lista[2]=="SEMICOLON" or lista[2]=="SQPARENTESISCERRADO"):
        respuesta=True

    return(respuesta)

def facing(lista):
    respuesta=False
    if lista[0]=="FACING" and lista[1]=="dospuntos" and (lista[2]=="NORTE" or lista[2]=="SUR" or lista[2]=="ESTE" or lista[2]=="OESTE" ):
        respuesta=True
    return respuesta

def canput(lista):
    respuesta=False
    if lista[0]=="CANPUT" and lista[1]=="dospuntos" and (lista[2]=="var" or lista[2]=="INT") and lista[3]=="COMMA" and (lista[4]=="CHIPS" or lista[4]=="BALLONS" ):
        respuesta=True
    return respuesta

def canpick(lista):
    respuesta=False
    if lista[0]=="CANPICK" and lista[1]=="dospuntos" and (lista[2]=="var" or lista[2]=="INT") and lista[3]=="COMMA" and (lista[4]=="CHIPS" or lista[4]=="BALLONS" ):
        respuesta=True
    return respuesta

def canmoveindir(lista):
    respuesta=False
    if lista[0]=="CANMOVEINDIR" and lista[1]=="dospuntos" and (lista[2]=="var" or lista[2]=="INT") and lista[3]=="COMMA" and (lista[4]=="NORTE" or lista[4]=="SUR" or lista[4]=="ESTE" or lista[4]=="OESTE"):
        respuesta=True
    return respuesta

def canjumpindir(lista):
    respuesta=False
    if lista[0]=="CANJUMPINDIR" and lista[1]=="dospuntos" and (lista[2]=="var" or lista[2]=="INT") and lista[3]=="COMMA" and (lista[4]=="NORTE" or lista[4]=="SUR" or lista[4]=="ESTE" or lista[4]=="OESTE"):
        respuesta=True
    return respuesta

def canmovetothe(lista):
    respuesta=False
    if lista[0]=="CANMOVETOTHE" and lista[1]=="dospuntos" and (lista[2]=="var" or lista[2]=="INT") and lista[3]=="COMMA" and (lista[4]=="ADELANTE" or lista[4]=="DERECHA" or lista[4]=="IZQUIERDA" or lista[4]=="ATRAS"):
        respuesta=True
    return respuesta

def canjumptothe(lista):
    respuesta=False
    if lista[0]=="CANJUMPTOTHE" and lista[1]=="dospuntos" and (lista[2]=="var" or lista[2]=="INT") and lista[3]=="COMMA" and (lista[4]=="ADELANTE" or lista[4]=="DERECHA" or lista[4]=="IZQUIERDA" or lista[4]=="ATRAS"):
        respuesta=True
    return respuesta

def condnot(lista):
    respuesta=False
    diccionario= reservadasCONDITIONS
    if lista[0]=="NOT" and lista[1]=="dospuntos" and lista[2] in diccionario:
        respuesta=True
    return respuesta



#print(parcer(lexer.leer_archivo("programa.txt")))
print(parcer(lexer.leer_archivo("programa.txt")))