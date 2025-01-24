import utils as func;

def round_robin():
    # Entrada de dados
    n = int(input("Quantas tarefas (processos) você deseja simular? "))
    tasks = []
    
    for i in range(n):
        arrival_time = int(input(f"Digite o tempo de ingresso da tarefa {i+1}: "))
        duration = int(input(f"Digite a duração da tarefa {i+1}: "))
        tasks.append({
            'id': i+1,
            'arrival_time': arrival_time,
            'duration': duration,
            'remaining_time': duration,
            'waiting_time': 0,
            'turnaround_time': 0
        })
    
    quantum = int(input("Digite o tempo de quantum (unidades de tempo): "))
    context_switch = input("Você deseja considerar o tempo de troca de contexto? (s/n): ").lower()
    
    if context_switch == 's':
        context_duration = int(input("Digite a duração do tempo de troca de contexto (unidades de tempo): "))
    else:
        context_duration = 0

    func.clean_screen();
    func.loading_simulator(1.0);

    # Simulação do algoritmo Round Robin
    current_time = 0
    queue = []
    completed_tasks = 0
    total_waiting_time = 0
    total_turnaround_time = 0
    
    while completed_tasks < n:
        # Adiciona tarefas que chegaram no tempo atual
        for task in tasks:
            if task['arrival_time'] <= current_time and task not in queue and task['remaining_time'] > 0:
                queue.append(task)

        if queue:
            task = queue.pop(0)

            # Calcula o tempo de execução da tarefa com base no quantum
            exec_time = min(task['remaining_time'], quantum)
            current_time += exec_time

            # Atualiza o tempo restante da tarefa
            task['remaining_time'] -= exec_time
            
            # Se a tarefa não terminou, retorna para a fila
            if task['remaining_time'] > 0:
                queue.append(task)
            else:
                # Tarefa concluída, calcula o tempo de vida e espera
                task['turnaround_time'] = current_time - task['arrival_time']
                task['waiting_time'] = task['turnaround_time'] - task['duration']
                total_waiting_time += task['waiting_time']
                total_turnaround_time += task['turnaround_time']
                completed_tasks += 1

            # Se há tempo de troca de contexto, adiciona ao tempo atual
            if context_duration > 0 and queue:
                current_time += context_duration

        else:
            current_time += 1  # Se não houver tarefa pronta para execução, avança o tempo

    # Exibe os resultados
    print("\nResultados:")
    for task in tasks:
        print(f"Tarefa {task['id']}:")
        print(f"  Tempo de vida: {task['turnaround_time']} u.t")
        print(f"  Tempo de espera: {task['waiting_time']} u.t")
    
    avg_waiting_time = total_waiting_time / n
    avg_turnaround_time = total_turnaround_time / n
    
    print(f"\nTempo médio de espera: {avg_waiting_time:.2f} u.t")
    print(f"Tempo médio de vida: {avg_turnaround_time:.2f} u.t")

if __name__ == "__main__":
    round_robin()