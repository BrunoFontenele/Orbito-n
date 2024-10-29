
#TAD Posição - Funções Básicas

def cria_posicao(col, lin):
    '''
    Recebe um caractere e um inteiro correspondentes a coluna e a linha, respetivamente, e devolve a posição correspondente.
    '''
    if type(col) == str and len(col) == 1 and 97<=ord(col)<=106 and type(lin) == int and 1<=lin<=10:
        return f"{col}{lin}"
    raise ValueError('cria_posicao: argumentos invalidos')

def obtem_pos_col(p):
    '''
    Recebe uma posição e devolve a coluna dessa posição.
    '''
    return p[0]

def obtem_pos_lin(p):
    '''
    Recebe uma posição e devolve a linha dessa posição.
    '''
    return int(p[1:]) #retornamos a posição a partir do segundo elemento da string, pois a primeira é a coluna

def eh_posicao(arg):
    '''
    A função verifica se o seu argumento é um TAD posição, devolvendo True se for e
    False se não.
    '''
    if type(arg) == str and 2<=len(arg)<=3 and type(arg[0]) == str and \
        97<=ord(arg[0])<=106 and arg[1:].isdigit() and 1<=int(arg[1:])<=10:
        return True
    return False

def posicoes_iguais(p1, p2):
    '''
    A função verifica se seus dois argumentos são posições e se são iguais, retornando True
    se as condições forem cumpridas e False caso não sejam um desses.
    '''
    if eh_posicao(p1) and eh_posicao(p2) and p1 == p2:
        return True
    return False

def posicao_para_str(p):
    '''
    A função recebe um TAD posição devolve uma cadeia de caracteres que representa seu argumento.
    '''
    return f"{p[0]}{p[1:]}"

def str_para_posicao(s):
    '''
    A função recebe uma string e devolve a posição representada por ela.
    '''
    return f"{s[0]}{s[1:]}"

#TAD Posição - Funções Auxiliares (também de alto nível, apenas utilizam funções básicas do TAD posição)

def posicao_para_coord(p):
    '''
    Recebe uma posição e retorna um tuplo com as coordenadas dessa. Considere que a posição inicial (a1) teria coordenadas (1,1)
    e que as coordenadas são dadas por (coluna, linha).
    '''
    posicoes_colunas = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j")
    coluna = posicoes_colunas.index(obtem_pos_col(p))+1
    return (coluna, int(obtem_pos_lin(p)))

def coord_para_posicao(t):
    '''
    Recebe um tuplo com as coordenadas de uma posição e retorna essa posição. Considere que as coordenadas são definidas como
    na função coord_para_posicao.
    '''
    posicoes_colunas = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j")
    coluna = posicoes_colunas[t[0]-1]
    if t[1] != 10:
        return cria_posicao(coluna,t[1])
    return cria_posicao(coluna, 10)

def orbita_posicao(p,n):
    '''
    A função recebe um TAD posição e um inteiro indicando o número de órbitas de um tabuleiro de orbito-n e devolve
    a órbita em que essa posição se encontra.
    '''
    posicao_central1 = (n,n) #em qualquer tabuleiro, podemos considerar (n,n) e (n+1,n+1) como duas posições centrais
    posicao_central2 = (n+1,n+1)
    coord_principal = posicao_para_coord(p)
    orbita_posicao = max(max((abs(posicao_central1[1]-coord_principal[1]),abs(posicao_central1[0]-coord_principal[0]))), max((abs(posicao_central2[1]-coord_principal[1]),abs(posicao_central2[0]-coord_principal[0]))))
    #no cálculo acima, fazemos a distância de chebyshev de um ponto para cada um dos pontos centrais, escolhendo sempre a maior distância.
    return orbita_posicao

#Funções de Alto Nível - TAD Posição

def eh_posicao_valida(p,n):
    '''
    Recebe uma posição (p) e um inteiro (n), sendo esse o número de órbitas de um tabuleiro de Orbito-n. 
    Devolve True se essa posição estiver contida no tabuleiro e False se não estiver.
    '''
    if eh_posicao(p):
        if 1<=int(obtem_pos_lin(p))<=n*2 and ord(obtem_pos_col(p)) in range(97, 97+(n*2)):
         return True
    return False


def obtem_posicoes_adjacentes(p,n,d): 
    '''
    A função recebe uma posição do TAD posição (p), o número de órbitas de um tabuleiro de Orbito-n (n) e um booleano (d). 
    Retorna as posições adjacentes (incluindo diagonais) se d for True ou obterá as adjacentes ortogonais (sem diagonais) se d for False.
    '''
    resultado = ()
    coord = posicao_para_coord(p)
    coluna, linha = coord
    if d:
        # verificamos se existe cada posição a volta da nossa posição principal e guardamos no resultado. A veficação é feita em sentido horário.
        if linha != 1: # cima
            resultado += (coord_para_posicao((coluna, linha-1)),)
        if linha != 1 and coluna != n*2: # direita cima
            resultado += (coord_para_posicao((coluna+1, linha-1)),)
        if coluna != n*2: # direita
            resultado += (coord_para_posicao((coluna+1, linha)),)
        if coluna != n*2 and linha != n*2: # direita baixo
            resultado += (coord_para_posicao((coluna+1, linha+1)),)
        if linha != n*2: # baixo
            resultado += (coord_para_posicao((coluna, linha+1)),)
        if linha != n*2 and coluna != 1: # esquerda baixo
            resultado += (coord_para_posicao((coluna-1, linha+1)),)
        if coluna != 1: # esquerda
            resultado += (coord_para_posicao((coluna-1, linha)),)
        if coluna != 1 and linha != 1: # esquerda cima
            resultado += (coord_para_posicao((coluna-1, linha-1)),)
    else:
        if linha != 1: # cima
            resultado += (coord_para_posicao((coluna, linha-1)),)
        if coluna != n*2: # direita
            resultado += (coord_para_posicao((coluna+1, linha)),)
        if linha != n*2: # baixo
            resultado += (coord_para_posicao((coluna, linha+1)),)
        if coluna != 1: # esquerda
            resultado += (coord_para_posicao((coluna-1, linha)),)
    return resultado


