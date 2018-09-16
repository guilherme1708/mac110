"""
  Nome : Guilherme Navarro
  NUSP : 8943160
  Turma: 41
  Prof.: Hitoshi

  """
def main():
    print("Verificar se é possível trocar uma cédula de valor c por um punhado de moedas de valor a e b")
    
    a=int(input("Digite o valor de uma moeda: "))
    b=int(input("Digite o valor da outra moeda: "))
    c=int(input("Digite o valor da cédeula: "))
    achou = False
    i=0
    
    if b<a:
        a, b = b, a 
        
    while i <= c//a and not achou:
        j=0
        while j <= c//b and not achou:
            if a*i + b*j == c:
                achou = True
                if a > b:
                    print("\n%d moeda(s) de %d e %d moeda(s) de %d" %(i,a,j,b))
                else:
                    print("\n%d moeda(s) de %d e %d moeda(s) de %d" %(j,b,i,a))
            j+=1
        i+=1
            
    if not achou:
        print("\nNão é possível trocar a cédula")
        
main()