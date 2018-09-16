"""
  Nome : Guilherme Navarro
  NUSP : 8943160
  Turma: 41
  Prof.: Hitoshi

  """
def main():
    print("Verificar se um numero é soma de um trio Pitagoreano")

    n = int(input("Digite o valor de n: "))
    achei = False
    a = 1

    while a < n and not achei:
        b = a+1
        while b < n-a and not achei:
            c = n - a - b  
            if a*a + b*b == c*c and a+b+c == n:
                achei = True
            b += 1
        a += 1
    
    if achei:
        a -= 1
        b -= 1
        print(n, "é soma do trio (%d, %d, %d)" %(a,b,c))
    else:
        print(n, "não é soma de trio Pitagoreano")
        
main()