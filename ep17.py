#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÃALHO 
# NÃO ALTERE OS NOMES DAS FUNÃÃES
# NÃO APAGUE OS DOCSTRINGS
#------------------------------------------------------------------

'''

    Nome: Guilherme Navarro
    NUSP: 8943160

    Ao preencher esse cabeÃ§alho com o meu nome e o meu nÃºmero USP,
    declaro que todas as partes originais desse exercÃ­cio programa (EP)
    foram desenvolvidas e implementadas por mim e que portanto nÃ£o 
    constituem desonestidade acadÃªmica ou plÃ¡gio.
    Declaro tambÃ©m que sou responsÃ¡vel por todas as cÃ³pias desse
    programa e que nÃ£o distribui ou facilitei a sua distribuiÃ§Ã£o.
    Estou ciente que os casos de plÃ¡gio e desonestidade acadÃªmica
    serÃ£o tratados segundo os critÃ©rios divulgados na pÃ¡gina da 
    disciplina.
    Entendo que EPs sem assinatura devem receber nota zero e, ainda
    assim, poderÃ£o ser punidos por desonestidade acadÃªmica.

'''

def main():
    '''
    Testa a funÃ§Ã£o uniÃ£o de listas ordenadas
    '''

    # teste pertence()
    print("pertence(1, []):", pertence(1, []))
    print("pertence(1, [2, 3, 4]):", pertence(1, [2, 3, 4]))
    print("pertence(1, [2, 1, 4]):", pertence(1, [2, 1, 4]))
    print("pertence('abc', [-1, 5, 'MAC0110']):", pertence('abc', [-1, 5, 'MAC0110']))
    print("pertence(10, [2, 1, 4, 5, 4, 8, 10]):", pertence(10, [2, 1, 4, 5, 4, 8, 10]))

    # teste uniao()
    lista1 = [-1, 1, 2, 3]
    lista2 = [1, 2, 2]
    print("lista 1:", lista1)
    print("lista 2:", lista2)
    print("uniao(lista1,lista2):", uniao(lista1, lista2))
    uniao1 = uniao(lista1, lista2)
    print("uniao1:", uniao1)
    lista2 = [-5, 7, 7, 123]
    print("lista 2:", lista2)
    uniao2 = uniao(uniao1, lista2)
    print("uniao(uniao1,lista2):", uniao2)
    
    # escreva abaixo outros testes
    lista3 = [12,21,35]
    lista4 = [1,2,2,3,7,11]
    uniao3 = uniao(lista3, lista4)
    print("uniao(lista3,lista4):", uniao(lista3, lista4))
    
# ===============================================================
def pertence(elemento, seq):
    ''' (valor, list) -> bool

    Recebe um valor `elemento` e uma lista `seq`. 
    A funÃ§Ã£o deve percorrer a lista e retornar True caso `elemento` esteja 
    na lista `seq`, e False em caso contrÃ¡rio.
    
    Exemplos:
    >>> pertence(1, [])
    False
    >>> pertence(1, [2, 3, 4])
    False
    >>> pertence(1, [2, 1, 4])
    True
    >>> pertence('abc', [-1, 5, 'MAC0110'])
    False
    '''
    # escreva a sua funÃ§Ã£o a seguir
    i = 0
    
    if len(seq) == 0:
        return False
    
    while i < len(seq) :
        if elemento == seq[i]:
            return True
        i+=1
    return False
    
# ===============================================================
def uniao(seq1, seq2):
    ''' (list, list) -> list

    Recebe duas listas de nÃºmeros `seq1` e `seq2` ordenados crescentemente. 
    Cada lista _pode_ conter elementos repetidos.
    A funÃ§Ã£o cria e retorna uma lista, tambÃ©m ordenada, com os nÃºmeros 
    de seq1 e seq2. A lista retornada _nÃ£o deve_ conter nÃºmeros 
    repetidos e seus elementos _devem_ estar ordenados crescentemente.
    
    Exemplos:
    
    >>> uniao([11, 11, 11], [])
    [11]

    >>> uniao([11, 11, 11], [11, 11])
    [11]

    >>> uniao([1,2,3], [1,2,2]) 
    [1, 2, 3]

    >>> uniao([2,3,7], [1,5,7,16])
    [1, 2, 3, 5, 7, 16]

    >>> uniao([12,21,35], [1,2,2,3,7,11])
    [1, 2, 3, 7, 11, 12, 21, 35]
    '''

    # escreva a sua funÃ§Ã£o a seguir
    seq3 = seq1 + seq2
    
    nova = list(set(seq3))
    uniao = crescente (nova)
    return uniao
# ===============================================================
def crescente(lista):
    ''' (list) -> (list) 
    Recebe uma lista e coloca os valores em ordem crescente
    
    Exemplos:
    
    >>> crescente([35, 2, 7, 3, 11, 21, 11, 1])
    [1, 2, 3, 7, 11, 12, 21, 35]
    
    >>> crescente([5, 8, 9, 1, 2])
    [1, 2, 5, 8, 9]
    '''
    # função crescente
    ordem = len(lista)
    i = 0
    crescente = []
    
    while i < ordem:
        j = i + 1
        while j < ordem:
            if lista[i] > lista[j]:
                temp = lista[i]
                lista[i] = lista [j]
                lista[j] = temp
            j+=1
        i+=1
        
    i = 0

    while i < ordem:
        crescente = crescente + [lista[i]]
        i+=1
    return crescente

# ===============================================================

if __name__ == '__main__':
    main()
