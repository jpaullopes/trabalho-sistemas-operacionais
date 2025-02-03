from collections import deque # Importa a classe deque para a fila de prontos
#tive que importar uma biblioteca para poder usar a função de criar uma filazinha

def round_robin():
    # Entrada
    #A gente pode colocar os dados em um .txt pra agilizar a leitura
    n = int(input("Número de processos: "))
    quantum = int(input("Valor do quantum: "))
    
    usar_contexto = input("Utilizar tempo de troca de contexto? (s/n): ").strip().lower()
    if usar_contexto == 's':
        tempo_contexto = int(input("Tempo de troca de contexto: "))
    else:
        tempo_contexto = 0
    
    # Criação da lista de processos.
    # Cada processo é representado por um dicionário com:
    # id, tempo de chegada, duração, tempo restante,tempo de início e tempo de fim dele.
    processos = []
    for i in range(1, n + 1):
        print(f"\nProcesso {i}:")
        chegada = int(input("  Tempo de chegada: "))
        duracao = int(input("  Duração : "))
        processos.append({
            "id": i,
            "chegada": chegada,
            "duracao": duracao,
            "restante": duracao,
            "inicio": None,
            "fim": None
        })
    
    # Lista de processos que ainda não foram enfileirados
    # Já estão na ordem de criação (o que resolve o critério de desempate pelo id em caso de mesmo tempo de chegada)
    # Essa parte do código é para garantir que os processos sejam enfileirados na ordem correta pra não dar o erro que tava dando antes
    processos_nao_enfileirados = sorted(processos, key=lambda p: (p["chegada"], p["id"]))
    
    tempo_atual = 0
    fila_prontos = deque() # Fila de processos prontos para execução
    
    # Função para inserir processos que chegaram até o tempo_atual na fila de prontos.
    def inserir_processos():
        nonlocal processos_nao_enfileirados, fila_prontos # Acessa as variáveis do escopo externo
        # Obter processos cujo tempo de chegada é <= tempo_atual
        processos_chegaram = [p for p in processos_nao_enfileirados if p["chegada"] <= tempo_atual]
        # Se houverem, adiciona na ordem de chegada (e de id, pois já tão ordenados)
        for p in processos_chegaram:
            fila_prontos.append(p)
        # Remove os processos que foram enfileirados
        processos_nao_enfileirados = [p for p in processos_nao_enfileirados if p["chegada"] > tempo_atual]
    
    print("\n--- Início da simulação ---")
    
    # Loop principal: executa enquanto houver processos com tempo restante
    while any(p["restante"] > 0 for p in processos):
        # Insere na fila os processos que chegaram até o tempo atual
        inserir_processos() # ele vai inserir os processos que chegaram até o tempo atual na fila de prontos
        
        # Se a fila estiver vazia, significa que nenhum processo chegou ainda; avança o tempo
        if not fila_prontos:
            if processos_nao_enfileirados:
                tempo_atual = processos_nao_enfileirados[0]["chegada"]
                inserir_processos()
            else:
                break  # Não há mais processos a serem executados
        
        # Seleciona o próximo processo da fila
        processo_atual = fila_prontos.popleft()
        
        # Registra o tempo de início (primeira vez que o processo é executado)
        if processo_atual["inicio"] is None:
            processo_atual["inicio"] = tempo_atual
        
        # Executa o processo
        #primeiro verifica se pelo menos o processo atual tem tempo restante maior que o quantum 
        if processo_atual["restante"] > quantum:
            # Executa por quantum unidades
            print(f"Tempo {tempo_atual}: Processo {processo_atual['id']} executa por {quantum} unidades")
            tempo_atual += quantum
            processo_atual["restante"] -= quantum
            # Após a execução, insere tempo de troca de contexto, se aplicável
            if tempo_contexto > 0:
                print(f"Tempo {tempo_atual}: Troca de contexto (+{tempo_contexto})")
                tempo_atual += tempo_contexto
        else:
            # Executa pelo tempo restante (processo finaliza)
            tempo_exec = processo_atual["restante"]
            print(f"Tempo {tempo_atual}: Processo {processo_atual['id']} executa por {tempo_exec} unidades e finaliza")
            tempo_atual += tempo_exec
            processo_atual["restante"] = 0
            processo_atual["fim"] = tempo_atual
            # Se ainda existirem processos com tempo restante, inclui troca de contexto
            if any(p["restante"] > 0 for p in processos):
                if tempo_contexto > 0:
                    print(f"Tempo {tempo_atual}: Troca de contexto (+{tempo_contexto})")
                    tempo_atual += tempo_contexto
        
        # Durante a execução, podem ter chegado novos processos:
        inserir_processos()
        
        # Se o processo atual ainda não terminou, reinsere-o na fila de prontos
        if processo_atual["restante"] > 0:
            fila_prontos.append(processo_atual)
    
    print("\n--- Fim da simulação ---\n")
    
    # Exibe os resultados
    print("Processo\tChegada\tDuração\tInício\tFim\tVida\t\tEspera")
    for p in sorted(processos, key=lambda x: x["id"]):
        vida = p["fim"] - p["chegada"]
        espera = vida - p["duracao"]
        print(f"{p['id']}\t\t{p['chegada']}\t{p['duracao']}\t{p['inicio']}\t{p['fim']}\t{vida}\t\t{espera}")

    # Cálculo dos tempos médios de espera e de execução (vida)
    total_espera = sum((p["fim"] - p["chegada"] - p["duracao"]) for p in processos)
    total_vida = sum((p["fim"] - p["chegada"]) for p in processos)
    avg_espera = total_espera / len(processos)
    avg_vida = total_vida / len(processos)
    print('\n--- Médias ---')
    print(f"Tempo médio de vida: {avg_vida:.2f}")
    print(f"Tempo médio de espera: {avg_espera:.2f}")

if __name__ == "__main__":
    round_robin()