def ordena_posicoes(t, n):
    '''
    A função recebe um tuplo de posições do TAD (t) e um inteiro (n) que indica o número de órbitas do tabuleiro. 
    Devolve um tuplo com as posições ordenadas pela ordem de leitura do tabuleiro.
    '''
    resultado = ()
    d = {}
    for i in t:
        orbita = orbita_posicao(i, n)
        if orbita in d:
            d[orbita] += [i] #adicionamos a posição a órbita se ela já tiver sido criada
        else:
            d[orbita] = [i] #criamos uma chave com a órbita de cada posições e guardamos essas posições como valores de suas órbitas
    for key in d:
        d[key] = sorted(d[key], key=lambda p: (obtem_pos_lin(p), obtem_pos_col(p))) #os valores de cada chave são organizados pela sua primeira entrada (linha) e em seguida pela sua segunda (coluna)
    d = {key: d[key] for key in sorted(d)} #como sorted(d) retorna uma lista, precisamos criar um dicionário em que as chaves sáo os itens dessa lista
    for valor in d.values(): #vamos iterar uma lista com cada valor do dicionário
        for pos in valor: #iteremos cada posição da lista
            resultado += (pos,) #adicionamos as posições para nosso resultado
    return resultado


#TAD Pedra - Funções Básicas

def cria_pedra_branca():
    '''
    A função devolve uma pedra pertencente ao jogador branco.
    '''
    return "branca"

def cria_pedra_preta():
    '''
    A função devolve uma pedra pertencente ao jogador preto.
    '''
    return "preta"

def cria_pedra_neutra():
    '''
    A função devolve uma pedra neutra.
    '''
    return ""

def eh_pedra(arg):
    '''
    A função verifica se seu argumento é um TAD pedra e devolve um booleano, sendo True
    se for e False se não for.
    '''
    if arg in ("branca","preta",""):
        return True
    return False

def eh_pedra_branca(p):
    '''
    A função recebe uma pedra e retorna um booleano, sendo True se a pedra for do 
    jogador branco e False se não for.
    '''
    if p == cria_pedra_branca():
        return True
    return False

def eh_pedra_preta(p):
    '''
    A função recebe uma pedra e retorna um booleano, sendo True se a pedra for do 
    jogador preto e False se não for.
    '''
    if p == cria_pedra_preta():
        return True
    return False

def pedras_iguais(p1,p2):
    '''
    A função verifica se seus dois argumentos são pedras e, se forem, se são iguais. Retorna um booleano,
    com valor de True se as condições forem cumpridas e False se não forem.
    '''
    if eh_pedra(p1) and eh_pedra(p2) and p1==p2:
        return True
    return False

def pedra_para_str(p):
    '''
    A função recebe um TAD pedra e devolve "O" se a pedra for do jogador branco, "X" se for do jogador preto
    e " " se for neutra.
    '''
    if eh_pedra_branca(p):
        return "O"
    if eh_pedra_preta(p):
        return "X"
    return " "
    

#Funções de Alto Nível - TAD Pedra

def eh_pedra_jogador(p):
    '''
    A função recebe um TAD pedra e devolve se é de um jogador, retornando um booleano com valor de True
    se for ou False se não for.
    '''
    if eh_pedra_branca(p) or eh_pedra_preta(p):
        return True
    return False

def pedra_para_int(p):
    '''
    A função recebe um TAD pedra e retorna um inteiro, tendo valor de 1 se a pedra for do jogador preto,
    -1 se for do jogador branco, ou 0 se for neutra.
    '''
    if eh_pedra_branca(p):
        return -1
    if eh_pedra_preta(p):
        return 1
    return 0




#TAD Tabuleiro - Funções Básicas


def cria_tabuleiro_vazio(n):
    '''
    A função recebe um inteiro (n) que indica o número de órbitas de um tabuleiro e retorna
    um tabuleiro vazio com as proporções adequadas para o inteiro recebido.
    '''
    if type(n) != int:
        raise ValueError('cria_tabuleiro_vazio: argumento invalido')
    if not 2<=n<=5:
        raise ValueError('cria_tabuleiro_vazio: argumento invalido')
    resultado = []
    for _ in range(1,(n*2)+1): #adicionamos sublistas na lista principal, sendo essa quantidade de 1 até n*2 (linhas)
        resultado += [[]]
    for _ in resultado:
        for j in range(1,(n*2)+1): #adicionando sublistas as sublistas (colunas)
            resultado[j-1] += [[cria_pedra_neutra()]]
    return resultado

