def cria_posicao(col, lin):
    if type(col) == str and len(col) == 1 and 97<=ord(col)<=106 and type(lin) == int and 1<=lin<=10:
        return f"{col}{lin}"
    raise ValueError('cria_posicao: argumentos invalidos')

def obtem_pos_col(p):
    return p[0]

def obtem_pos_lin(p):
    return p[1]

def eh_posicao(arg):
    if type(arg) == str and len(arg) == 2 and 97<=ord(arg[0])<=106 and arg[1].isdigit() and 1<=int(arg[1])<=10:
        return True
    return False

def posicoes_iguais(p1, p2):
    if eh_posicao(p1) and eh_posicao(p2) and p1 == p2:
        return True
    return False

def posicao_para_str(p):
    return f"{p[0]}{p[1]}"

def str_para_posicao(s):
    return f"{s[0]}{s[1]}"

def posicao_para_coord(p):
    posicoes_colunas = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j")
    coluna = posicoes_colunas.index(p[0])+1
    return (coluna, int(p[1]))

def coord_para_posicao(t):
    posicoes_colunas = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j")
    return f"{posicoes_colunas[t[0]-1]}{t[1]}"


def eh_posicao_valida(p,n):
    if eh_posicao(p) and type(n) == int and 2<=n<=5:
        if n*2 == p[1] and p[0] in range(97, 97+n*2):
            return True
    return False


def obtem_posicoes_adjacentes(p,n,d):
    resultado = ()
    if d == True:
        coord = posicao_para_coord(p)
        if coord[1] != 1: #cima
            resultado += (coord_para_posicao((coord[0], coord[1]-1)),)
        if coord[1] != 1 and coord[0] != n*2: #direita cima
            resultado += (coord_para_posicao((coord[0]+1, coord[1]-1)),)
        if coord[0] != n*2: #direita
            resultado += (coord_para_posicao((coord[0]+1, coord[1])),)
        if coord[1] != n*2 and coord[1] != n*2: #direita baixo
            resultado += (coord_para_posicao((coord[0]+1, coord[1]+1)),)
        if coord[1] != n*2: #baixo
            resultado += (coord_para_posicao((coord[0], coord[1]+1)),)
        if coord[1] != n*2 and coord[0] != 1: #esquerda baixo
            resultado += (coord_para_posicao((coord[0]-1, coord[1]+1)),)
        if coord[0] != 1: #esquerda
            resultado += (coord_para_posicao((coord[0]-1, coord[1])),)
        if coord[0] != 1 and coord[1] != 1: #esquerda cima
            resultado += (coord_para_posicao((coord[0]-1, coord[1]-1)),)
    if d == False:
        coord = posicao_para_coord(p)
        if coord[1] != 1: #cima
            resultado += (coord_para_posicao((coord[0], coord[1]-1)),)
        if coord[0] != n*2: #direita
            resultado += (coord_para_posicao((coord[0]+1, coord[1])),)
        if coord[1] != n*2: #baixo
            resultado += (coord_para_posicao((coord[0], coord[1]+1)),)
        if coord[0] != 1: #esquerda
            resultado += (coord_para_posicao((coord[0]-1, coord[1])),)
    return resultado


def ordena_posicoes(t, n):
    posicao_central1 = (n,n) #em qualquer tabuleiro, podemos considerar (n,n) e (n+1,n+1) como duas posições centrais
    posicao_central2 = (n+1,n+1)
    posicao = ()
    resultado = ()
    d = {}
    for i in t:
        posicao = posicao_para_coord(i)
        distancia = max(max((abs(posicao_central1[1]-posicao[1]),abs(posicao_central1[0]-posicao[0]))), max((abs(posicao_central2[1]-posicao[1]),abs(posicao_central2[0]-posicao[0]))))
        #no cálculo acima, fazemos a distância de chebyshev de um ponto para cada um dos centrais, escolhendo sempre a maior distância.
        if distancia in d:
            d[distancia] += [posicao] #criamos um dicionário organizado pelas órbitas
        else:
            d[distancia] = [posicao]
    for key in d:
        d[key] = sorted(d[key], key=lambda p: (p[1], p[0])) #os valores de cada chave são organizados pela sua primeira entrada (linha) e em seguida pela sua segunda (coluna)
    d = {key: d[key] for key in sorted(d)} #organizando as chaves do dicionario !!!!!!!!!!!!!!!!!!!!!!!!!!!
    for valor in d.values(): #vamos iterar uma lista com cada valor do dicionário
        for coord in valor: #iteremos cada tuplo da lista
            coord = coord_para_posicao(coord)
            resultado += (coord,) #adicionamos as posições para nosso resultado
    return resultado


def cria_pedra_branca():
    return "branca"

def cria_pedra_preta():
    return "preta"

def cria_pedra_neutra():
    return "neutra"

def eh_pedra(arg):
    if arg in ("branca","preta","neutra"):
        return True
    return False

def eh_pedra_branca(p):
    if p == "branca":
        return True
    return False

def eh_pedra_preta(p):
    if p == "preta":
        return True
    return False

def pedras_iguais(p1,p2):
    if eh_pedra(p1) and eh_pedra(p2) and p1==p2:
        return True
    return False

def pedra_para_str(p):
    if eh_pedra(p):
        if eh_pedra_branca(p):
            return "O"
        if eh_pedra_preta(p):
            return "X"
        return " "
    
def eh_pedra_jogador(p):
    if eh_pedra_branca(p) or eh_pedra_preta(p):
        return True
    return False

def pedra_para_int(p):
    if eh_pedra_branca(p):
        return -1
    if eh_pedra_preta(p):
        return 1
    return 0


print(not pedras_iguais(cria_pedra_branca(), cria_pedra_preta()))
        

