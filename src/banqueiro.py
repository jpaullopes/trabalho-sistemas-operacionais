def banqueiro():
    numero_de_processos = int(input("Digite o número de processos: "))
    numero_de_recursos = int(input("Digite o número de recursos: "))

    # Inicializa as estruturas de dados
    processos = []
    recursos_disponiveis = []

    # Entrada de dados para os recursos disponíveis
    for i in range(numero_de_recursos):
        recursos_disponiveis.append(int(input(f"Digite a quantidade disponível do recurso {i+1}: ")))

    # Entrada de dados para os processos
    for i in range(numero_de_processos):
        processos.append({'recursos': [], 'necessarios': []})
        for j in range(numero_de_recursos):
            processos[i]['recursos'].append(int(input(f"Digite a quantidade de recurso {j+1} alocada ao processo {i+1}: ")))
        for j in range(numero_de_recursos):
            processos[i]['necessarios'].append(int(input(f"Digite a quantidade de recurso {j+1} necessária ao processo {i+1}: ")))

    # Implementação do algoritmo do banqueiro
    marcado = [False] * numero_de_processos

    while True:
        processo_encontrado = False
        for i in range(numero_de_processos):
            # Verifica se o processo pode ser atendido com os recursos disponíveis
            if not marcado[i] and all(processos[i]['necessarios'][j] <= recursos_disponiveis[j] for j in range(numero_de_recursos)):
                # Adiciona os recursos alocados ao processo i aos recursos disponíveis
                for j in range(numero_de_recursos):
                    recursos_disponiveis[j] += processos[i]['recursos'][j]
                marcado[i] = True
                processo_encontrado = True
                break
        
        if not processo_encontrado:
            break

    # Verifica se todos os processos foram atendidos
    if all(marcado):
        print("Todos os processos podem ser atendidos.")
    else:
        print("Nem todos os processos podem ser atendidos.")

# Exemplo de uso
banqueiro()