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


PAREDE           = '#'
PISO_VAZIO       = ' '
MARCA_VAZIA      = '.'
CAIXA_NO_PISO    = '$'
CAIXA_NA_MARCA   = '*'
ZELADOR_NO_PISO  = '@'
ZELADOR_NA_MARCA = '+'
NOVA_LINHA = '|'


BAIXO    = 'b'
CIMA     = 'c'
DIREITA  = 'd'
ESQUERDA = 'e'

# ============================================================

def main():
    '''(None) -> None

    Colque testes para a função mova_zelador().

    '''
    mapa = [['#', '#', '#', '#', '#', '#', '#'],
            ['#', ' ', ' ', ' ', ' ', ' ', '#'],
            ['#', ' ', ' ', '*', ' ', ' ', '#'],
            ['#', ' ', '*', '+', '*', ' ', '#'],
            ['#', ' ', ' ', '*', ' ', ' ', '#'],
            ['#', ' ', ' ', ' ', ' ', ' ', '#'],
            ['#', '#', '#', '#', '#', '#', '#']
            ]
    
    movimento = input("Digite um movimento: ")
    
    mov_val = mova_zelador(mapa, movimento)
    
    print(mov_val)
    
    

#-----------------------------------------------------------------------

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

    # escreva abaixo o corpo da função
    lin,col = procura_zelador(mapa)

    if mov == ESQUERDA:
        mov_lin, mov_col = 0, -1
    elif mov == DIREITA:
        mov_lin, mov_col = 0, 1
    elif mov == CIMA:
        mov_lin, mov_col = -1, 0
    elif mov == BAIXO:
        mov_lin, mov_col = 1, 0
    else:
        return False, False
        
    if mapa[lin+mov_lin][col+mov_col] == PAREDE:
        return False, False
    elif mapa[lin+mov_lin][col+mov_col] == CAIXA_NO_PISO and mapa[lin+2*mov_lin][col+2*mov_col] == PAREDE or mapa[lin+2*mov_lin][col+2*mov_col] == CAIXA_NO_PISO:
        return False, False
    
    if mapa[lin+mov_lin][col+mov_col] == CAIXA_NO_PISO or mapa[lin+mov_lin][col+mov_col] == CAIXA_NA_MARCA:
        achei_caixa = True
        if mapa[lin+2*mov_lin][col+2*mov_col] == PAREDE:
            return False, False
        elif mapa[lin+2*mov_lin][col+2*mov_col] == MARCA_VAZIA:
            mapa[lin+mov_lin][col+mov_col] = ZELADOR_NA_MARCA
            mapa[lin+2*mov_lin][col+2*mov_col] = CAIXA_NA_MARCA
        elif mapa[lin+2*mov_lin][col+2*mov_col] == CAIXA_NA_MARCA:
            return False, False
        else:
            mapa[lin+mov_lin][col+mov_col] = ZELADOR_NA_MARCA
            mapa[lin+2*mov_lin][col+2*mov_col] = CAIXA_NO_PISO 
    else:
        achei_caixa = False
        
    if mapa[lin+mov_lin][col+mov_col] == MARCA_VAZIA :
        mapa[lin+mov_lin][col+mov_col] = ZELADOR_NA_MARCA
    elif mapa[lin+mov_lin][col+mov_col] == PISO_VAZIO:
        mapa[lin+mov_lin][col+mov_col] = ZELADOR_NO_PISO
    
    if mapa[lin][col] == ZELADOR_NA_MARCA:
        mapa[lin][col] = MARCA_VAZIA
    else:
        mapa[lin][col] = PISO_VAZIO
    
        
    return True, achei_caixa

        
#-----------------------------------------------------------------------
def procura_zelador(mapa):
    """(list) -> int, int
    
    Recebe o mapa e devolve a posição do zelador caso ele esteja no mapa, 
    se não devolve -1.
    
    """
    
    nlin = len(mapa)
    
    for lin in range(nlin):
        for col in range(len(mapa[lin])):
            if mapa[lin][col] == ZELADOR_NO_PISO or mapa[lin][col] == ZELADOR_NA_MARCA:
                return lin, col
    return -1,-1

#-----------------------------------------------------------------------

if __name__ == "__main__":
    main()