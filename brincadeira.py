#Exercio Jaque brincadeira para acertar numeros.
nro = input("Insira um numero: ")

while True:
    dig = input("Insira um numero: ")

    if (dig > nro):
        print("O numero digitado eh maior")
    elif (dig < nro):
        print("O numero digitado eh menor")
    elif (dig == nro):
        print("Voce acertou o numero!!!")
        break
    else:
        print("Numero invalido, saindo...")
        break
