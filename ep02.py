"""
  Nome : Guilherme Navarro
  NUSP : 8943160
  Turma: 41
  Prof.: Hitoshi

  """
def main():
    print("Calcular IMC\n")
    p=float(input("Digite Seu altura em metros: "))
    a=float(input("Digite sua massa em kilogramas: "))
    i= a/(p*p)
    print("Seu IMC é: ", i)
main()