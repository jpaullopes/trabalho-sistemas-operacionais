#include <iostream>
#include <cstdlib>
#include <string>
#include <list>

void clearScreen() {
    #ifdef _WIN32
        system("cls");
    #else
        system("clear");
    #endif
}

std::string solicitarAlgoritmo() {
    std::string algoritmo;

    while (true) {
        std::cout << "ALGORITMOS\n";
        std::cout << "1. Circular\n";
        std::cout << "2. Filósofo\n";
        std::cout << "Selecione o Algoritmo: ";
        std::cin >> algoritmo;

        if (algoritmo == "1" || algoritmo == "2") {
            break;
        } else {
            clearScreen();
        }
    }
    return algoritmo;
}

std::list<int> solicitarTempoTarefas() {
    std::list<int> tempos;
    int numTarefas, tempo;

    std::cout << "Quantas Tarefas Você Deseja Inserir? ";
    std::cin >> numTarefas;

    for (int i = 0; i < numTarefas; ++i) {
        std::cout << "Digite o Tempo da Tarefa " << i + 1 << ": ";
        std::cin >> tempo;
        tempos.push_back(tempo);
    }

    return tempos;
}

void mostrarTabelaTarefas(const std::list<int>& tempos) {
    std::cout << "Tabela de Tarefas\n";
    std::cout << "Tarefa | Tempo\n";
    std::cout << "-------|------\n";
    int tarefaNum = 1;
    for (const int& tempo : tempos) {
        std::cout << "T" << tarefaNum << "     | " << tempo << "\n";
        tarefaNum++;
    }
}

int main() {
    std::string algoritmo;
    std::list<int> tempos;

    clearScreen();
    algoritmo = solicitarAlgoritmo();
    tempos = solicitarTempoTarefas();

    mostrarTabelaTarefas(tempos);
        
    return 0;
}