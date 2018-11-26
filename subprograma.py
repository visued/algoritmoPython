from math import factorial as fat
def tabuada(nro):
    n = float(nro)
    for i in range(0,11):
        print("{0} x {1} = {2}".format(n, i, n*i))

def imc(peso, altura):
    p = float(peso)
    a = float(altura)
    print("O calculo do IMC: {:0.2f}".format(p/a*a))

def fatorial(nro):
    print("O fatorial do número {0} é: {1}".format(nro, fat(int(nro))))

def menorElemento(vet):
    print("O menor elemento do vetor é: {0}".format(min(vet)))

def media(vet):
    media = 0
    for k in vet:
        if(float(k) % 2 != 0):
            media += float(k) / 20
    print("A média dos elementos impares do vetor é: {0}".format(media))

op = 0
vet = []
vet2 = []
while(op != "-1"):
    print(30 * '-')
    print('| 1 - Tabuada                |')
    print('| 2 - IMC                    |')
    print('| 3 - Fatorial               |')
    print('| 4 - Menor elemento digitado|')
    print('| 5 - Média dos impares      |')
    print(30 * '-')
    op = input('Digite a operação: ')
    if(op == "1"):
        nro = input('Digite um número para tabuada: ')
        tabuada(nro)
    elif(op == "2"):
        p = input('Digite o peso: ')
        a = input('Digite a altura: ')
        imc(p, a)
    elif(op == "3"):
        nro = input('Digite o número para o fatorial: ')
        fatorial(nro)
    elif(op == "4"):
        for i in range(10):
            vet.append(input('Digite o número para a posição {0} do vetor: '.format(i)))
        menorElemento(vet)
    elif(op == "5"):
        for i in range(20):
            vet.append(input('Digite o número para a posição {0} do vetor: '.format(i)))
        media(vet)
    else:
        print("O valor digita não é valido!")
print("saindo....")
