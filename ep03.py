"""
  Nome : Guilherme Navarro
  NUSP : 8943160
  Turma: 41
  Prof.: Hitoshi

  """
def main():
    print("Verificar se os vertices são lados de um triangulo retangulo\n")
    a=float(input("Digite o comprimento do primeiro cateto: "))
    b=float(input("Digite o comprimento do segundo cateto: "))
    c=float(input("Digite o valor da hipotenusa: "))
    d=c*c==a*a+b*b
    print(d)
main()