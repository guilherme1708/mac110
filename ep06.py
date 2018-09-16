"""
  Nome : Guilherme Navarro
  NUSP : 8943160
  Turma: 41
  Prof.: Hitoshi

  """
def main():
    print("Verificar a posição do mapa se esse tiro acertou ou errou o alvo")
    
    x=float(input("digite a coordenada x (horizontal): "))
    y=float(input("digite a coordenada y (vertical): "))
    dentro = True
    
    if 5 < x < 75 and -35 < y < 35: # esta dentro do mapa
        dentro = True
        if 5 < x < 35 and 5 < y < 10:
            dentro = True
        else:
            dentro = False
        if 5 < x < 10 and 10 <= y < 35:
            dentro = True
        if 15 < x < 25 and 5 < y < 25 and x<y:
            dentro =  True
        if 10 <= x <= 30 and 30 < y < 35:
            dentro = True
        if 30 < x < 35 and 10 <= y <= 30:
            dentro = True
        if 15 < x < 30 and -30 < y < 0:
            dentro = True
        if 30 <= x < 50 and -30 < y < -25:
            dentro = True
        if 35 < x < 40 and -15 < y < -10:
            dentro = True
        if 30 <= x < 50 and -5 < y < 0:
            dentro = True
        if 30 <= x < 50 and -30 < y < -25:
            dentro = True
        if 45 <= x < 50 and -25 < y < -5:
            dentro = True
        if 45 < x < 75 and 10 < y < 25:
            dentro = True
        if 65 < x < 75 and -35 < y <= 10:
            dentro = True
    else: #esta fora do mapa
        dentro = False
        
    if dentro:
        print("Acertou")
    else:
        print("Errou")
main()