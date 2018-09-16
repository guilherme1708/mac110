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

NADA       = ' '
VAZIA      = '-'
NOVA_LINHA = '|'
DIGITOS    = "0123456789" 
NUMERO     = [0,1,2,3,4,5,6,7,8,9]


# ============================================================

def main():
    '''(None) -> None

    Usado apenas para testar e exemplificar a chamada da função
    monte_mapa().

    Exemplo:
    >>> main()
    ['#', '#', '#', '#', '#', '#', '#']
    ['#', '.', '@', ' ', '#', ' ', '#']
    ['#', '$', '*', ' ', '$', ' ', '#']
    ['#', ' ', ' ', ' ', '$', ' ', '#']
    ['#', ' ', '.', '.', ' ', ' ', '#']
    ['#', ' ', ' ', '*', ' ', ' ', '#']
    ['#', '#', '#', '#', '#', '#', '#']
    >>> 
    ''' 
    matriz = monte_mapa("7#|#.@-#-#|#$*-$-#|#3-$-#|#-..--#|#--*--#|7#")
    for linha in matriz:
        print(linha)

def monte_mapa (rlex):
    '''(str) -> list

    Recebe um string `rlex` com a descrição de um mapa de sokoban
    no formato RLE e cria e retorna uma matriz (lista de listas) que 
    representa esse mapa.

    Exemplos:
    
    >>>monte_mapa("7#")
    [['#', '#', '#', '#', '#', '#', '#']]
    >>>monte_mapa("2#|2.|3#")
    [['#', '#'], ['.', '.'], ['#', '#', '#']]
    >>>monte_mapa("2#|2.|@-|4-|3#")
    [['#', '#'], ['.', '.'], ['@', ' '], [' ', ' ', ' ', ' '], ['#', '#', '#']]
    >>>monte_mapa("7#|#.@-#-#|#$*-$-#|#3-$-#|#-..--#|#--*--#|7#")
    [['#', '#', '#', '#', '#', '#', '#'], ['#', '.', '@', ' ', '#', ' ', '#'], ['#', '$', '*', ' ', '$', ' ', '#'], ['#', ' ', ' ', ' ', '$', ' ', '#'], ['#', ' ', '.', '.', ' ', ' ', '#'], ['#', ' ', ' ', '*', ' ', ' ', '#'], ['#', '#', '#', '#', '#', '#', '#']]
    >>> m = monte_mapa("7#")
    >>> m
    [['#', '#', '#', '#', '#', '#', '#']]
    >>> monte_mapa("")
    []
    >>> monte_mapa(".")
    [['.']]
    >>> 
    
    '''
    n = len(rlex)
    mat, num, certa, final, ind, laux = [], [], [], [], [], []
    j = 0
    if n == 0:
        return []
    
    while j < len(rlex):
       i = 0
       while i < len(rlex[j]):
           laux += rlex[j][i]
           i += 1
       j += 1
    
    for car in laux:
        if car in DIGITOS:
            num += [int(car)]
        else:
            num += car
    
    i = 0
    while i < len(num):
        if num[i] in NUMERO:
            certa += (num[i]-1)*num[i+1]
        else:
            certa += [num[i]]
        i += 1
        
    
    for elemento in certa:
        if elemento == VAZIA:
            elemento = NADA
        final += elemento
    
    i = 0
    while i < len(final):
        if final[i] == NOVA_LINHA:
            ind += [i]
        i += 1
    ind += [len(final)]
    
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
    
 
#-----------------------------------------------
if __name__ == "__main__":
    main()

   

