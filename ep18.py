#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÃ‡ALHO 
# NÃƒO ALTERE OS NOMES DAS FUNÃ‡Ã•ES
# NÃƒO APAGUE OS DOCSTRINGS
#------------------------------------------------------------------

'''

    Nome: Guilherme Navarro
    NUSP: 8943160

    Ao preencher esse cabeÃƒÂ§alho com o meu nome e o meu nÃƒÂºmero USP,
    declaro que todas as partes originais desse exercÃƒÂ­cio programa (EP)
    foram desenvolvidas e implementadas por mim e que portanto nÃƒÂ£o 
    constituem desonestidade acadÃƒÂªmica ou plÃƒÂ¡gio.
    Declaro tambÃƒÂ©m que sou responsÃƒÂ¡vel por todas as cÃƒÂ³pias desse
    programa e que nÃƒÂ£o distribui ou facilitei a sua distribuiÃƒÂ§ÃƒÂ£o.
    Estou ciente que os casos de plÃƒÂ¡gio e desonestidade acadÃƒÂªmica
    serÃƒÂ£o tratados segundo os critÃƒÂ©rios divulgados na pÃƒÂ¡gina da 
    disciplina.
    Entendo que EPs sem assinatura devem receber nota zero e, ainda
    assim, poderÃƒÂ£o ser punidos por desonestidade acadÃƒÂªmica.

'''

def main():
    '''
    Este programa lÃª um inteiro `m`, um inteiro `n` e uma sequÃªncia com 
    n inteiros, e altera os valores no(s) segmento(s) de menor tamanho 
    para `m`.

    Exemplos:

    para m = 0, n = 6 e a lista [2, 2, 3, 4, 5, 5]
    o programa imprime: [2, 2, 0, 0, 5, 5]

    para m = -1, n = 7 e a lista [22, 2, 2, 1, 5, 5, 3]
    o programa imprime: [-1, 2, 2, -1, 5, 5, -1]

    para m = 101, n = 8 e a lista [22, 22, 22, 1, 1, 53, 53, 53]
    o programa imprime: [22, 22, 22, 101, 101, 53, 53, 53]
    '''

    m = int(input('Digite um valor da marca: '))
    lista = carregue_lista()
    
    ###########################################################
    # A funÃ§Ã£o menor_segmento() retorna dois inteiros.
    # Por isso Ã© feita uma atribuiÃ§Ã£o para duas variÃ¡veis.
    # Desta forma, as variÃ¡veis ini e fim recebem os valores retornados.
    # Essa operaÃ§Ã£o recebe o nome de atribuiÃ§Ã£o mÃºltipla, semelhante a
    #    a, b = 0, 1
    # que tem o mesmo efeito que
    #    a = 0
    #    b = 1
    ###########################################################
    ini, fim = menor_segmento(lista)

    ###########################################################
    # A funÃ§Ã£o marque_segmentos() nÃ£o possui return ou, como se diz
    # em Python, returna None. A funÃ§Ã£o apenas alterar algumas 
    # posiÃ§Ãµes da lista.
    ###########################################################
    marque_segmentos(lista, fim-ini, m)
    print(lista)
    
    
# ===============================================================
def carregue_lista():
    '''(None) -> list

    LÃª um inteiro positivo `n` e uma sequÃªncia com `n` inteiros 
    e cria e retorna uma lista com esses inteiros.

    NÃ£o altere esta funÃ§Ã£o. Ela estÃ¡ totalmente feita. 
    '''
    # leia n
    n = int(input("Digite n: "))

    # crie uma lista com n posiÃ§Ãµes, cada uma contendo um 0
    seq = [0] * n

    # leia a sequÃªncia e atribua cada valor lido a uma posiÃ§Ã£o
    # da lista
    i = 0
    while i < n:
        seq[i] = int(input("Digite um número da sequência: "))
        i += 1

    # retorne a lista criada    
    return seq
    
# ===============================================================
def segmentos(vals):
    ''' (list) -> list

    Recebe uma lista de valores `vals` e retorna uma lista com 
    os Ã­Â­ndices das posiÃ§Ãµes que sÃ£o os inÃ­Â­cios dos segmentos 
    da lista. 

    A lista retornada deve conter os Ã­ndices em ordem crescente.

    Exemplos:
    
    >>> segmentos( [] )
    []
    >>> segmentos( [1] )
    [0]
    >>> segmentos( [1, 2, 3] )
    [0, 1, 2]
    >>> segmentos( [1, -2, -2, -2, 3, 3] )
    [0, 1, 4]
    >>> segmentos( [101, 52, 52, 13, 13, 13] )
    [0, 1, 3]
    '''
    # escreva a sua funÃ§Ã£o a seguir
    n = len(vals)
    lista = [0]
    
    if n == 0:
        return []
    
    i = 1
    while i < n:
        if vals[i] != vals [i-1]:
            lista+=[i]
        i+=1
        
    return lista
# ===============================================================