def cria_tabuleiro(n,tp,tb):
    '''
    A função recebe um inteiro (n) que indica a quantidade de órbitas de um tabuleiro, um tuplo
    de posições ocupadas por pedras pretas (tp) e um tuplo de posições ocupadas por pedras brancas (tb).
    '''
    if not type(n) == int or not type(tp) == tuple or not type(tb) == tuple:
        raise ValueError('cria_tabuleiro: argumentos invalidos')
    if not 2<=n<=5:
        raise ValueError('cria_tabuleiro: argumentos invalidos')
    for pos in tb: #verificando se alguma posição do tuplo do jogador preto está no tuplo do jogador branco
        if pos in tp:
            raise ValueError('cria_tabuleiro: argumentos invalidos')
    for i in tp: #verificando se as posições de tp são válidas
        if not eh_posicao_valida(i,n):
            raise ValueError('cria_tabuleiro: argumentos invalidos')
    for i in tb: #verificando se as posições de tb são válidas
        if not eh_posicao_valida(i,n):
            raise ValueError('cria_tabuleiro: argumentos invalidos')
    tab = cria_tabuleiro_vazio(n)
    for i in tp:
        coluna,linha = posicao_para_coord(i)
        tab[linha-1][coluna-1] = [cria_pedra_preta()] #alteramos o tabuleiro vazio na posição que queremos
    for i in tb:
        coluna,linha = posicao_para_coord(i)
        tab[linha-1][coluna-1] = [cria_pedra_branca()]
    return tab

def obtem_numero_orbitas(t):
    '''
    A função recebe um tabuleiro (t) e retorna o número de órbitas desse.
    '''
    return len(t)//2

def obtem_pedra(t,p):
    '''
    A função recebe um tabuleiro (t) e uma posição (p) e retorna a pedra que está nessa posição.
    '''
    coluna,linha = posicao_para_coord(p)
    if t[linha-1][coluna-1][0] == cria_pedra_branca(): 
        return cria_pedra_branca()
    if t[linha-1][coluna-1][0] == cria_pedra_preta():
        return cria_pedra_preta()
    return cria_pedra_neutra()

def cria_copia_tabuleiro(t):
    '''
    A função recebe um tabuleiro (t) e retorna uma cópia desse.
    '''
    novo_t = []
    contador = 0
    contador1 = 0
    novo_t = cria_tabuleiro_vazio(obtem_numero_orbitas(t))
    for i in t:
        for _ in i:
            posicao = coord_para_posicao((contador1+1,contador+1))
            pedra = obtem_pedra(t,posicao)
            novo_t[contador][contador1] = [pedra]
            contador1 += 1
        contador1 = 0
        contador += 1
    return novo_t


def obtem_linha_horizontal(t,p):
    '''
    A função recebe um tabuleiro (t) e uma posição (p) e devolve um tuplo com subtuplos de dois elementos, um indicando a posição
    e o outro indicando o valor dessa posição. Isso é feito para toda a linha horizontal que inclui a posição, ordenado da esquerda
    para a direita.
    '''
    resultado = ()
    posicao = posicao_para_coord(p)
    i = 1
    n = obtem_numero_orbitas(t)
    posicoes = ()
    while i != (n*2)+1: #até o final da linha
        posicoes += (coord_para_posicao((i, posicao[1])),)
        resultado += (obtem_pedra(t, coord_para_posicao((i, int(obtem_pos_lin(p))))),) #obteremos a pedra em cada coluna da linha
        i += 1
    return tuple((posicoes[i], resultado[i]) for i in range(len(posicoes)))



def obtem_linha_vertical(t,p):
    resultado = ()
    i = 1
    n = obtem_numero_orbitas(t)
    posicoes = ()
    while i != (n*2)+1: #até o final da coluna
        posicoes += (str_para_posicao(f"{obtem_pos_col(p)}{i}"),)
        resultado += (obtem_pedra(t, posicoes[i-1]),) #obteremos a pedra em cada coluna da linha
        i += 1
    return tuple((posicoes[i], resultado[i]) for i in range(len(posicoes)))


def obtem_linhas_diagonais(t,p):
    coluna,linha = posicao_para_coord(p)
    coluna_anti,linha_anti = coluna,linha
    n = obtem_numero_orbitas(t) 
    while coluna != 1 and linha != 1: #voltando para o começo da diagonal
        coluna,linha = (coluna - 1, linha - 1)
    p1 = coord_para_posicao((coluna,linha))
    diagonal = ((p1, obtem_pedra(t,p1)),)
    while coluna != n*2 and linha != n*2: #avançando na diagonal
        coluna,linha = (coluna + 1, linha + 1)
        p1 = coord_para_posicao((coluna,linha))
        diagonal += ((p1, obtem_pedra(t,p1)),)
    while coluna_anti != n*2 and linha_anti != 1: #voltando para o começo da antidiagonal
        coluna_anti,linha_anti = (coluna_anti + 1, linha_anti - 1)
    p1 = coord_para_posicao((coluna_anti,linha_anti))
    antidiagonal = ((p1, obtem_pedra(t,p1)),)
    while coluna_anti != 1 and linha_anti != n*2: #avançando na antidiagonal
        coluna_anti,linha_anti = (coluna_anti - 1, linha_anti + 1)
        p1 = coord_para_posicao((coluna_anti,linha_anti))
        antidiagonal += ((p1, obtem_pedra(t,p1)),)
    return diagonal, antidiagonal[::-1]

