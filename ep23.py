# -*- coding: utf-8 -*-
#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
# NÃO ALTERE OS NOMES DAS FUNÇÕES
# NÃO APAGUE OS DOCSTRINGS
#------------------------------------------------------------------

'''

    Nome: Guilherme Navarro
    NUSP: 8943160

    Ao preencher esse cabeçalho com o meu nome e o meu número USP,
    declaro que todas as partes originais desse exercício programa (EP)
    foram desenvolvidas e implementadas por mim e que portanto não 
    constituem desonestidade acadêmica ou plágio.
    Declaro também que sou responsável por todas as cópias desse
    programa e que não distribui ou facilitei a sua distribuição.
    Estou ciente que os casos de plágio e desonestidade acadêmica
    serão tratados segundo os critérios divulgados na página da 
    disciplina.
    Entendo que EPs sem assinatura devem receber nota zero e, ainda
    assim, poderão ser punidos por desonestidade acadêmica.

'''

# ============================================================

# DEFINIÇÃO DE CONSTANTES QUE VOCÊ PODE UTILIZAR
# DEFINA OUTRAS SE DESEJAR

NUMERO           = [0,1,2,3,4,5,6,7,8,9]
DIGITOS          = '123456789'
NADA             = '-'
NOVA_LINHA       = '|'
PAREDE           = '#'
PISO_VAZIO       = ' '
MARCA_VAZIA      = '.'
CAIXA_NO_PISO    = '$'
CAIXA_NA_MARCA   = '*'
ZELADOR_NO_PISO  = '@'
ZELADOR_NA_MARCA = '+'

SAIR = 's'

# ============================================================
def main():
    '''

    Sokoban

    '''
    print()
    print('========================================')
    print('         Bem-vindo ao Sokoban!          ')
    print('========================================')
    print()
    
    mapa = monte_mapa(carrega_mapa()) # carrega e monta um mapa
    imprima_mapa(mapa) # imprime o mapa
        
    lin, col = procura_zelador(mapa) # posição inicial do zelador
    
    print()
    print('Posição inicial do zelador: %d,%d\n' %(lin,col))      
    print()
    
    # instruções de movimentos
    print('instruções:')
    print('b: baixo')
    print('c: cima')
    print('d: direita')
    print('e: esquerda')
    print('r: reiniciar o jogo')
    print('s: sair do jogo')
    print()
    
    movimentos = input('Digite um movimento: ')
    
    while not jogo_concluido(mapa) and movimentos != SAIR: #laço para pedir novos movimentos 
        print()
        mov_val, mov_caixa = mova_zelador(mapa, movimentos)
        if mov_val: # verifica se os movimentos são válidos
            imprima_mapa(mapa) # imprime um mapa atualizado 
            lin, col = procura_zelador(mapa) # posição atual do zelador
            print()
            print("O jogador está na posição: %d, %d"%(lin, col))
            print()

        if not jogo_concluido(mapa): # se o jogo não for concluído pede um novo movimento
            movimentos = input('Digite um novo movimento: ')
        
    if jogo_concluido(mapa): # Terminou o jogo vencendo
        print('Parabéns! Você conseguiu!!!')
    else: # Saiu do jogo
        print("Até logo!")
    
#---------------------------------------------------------------
# COLOQUE AQUI TODAS AS FUNÇÃO DESENVOLVIDAS NOS EPS ANTERIORES
#---------------------------------------------------------------
def monte_mapa (rlex):
    '''(str) -> matriz

    Recebe um string `rlex` com a descrição de um mapa de sokoban
    no formato RLE e cria e retorna uma matriz que representa esse
    mapa.
    
    '''
    n = len(rlex) # tamanho do string rlex
    mat, num, certa, final, ind, laux = [], [], [], [], [], [] # iniciação de listas vazias
    j = 0
    if n == 0:
        return [] # se string vazio, retorna lista vazia
    
    # cria uma lista com elementos individuais de strings
    while j < len(rlex): 
       i = 0
       while i < len(rlex[j]):
           laux += rlex[j][i]
           i += 1
       j += 1
    
    # cria uma lista com os numeros contidos no rlex
    for car in laux:
        if car in DIGITOS:
            num += [int(car)]
        else:
            num += car
    
    # cria uma lista que multiplica o número antes do string com caracterítica do mapa
    i = 0
    while i < len(num):
        if num[i] in NUMERO:
            certa += (num[i]-1)*num[i+1]
        else:
            certa += [num[i]]
        i += 1
        
    # cria uma lista que troca o string '-' por string VAZIO
    for elemento in certa:
        if elemento == NADA:
            elemento = PISO_VAZIO
        final += elemento
    
    # cria uma lista com as linhas da matriz utilizando de separador o string '|'
    i = 0
    while i < len(final):
        if final[i] == NOVA_LINHA:
            ind += [i]
        i += 1
    ind += [len(final)]
    
    # cria a matriz com o mapa 
    ini = 0
    j = 1
    fim = ind[0]
    while ini < len(final) and j < len(ind):
        mat += [final[ini:fim]]
        ini = fim+1 
        fim = ind[j]
        j += 1
    
    mat += [final[ini:fim]]
    
    return mat

