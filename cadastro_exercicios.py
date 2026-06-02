import os
os.system('cls' if os.name == 'nt' else 'clear')

'''
O usuário poderá cadastrar exercícios relacionados a cada treino (como
agachamento, supino, corrida e abdominal), informando séries, repetições,
tempo ou distância.

O menu da gente só aparece quando o usuário selecionar "editar plano de treino" no menu principal.
1- cadastrar exercícios no plano (<mini dicionários! Dicionários em listas)
2- adicionar ao banco de exercícios quando o treino escrito for novo
3- voltar para o menu principal (CRUD)
'''
#receber intrução >adicionar qual exercício?, qual meta?
def submenu_exercicios(banco, plano_escolhido):
    escolha = 0
    while escolha != "x":
        exercicios_plano = banco["Planos"][plano_escolhido]["Exercícios"]
        print(f"==== EDITANDO: {plano_escolhido} ====")
        if len(exercicios_plano) > 0:
            for exercicios, ex in enumerate(exercicios_plano):
                print(f" {exercicios+1}. {ex['Nome']} \t- {ex['Séries']} Séries de {ex['Repetições']}")
            print("1. Adicionar Exercício\n2. Editar Exercício\n3. Excluir Exercício\n4. Salvar\n5. Voltar")
        else:
            print("1. Adicionar Exercício\n\n\n\n2. Voltar")
        escolha = input("> ")
        # -------------     
        if escolha == "1":
            ex_cadastro(banco, plano_escolhido)
            
        elif (escolha =="2" and len(exercicios_plano) ==0) or (escolha =="5" and len(exercicios_plano)>0):
            print("Voltar")
            break
        
        elif escolha =="2":
            print("\n--- Editar Exercício ---")
            try:
                numero = int(input("Digite o número do exercício que deseja editar:\n> "))
                indice = numero - 1
                
                if 0 <= indice <len(exercicios_plano):
                    ex_atual = exercicios_plano[indice]
                    print(f"Editando: {ex_atual['Nome']}")
                    
                    campo = input("Insira o nome do campo que deseja alterar:\n> ").lower()
                    mapa_campos = {
                    "nome": "Nome",
                    "séries": "Séries","series": "Séries",
                    "repetições": "Repetições","repeticoes": "Repetições", 
                    "tempo": "Tempo",
                    "distância": "Distância","distancia": "Distância"
                    }
                    
                    if campo in mapa_campos:
                        chave_real = mapa_campos[campo]
                        novo_valor = input(f"Novo valor para {chave_real}:\n> ")
                        ex_atual[chave_real] = novo_valor
                        print("Exercício atualizado com sucesso!")
                    else:
                        print("[!!] Campo Inválido. [!!]")
                else:
                    print("Número não encontrado na lista.")
            except ValueError:
                print("Por favor, digite apenas números.")
                
        elif escolha =="3":
            print("\n--- Excluir Exercício ---")
            try:
                numero = int(input("Insira número do exercício que deseja excluir:\n> "))
                indice = numero -1
                
                if 0 <= indice < len(exercicios_plano):
                    removido = exercicios_plano.pop(indice)
                    print(f"Exercício '{removido['Nome']}' excluído com sucesso!")
                else:
                    print("Número não encontrado na lista.")
            except ValueError:
                print("Por favor, digite apenas números.")
                
        elif escolha =="4":
            print("--- Dados salvos! ---")
            # O salvamento no bloco de notas (.txt) será feito quando o usuário voltar para o FITPLANNER.
            pass
        else:
            print("Por favor, digite apenas os números indicados.")

def ex_cadastro(banco, plano_escolhido):
    print("=== Novo Exercício ===\n")
    nome = input("Nome do exercício: ")
    series = input("Séries: ")
    repeticoes = input("Repetições: ")
    tempo = input("Tempo (min): ")
    distancia = input("Distância (km): ")
            
    #crando dicionário pro exercício novo:
    exercicio_novo = {
    "Nome": nome,
    "Séries": series,
    "Repetições": repeticoes,
    "Tempo": tempo,
    "Distância": distancia    
    }
    #adicionando o exercício novo na lista do plano escolhido:
    banco["Planos"][plano_escolhido]["Exercícios"].append(exercicio_novo)
    print("\nExercício cadastrado com sucesso!")
    
def ver_evolucao(banco):
    print("\n=== ACOMPANHAMENTO DE EVOLUÇÃO ===")

    print("\n--- SUA META SEMANAL ---")
    realizados = banco.get("treinos_feitos_na_semana", 0)
    meta = banco.get("meta_semanal", 1) 
    total_geral = banco.get("total_historico", 0)

    # Cálculo da porcentagem e barrinha de progresso
    porcentagem = (realizados / meta) * 100
    if porcentagem > 100: porcentagem = 100 # Trava a barra em 100%

    blocos = int(porcentagem // 10)
    barra = "█" * blocos + "-" * (10 - blocos)

    print(f"Treinos: {realizados}/{meta}")
    print(f"Progresso: [{barra}] {porcentagem:.0f}%")
    
    if realizados >= meta:
        print("Status: Meta batida. Parabéns!")
    else:
        print(f"Status: Faltam {meta - realizados} treinos para esta meta.")

    print(f"Histórico: {total_geral} treinos realizados desde o início.")

    print("\n--- SEUS PLANOS DE TREINO ---")
    quantidade_planos = len(banco.get("Planos", {}))
    print(f"Quantidade de Planos cadastrados: {quantidade_planos}")

    total_exercicios = 0

    for nome_treino, info in banco.get("Planos", {}).items():
        qtd_ex_neste_treino = len(info.get("Exercícios", []))
        total_exercicios += qtd_ex_neste_treino
        print(f" -> {nome_treino} possui {qtd_ex_neste_treino} exercícios.")

    print(f"\nTotal de exercícios praticados: {total_exercicios}")
    
    input("\nPressione ENTER para voltar")
