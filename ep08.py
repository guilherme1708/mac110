"""
  Nome : Guilherme Navarro
  NUSP : 8943160
  Turma: 41
  Prof.: Hitoshi

  """
def main():
    print("Verificar se todos os números da sequência são ímpares")
    
    n = int(input("Digite o valor de n: "))
    i=0
    achei = False
    
    while i<n and not achei :
        num = int(input("Digite um número: "))
        if num%2 == 0:
            achei = True
            print("\nPar na Posição ", i)
        i+=1
    if not achei:
        print("\nTodos ímpares")
main()