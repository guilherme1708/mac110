"""
  Nome : Guilherme Navarro
  NUSP : 8943160
  Turma: 41
  Prof.: Hitoshi

  """
def main():
    print("Verificar se um número é alternante")
    
    n = int(input("Digite n: "))
    achei = False

    
    while n>10 and not achei:
        r=n%10
        a=n//10
        n=a%10
        if r==n:
            achei = True
                
    if not achei:
        print("Sim")
    else:
        print("Não")
         
        
main ()