#---------------------------------------------------------------------
def imprima_mapa(mapa):
    '''(list) -> None

    Função que imprime um mapa com moldura.
    Exemplo:
    >>> mapa = [
        ['#', '#', '#', '#', '#', '#', '#'],
        ['#', '.', '@', ' ', '#', ' ', '#'],
        ['#', '$', '*', ' ', '$', ' ', '#'],
        ['#', ' ', ' ', ' ', '$', ' ', '#'],
        ['#', ' ', '.', '.', ' ', ' ', '#'],
        ['#', ' ', ' ', '*', ' ', ' ', '#'],
        ['#', '#', '#', '#', '#', '#', '#']
    ]
    >>> imprima_mapa(mapa)
          0   1   2   3   4   5   6 
        +---+---+---+---+---+---+---+
      0 | # | # | # | # | # | # | # |
        +---+---+---+---+---+---+---+
      1 | # | . | @ |   | # |   | # |
        +---+---+---+---+---+---+---+
      2 | # | $ | * |   | $ |   | # |
        +---+---+---+---+---+---+---+
      3 | # |   |   |   | $ |   | # |
        +---+---+---+---+---+---+---+
      4 | # |   | . | . |   |   | # |
        +---+---+---+---+---+---+---+
      5 | # |   |   | * |   |   | # |
        +---+---+---+---+---+---+---+
      6 | # | # | # | # | # | # | # |
        +---+---+---+---+---+---+---+

    '''
    mapa = ponha_espacos(mapa) # põe espaços para formar uma matriz para o caso irregular
    
    nlin = len (mapa) # numero de linhas da matriz
    ncol = len(mapa[0]) # numero de colunas da matriz
    
    colunas = '%7d' %0 # há 6 colunas em branco antes do primeiro 0 
    
    # cria um string com o numero de colunas do mapa
    for col in range(1,ncol):
        colunas += '%4d' %(col)
    colunas += PISO_VAZIO 
    print(colunas)
    
    # cria um string com a moldura
    mold = '%4s'%(PISO_VAZIO) + ncol * '+---' + '+'
    print(mold)
    
    # coloca no mapa elemento por elemento junto a moldura
    i = 0
    while i < nlin:
        j = 0
        tab = '%3d' %(i)
        while j < ncol:
            tab += '%2s %s' %(NOVA_LINHA, mapa[i][j])
            j += 1
        tab += '%2s' %NOVA_LINHA
        print(tab)
        print(mold)
        i += 1

#---------------------------------------------------------------

