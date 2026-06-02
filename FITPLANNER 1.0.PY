import os
from datetime import datetime
from cadastro_exercicios import submenu_exercicios, ver_evolucao
os.system('cls' if os.name == 'nt' else 'clear')

data_atual = datetime.now().strftime("%d/%m/%y %H:%M")

""" 
> o ID vai ser o Índice da lista
> ajustar prints e menu
https://streamlit.io
https://www.gradio.app """



def salvar_dados(banco, nome_arquivo="dados_fitplanner.txt"):
    try:
        with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
            for nome_treino, info in banco["Planos"].items():
                arquivo.write(f"PLANO|{nome_treino}\n")
                for ex in info["Exercícios"]:
                    arquivo.write(f"EXERCICIO|{nome_treino}|{ex['Nome']}|{ex['Séries']}|{ex['Repetições']}|{ex.get('Tempo', '')}|{ex.get('Distância', '')}\n")
                for ex_catalogo in banco["Catalogo_exercicios"]:
                    arquivo.write(f"CATALOGO|{ex_catalogo}\n")
        
        print("\n[!!] Alterações salvas com sucesso! [!!]")
    except Exception as e:
        print(f"\n[ERRO] Não foi possível salvar os dados: {e}")

def carregar_dados(nome_arquivo="dados_fitplanner.txt"):
    banco = {
        "Planos": {},
        "Catalogo_exercicios": [],
        "Metas": [],
        "Histórico": [],
        "Exercícios": [],
        "Acompanhamento":[]

        
    }
    if not os.path.exists(nome_arquivo):
        return banco
    
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                if not linha:
                    continue
                
                partes = linha.split("|")
                
                tipo_linha = partes[0]
                if tipo_linha == "PLANO":
                    nome_treino = partes[1]
                    banco["Planos"][nome_treino] = {
                        "Tipo": [],
                        "Objetivo": [],
                        "Exercícios": []
                    }
                elif tipo_linha == "EXERCICIO":
                    nome_treino = partes[1]
                    nome_ex = partes[2]
                    series = partes[3]
                    repeticoes = partes[4]
                    
                    if nome_treino in banco["Planos"]:
                        banco["Planos"][nome_treino]["Exercícios"].append({
                            "Nome": nome_ex,
                            "Séries": series,
                            "Repetições": repeticoes
                        })
                elif tipo_linha == "CATALOGO":
                    banco["Catalogo_exercicios"].append(partes[1])
        return banco
    except Exception as e:
        print(f"[ERRO] Falha ao ler o arquivo de salvamento: {e}. Criando novo arquivo...")
        return banco
    
def adicionar_plano(banco):
    id_plano = input("Nome do Plano de Treino: ")
    
    if id_plano in banco["Planos"]:
        print("Erro. Plano já existente, por favor, tente novamente!")
        return
    
    banco["Planos"][id_plano] = {
        "nome": id_plano,
        "Data de criação": data_atual,
        "duracao": input("Duração do plano: "),
        "objetivo": input("Objetivo do plano: "),
        "Exercícios": []
    }
    print("Plano adicionado com sucesso!") #abrir cadastro_exercicios.py

def visualizar_plano(banco):
    print("\n====Planos de Treino====")
    if not banco["Planos"]:
        print("Nenhum Plano cadastrado.")
        return

    for id_planos, dados in banco["Planos"].items():
        print(
            f"Nome do Plano de Treino: {id_planos} \n"
            f"Data de Criação: {dados.get("Data de criação", data_atual)} \n"
            f"Duração: {dados["duracao"]}\n"
            f"Objetivo: {dados.get("objetivo", "N/I")}\n"
        )

        print("Exercícios: ")
        if not dados.get("Exercícios"):
            print("[!!] Nenhum exercício cadastrado. [!!]")
        else:
            for i, ex in enumerate(dados["Exercícios"]):
                print(f"{i+1}. {ex['Nome']} - {ex['Séries']}x{ex['Repetições']} (Tempo: {ex.get('Tempo','')} min | Distância: {ex.get('Distância','')} km)")
    print("-"*32)
    print("Opções:")
    print(" 1. Editar informações básicas do plano (Nome, Duração, Objetivo)")
    print(" 2. Gerenciar Exercícios deste plano")
    print(" 3. Voltar ao Menu Principal")
    
    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        id_antigo = input("Digite o nome do plano que deseja atualizar: ")
        if id_antigo in banco["Planos"]:
            item = input("Qual item deseja alterar? (Nome, Duração, Objetivo): ").lower().strip()
            mapeamento_chaves = {
                                "nome": "nome", 
                                 "duração": "duracao", 
                                 "duracao": "duracao", 
                                 "objetivo": "objetivo"
                                 }
            
            if item in mapeamento_chaves:
                chave_real = mapeamento_chaves[item]
                novo_valor = input(f"Novo valor para {item}: ")
                
                if item == "nome":
                    if novo_valor in banco["Planos"]:
                        print("Erro! Já existe um plano com esse nome.")
                        return
                    
                    # Remove o plano com o nome antigo e guarda os dados dele
                    dados_plano = banco["Planos"].pop(id_antigo)
                    
                    # ATENÇÃO: Se o dicionário interno também guardar a chave "nome", atualizamos aqui:
                    if "nome" in dados_plano:
                        dados_plano["nome"] = novo_valor
                        
                    # Insere de volta no banco com o novo nome como chave principal
                    banco["Planos"][novo_valor] = dados_plano
                else:
                    banco["Planos"][id_antigo][chave_real] = novo_valor
                print("Plano atualizado com sucesso!")
            else:
                print("Item inválido.")
        else:
            print("Plano não encontrado.")

    elif opcao == "2":
        plano_escolhido = input("Digite o nome do plano para gerenciar os exercícios: ")
        if plano_escolhido in banco["Planos"]:
            submenu_exercicios(banco, plano_escolhido)
        else:
            print("Plano não encontrado.")

    elif opcao == "3":
        print("Voltando ao menu principal....")
        return
        
    else:
        print("Opção inválida, tente novamente.")

def deletar_plano(banco):
    id_plano = input("Digite o nome do plano que deseja excluir: ")
    if id_plano in banco["Planos"]:
        banco["Planos"].pop(id_plano)
        print(f"Plano: {id_plano} removido.")
    else:
        print("O item solicitado não está no seu plano, tente novamente!")

def escolhas():
    meu_banco = carregar_dados()
    
    while True:
        print("\n--- FitPlanner ---")
        escolha = input(
            "Escolha uma opção:\n"
            " 1. Adicionar Plano de Treino\n"
            " 2. Visualizar/Gerenciar Planos de Treino\n"
            " 3. Acompanhar Evolução\n"
            " 4. Deletar Plano\n"
            " 5. Sair\n> "
        )

        if escolha == "1":
            adicionar_plano(meu_banco)
            salvar_dados(meu_banco)
            
        elif escolha == "2":
            visualizar_plano(meu_banco)
            salvar_dados(meu_banco)
            
        elif escolha == "3":
            ver_evolucao(meu_banco)
            
        elif escolha == "4":
            deletar_plano(meu_banco)
            salvar_dados(meu_banco)
            
        elif escolha == "5":
            print("Agradecemos a preferência, volte sempre!")
            break
        else:
            print("Opção inválida, tente novamente!")

escolhas()