def obtem_posicoes_pedra(t,j):
    '''
    A função recebe um tabuleiro (t) e uma pedra (j) e devolve o tuplo formado por todas as
    posições do tabuleiro ocupadas pela pedra (j) ordenadas pela ordem de leitura do tabuleiro.
    '''
    resultado = ()
    linha = 1
    for i in t:
        coluna = 1
        for _ in i: 
            posicao = coord_para_posicao((coluna, linha)) #verificandoa para cada posição
            if pedras_iguais(obtem_pedra(t,posicao), j):
                resultado += (posicao,)
            coluna += 1
        linha += 1
    return ordena_posicoes(resultado, obtem_numero_orbitas(t))


def coloca_pedra(t,p,j):
    '''
    A função recebe um tabuleiro (t), uma posição (p) e uma pedra (j) e devolve o tabuleiro, mas com a pedra na
    posição indicada.
    '''
    coluna,linha = posicao_para_coord(p)
    t[linha-1][coluna-1][0] = j #alteramos as coordenadas da posição para a peça que queremos, retirando um das duas para que funcionem como índice
    return t


def remove_pedra(t,p):
    '''
    A função recebe um tabuleiro (t) e uma posição (p) e devolve o tabuleiro com a posição removida,
    ou seja, com uma pedra neutra no lugar.
    '''
    t = coloca_pedra(t, p, cria_pedra_neutra()) #colocar uma pedra neutra na posição é o mesmo que tirar uma pedra.
    return t


def eh_tabuleiro(arg):
    '''
    A função verifica se seu argumento é um TAD tabuleiro, retornando um booleano com valor True se for
    ou um com False se não for.
    '''
    if type(arg) == list:
        if 2<=len(arg)//2<=5 and not any(type(i)!=list for i in arg):
            if len(arg) == len(arg[0]):
                for i in arg:
                    for j in i:
                        if type(j) != list or not eh_pedra(j[0]):
                            return False
                return True
            return False
        return False
    return False

def tabuleiros_iguais(t1,t2):
    '''
    A função verifica se seus dois argumentos são tabuleiros e se são iguais, retornando um booleano com valor True
    se as condições forem cumpridas ou um com False se não forem.
    '''
    if (eh_tabuleiro(t1) == True) and (eh_tabuleiro(t2) == True) and (t1 == t2):
        return True
    return False
        
def tabuleiro_para_str(t):
    '''
    A função recebe um tabuleiro (t) e devolve uma cadeia de caracteres que representa o tabuleiro.
    '''
    resultado = "    a   b   c   d"
    if len(t[0])-4 > 0:
        contador = len(t[0])-4
        contador1 = ord("d")
        while contador != 0:
            contador1 += 1
            resultado += "   " + f"{chr(contador1)}"
            contador -= 1
    resultado += "\n"
    contador = 0
    contador1 = 0
    for linha in t:
        contador += 1
        contador1 = 0
        if contador == 10:
            resultado += "10 "
        else:
            resultado += "0"+ f"{contador} "
        for coluna in linha:
            contador1 += 1
            if pedras_iguais(coluna[0],cria_pedra_neutra()):
                resultado += "[ ]"
            if pedras_iguais(coluna[0],cria_pedra_preta()):
                resultado += "[X]"
            if pedras_iguais(coluna[0],cria_pedra_branca()):
                resultado += "[O]"
            if contador1 != len(t[0]):
                resultado += "-"
            elif contador == len(t[0]):
                continue
            else:
                resultado += "\n"
        if contador != len(t):
            resultado += "    "
            for i in range(len(linha)):
                if i == len(linha)-1:
                    resultado += "|"
                else:
                    resultado += "|   "
            resultado += "\n"
    return resultado



#TAD Tabuleiro - Funções Auxiliares (também de alto nível, apenas utilizam funções básicas)

def obtem_linha_horizontal_posicoes(t,p):
    '''
    A função recebe um tabuleiro (t) e uma posição (p) e retorna um tuplo com as posições da linha horizontal
    na qual a posição recebida está contida.
    '''
    resultado = ()
    posicao = posicao_para_coord(p)
    i = 1
    n = obtem_numero_orbitas(t)
    posicoes = ()
    while i != (n*2)+1: #até o final da linha
        posicoes += (coord_para_posicao((posicao[0], i)),)
        resultado += (coord_para_posicao((i, int(obtem_pos_lin(p)))),) #obteremos a pedra em cada coluna da linha
        i += 1
    return resultado


def obtem_linha_vertical_posicoes(t,p):
    '''
    A função recebe um tabuleiro (t) e uma posição (p) e retorna um tuplo com as posições da linha vertical
    na qual a posição recebida está contida.
    '''
    resultado = ()
    i = 1
    n = obtem_numero_orbitas(t)
    posicoes = ()
    coluna = obtem_pos_col(p)
    while i != (n*2)+1: #até o final da coluna
        posicoes += (str_para_posicao(f"{coluna}{i}"),)
        resultado += (posicoes[i-1],) #obteremos a pedra em cada coluna da linha
        i += 1
    return resultado

