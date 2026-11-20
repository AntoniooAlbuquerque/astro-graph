import networkx as nx
from pyvis.network import Network


def gerar_visualizacao_interativa(grafo: nx.DiGraph, nome_arquivo: str = "sistema_solar.html") -> None:
    """Renderiza o grafo direcionado em uma pagina HTML interativa via PyVis."""
    net = Network(
        notebook=False,
        directed=True,
        height="850px",
        width="100%",
        bgcolor="#EFE9E9",
        font_color="black"
    )
    net.force_atlas_2based(
        gravity=-120,
        central_gravity=0.015,
        spring_length=150,
        spring_strength=0.1
    )

    for no, dados in grafo.nodes(data=True):
        tipo = dados.get("tipo", "")
        classif = dados.get("classificacao", "")

        if tipo == "Estrela":
            cor, tamanho = "#ff0055", 75
        elif tipo == "Planeta":
            cor, tamanho = "#00bbf9", 45
        elif tipo == "Planeta Anao":
            cor, tamanho = "#00f5d4", 32
        else:
            cor, tamanho = "#fee440", 20

        net.add_node(
            no,
            label=no,
            title=f"Tipo: {tipo}\nClassificacao: {classif}",
            color=cor,
            size=tamanho,
            font={
                "size": 20,
                "face": "Arial",
                "color": "#ffffff",
                "strokeWidth": 2,
                "strokeColor": "#000000"
            }
        )

    for origem, destino in grafo.edges():
        tipo_origem = grafo.nodes[origem].get("tipo", "")
        comprimento = 70 if tipo_origem == "Satelite" else 280
        net.add_edge(
            origem,
            destino,
            arrows="to",
            length=comprimento,
            color={"color": "#555555"},
            width=2.0
        )

    net.save_graph(nome_arquivo)
    print(f"\nArquivo HTML '{nome_arquivo}' gerado com sucesso!")
