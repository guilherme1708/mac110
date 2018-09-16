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

#------------------------------------------------------------------

def main():
    '''
    A função main() não será considerada na correção.
    
    No entanto, testes são fundamentais para o desenvolvimento da sua 
    solução. Teste cada uma de suas funções, individualmente, antes de 
    entregar o exercício.
    
    Coloque a seguir testes para a sua função posicoes_certas.
    '''
    n, s, c = 3, 467, 746
    print("posicoes_certas(%d, %d, %d) = %d"%(n, s, c, posicoes_certas(n,s,c)))
    
    n, s, c = 4, 467, 746
    print("posicoes_certas(%d, %d, %d) = %d"%(n, s, c, posicoes_certas(n,s,c)))
    
    n, s, c = 5, 467, 746
    print("posicoes_certas(%d, %d, %d) = %d"%(n, s, c, posicoes_certas(n,s,c)))
    
    n, s, c = 3, 123, 23
    print("posicoes_certas(%d, %d, %d) = %d"%(n, s, c, posicoes_certas(n,s,c)))
    
    n, s, c = 4, 1, 1
    print("posicoes_certas(%d, %d, %d) = %d"%(n, s, c, posicoes_certas(n,s,c)))

    n, s, c = 10, 0, 0
    print("posicoes_certas(%d, %d, %d) = %d"%(n, s, c, posicoes_certas(n,s,c)))

    n, s, c = 10, 34567, 1234567
    print("posicoes_certas(%d, %d, %d) = %d"%(n, s, c, posicoes_certas(n,s,c)))

    n, s, c = 10, 1234567890, 9876543210
    print("posicoes_certas(%d, %d, %d) = %d"%(n, s, c, posicoes_certas(n,s,c)))
    
    # escreva a seguir outros testes que desejar.
    n, s, c = 4, 123, 10
    print("posicoes_certas(%d, %d, %d) = %d"%(n, s, c, posicoes_certas(n,s,c)))

# -----------------------------------------------------------------------------

def posicoes_certas(ndig, segredo, chute):
    '''(int, int, int) -> int
    
    Recebe um inteiro ndig > 0, dois inteiros segredo e chute,
    0 <= segredo < 10**ndig e 0 <= chute < 10**ndig e retorna o número
    de posições certas de segredo e chute,

    Exemplos:
    >>> posicoes_certas(3,467,746)
    0
    >>> posicoes_certas(4,467,746) # 0467 e 0746
    1
    >>> posicoes_certas(5,467,746) # 00467, 00746
    2
    >>> posicoes_certas(3,123,23)
    2
    >>> posicoes_certas(4,1,1) # 0001 e 0001
    4
    >>> posicoes_certas(10,0,0) # 0000000000 0000000000
    10
    >>> posicoes_certa(10,34567,1234567) # 0000034567 e 0001234567
    8
    >>> posicoes_certa(10,1234567890,9876543210) #
    2
    >>>
    '''
    n_correto=0
    i=0
    
    while i<ndig:
        if segredo%10 == chute%10:
            n_correto+=1
        segredo= segredo//10
        chute= chute//10
        i+=1
    return n_correto

# -----------------------------------------------------------------------------

if __name__ == "__main__":
    main()