def obtem_linhas_diagonais_posicoes(t,p):
    '''
    A função recebe um tabuleiro (t) e uma posição (p) e retorna um tuplo, sendo
    o primeiro elemento um tuplo as posições da linha diagonal na qual a posição recebida está contida
    e o segundo elemento um tuplo as posições da linha antidiagonal na qual a posição recebida está contida.
    O processo é exatamente o mesmo do obtem_linhas_diagonais_posicoes.
    '''
    posicao = posicao_para_coord(p)
    posicao1 = posicao
    n = obtem_numero_orbitas(t)
    while posicao[0] != 1 and posicao[1] != 1:
        posicao = (posicao[0] - 1, posicao[1] - 1)
    diagonal = (coord_para_posicao(posicao),)
    while posicao[0] != n*2 and posicao[1] != n*2:
        posicao = (posicao[0] + 1, posicao[1] + 1)
        diagonal += (coord_para_posicao(posicao),)
    while posicao1[0] != n*2 and posicao1[1] != 1:
        posicao1 = (posicao1[0] + 1, posicao1[1] - 1)
    antidiagonal = (coord_para_posicao(posicao1),)
    while posicao1[0] != 1 and posicao1[1] != n*2:
        posicao1 = (posicao1[0] - 1, posicao1[1] + 1)
        antidiagonal += (coord_para_posicao(posicao1),)
    return (diagonal,antidiagonal[::-1])

def obtem_linha_horizontal_filtrada(t,p):
    '''
    A função recebe um tabuleiro (t) e uma posição (p) e retorna um tuplo indicando o valor de todas 
    as posições da mesma órbita que a posição da linha horizontal que inclui a posição, ordenado da esquerda para a direita.
    '''
    posicoes = obtem_linha_horizontal_posicoes(t,p)
    resultado = ()
    orbita = obtem_numero_orbitas(t)
    orbita_pos = orbita_posicao(p, orbita)
    for i in posicoes:
        if orbita_posicao(i, orbita) == orbita_pos: #apenas queremos guardar as posições de mesma órbita da nossa principal
            resultado += (i,)
    return resultado


def obtem_linha_vertical_filtrada(t,p):
    '''
    A função recebe um tabuleiro (t) e uma posição (p) e retorna um tuplo indicando o valor de todas 
    as posições da mesma órbita que a posição da linha vertical que inclui a posição, ordenado da cima para baixo.
    '''
    posicoes = obtem_linha_vertical_posicoes(t,p)
    resultado = ()
    orbita = obtem_numero_orbitas(t)
    orbita_pos = orbita_posicao(p, orbita)
    for i in posicoes:
        if orbita_posicao(i, orbita) == orbita_pos:
            resultado += (i,)
    return resultado


#Funções de Alto Nível - TAD Tabuleiro

def move_pedra(t, p1, p2):
    '''
    A função recebe um tabuleiro (t) e duas posições (p1 para a inicial e p2 para a seguinte) e devolve o próprio tabuleiro
    em que a pedra da posição 1 e moveu para a posição 2.
    '''
    t = coloca_pedra(t, p2, obtem_pedra(t,p1))
    t= remove_pedra(t,p1)
    return t


def obtem_posicao_seguinte(t, p, s):
    '''
    A função recbe um tabuleiro (t), uma posição (p) e um booleano (s) que indica o sentido, sendo horário
    se for True e anti-horário se for False. Devolve a posição da mesma órbita que a posição (p) que se encontra
    a seguir no tabuleiro (t) no sentido desejado (s).
    '''
    coluna,linha = posicao_para_coord(p)[0], posicao_para_coord(p)[1]
    n = obtem_numero_orbitas(t)
    orbita_principal = orbita_posicao(p, n)
    posicoes_adjacentes = tuple(i for i in obtem_posicoes_adjacentes(p, n, False) if orbita_posicao(i,n) == orbita_principal) #selecionando as posições adjacentes ortogonais da mesma órbita que a posição
    if s == True:   #horario
        prop = max((obtem_linha_horizontal_filtrada(t,p), obtem_linha_vertical_filtrada(t,p)), key=len) 
        '''
        A linha que define o prop utiliza o seguinte processo: 
        obtemos a linha horizontal e vertical filtradas (apenas com posições da mesma órbita da nossa posição) e 
        escolhemos a que tem o maior tamanho. Isso é feito pois existem linhas, como a da posição a2 num tabuleiro 
        de 2 órbitas, que apenas entrega duas posições na linha filtrada, mas queremos sempre trabalhar com 
        a linha maior. 
        '''
        while orbita_principal != n: #vamos reduzir as coordenadas da posição caso ela esteja numa orbita menor, pois estamos eliminando as orbitas mais exteriores
            coluna,linha = (coluna-1,linha-1)
            n -= 1
        if coluna != prop.index(prop[-1])+1 and linha == prop.index(prop[0])+1: #se a posição estiver na primeira linha e antes da última coluna
            return posicoes_adjacentes[0]
        if coluna == prop.index(prop[-1])+1 and prop.index(prop[0])+1<linha<prop.index(prop[-1])+1: #se a posição estiver na última coluna e estiver antes da última linha
            return posicoes_adjacentes[1]
        if coluna == prop.index(prop[-1])+1 and linha == prop.index(prop[0])+1: #se a posição estiver no canto superior direito. Fiz um ponto separado para todas as linhas analisadas terem o mesmo comprimento.
            return posicoes_adjacentes[0]
        if coluna!=prop.index(prop[0])+1 and linha == prop.index(prop[-1])+1: #se a posição estiver na última linha e antes da primeira coluna
            return posicoes_adjacentes[1]
        if coluna == prop.index(prop[0])+1 and linha!=prop.index(prop[0])+1: #se a posição estiver na primeira coluna e antes da primeira linha
            return posicoes_adjacentes[0]
    if s == False: #anti-horario
        '''
        Mesmo processo da anterior, apenas invertendo a ordem. Sentido anti-horário
        '''
        prop = max((obtem_linha_vertical_filtrada(t,p), obtem_linha_horizontal_filtrada(t,p)), key=len)
        while orbita_principal != n:
            coluna,linha = (coluna-1,linha-1)
            n -= 1
        if linha != prop.index(prop[0])+1 and coluna == prop.index(prop[-1])+1: #se a posição estiver depois da primeira linha e na última coluna
            return posicoes_adjacentes[0]
        if linha == prop.index(prop[-1])+1 and prop.index(prop[0])+1<coluna<prop.index(prop[-1])+1: #se a posição está na última linha e não está na última coluna e nem na primeira
            return posicoes_adjacentes[0]
        if linha == prop.index(prop[-1])+1 and coluna == prop.index(prop[0])+1: #se estiver na última linha e na primeira coluna.
            return posicoes_adjacentes[1]
        if coluna == prop.index(prop[0])+1 and linha!=prop.index(prop[-1])+1: #se a posição estiver na primeira coluna e não estiver na última linha
            return posicoes_adjacentes[1]
        if linha == prop.index(prop[0])+1 and coluna!=prop.index(prop[0])+1: #se a posição estiver na primeira linha e não estiver na primeira coluna
            return posicoes_adjacentes[1]


