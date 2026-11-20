from src.graph_manager import (
    adicionar_astro,
    adicionar_orbita,
    consultar_astro,
    criar_grafo_sistema_solar,
    remover_astro,
    remover_orbita,
)
from src.visualizer import gerar_visualizacao_interativa


def main():
    grafo = criar_grafo_sistema_solar()
    print(f"Grafo inicializado com {grafo.number_of_nodes()} nos e {grafo.number_of_edges()} arestas.")

    while True:
        print("\n--- MENU ASTRO-GRAPH ---")
        print("1. Consultar Astro e Orbitas")
        print("2. Adicionar Novo Astro")
        print("3. Adicionar Nova Orbita")
        print("4. Remover Astro")
        print("5. Remover Orbita")
        print("6. Gerar Visualizacao Interativa (HTML)")
        print("7. Sair")

        opcao = input("Opcao: ").strip()

        if opcao == "1":
            consultar_astro(grafo, input("Astro para busca: "))
        elif opcao == "2":
            nome = input("Nome do astro: ")
            tipo = input("Tipo (Estrela, Planeta, Planeta Anao, Satelite): ")
            classificacao = input("Classificacao: ")
            adicionar_astro(grafo, nome, tipo, classificacao)
        elif opcao == "3":
            origem = input("Astro orbital: ")
            destino = input("Centro gravitacional: ")
            try:
                dist = int(input("Distancia media (km): "))
            except ValueError:
                dist = 0
            adicionar_orbita(grafo, origem, destino, dist)
        elif opcao == "4":
            remover_astro(grafo, input("Nome do astro para remover: "))
        elif opcao == "5":
            origem = input("Astro orbital: ")
            destino = input("Centro gravitacional: ")
            remover_orbita(grafo, origem, destino)
        elif opcao == "6":
            gerar_visualizacao_interativa(grafo)
        elif opcao == "7":
            print("Saindo...")
            break
        else:
            print("Opcao invalida.")


if __name__ == "__main__":
    main()
    