def menor_segmento(vals):
    '''(list) -> int, int

    Recebe uma lista de valores `vals` e retorna inteiros `ini` 
    e `fim` tais que o pedaço de ini a fim é um dos segmentos de 
    menor comprimento da lista.

    O comprimento de um pedaço é o número de elementos no pedaço.

    Se houver mais que um par ini e fim possíveis a função 
    deve retornar par tal que ini é o menor de todos.

    Voce deve utilizar obrigatoriamente a função `segmentos()`.

    Exemplos:

     >>> menor_segmento( [] )
     (0, 0)
     >>> menor_segmento( [1] )
     (0, 1)
     >>> menor_segmento( [False, False, False] )
     (0, 3)
     >>> menor_segmento( [1, 1, 1, 2, 2] )
     (3, 5)
     >>> menor_segmento( [1, 1, 1, 'oi', 2, 2, True, True, True, 3.14] )
     (3, 4)
     >>> menor_segmento( [1.1, 1.1, 1.1, None, 2, 2, 'a'] )
     (3, 4)
    '''
    # escreva a sua funÃ§Ã£o a seguir
    n = len(vals)
    seg = segmentos(vals)
    k = len(seg)
    nova = seg + [n]
    j = len(nova)

    if n == 0:
        return (0,0)
    if n == 1:
        return (0,1)
    if k == 1:
        return (0, n)
    if k == 2:
        i, lista = 1, []
        while i < j:
            lista += [nova[i] - nova[i-1]] 
            i+=1
        m = min(lista)-1
        ini = nova[m]
        fim = ini + lista[-1]
        return (ini, fim)
    
    i, lista = 1, []
    while i < j:
        lista += [nova[i] - nova[i-1]] 
        i+=1
    m = min(lista)
    pos = lista.index(m)
    
    if m == lista[0]:    
        ini = 0
        fim = m
    else:
        ini = nova[pos]
        fim = ini + m
    
        
    return (ini, fim)
        
# ===============================================================

def marque(vals, ini, fim, m):
    '''(list, int, int, valor) -> None

    Recebe uma lista `vals`, Ã­Â­ndices `ini` e `fim` e um valor `m`.
    A funÃ§Ã£o atribui `m` a toda posiÃ§Ã£o de Ã­Â­ndice i de `vals` 
    tal que `ini` <= i < `fim`.

    PrÃ©-condiÃ§Ã£o. A funÃ§Ã£o supÃµe que 

           0 <= ini <= fim <= len(vals)

    Exemplos:
    >>> a = []
    >>> marque(a, 0, 0, 1)
    >>> a
    []
    >>> a = [0]
    >>> marque(a, 0, 0, 1)
    >>> a
    [0]
    >>> a = [0, 0, 0]
    >>> marque(a, 1, 1, 1)
    >>> a
    [0, 0, 0]
    >>> a = [0, 0, 0, 0]
    >>> marque(a, 0, 4, 1)
    >>> a
    [1, 1, 1, 1]
    >>> a = [0, 0, 0, 0]
    >>> marque(a, 2, 4, -1)
    >>> a
    [0, 0, -1, -1]
    >>> a = [1, 2, 3]
    >>> marque(a, 0, 2, 3)
    >>> a
    [3, 3, 3]
    >>> a = [3, 2, 3, 3, 3]
    >>> marque(a, 2, 4, 2)
    >>> a
    [3, 2, 2, 2, 3]
    >>> a = [1, 2, 3, 4, 5]
    >>> marque(a, 2, 4, 'X')
    >>> a
    [1, 2, 'X', 'X', 5]
    >>> 
    '''
    # escreva a sua funÃ§Ã£o a seguir
    while ini < fim:
        vals[ini] = m
        ini+=1
    
# ===============================================================

def marque_segmentos(vals, tamanho, m):
    '''(list, int, valor) -> None

    Recebe uma lista `vals`, um inteiro `tamanho`, e um valor `m`.
    A funÃ§Ã£o modifica a lista `vals` de forma que todos os segmentos 
    de comprimento `tamanho` tenham os seus valores alterados 
    para `m`.

    Voce deve utilizar obrigatoriamente a funÃ§Ã£o segmentos() 
    e marque().

    Exemplos
    >>> lista = [22, 22, 22, 'oi', 'oi', True, True, True, False, False, None]
    >>> marque_segmentos(lista, 1, 44)
    >>> lista
    [22, 22, 22, 'oi', 'oi', True, True, True, False, False, 44]
    >>> marque_segmentos(lista, 2, 'X')
    >>> lista
    [22, 22, 22, 'X', 'X', True, True, True, 'X', 'X', 44]
    >>> marque_segmentos(lista, 3, 'Y')
    >>> lista
    ['Y', 'Y', 'Y', 'X', 'X', 'Y', 'Y', 'Y', 'X', 'X', 44]
    >>> 
    '''
    # escreva a sua funÃ§Ã£o a seguir
    j = len(vals)
    seg = segmentos(vals)
    nova = seg + [j]
    n = len(nova)
    i=1  
    
    while i < n:
        fim = nova[i]
        ini = nova[i-1]
        if (fim - ini) == tamanho:
            marque(vals, ini, fim, m)
        i+=1

# ===============================================================

if __name__ == '__main__':
    main()