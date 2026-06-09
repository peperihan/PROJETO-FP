def acompanhar_metas():

    #-------------------------------------------------------
    while True:
        print("Opções de metas:")
        print(" 1. Perder Peso")
        print(" 2. Distância percorrida")
        print(" 3. Ganho de massa muscular")
        print(" 4. Sair")
        escolha = input("\nEscolha a meta que deseja acompanhar: ")

        if escolha == "1":
            #Peso 

            peso_atual = float(input("Digite seu peso atual (em kg): "))
            peso_objetivo = float(input("Digite o peso que quer alcançar (em kg): "))

            while peso_atual != peso_objetivo:
                novo_peso_atual = float(input("Digite seu novo peso atual (em kg): "))
                if novo_peso_atual > peso_objetivo:
                    print(f"Faltam {novo_peso_atual - peso_objetivo:.2f} kg para alcançar seu objetivo de peso.")
                elif novo_peso_atual < peso_objetivo:
                    print(f"Parabéns! Você ultrapassou seu objetivo de peso por {peso_objetivo - novo_peso_atual:.2f} kg!")
                    break
                else:
                    print("Parabéns! Você alcançou seu objetivo de peso!")
                    break
                    
        #---------------------------------------

        elif escolha == "2":
            # Distância

            distancia_atual = 0
            distancia_objetivo = float(input("Digite a distância que quer percorrer (em km): "))

            while distancia_atual != distancia_objetivo:
                nova_distancia_atual = float(input("Digite a distância percorrida até agora (em km): "))
                if nova_distancia_atual < distancia_objetivo:
                    print(f"Faltam {distancia_objetivo - nova_distancia_atual:.2f} km para alcançar seu objetivo de distância.")
                elif nova_distancia_atual > distancia_objetivo:
                    print(f"Parabéns! Você ultrapassou seu objetivo de distância por {nova_distancia_atual - distancia_objetivo:.2f} km!")
                    break
                else:
                    print("Parabéns! Você alcançou seu objetivo de distância!")
                    break
        #---------------------------------------
        elif escolha == "3":
            # Ganho de massa muscular

            massa_atual = float(input("Digite a quantidade de massa muscular que tem atualmente (em kg): "))
            massa_objetivo = float(input("Digite a quantidade de massa muscular que quer alcançar (em kg): "))

            while massa_atual != massa_objetivo:
                nova_massa_atual = float(input("Digite a quantidade de massa muscular ganha até agora (em kg): "))
                if nova_massa_atual < massa_objetivo - massa_atual:
                    print(f"Faltam {massa_objetivo - nova_massa_atual:.2f} kg para alcançar seu objetivo de ganho de massa muscular.")
                elif nova_massa_atual > massa_objetivo - massa_atual:
                    print(f"Parabéns! Você ultrapassou seu objetivo de ganho de massa muscular por {nova_massa_atual - massa_objetivo:.2f} kg!")
                    break
                else:
                    print("Parabéns! Você alcançou seu objetivo de ganho de massa muscular!")
                    break
        elif escolha == "4":
            print("Retornando ao menu principal")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
        #--------------------------------------------
        #Dicionário para armazenar as metas
        metas = {
            "Perder Peso": {},
            "Distância": {},
            "Ganho de Massa Muscular": {}
            }

acompanhar_metas()