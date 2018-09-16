# Digite seu programa 
def main():
    print("Calcular a soma dos algarismos digitados\n")
    num=int(input("Digite um numeo: "))
    soma=0
    while num>0:
        resto=num%10
        num=(num-resto)//10
        soma=soma+resto
    print(soma)
main()