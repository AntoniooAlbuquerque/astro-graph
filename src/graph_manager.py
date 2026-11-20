import networkx as nx
from src.data import astros, conexoes


def criar_grafo_sistema_solar() -> nx.DiGraph:
    """Inicializa e popula o grafo direcionado com os astros e orbitas."""
    grafo = nx.DiGraph()

    for nome, propriedades in astros.items():
        grafo.add_node(nome, **propriedades)

    for origem, destino, dist in conexoes:
        grafo.add_edge(origem, destino, relacao="ORBITA", distancia_km=dist)

    return grafo


def buscar_nome_no(grafo: nx.DiGraph, entrada: str):
    """Localiza o nome exato do no ignorando diferencas de capitalizacao."""
    entrada_lower = entrada.strip().lower()
    for no in grafo.nodes():
        if no.lower() == entrada_lower:
            return no
    return None


def consultar_astro(grafo: nx.DiGraph, nome_entrada: str) -> None:
    nome = buscar_nome_no(grafo, nome_entrada)
    if not nome:
        print("Astro nao encontrado.")
        return

    dados = grafo.nodes[nome]
    print(f"\nNome: {nome}")
    print(f"Tipo: {dados.get('tipo')}")
    print(f"Classificacao: {dados.get('classificacao')}")

    for sucessor in grafo.successors(nome):
        aresta = grafo.get_edge_data(nome, sucessor)
        print(f"Orbita: {sucessor} (Distancia: {aresta['distancia_km']:,} km)")

    satelites = list(grafo.predecessors(nome))
    if satelites:
        print(f"Orbitado por ({len(satelites)}): {', '.join(satelites)}")


def adicionar_astro(grafo: nx.DiGraph, nome: str, tipo: str, classificacao: str) -> None:
    nome_formatado = nome.strip().title()
    if not nome_formatado:
        print("Nome invalido.")
        return
    if buscar_nome_no(grafo, nome_formatado):
        print("Este astro ja existe no grafo.")
        return

    grafo.add_node(nome_formatado, tipo=tipo.strip().title(), classificacao=classificacao.strip().title())
    print(f"Astro '{nome_formatado}' adicionado.")


def adicionar_orbita(grafo: nx.DiGraph, astro_orbital: str, centro: str, distancia_km: int) -> None:
    origem = buscar_nome_no(grafo, astro_orbital)
    destino = buscar_nome_no(grafo, centro)

    if origem and destino:
        grafo.add_edge(origem, destino, relacao="ORBITA", distancia_km=distancia_km)
        print(f"Orbita '{origem} -> {destino}' adicionada.")
    else:
        print("Erro: Um ou ambos os astros nao existem.")


def remover_astro(grafo: nx.DiGraph, nome_entrada: str) -> None:
    nome = buscar_nome_no(grafo, nome_entrada)
    if nome:
        grafo.remove_node(nome)
        print(f"Astro '{nome}' e seus vinculos foram removidos.")
    else:
        print("Astro nao encontrado.")


def remover_orbita(grafo: nx.DiGraph, astro_orbital: str, centro: str) -> None:
    origem = buscar_nome_no(grafo, astro_orbital)
    destino = buscar_nome_no(grafo, centro)

    if origem and destino and grafo.has_edge(origem, destino):
        grafo.remove_edge(origem, destino)
        print(f"Orbita '{origem} -> {destino}' removida.")
    else:
        print("Erro: Relacionamento orbital nao encontrado.")
