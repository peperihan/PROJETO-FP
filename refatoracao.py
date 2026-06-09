def ver_evolucao(banco):
    """
    Exibe o painel de evolução do usuário, incluindo a barra de progresso
    da meta semanal e o resumo dos planos de treino cadastrados.
    """
    print("\n=== ACOMPANHAMENTO DE EVOLUÇÃO ===")

    print("\n--- SUA META SEMANAL ---")
    realizados = banco.get("treinos_feitos_na_semana", 0)
    meta = banco.get("meta_semanal", 1) 
    total_geral = banco.get("total_historico", 0)

    # Prevenção contra divisão por zero (ZeroDivisionError)
    porcentagem = (realizados / meta) * 100 if meta > 0 else 0
    porcentagem = min(porcentagem, 100) # Mantém a barra travada no máximo de 100%

    blocos = int(porcentagem // 10)
    barra = "█" * blocos + "-" * (10 - blocos)

    print(f"Treinos:      {realizados}/{meta}")
    print(f"Progresso:    [{barra}] {porcentagem:.0f}%")
    
    if realizados >= meta:
        print("Status: Meta batida. Parabéns!")
    else:
        print(f"Status: Faltam {meta - realizados} treinos para esta meta.")

    print(f"Histórico: {total_geral} treinos realizados desde o início.")

    print("\n--- SEUS PLANOS DE TREINO ---")
    planos = banco.get("Planos", {})
    print(f"Quantidade de Planos cadastrados: {len(planos)}")

    total_exercicios = 0

    for nome_treino, info in planos.items():
        qtd_ex_neste_treino = len(info.get("Exercícios", []))
        total_exercicios += qtd_ex_neste_treino
        print(f" -> {nome_treino} possui {qtd_ex_neste_treino} exercícios.")

    # Correção do texto: são exercícios cadastrados na base, não praticados
    print(f"\nTotal de exercícios cadastrados na base: {total_exercicios}")
    
    #adc ponte entre aqui e acompanhamento_metas
    print("-" * 30)
    print(" 1. Visualizar Metas Corporais e Corrida")
    print(" 2. Voltar para o Menu Principal")  
    opcao = input("\n> ")

    if opcao == "1":
        from acompanhamento_metas import acompanhar_metas
        acompanhar_metas(banco)
    else:
        print("\nRetornando ao menu principal...")