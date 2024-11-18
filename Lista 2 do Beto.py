# ex1 SOMA _________________________________________________________________________________________

def soma (num1,num2):
    soma = num1+num2
    print (soma)
    return soma

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

soma(num1,num2)

# # ex2 VERIFICAR NUM PAR ___________________________________________________________________________

num1 = int (input("Digite um número para descobrir se é par ou ímpar: "))

if (num1 % 2) == 0:
    print("O número", num1, "é par.")
else:
    print("O número", num1, "é ímpar.")

# # ex3 PASSAR DE C PARA F __________________________________________________________________________

temp = int(input("Digite a temperatura em Celsius para transformarmos em Fahrenheit: "))
temp1 = ((temp * 1.8)+32)
print ("A temperatura em Celsius é: ", temp, "e em Fahrenheit: ", temp1) 

# # ex4 CONTAR LETRAS DE UMA PALAVRA ________________________________________________________________

palavra = input("digite uma palavra: ")
plv = len(palavra)
print ("sua palavra tem: ", plv,"letras.")

# #ex5 MOSTRAR TABUADA DE NUMERO X __________________________________________________________________

num = int(input("Digite o número que deseja saber a tabuada: "))
for x in range (1, 11):
    x1 = (num * x)
    print (num, "x", x, "=", x1)

# # ex6 CALCULAR MEDIA DE 3 NOTAS ____________________________________________________________________

prova1 = float(input("Digite a nota que tirou na sua primeira prova: ")) 
prova2 = float(input("Digite a nota que tirou na sua segunda prova: ")) 
prova3 = float(input("Digite a nota que tirou na sua terceira prova: "))
media = (prova1+prova2+prova3)/3
print("Sua média foi de: ",media) 

# # ex7 ESCREVER PALAVRA DE TRÁS PRA FRENTE __________________________________________________________

palavra = input("Digite uma palavra e eu te mostrarei ela ao contrário: ")
palavrai = ""

for letra in range (len(palavra)):
    palavrai = palavra[letra] + palavrai
print(palavrai) 

# # ex8 MOSTRAR QUANTOS NUMEROS TEM NUMA LISTA _______________________________________________________

nums = [1,5,7,2,7,734,234,765]
qnt = len(nums)
print (qnt)

# # ex9 VERIFICAR SE É MAIOR DE IDADE ________________________________________________________________

idade = int(input("digite sua idade: "))
if idade > 18:
    print("você é maior de idade!")
else:
    print("você é menor de idade")

# # ex10 DAR A AREA DE UM RETANGULO __________________________________________________________________

base = int(input("Digite o valor da Base do retangulo: "))
altura = int(input("Digite o valor da Altura do retangulo: "))
area = (base*altura) /2

print("A área do seu retângulo é: ",area)

# # ex11 CONTAR PALAVRAS UNICAS ______________________________________________________________________

palavra = (input("Digite um texto: ").lower())
palavraU = palavra.split()
letras = set(palavra.replace(" ", ""))

print("as palavras que não se repetem são: ", (set(palavraU)),
 "as letras que não se repetem são: ",(letras), "totalizando ",(len(letras),"letras"))

# # ex12 NUM PRIMOS ENTRE 2 NUM _________________________________________________________________________

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Agora o segundo numero: "))
contador = 0

for x in range (num1, num2 +1):
    contador = 0
    for y in range (1, x +1):
        if x % y == 0:
            contador +=1
    if contador == 2:
        print (x, "é primo")

#_______________________________________ D E S A F I O ___________________________________________________
#______________encontrar todos os numeros perfeitos dentro de um intervalo de números_____________________

# num1 = int(input("Digite o primeiro numero: "))
# num2 = int(input("Agora o segundo numero: "))
# divisores = []

# # ex: 6 seu divisores são 1,2,3 e 1+2+3 = 6
# for x in range (num1, num2 +1): 
#     for y in range (1, x): 
#         if x % y == 0:
#             divisores.append(y)
#             print (divisores)

# # ex13 RECEBER NOTAS E MOSTRAS AS ACIMA DA MÉDIA _________________________________________________________

notas = [6,5,3.5,7,8.8,9,6,3,6.8]
print("As notas acima da média de 6 são: ")

for x in range (len(notas)):
    if notas[x] >= 6:
        print(notas[x])

# # ex14 CONFERIR SE PALAVRA É PALINDROMO ____________________________________________________________________

palavra = input("Digite uma palavra e eu te mostrarei ela ao contrário: ")
palavrai = ""

for letra in range (len(palavra)):
    palavrai = palavra[letra] + palavrai
print("Ao contrário sua palavra fica: ",palavrai) 

if palavrai == palavra:
    print ("Sua palavra é um palindromo")
else:
    print ("Sua palavra não é um palindromo")

# #ex15  JOGO DE ADIVINHACAO ________________________________________________________________________________

from random import randint

numsec = randint (1,100)
chutes = 0
tentativa = int(input("Chute um número de 0 a 100 e tente acertar o que eu pensei: "))

while tentativa != numsec:
    chutes += 1
    if tentativa < numsec:
        tentativa = int(input("Você errou, o número que pensei é MAIOR que seu chute, tente novamente !"))
    else:
        tentativa = int(input("Você errou, o número que pensei é MENOR que seu chute, tente novamente !"))
if tentativa == numsec:
    print("parabéns, você acertou na sua",chutes +1,"tentativa !")

# # ex16 CALCULAR FATORIAL _____________________________________________________________________________________

def fat (i):
    if i == 1:
        return 1
    else:
        return i * fat(i - 1)
    
num = int(input("Digite um número e eu te mostrarei seu fatorial: "))
print ("O fatorial de",num,"é",(fat (num)))
            
# #ex 17 ORDENAR NUMEROS _____________________________________________________________

list = [0,-3,-12,584,-213,83,10,2,-7]
list.sort()
print("Sua lista é",list)