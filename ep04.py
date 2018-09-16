# programa principal
# ------------------
def main():
    print("Cálculo do fatorial de um número\n")
    n = int(input("Digite um número inteiro positvo: "))
    i=1
    fat=1
    while i<=n:
        fat=fat*i
        i=i+1
    print(fat)
main()
