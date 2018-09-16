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

VAZIO = ''
ESPAÇO = ' '
LIMPAR = '\n'  # caracteres que precisam ser "limpados" do texto

# ============================================================

def main():
    '''
    Este programa pergunta pelo nome de um arquivo
    e o número cols de colunas, e imprime o conteúdo
    do arquivo justificado com C colunas.
    '''

    nome = input("Digite o nome do arquivo: ")
    cols = int(input("Digite o número de colunas: "))

    with open(nome, 'r', encoding='utf-8') as arq:
        texto = limpe_texto(arq.read())
    print("Texto original: ")
    print(texto)  
    print()
    justificado = justifique_texto(texto, cols)
    print("Texto justificado com %d colunas: "%(cols))
    print(justificado)

# ============================================================

def limpe_texto( texto ):
    ''' (str) -> str
    Substitui sequencias de caracteres espaço e `\n`
    por um único espaço.
    
    Exemplos:
    
    >>> texto1 = """
                 O    rato
                 roeu a    roupa
                 do        rei de Roma
                 """
    >>> texto2 = "Três pratos de    trigo\n\n    para   três tigres tristes"    
        
    >>> limpa_texto("")
    
    >>> limpa_texto("Cogito ergo sum")
    Cogito ergo sum
    >>> limpa_texto("Per                       to")
    Per to
    >>>limpa_texto("1\n2\n3")
    1 2 3
    >>> limpa_texto(texto1)
    O rato roeu a roupa do rei de Roma
    >>> limpa_texto(texto2)
    Três pratos de trigo para três tigres tristes
    '''
    mundo = texto.split()
    certo = VAZIO
    
    for pal in mundo:
        certo += (pal + ESPAÇO)
        
    limpo = certo.strip()
        
    return limpo

# ============================================================
    
def justifique_texto( texto, ncols ):
    ''' (str, int) -> str 
    Recebe um texto "limpo" (veja função limpe_texto()), e
    sem quebra de linhas e sem múltiplos espaços consecutivos,  
    e cria um novo texto justificado, ou seja, que possua linhas
    com as palavras justificadas. Em uma linha justificada,
    a primeira palavra encosta na 1a coluna e o final da última 
    palavra encosta na última coluna da linha.
    Observe que a última linha do texto não deve ser justificada.
    
    Exemplos:
    
    >>> justifique_texto("O rato roeu a roupa do rei de Roma", 5)
    O
    rato
    roeu
    a
    roupa
    do
    rei
    de
    Roma
    >>> justifique_texto("O rato roeu a roupa do rei de Roma", 10)
    O     rato
    roeu     a
    roupa   do
    rei     de
    Roma
    >>> justifique_texto("Qual a cor do cavalo branco de Napoleao?", 25)
    Qual   a  cor  do  cavalo
    branco de Napoleao?
    >>> justifique_texto("A dog is loyal to people, not to other dogs", 18)
    A  dog is loyal to
    people,   not   to
    other dogs
    >>> justifique_texto("A dog is loyal to people, not to other dogs", 60)
    A dog is loyal to people, not to other dogs
    '''
    lista = texto.split()
    just = VAZIO
    i = 0
    n = len(texto)
    fim = ncols
    
    if len(lista) <= 1:
        return texto
            
    while i < n and fim < n:
        while fim > i and texto[fim] != ESPAÇO:
            fim-=1
        just += espalhe_espacos(texto[i:fim],ncols) + LIMPAR
        i = fim+1
        fim += ncols+1
    
    just += texto[i:fim]

    return just
   

# ============================================================

def espalhe_espacos( texto, ncols ):
    ''' (str, int) --> str
    Recebe um texto com tamanho menor que ncols e insere brancos
    entre as palavras no texto de forma uniforme até que ele
    tenha ncols colunas. Se a quantidade de brancos não puder
    ser dividida igualmente entre as palavras, os buracos
    mais à esquerda serão sempre maiores ou iguais que 
    os da direita.
    
    Exemplos:
    
    >>> espalhe_espacos("", 10)
    
    >>> espalhe_espacos("umapalavra", 12)
    umapalavra
    >>> espalhe_espacos(" umapalavra", 15)
    umapalavra
    >>> espalhe_espacos("duas palavras", 20)
    duas        palavras
    >>> espalhe_espacos("uma mais duas", 15)
    uma  mais  duas
    >>> espalhe_espacos("uma mais duas", 14)
    uma  mais duas
    >>> espalhe_espacos("Longe? T a l v e z.", 30)
    Longe?   T   a   l   v   e  z.
    
    '''
    texto = texto.strip()
    lista = texto.split()
    n = len(texto)  
    espalhado = VAZIO
    n_esp = 0
    
    if len(lista) <= 1:
        return texto
    
    for car in texto:
        if car == ESPAÇO:
            n_esp += 1
            
    tam_esp = (ncols - n)//n_esp
    tamanho = (((ncols - n )//n_esp)+1)
    
    if ncols % len(lista) != 0:
        for car in texto:
            espalhado += car
            if car == ESPAÇO and n<ncols:  
                espalhado += tamanho * ESPAÇO
                n+=tamanho   
                            
    else:        
        for car in texto:
            espalhado += car
            if car == ESPAÇO:
                espalhado += tam_esp * ESPAÇO

    return espalhado

# ============================================================
if __name__ == '__main__':
    main() 