def roda_tabuleiro(t):
    '''
    A função recebe um tabuleiro (t) e move todas as peças em sentido anti-horário, devolvendo o mesmo tabuleiro.
    '''
    t_copia = cria_copia_tabuleiro(t)
    orbitas = obtem_numero_orbitas(t)
    for i in range(1,(orbitas*2)+1):
        for j in range(1,(orbitas*2)+1):
            posicao = coord_para_posicao((j,i))
            pedra = obtem_pedra(t_copia, posicao)
            if not pedras_iguais(pedra, cria_pedra_neutra()): #verificamos se a pedra nessa posição é neutra
                seguinte = obtem_posicao_seguinte(t_copia, posicao, False)
                anterior = obtem_posicao_seguinte(t_copia, posicao, True)
                if pedras_iguais(obtem_pedra(t_copia, anterior), cria_pedra_neutra()): #se não for neutra, verificamos se a pedra na posição anterior
                    #é igual a pedra neutra
                    t = coloca_pedra(t, seguinte, pedra) #se a anterior for neutra, podemos só colocar a pedra na posição seguinte e remover a pedra que está na posição atual
                    t = remove_pedra(t, posicao)
                else:
                    t = coloca_pedra(t, seguinte, pedra) #caso a anteior não seja neutra, não podemos remover a pedra, apenas substituímos a seguinte pela nossa
    return t
           

def verifica_linha_pedras(t,p,j,k):
    '''
    A função recebe um tabuleiro (t), uma posição (p), uma pedra (j) e um inteiro (k).
    Devolve um booleano True se existir uma linha (vertical, horizontal ou diagonal)
    que contenha a posição (p) com o inteiro (k) ou mais pedras consecutivas do jogador com pedras j e devolve
    um False caso contrário.
    '''
    coluna_pos = obtem_linha_vertical_posicoes(t,p)
    linha_pos = obtem_linha_horizontal_posicoes(t,p)
    diagonal = obtem_linhas_diagonais_posicoes(t,p)[0]
    antidiagonal = obtem_linhas_diagonais_posicoes(t,p)[1]
    contador = 0
    tuplo_pos = ()
    for i in coluna_pos: #coluna
        if pedras_iguais(obtem_pedra(t,i), j): #se houver a pedra do jogador, começamos a contar a sequência
            contador += 1
            tuplo_pos += (i,) #armazenamos a posição
        else:
            contador = 0 #em caso de não ser a pedra do jogador, a sequência reinicia
        if contador >= k: #atingimos a sequência indicada por k ou mais
            if p in tuplo_pos: #apenas será verdadeiro se a posição indicada estiver contida no tuplo das posições
                return True
    contador = 0
    tuplo_pos = ()
    for i in linha_pos: #linha
        if pedras_iguais(obtem_pedra(t,i), j):
            contador += 1
            tuplo_pos += (i,) 
        else:
            contador = 0 
        if contador >= k:
            if p in tuplo_pos:
                return True
    contador = 0
    tuplo_pos = ()
    for i in diagonal: #diagonal esquerda direita
        if pedras_iguais(obtem_pedra(t,i), j):
            contador += 1
            tuplo_pos += (i,)
        else:
            contador = 0
        if contador >= k:
            if p in tuplo_pos:
                return True
    contador = 0
    tuplo_pos = ()
    for i in antidiagonal: #diagonal direita esquerda
        if pedras_iguais(obtem_pedra(t,i), j):
            contador += 1
            tuplo_pos += (i,)
        else:
            contador = 0
        if contador >= k:
            if p in tuplo_pos:
                return True
    return False



#Funções Adicionais

def eh_vencedor(t,j):
    '''
    A função recebe um tabuleiro (t) e uma pedra (j) e devolve um booleano True se o jogador com pedras j
    venceu o jogo, ou seja, se existe uma linha completa do tabuleiro de pedras do jogador, e False se não.
    '''
    orbitas = obtem_numero_orbitas(t)
    for i in obtem_posicoes_pedra(t,j):
        if verifica_linha_pedras(t,i,j,orbitas*2): #verificando as linhas inteiras
            return True
    return False


