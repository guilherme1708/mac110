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

import math
# utilize a função sqrt do pacote math
# Por exemplo, para calcular a raiz de 2 use
# math.sqrt(2)


#------------------------------------------------------------------
def main():
    '''
    A função main() não será considerada na correção.

    No entanto, testes são fundamentais para o desenvolvimento da sua 
    solução. Teste cada uma de suas funções, individualmente, antes de 
    entregar o exercício.

    Coloque aqui testes das suas funções 
    '''
    a, b, k = 0, 1, 5
    print('retangulo(%f, %f, %d) = %f'%(a, b, k, retangulo(a, b,k)))
    a, b, k = 0.1, 0.8, 7
    print('retangulo(%f, %f, %d) = %f'%(a, b, k, retangulo(a, b,k)))   
    a, b, k = 0, 1, 7
    print('retangulo(%f, %f, %d) = %f'%(a, b, k, retangulo(a, b,k)))
    a, b, k = 0, 1, 1
    print('retangulo(%f, %f, %d) = %f'%(a, b, k, retangulo(a, b,k)))
    a, b, k = 0, 1, 2
    print('retangulo(%f, %f, %d) = %f'%(a, b, k, retangulo(a, b,k)))
           
    eps = 0.0001
    print('aproxima_pi(', eps, ') = ', aproxima_pi(eps))
    eps = 0.000001
    print('aproxima_pi(', eps, ') = ', aproxima_pi(eps))
    eps = 0.00000001
    print('aproxima_pi(', eps, ') = ', aproxima_pi(eps))

    # escreva a seguir outros testes que desejar.
    
#------------------------------------------------------------------
def erro_rel(y, x):
    ''' (float, float) -> float

    Recebe dois reais y e x, e retorna o erro relativo entre y e x
    como |(y-x)/x|, ou 0 se x=0=y ou 1 se x=0!=y.

    Exemplos:
   
    >>> erro_rel(0, 0)
    0.0
    >>> erro_rel(1, 0)
    1.0
    >>> erro_rel(0.2, 0.1)
    1.0

    '''
    # substitua o trecho de código a seguir com a sua função
    if y!=0 and x==0:
        return 1.0
    elif y==0 and x==0:
        return 0.0
    else:
        erro=(y-x)/x
        if erro>0:
            return erro
        return -erro
   
#------------------------------------------------------------------
def retangulo(a, b, k):
    ''' (float, float, int) -> float

    recebe dois reais que definem um intervalo real [a, b] e calcula 
    a área da função semi-circunferência de raio 1 nesse intervalo
    usando o método dos retângulos com k retângulos, como descrito
    no enunciado.
    
    Exemplos:
    >>> retangulo(0, 1, 5)
    0.7929969559032712
    >>> retangulo(0.1, 0.8, 7)
    0.6043246777819646
    >>> retangulo(0, 1, 7)
    0.7900030470802559    

    Utilize a função sqrt do pacote math.
    '''
    # substitua o trecho de código a seguir com a sua função
    largura = (b-a)/k
    x = (a+(largura/2))
    i = 1
    area = 0
    while i<=k:
        altura = (math.sqrt(1 -(x*x)))
        area = area + altura*largura
        x = (a+(2*i+1)*(largura/2))
        i+=1    
    return area

#------------------------------------------------------------------
def aproxima_pi( eps ):
    ''' (float) -> float
    recebe um real eps e retorna a aproximação de pi considerando
    o cálculo da área do 1o quadrante da semicircunferência de
    raio unitário usando o método dos retângulos.
    A função deve calcular a área usando valores de k na sequência
    1, 2, 4, 8, 16, etc
    até que o erro relativo entre duas iterações consecutivas seja
    menor que eps. Ou seja, se o erro relativo do valor de pi 
    a partir das áreas calculadas usando k = 4 e k = 8 for menor 
    que eps, então a função deve retonar o valor de pi calculado 
    com k = 8.

    Exemplos:
    >>> aproxima_pi (0.0001)
    3.1416767224820807
    >>> aproxima_pi (0.00001)
    3.1416031642838775
    >>> aproxima_pi (0.0000001)
    3.1415928178295482
    '''
    # substitua o trecho de código a seguir com a sua função
    a,b = 0,1
    k = 1
    ret0 = retangulo(a, b, k)
    k = 2
    ret1 = retangulo(a, b, k)
    erro = erro_rel(ret0, ret1)
    
    while erro >= eps:
        k*= 2
        ret0 = ret1
        ret1 = retangulo(a, b, k)
        erro = erro_rel(ret1, ret0)
        
    pi=4*ret1
    
    return pi


#------------------------------------------------------------------
if __name__ == '__main__':
    main()