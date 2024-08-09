#Questão 1 

a= int(input("digite um numero inteiro"))
b= int(input("digite outro numero inteiro"))

soma = 0
if a<b:
    for x in range(a,b+1):
        soma += x
    print(soma)
    
else:
    print("Erro!")
