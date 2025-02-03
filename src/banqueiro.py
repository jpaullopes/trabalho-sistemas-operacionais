def is_safe_state(disponivel, alocado, precisa):
    """
    Verifica se o sistema está em estado seguro e retorna a sequência segura.

    Parâmetros:
      disponivel: lista com a quantidade disponível de cada recurso.
      alocado: matriz (lista de listas) com a alocação atual de cada processo.
      precisa: matriz (lista de listas) informada pelo usuário, representando a necessidade
            de recursos para que cada processo finalize sua execução.
    
    Retorna:
      (True, safe_sequence) se o estado for seguro, ou (False, []) se não for.
    """
    n_processos = len(alocado)
    n_recursos = len(disponivel)
    
    work = disponivel.copy()
    finish = [False] * n_processos
    safe_sequence = []
    
    while True:
        found = False
        for i in range(n_processos):
            if not finish[i] and all(precisa[i][j] <= work[j] for j in range(n_recursos)):
                # Simula a finalização do processo i e libera seus recursos
                for j in range(n_recursos):
                    work[j] += alocado[i][j]
                finish[i] = True
                safe_sequence.append(i)
                found = True
        if not found:
            break

    if all(finish):
        return True, safe_sequence
    else:
        return False, []


def main():
    print("Algoritmo do Banqueiro - Sequência de Execução (precisa informado pelo usuário)")
    
    # Entrada de dados
    n_processos = int(input("Número de processos: "))
    n_recursos = int(input("Número de tipos de recursos: "))
    
    # Disponivél: quantidade disponível de cada recurso
    print("\nDigite o vetor de recursos disponíveis (separados por espaço):")
    disponivel = list(map(int, input().split()))
    if len(disponivel) != n_recursos:
        print("Erro: O número de valores informados no vetor 'Disponivél' não corresponde ao número de tipos de recursos.")
        return
    
    # Matrizes alocado e precisa
    alocado = []
    precisa = []
    
    for i in range(n_processos):
        print(f"\nProcesso {i + 1}:")
        print("  Digite a alocação atual (separados por espaço):")
        alloc = list(map(int, input().split()))
        if len(alloc) != n_recursos:
            print("Erro: número de valores na alocação inválido.")
            return
        alocado.append(alloc)
        
        print("  Digite o precisa (necessidade) de recursos (separados por espaço):")
        recursos_necessarios = list(map(int, input().split())) 
        if len(recursos_necessarios) != n_recursos:
            print("Erro: número de valores no precisa inválido.")
            return
        precisa.append(recursos_necessarios)
    
    # Exibe o estado atual dos processos
    print("\nEstado Atual:")
    print("Processo\tAlocado\t\tRequisição")
    for i in range(n_processos):
        print(f"P{i + 1}\t\t{alocado[i]}\t{precisa[i]}")
    print("\nRecursos disponíveis: ")
    print(f"Disponivél: {disponivel}")
    
    # Verifica o estado seguro e exibe a sequência de execução
    seguro, safe_sequence = is_safe_state(disponivel, alocado, precisa)
    if seguro:
        print("\nO sistema está em estado seguro.")
        print("A ordem de execução (sequência segura) dos processos é:")
        print(" -> ".join([f"P{pid+1}" for pid in safe_sequence]))
    else:
        print("\nO sistema NÃO está em estado seguro. Não há uma sequência de execução segura que permita a finalização de todos os processos.")


if __name__ == "__main__":
    main() # a main né
