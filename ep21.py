# -*- coding: utf-8 -*-
#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
# NÃO ALTERE OS NOMES DAS FUNÇÕES
# NÃO APAGUE OS DOCSTRINGS
#------------------------------------------------------------------

'''

    Nome: Gulherme Navarro
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


PISO_VAZIO = ' ' #f#
VAZIA      = '-'
NOVA_LINHA = '|'
DIGITOS    = "0123456789"

# ============================================================

def main():
    '''(None) -> None

    Usado apenas para testar e exemplificar a chamada da função
    monte_mapa().

    Exemplo:
    >>> main()
    >>> 
    '''
    mapa = [
    ['#', '#', '#', '#', '#', '#', '#'],
    ['#', '.', '@', ' ', '#', ' ', '#'],
    ['#', '$', '*', ' ', '$', ' ', '#'],
    ['#', ' ', ' ', ' ', '$', ' ', '#'],
    ['#', ' ', '.', '.', ' ', ' ', '#'],
    ['#', ' ', ' ', '*', ' ', ' ', '#'],
    ['#', '#', '#', '#', '#', '#', '#']
    ]
    novo_mapa = ponha_espacos(mapa)

    imprima_mapa( novo_mapa )

#-----------------------------------------------------------------------

def ponha_espacos(mapa):
    '''(list) -> (list)'''
    
    nlin = len(mapa)
    i = 0
    cols = []
    
    while i < nlin:
        cols += [len(mapa[i])]
        i+=1
    ncol = maxi(cols)
    
    for elemento in mapa:
        while len(elemento) != ncol:
            elemento += PISO_VAZIO

    return mapa
#-----------------------------------------------------------------------
def maxi(ncols):
    '''list -> int '''
    
    i = 0
    tam = len(ncols)
    maior = ncols[0]
    
    while i < tam:
        if ncols[i] > maior:
            maior = ncols[i]
        i += 1
            
    return maior
#-----------------------------------------------------------------------

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
    
>>> mapa = [
    ['#', '#', '#', '#'],
    ['#', '.', '@', '#', '#'],
    ['#', '$', '*', ' ', '$', '#'],
    ['#', ' ', ' ', ' ', '$', '#'],
    ['#', ' ', '.', '.', ' ', '#'],
    [' ', '#', '#', '#', '#'],
    ]
>>> imprima_mapa(mapa)
      0   1   2   3   4   5 
    +---+---+---+---+---+---+
  0 | # | # | # | # |   |   |
    +---+---+---+---+---+---+
  1 | # | . | @ | # | # |   |
    +---+---+---+---+---+---+
  2 | # | $ | * |   | $ | # |
    +---+---+---+---+---+---+
  3 | # |   |   |   | $ | # |
    +---+---+---+---+---+---+
  4 | # |   | . | . |   | # |
    +---+---+---+---+---+---+
  5 |   | # | # | # | # |   |
    +---+---+---+---+---+---+

Dica: os números das linhas antes da primeira barra ('|') 
podem ser impressos usando o formato ' %2d ', da mesma forma,
há 4 colunas em branco antes do primeiro '+'.

    '''
    
    # escreva abaixo o corpo da função
    mapa = ponha_espacos(mapa)
    
    nlin = len (mapa)
    ncol = len(mapa[0])    
    
    colunas = '%7d' %0
    for col in range(1,ncol):
        colunas += '%4d' %(col)
    colunas += PISO_VAZIO 
    print(colunas)
    
    mold = '%4s'%(PISO_VAZIO) + ncol * '+---' + '+'
    print(mold)
    
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
    
#-----------------------------------------------------------------------
if __name__ == "__main__":
    main()

   

