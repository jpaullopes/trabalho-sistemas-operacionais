def calcula_need(max_demand, allocation):
    """
    Calcula a matriz need, que representa a necessidade de recursos de cada processo.
    need[i][j] = max_demand[i][j] - allocation[i][j]
    """
    n_processos = len(max_demand)
    n_recursos = len(max_demand[0])
    need = [[0] * n_recursos for _ in range(n_processos)]
    for i in range(n_processos):
        for j in range(n_recursos):
            need[i][j] = max_demand[i][j] - allocation[i][j]
    return need


def is_safe_state(available, max_demand, allocation):
    """
    Verifica se o sistema está em um estado seguro utilizando o Algoritmo do Banqueiro.
    
    Parâmetros:
      - available: lista com a quantidade disponível de cada recurso.
      - max_demand: matriz (lista de listas) que indica o máximo de recursos que cada processo pode solicitar.
      - allocation: matriz (lista de listas) que indica os recursos atualmente alocados a cada processo.
    
    Retorna:
      - (True, safe_sequence) se o sistema estiver em estado seguro, onde safe_sequence é a sequência segura.
      - (False, safe_sequence) caso contrário.
    """
    n_processos = len(max_demand)
    need = calcula_need(max_demand, allocation)
    
    finish = [False] * n_processos
    work = available.copy()
    safe_sequence = []
    
    while True:
        encontrado = False
        for i in range(n_processos):
            if not finish[i]:
                # Verifica se as necessidades do processo i podem ser satisfeitas com os recursos disponíveis
                if all(need[i][j] <= work[j] for j in range(len(work))):
                    # Se sim, o processo pode terminar, liberando seus recursos
                    for j in range(len(work)):
                        work[j] += allocation[i][j]
                    finish[i] = True
                    safe_sequence.append(i)
                    encontrado = True
        if not encontrado:
            break  # Nenhum processo adicional pode ser finalizado neste momento
    
    if all(finish):
        return True, safe_sequence
    else:
        return False, safe_sequence


def request_resources(process_id, request, available, max_demand, allocation):
    """
    Processa um pedido de recursos por um processo específico.
    
    Parâmetros:
      - process_id: índice do processo que está solicitando recursos.
      - request: lista com a quantidade de cada recurso solicitada.
      - available: lista com a quantidade disponível de cada recurso.
      - max_demand: matriz que indica o máximo de recursos que cada processo pode solicitar.
      - allocation: matriz que indica os recursos atualmente alocados a cada processo.
    
    Retorna:
      - True se o pedido for concedido (mantém o sistema em estado seguro).
      - False caso contrário.
    """
    n_recursos = len(available)
    
    # Cálculo da matriz need
    need = calcula_need(max_demand, allocation)
    
    # Verifica se o pedido é menor ou igual à necessidade
    if any(request[j] > need[process_id][j] for j in range(n_recursos)):
        print("Erro: o processo excede sua necessidade máxima.")
        return False
    
    # Verifica se o pedido é menor ou igual aos recursos disponíveis
    if any(request[j] > available[j] for j in range(n_recursos)):
        print("Recursos insuficientes disponíveis no sistema.")
        return False
    
    # Simula a alocação temporária dos recursos solicitados
    available_temp = available.copy()
    allocation_temp = [row.copy() for row in allocation]
    for j in range(n_recursos):
        available_temp[j] -= request[j]
        allocation_temp[process_id][j] += request[j]
    
    # Verifica se o sistema permanecerá em estado seguro após a alocação
    seguro, seq = is_safe_state(available_temp, max_demand, allocation_temp)
    if seguro:
        # Se seguro, atualiza o estado real
        for j in range(n_recursos):
            available[j] = available_temp[j]
            allocation[process_id][j] = allocation_temp[process_id][j]
        print(f"Pedido concedido. Sequência segura: {seq}")
        return True
    else:
        print("Pedido negado. O sistema não permanecerá em estado seguro.")
        return False


# Exemplo de uso
if __name__ == "__main__":
    # Exemplo de dados para 5 processos e 3 tipos de recursos
    available = [3, 3, 2]

    max_demand = [
        [7, 5, 3],  # Processo 0
        [3, 2, 2],  # Processo 1
        [9, 0, 2],  # Processo 2
        [2, 2, 2],  # Processo 3
        [4, 3, 3]   # Processo 4
    ]

    allocation = [
        [0, 1, 0],  # Processo 0
        [2, 0, 0],  # Processo 1
        [3, 0, 2],  # Processo 2
        [2, 1, 1],  # Processo 3
        [0, 0, 2]   # Processo 4
    ]

    # Verifica estado seguro atual
    seguro, safe_sequence = is_safe_state(available, max_demand, allocation)
    if seguro:
        print("O sistema está em estado seguro.")
        print("Sequência segura:", safe_sequence)
    else:
        print("O sistema NÃO está em estado seguro.")

    # Exemplo de pedido de recurso: o processo 1 solicita [1, 0, 2]
    processo_id = 1
    request = [1, 0, 2]
    print(f"\nProcesso {processo_id} solicita os recursos: {request}")
    request_resources(processo_id, request, available, max_demand, allocation)

    # Após a alocação (caso o pedido seja concedido), imprime o novo estado disponível
    print("\nEstado disponível após o pedido:", available)
