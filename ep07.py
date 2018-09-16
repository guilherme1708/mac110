"""
  Nome : Guilherme Navarro
  NUSP : 8943160
  Turma: 41
  Prof.: Hitoshi

"""
def main():
    print("Verificar se é triangulo e se for indicar a classifição dele quanto ao ângulo e o lado")
    
    a = int(input("Digite um inteiro: "))
    b = int(input("Digite um inteiro: "))
    c = int(input("Digite um inteiro: "))
    if a >= b + c or b >= a + c or c >= a + b:
        print("Não é um triângulo")
    else:
        if a*a == b*b + c*c or b*b == a*a + c*c or c*c == a*a + b*b:
            print("retângulo")
        elif a*a >  b*b + c*c or b*b >  a*a + c*c or c*c >  a*a + b*b:
            print("obtusângulo")
        else:
            print("acutângulo")
        if  c == a == b:
            print("equilátero")
        elif a == c or a == b or b == c:
            print("isósceles")
        else:
            print("escaleno")
main()