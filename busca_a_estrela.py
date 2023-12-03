import heapq

def estimativa_custo_heuristico(inicio, objetivo):
    #calcula a distancia de pontos entre o inicio e objetivo
    return abs(objetivo[0] - inicio[0]) + abs(objetivo[1] - inicio[1])

def busca_a_estrela(mapa, inicio, objetivo):
    conjunto_aberto = [] #nos que vão ser verificados
    conjunto_fechado = set() #nos que foram vistos
    heapq.heappush(conjunto_aberto, (0, inicio, []))

    while conjunto_aberto:
        custo_atual, no_atual, caminho_atual = heapq.heappop(conjunto_aberto)

        #verifica o no atual é o no de destino se for retorna o caminho percorrido até agora e o custo acumulado
        if no_atual == objetivo:
            return caminho_atual + [no_atual], custo_atual

        if no_atual in conjunto_fechado:
            continue

        conjunto_fechado.add(no_atual)

        for vizinho in vizinhos(no_atual, mapa):
            novo_custo = custo_atual + mapa[vizinho[0]][vizinho[1]]  # calcula p chegar ao vizinho

            #verifica se vizinho foi visitado
            if vizinho not in conjunto_fechado:
                heapq.heappush(conjunto_aberto, (novo_custo + estimativa_custo_heuristico(vizinho, objetivo), vizinho, caminho_atual + [no_atual]))
    
    #caminho n entrontrado
    return None, 0  

def calcular_esforco(caminho, mapa):
    esforco = sum(mapa[no[0]][no[1]] for no in caminho)
    return esforco

def obter_texto_caminho_formatado(caminho):
    return ' '.join([f"{ponto[0]},{ponto[1]}" for ponto in caminho])

#valida os vizinhos do nó no mapa
def vizinhos(no, mapa):
    vizinhos = []
    for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        novo_no = (no[0] + i, no[1] + j)
        if 0 <= novo_no[0] < len(mapa) and 0 <= novo_no[1] < len(mapa[0]) and mapa[novo_no[0]][novo_no[1]] != -1:
            vizinhos.append(novo_no)
    return vizinhos

#le o arquivo
def ler_mapa_do_arquivo(mapa):
    with open(mapa, 'r') as arquivo:
        linhas = arquivo.readlines()

    largura, altura = map(int, linhas[0].split())
    ponto_inicial = tuple(map(int, linhas[1].split()))
    mapa = [list(map(int, linha.split())) for linha in linhas[2:]]

    return largura, altura, ponto_inicial, mapa


mapa = 'mapa.txt' 
largura, altura, ponto_inicial, mapa = ler_mapa_do_arquivo(mapa)

print(f"Largura do mapa: {largura}")
print(f"Altura do mapa: {altura}")
print(f"Ponto inicial: {ponto_inicial}")


objetivo_x = int(input("Digite a coordenada X do ponto final: "))
objetivo_y = int(input("Digite a coordenada Y do ponto final: "))
ponto_objetivo = (objetivo_x, objetivo_y)

caminho, esforco = busca_a_estrela(mapa, ponto_inicial, ponto_objetivo)

if caminho:
    texto_caminho = obter_texto_caminho_formatado(caminho)
    print(f"Esforço: {esforco} | caminho: {texto_caminho}")
else:
    print("Não há caminho disponível")