def eh_fim_jogo(t):
    '''
    A função recebe um tabuleiro (t) e devolve um booleano True se o jogo acabou, ou seja, se um dos jogadores
    venceu ou se o tabuleiro está cheio, e False se não.
    '''
    if eh_vencedor(t,cria_pedra_branca()) or eh_vencedor(t,cria_pedra_preta()): #se um dos jogadores ganhou
        return True
    for i in range(1,obtem_numero_orbitas(t)*2+1):
        for j in range(1,obtem_numero_orbitas(t)*2+1):
            if pedras_iguais(obtem_pedra(t, coord_para_posicao((i,j))), cria_pedra_neutra()): #se ainda existir uma pedra neutra, ou seja, uma posição livre
                return False
    return True


def escolhe_movimento_manual(t):
    '''
    A função recebe um tabuleiro (t) e devolve uma posição escolhida pelo jogador, apenas se 
    essa for válida e livre, ou seja, sem pedras. Repete-se até receber uma posição válida.
    '''
    orbita = obtem_numero_orbitas(t)
    while True:
        posicao = str_para_posicao(input("Escolha uma posicao livre:"))
        if eh_posicao(posicao):
            if eh_posicao_valida(posicao, orbita):
                if pedras_iguais(obtem_pedra(t, posicao), cria_pedra_neutra()):
                    return posicao
                

def escolhe_movimento_auto(t,j,lvl):
    '''
    A função recebe um tabuleiro (t), uma pedra (j) e uma string (lvl) que indica o nível de dificuldade.
    Devolve uma posição escolhida pelo computador, de acordo com o nível de dificuldade escolhido.
    '''
    if lvl == "facil":
        orbitas = obtem_numero_orbitas(t)
        livres = ordena_posicoes(obtem_posicoes_pedra(t, cria_pedra_neutra()),orbitas)
        if obtem_posicoes_pedra(t, cria_pedra_branca()) == () and obtem_posicoes_pedra(t, cria_pedra_preta()) == (): #se apenas existirem pedras neutras  
            return livres[0] #retornamos a primeira posição livre na ordem de leitura do tabuleiro
        if obtem_posicoes_pedra(t,j) == ():
            return livres[0]
        for i in livres: #verificamos se existe uma posição que, ao ser preenchida, faz o jogador ter uma pedra adjacente a outra
            t_copia = cria_copia_tabuleiro(t)
            t_copia = coloca_pedra(t_copia, i, j) #colocamos a pedra do jogador
            t_copia = roda_tabuleiro(t_copia) #rodamos o tabuleiro
            if verifica_linha_pedras(t_copia, obtem_posicao_seguinte(t,i,False), j, 2): #verificamos se existe uma linha de 2 pedras, ou seja, uma posição adjacente que contém a mesma pedra
                return i
    if lvl == "normal":
        orbitas = obtem_numero_orbitas(t)
        livres = obtem_posicoes_pedra(t, cria_pedra_neutra())
        posicao_jogada_jogador = ()
        posicao_jogada_adversario = ()
        maximo_jogador = 0
        maximo_adversario = 0
        t_copia = cria_copia_tabuleiro(t)
        if j == cria_pedra_branca(): #descobrindo a pedra do adversário
            adv = cria_pedra_preta()
        else:
            adv = cria_pedra_branca()
        for posicao in livres: #vamos colocar uma pedra em cada espaço livre
            #para o jogador
            t_copia = coloca_pedra(t_copia, posicao, j) # colocamos a pedra do jogador
            t_copia = roda_tabuleiro(t_copia) # rodamos o tabuleiro
            seguinte_jog = obtem_posicao_seguinte(t_copia, posicao, False) # precisamos da posição seguinte à original, pois o tabuleiro rodou
            for i in range(orbitas*2, 0, -1): #o L irá reduzindo, assim teremos o maior que verifica orbita*2 (k) linhas
                if i > maximo_jogador and verifica_linha_pedras(t_copia, seguinte_jog, j, i):
                    posicao_jogada_jogador += ((posicao, i),) # guardaremos o conjunto da posição e seu k
                    maximo_jogador = i # se existir um k menor que satisfaz k linhas, não precisaremos o guardar pois já achamos o k mais elevado
            # para o adversário
            t_copia = coloca_pedra(t_copia, seguinte_jog, adv) # colocamos a pedra do adversário
            seguinte_adv = obtem_posicao_seguinte(t_copia, seguinte_jog, False)
            t_copia = roda_tabuleiro(t_copia)
            for i in range(orbitas*2, 0, -1):
                if i > maximo_adversario and verifica_linha_pedras(t_copia, seguinte_adv, adv, i): #precisamos obter a posição seguinte novamente, o tabuleiro rodou de novo
                    posicao_jogada_adversario += ((posicao, i),) # guardaremos o conjunto da posição e seus k
                    maximo_adversario = i
            maximo_jogador, maximo_adversario = 0,0 #zeramos os máximos para a próxima iteração
            t_copia = cria_copia_tabuleiro(t)
        maximo_jogador = max(posicao_jogada_jogador, key = lambda x: x[1]) #procurando o par com k mais elevado
        maximo_adversario = max(posicao_jogada_adversario, key = lambda x: x[1])
        if maximo_jogador[1] == maximo_adversario[1]: #se tiverem k (ou L) igual 
                return maximo_jogador[0] #jogar na posição que faz o jogador ganhar
        elif maximo_jogador[1] <= maximo_adversario[1]:
            return maximo_adversario[0] #impedir o adversário
        else:
            return maximo_jogador[0] #jogar na melhor posição
                    


