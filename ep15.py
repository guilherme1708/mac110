#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÃ‡ALHO 
# NÃƒO ALTERE OS NOMES DAS FUNÃ‡Ã•ES
# NÃƒO APAGUE OS DOCSTRINGS
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
import random

def main():
    '''
    Programa do MasterMind
    '''
    print("Tente adivinhar o número secreto de 1 a 1000! Você terá 10 tentativas!")
    semente = int(input("Digite uma semente para geração do número aleatório: "))
    random.seed(semente)
    num = random.randint(0, 99999)
    tent = 0
    acertou = False
    
    while tent < 10 and not acertou:
        tent+=1
        chute = int(input("Tentativa %d : " %(tent)))
        
        posicao = posicoes_certas(5, num, chute)
        certo = digitos_certos(5, num, chute)
        
        print("Numero de digitos na posição certa = ", posicao)
        print("Numero de digitos certos = ", certo)
        if posicao == 5:
            acertou = True
        
    if acertou:
        print("Parabens! Voce advinhou o numero")
    else:
        print("\nVocê não conseguiu adivinhar!")
        print("O número sorteado foi %d." %(num))
    
# ===============================================================

# escreva aqui outras funÃ§Ãµes que desejar, incluindo 

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
    
# ===============================================================

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
    cont=0
    i=0
    while i< segredo:
        j=0
        while j< chute:
            if segredo == chute%10:
                cont+=1
            segredo = segredo//10
            j+=1
        i+=1
    return cont

# ===============================================================

# ===============================================================

if __name__ == '__main__':
    main()