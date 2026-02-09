import networkx as nx

def carregar_dados():
    """Cria o grafo e adiciona as conexões (arestas)"""
    G = nx.Graph()
    
    # Adicionando relações: (Usuário, Música)
    conexoes = [
        ('Thiago', 'Bohemian Rhapsody'), ('Thiago', 'Imagine'),
        ('Mariana', 'Imagine'), ('Mariana', 'Hotel California'),
        ('Pedro', 'Bohemian Rhapsody'), ('Pedro', 'Back in Black'),
        ('Ana', 'Hotel California'), ('Ana', 'Back in Black')
    ]
    
    G.add_edges_from(conexoes)
    return G

def recomendar(G, usuario_alvo):
    """Encontra músicas baseadas em usuários com gostos similares"""
    if usuario_alvo not in G:
        return "Usuário não encontrado."

    musicas_do_usuario = set(G.neighbors(usuario_alvo))
    sugestoes = {}

    # 1. Ver quem ouve as mesmas músicas que eu
    for musica in musicas_do_usuario:
        for vizinho in G.neighbors(musica):
            if vizinho != usuario_alvo:
                # 2. Ver o que esse vizinho ouve que eu ainda não ouvi
                for musica_vizinho in G.neighbors(vizinho):
                    if musica_vizinho not in musicas_do_usuario:
                        sugestoes[musica_vizinho] = sugestoes.get(musica_vizinho, 0) + 1

    # Ordenar pelas músicas mais recomendadas
    ranking = sorted(sugestoes.items(), key=lambda x: x[1], reverse=True)
    return [musica for musica, peso in ranking]

# --- Execução ---
if __name__ == "__main__":
    grafo_musical = carregar_dados()
    user = "Thiago"
    lista_recomendada = recomendar(grafo_musical, user)
    
    print(f"--- Sistema de Recomendação Musical ---")
    print(f"Usuário alvo: {user}")
    print(f"Sugestões para você: {lista_recomendada}")