def orbito(n,modo,jog):
    '''
    A função recebe um inteiro (n), uma string referente ao modo de jogo (modo) e 
    uma string referente à representação externa de uma pedra (jog) e devolve um inteiro identificando
    o jogador vencedor (1 para preto, -1 para branco ou 0 para empate).
    '''
    if type(n) != int or type(modo) != str or type(jog) != str:
        raise ValueError('orbito: argumentos invalidos')
    if not 2<=n<=5 or not modo in ("facil", "normal", "2jogadores") or not jog in ("X", "O"):
        raise ValueError('orbito: argumentos invalidos')
    t = cria_tabuleiro_vazio(n)
    if modo != "2jogadores":
        print(f"Bem-vindo ao ORBITO-{n}.\nJogo contra o computador ({modo}).\nO jogador joga com '{jog}'.\n{tabuleiro_para_str(t)}")
    else:
        print(f"Bem-vindo ao ORBITO-{n}.\nJogo para dois jogadores.\n{tabuleiro_para_str(t)}")
    if jog == "X": 
        jog = cria_pedra_preta()
    else:
        jog = cria_pedra_branca()
    if eh_pedra_preta(jog) and modo != "2jogadores": #se o jogador for o de pedras pretas e não for um jogo de dois jogadores
        while not eh_fim_jogo(t):
            print("Turno do jogador.") #jogador começa
            posicao_jog = escolhe_movimento_manual(t)
            t = coloca_pedra(t, posicao_jog, jog)
            t = roda_tabuleiro(t)
            print(tabuleiro_para_str(t))
            if eh_fim_jogo(t):
                break
            print(f"Turno do computador ({modo}):")
            posicao_bot = escolhe_movimento_auto(t,cria_pedra_branca(),modo)
            t = coloca_pedra(t, posicao_bot, cria_pedra_branca())
            t = roda_tabuleiro(t)
            print(tabuleiro_para_str(t))
        if eh_vencedor(t,cria_pedra_preta()) and eh_vencedor(t,cria_pedra_branca()): #se ambos os jogadores ganharem ao mesmo tempo
            print("EMPATE")
            return 0
        if eh_vencedor(t,cria_pedra_preta()): #se o jogador ganhar
            print("VITORIA")
            return 1
        elif eh_vencedor(t,cria_pedra_branca()): #se o computador ganhar
            print("DERROTA")
            return -1
        else:
            print("EMPATE")
            return 0
    if eh_pedra_branca(jog) and modo != "2jogadores": #se o jogador for o de pedras brancas e não for um jogo de dois jogadores
        while not eh_fim_jogo(t):
            print(f"Turno do computador ({modo}):") #computador começa
            posicao_bot = escolhe_movimento_auto(t,cria_pedra_preta(),modo)
            t = coloca_pedra(t, posicao_bot, cria_pedra_preta())
            t = roda_tabuleiro(t)
            print(tabuleiro_para_str(t))
            if eh_fim_jogo(t):
                break
            print("Turno do jogador.")
            posicao_jog = escolhe_movimento_manual(t)
            t = coloca_pedra(t, posicao_jog, jog)
            t = roda_tabuleiro(t)
            print(tabuleiro_para_str(t))
        if eh_vencedor(t,cria_pedra_preta()) and eh_vencedor(t,cria_pedra_branca()):
            print("EMPATE")
            return 0
        if eh_vencedor(t,cria_pedra_branca()):
            print("VITORIA")
            return -1
        elif eh_vencedor(t,cria_pedra_preta()):
            print("DERROTA")
            return 1
        else:
            print("EMPATE")
            return 0 
    if modo == "2jogadores": #se for um jogo de dois jogadores
        while not eh_fim_jogo(t):
            print("Turno do jogador 'X'.")
            posicao_jog1 = escolhe_movimento_manual(t)
            t = coloca_pedra(t, posicao_jog1, cria_pedra_preta())
            t = roda_tabuleiro(t)
            print(tabuleiro_para_str(t))
            if eh_fim_jogo(t):
                break
            print("Turno do jogador 'O'.")
            posicao_jog2 = escolhe_movimento_manual(t)
            t = coloca_pedra(t, posicao_jog2, cria_pedra_branca())
            t = roda_tabuleiro(t)
            print(tabuleiro_para_str(t))
        if eh_vencedor(t,cria_pedra_preta()) and eh_vencedor(t,cria_pedra_branca()):
            print("EMPATE")
            return 0
        if eh_pedra_preta(jog): #se o jogador for o de pedras pretas
            if eh_vencedor(t,cria_pedra_preta()):
                print("VITORIA DO JOGADOR ""'X'""")
                return 1
            elif eh_vencedor(t,cria_pedra_branca()):
                print("DERROTA")
                return -1
        if eh_pedra_branca(jog): #se o jogador for o de pedras brancas
            if eh_vencedor(t,cria_pedra_branca()):
                print("VITORIA DO JOGADOR ""'O'""")
                return -1
            elif eh_vencedor(t,cria_pedra_preta()):
                print("DERROTA")
                return 1





