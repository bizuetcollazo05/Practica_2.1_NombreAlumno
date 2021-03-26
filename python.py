#nombre:jose bizuet collazorubio
#carrera:ing.informatica
#materia:desarrollo de app
#ejercicio o practica: 2.1- votos

candidatos=["amarillo","morado","rojo"] #esta es la lista de los candidatos 
contL=[0]*len(candidatos) #aqui  permitimos el voto de los candidatos 

voto=input("ingrese el color del candidato: ") #fin es para terminar los votos
while voto!="fin": #el while lo puse para poder repetir el siclo del votante asta poner fin 
    votoMayus=voto.capitalize()
    if votoMayus in candidatos: #
        pos=candidatos.index(votoMayus)# 
        contL[pos]+=1# aqui ya estoy contalizando un voto
    else:
        print("voto no valid")# este print nos manda un mensaje si hay algun error en los votos si es que ingresan un color incorrecto
    voto=input("ingrese el color del candidato `fin`: ")
cantEst=sum(contL) #aqui se hace la suma 
contMax=max(contL)# aqui se puso el maximo de votos
poscont=contL.index(contMax)# aqui podre encontrar el ganadar de los votos 
gana=candidatos[poscont] #aqui me dara el nombre del ganador 
print("el total de candidatos que votaron fue: {}".format(cantEst))
print("gana: {} con {} votos".format(gana,contMax))