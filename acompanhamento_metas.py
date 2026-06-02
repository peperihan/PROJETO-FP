import os
os.system("cls")


def acompanhamento():
    meta_nome=input("DEFINA SUA META: ")


    peso_inicial = float(input("Digite o seu peso atual: "))
    peso_objetivo = float(input("Digite seu peso que você está almejando: "))
    peso_obj_tempo = int(input("Digite em quanto tempo você quer atingir a meta: "))
    peso_final=False

    distancia_percorrida = 0
    distancia_objetivo = float(input("Digite quantos kilometros quer percorrer: "))
    distancia_final = False


    metas={"Meta":
           meta_nome}
    #-------------------------------------
    if peso_inicial > peso_objetivo:
        peso_maior=peso_inicial
        peso_menor=peso_objetivo
    else:
        peso_maior=peso_objetivo
        peso_menor=peso_inicial
    
    diferenca_peso = peso_maior - peso_menor

    if diferenca_peso == 0:
        peso_final = True
        print("Você conseguiu atingir sua meta,PARABÉNS!")
    else:
        print(f"ainda restam {diferenca_peso}Kg a serem perdidos")
    #--------------------------------------------------------------------------------
    while distancia_percorrida < distancia_objetivo:
        nova_distancia = float(input("Quantos kilometros você já percorreu?"))
        diferenca_distancia_parcial = distancia_objetivo - nova_distancia
        print(f"faltam {diferenca_distancia_parcial}Km para atingir sua meta")
        distancia_percorrida = distancia_percorrida + nova_distancia

    if distancia_percorrida == distancia_objetivo:
        distancia_final = True
        print("Você conseguiu atingir sua meta,PARABÉNS!")
    #---------------------------------------------------------------------------
    