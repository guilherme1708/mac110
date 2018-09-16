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

#------------------------------------------------------------------
def main():
    '''
    A funÃ§Ã£o main() nÃ£o serÃ¡ considerada na correÃ§Ã£o.

    No entanto, testes sÃ£o fundamentais para o desenvolvimento da sua 
    soluÃ§Ã£o. Teste cada uma de suas funÃ§Ãµes, individualmente, antes de 
    entregar o exercÃ­cio.

    Coloque aqui testes das suas funÃ§Ãµes conta_digito e 
    digitos_certos. 
    '''
    n, s, c = 6, 73, 37345
    print("digitos_certos(%d, %d, %d) = %d"%(n, s, c, digitos_certos(n,s,c)))
    
    n, s, c = 7, 4, 37345
    print("digitos_certos(%d, %d, %d) = %d"%(n, s, c, digitos_certos(n,s,c)))
    
    n, s, c = 6, 0, 37345
    print("digitos_certos(%d, %d, %d) = %d"%(n, s, c, digitos_certos(n,s,c)))
    
    n, s, c = 6, 0, 1001
    print("digitos_certos(%d, %d, %d) = %d"%(n, s, c, digitos_certos(n,s,c)))
    
    n, s, c = 16, 43245325, 1545345001
    print("digitos_certos(%d, %d, %d) = %d"%(n, s, c, digitos_certos(n,s,c)))
    
    n, s, c = 20, 548343245325, 3451545345001
    print("digitos_certos(%d, %d, %d) = %d"%(n, s, c, digitos_certos(n,s,c)))
    
    # escreva a seguir outros testes que desejar.
#------------------------------------------------------------------
def conta_digitos(ndig, dig, num):
   ''' (int, int, int) -> int

   Recebe um inteiro ndig > 0, um dÃ­gito 0 <= dig <= 9, e um inteiro num,
   0 <= num < 10**ndig, e retorna o nÃºmero de vezes que dig ocorre
   como dÃ­gito de num.

   Exemplos:
   
   >>> conta_digitos(6, 3, 37345)
   2
   >>> conta_digitos(7, 4, 37345)
   1
   >>> conta_digitos(6, 0, 37345)
   1
   >>> conta_digitos(6, 0, 1001)
   4
   >>>
   '''
   # Função p/ contar os digitos
   n_dig=0
   i=0
   
   while i<ndig:
       if dig == num%10:
           n_dig+=1
       num=num//10    
       i+=1

   return n_dig
#------------------------------------------------------------------
def digitos_certos(ndig, segredo, chute):
    ''' (int, int, int) -> int

    Recebe um inteiro ndig, dois inteiros segredo e chute,
    0 <= segredo < 10**ndig e 0 <= chute < 10**ndig, e
    retorna o nÃºmero de dÃ­gitos certos entre segredo e
    chute.
    
    Exemplos:
    >>> digitos_certos(6, 73, 037345)
    3
    >>> digitos_certos(7, 4, 0037345)
    3
    >>> digitos_certos(6, 0, 37345)
    1
    >>> digitos_certos(6, 0, 1001)
    4
    >>> digitos_certos(16, 43245325, 1545345001)
    13
    >>> digitos_certos(20, 548343245325, 3451545345001)
    16
    >>>
    '''
    # Função p/ digitos certos
    n_correto=0
    i=0
    achou = False 

    while i<ndig:
        if segredo%10 == chute%10:
            segredo= segredo//10
            achou = True
            if achou:
                n_correto+=1
     
        chute= chute//10
        i+=1
      
    return n_correto

#------------------------------------------------------------------

if __name__ == '__main__':
    main()