def mova_zelador(mapa, mov):
    '''(list, string) -> bool_1, bool_2

    Move o jogador e atualiza o mapa caso o movimento mov for válido. 
    Nesse caso, retorna bool_1 True. Bool_2 é True se uma caixa for movida
    e False caso contrário. Retorna bool_1 e bool_2 False caso o movimento
    seja inválido.

    Exemplo: para o movimento 'c' (CIMA) e os 6 mapas (m1 a m6):

    #####     #####     #####     #####     #####     #####
    #   #     # @ #     # $ #     #   #     #   #     #   #
    #   #     #   #     # @ #     # * #     # $ #     # . #
    # @ #     #   #     #   #     # + #     # $ #     # $ #
    #   #     #   #     #   #     # $ #     # + #     # @ #
    #####     #####     #####     #####     #####     #####
     m1        m2        m3        m4        m5        m6

    os mapas atualizados (quando o mov é válido) e os valores
    retornados pela função são (T para True e F para False):

    #####     #####     #####     #####     #####     #####
    #   #     # @ #     # $ #     # $ #     #   #     #   #
    # @ #     #   #     # @ #     # + #     # $ #     # * #
    #   #     #   #     #   #     # . #     # $ #     # @ #
    #   #     #   #     #   #     # $ #     # + #     #   #
    #####     #####     #####     #####     #####     #####

    T, F      F, F      F, F      T, T      F, F      T, T

    '''
    
    lin,col = procura_zelador(mapa) # posição do zelador

    # verificação de movimentos válidos e move o zelador
    if mov == 'e' or mov == 'E':
        mov_lin, mov_col = 0, -1
    elif mov == 'd' or mov == 'D':
        mov_lin, mov_col = 0, 1
    elif mov == 'c' or mov == 'C':
        mov_lin, mov_col = -1, 0
    elif mov == 'b' or mov == 'B':
        mov_lin, mov_col = 1, 0
    elif mov == 'r' or mov == 'R': # reinicia o jogo
        main()
    else:
        print("Movimento inválido, digite novamente!")
        return False, False
        
    if mapa[lin+mov_lin][col+mov_col] == PAREDE: # o próximo movimento for Parede
        print("Movimento inválido: zelador bateu na parede!")
        return False, False
    # zelador tenta mover caixa contra parede
    elif mapa[lin+2*mov_lin][col+2*mov_col] == PAREDE and mapa[lin+mov_lin][col+mov_col] == CAIXA_NO_PISO:
        print("Movimento inválido: zelador tentou mover caixa presa!")
        return False, False
    
    # mostra que o zelador esta na marca
    if mapa[lin+mov_lin][col+mov_col] == MARCA_VAZIA :
        mapa[lin+mov_lin][col+mov_col] = ZELADOR_NA_MARCA
    # mostra movimento do zelador no piso
    elif mapa[lin+mov_lin][col+mov_col] == PISO_VAZIO:
        mapa[lin+mov_lin][col+mov_col] = ZELADOR_NO_PISO    
    
    # movimentos com a caixa
    if mapa[lin+mov_lin][col+mov_col] == CAIXA_NO_PISO or mapa[lin+mov_lin][col+mov_col] == CAIXA_NA_MARCA:
        achei_caixa = True
        # moveu a caixa contra a parede
        if mapa[lin+2*mov_lin][col+2*mov_col] == PAREDE:
            print("Movimento inválido: zelador bateu a caixa na parede!")
            return False, False
        # moveu uma caixa na marca para uma posição com marca vazia
        elif mapa[lin+mov_lin][col+mov_col] == CAIXA_NA_MARCA and mapa[lin+2*mov_lin][col+2*mov_col] == MARCA_VAZIA:
            mapa[lin+mov_lin][col+mov_col] = ZELADOR_NA_MARCA
            mapa[lin+2*mov_lin][col+2*mov_col] = CAIXA_NA_MARCA
        # moveu uma caixa na marca para uma posição com piso vazio
        elif mapa[lin+mov_lin][col+mov_col] == CAIXA_NA_MARCA and mapa[lin+2*mov_lin][col+2*mov_col] == PISO_VAZIO:
            mapa[lin+mov_lin][col+mov_col] = ZELADOR_NA_MARCA
            mapa[lin+2*mov_lin][col+2*mov_col] = CAIXA_NO_PISO
        # moveu uma caixa na marca vazia
        elif mapa[lin+2*mov_lin][col+2*mov_col] == MARCA_VAZIA:
            mapa[lin+mov_lin][col+mov_col] = ZELADOR_NO_PISO
            mapa[lin+2*mov_lin][col+2*mov_col] = CAIXA_NA_MARCA
        # moveu uma caixa no piso vazio
        elif mapa[lin+2*mov_lin][col+2*mov_col] == PISO_VAZIO:
            mapa[lin+mov_lin][col+mov_col] = ZELADOR_NO_PISO
            mapa[lin+2*mov_lin][col+2*mov_col] = CAIXA_NO_PISO
        # moveu uma caixa na marca para uma posição com caixa no piso
        elif mapa[lin+2*mov_lin][col+2*mov_col] == CAIXA_NA_MARCA or mapa[lin+2*mov_lin][col+2*mov_col] == CAIXA_NO_PISO:
            print("Movimento inválido: zelador tentou mover duas ou mais caixas!")
            return False, False
        else:
            mapa[lin+mov_lin][col+mov_col] = ZELADOR_NA_MARCA
            mapa[lin+2*mov_lin][col+2*mov_col] = CAIXA_NO_PISO 
    else: # não moveu a caixa
        achei_caixa = False
            
    # caso o zelador passe sobre a marca ele não apaga ela
    if mapa[lin][col] == ZELADOR_NA_MARCA:
        mapa[lin][col] = MARCA_VAZIA
    else:
        mapa[lin][col] = PISO_VAZIO
        
    return True, achei_caixa

#-----------------------------------------------------------------------
def ponha_espacos(mapa):
    '''(list) -> (list)
    Recebe uma matriz mapa e completa com espaços em branco, os mapas que são irregulares, deixando
    os mapas em formato de Matriz.
    
    '''
    
    nlin = len(mapa) # numero de linhas do mapa
    i = 0
    cols = []
    
    # conta o numero de colunas e põe em uma lista
    while i < nlin:
        cols += [len(mapa[i])]
        i+=1
        
    ncol = maxi(cols) # pega o maior numero de colunas do mapa
    
    # se caso o numero de colunas for diferente entre as linhas preencher com espaços
    for elemento in mapa:
        while len(elemento) != ncol:
            elemento += PISO_VAZIO

    return mapa

#-----------------------------------------------------------------------
def maxi(ncols):
    '''(list) -> int 
    
    Recebe uma lista com o numero de colunas do mapa e retorna o maior deles.
    
    '''
    
    maior = ncols[0] # primeiro elemento da lista ncols
    
    # veirifica elemento por elemento e devolver o maior
    for elemento in ncols:
        if elemento >= maior:
            maior = elemento
       
    return maior

#-----------------------------------------------------------------------
def procura_zelador(mapa):
    """(list) -> int, int
    
    Recebe o mapa e devolve a posição do zelador caso ele esteja no mapa, 
    se não devolve -1.
    
    """
    
    nlin = len(mapa) # numero de linhas do mapa
    
    # varre todos elementos da matriz e retorna a posição do zelador no mapa 
    for lin in range(nlin):
        for col in range(len(mapa[lin])):
            if mapa[lin][col] == ZELADOR_NO_PISO or mapa[lin][col] == ZELADOR_NA_MARCA:
                return lin, col
    return -1,-1

#-----------------------------------------------------------------------
def jogo_concluido(mapa):
    '''(list) -> bool 
    
    Recebe o mapa e verifica se o jogo foi concluído, retornando um booleano
    True ou False.
    
    '''
    
    nlin = len(mapa) # numero de linhas no mapa
    ncol = len(mapa[0]) # numero de colunas no mapa
    
    # verifica se existe um elemento marca vazia ou zelador na marca, se existir continua o jogo 
    for lin in range(nlin):
        for col in range(ncol):
            if mapa[lin][col] == MARCA_VAZIA or mapa[lin][col] == ZELADOR_NA_MARCA:
                return False
    return True
                
#-----------------------------------------------------------------------
def carrega_mapa():
    """ None -> String
    
    Carrega um mapa a partir da escolha do jogador.
    
    """
    # mapas em rlex organizados por dificuldade
    m1 = '5#|#3-#|#-$@#|#-.-#|5#'
    m2 = '3#2-|#.3#|#*$-#|#2-@#|5#'
    m3 = '5#-|#@-.##|#$-$-#|#.---#|6#'
    m4 = '8#|#2-@3.#|#-3$2-#|#6-#|8#'
    m5 = '5#|#.@--#|#$*--#|#3-$-#|#--.--#|-#-*--#|-6#'
    m6 = '--5#|3#3-#|#.@$2-#|3#-$.#|#.2#$-#|#-#-.-2#|#$-*2$.#|#3-.2-#|8#' 
    m7 = '7#|#.@-#-#|#$*-$-#|#3-$-#|#-2.2-#|#2-*2-#|7#'
    m8 = '4#6-|#2-4#3-|#2--2-3#-|#-$#$2-.2#|#2-$2--2.#|#-$#$--2.#|#2--2-4#|#@-4#3-|4#6-'
    m9 = '6#4-|#-.2--#|#@-*$-2#2-|2#2-.2--#-|-2#-$*$-2#|2-2#2-.2-#|3-2#2-*-#|4-2#3-#|5-2#-2#|6-3#-'
    
    
    lista = [m1,m2,m3,m4,m5,m6,m7,m8,m9] # lista com os mapas
    
    escolha = int(input('Digite o número do mapa que você quer jogar (1 à 9): '))
    print()
    
    
    if escolha not in range(1,10): # verifica se o numero digitado é um índice válido da lista 
        print('Mapa não existe!')
        escolha = int(input('Digite o número do mapa válido: '))
    print()
    
    # escolhe um mapa de acordo com o índice + 1
    i = 0
    while i < 9:
        if escolha == i+1:
            escolha = lista[i]
            print("Mapa escolhido Mapa %d: " %(i+1))
        i += 1
    print()
    
    return escolha
    
#-----------------------------------------------------------------------

if __name__ == "__main__":
    main()