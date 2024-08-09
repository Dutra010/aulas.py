#Questão 2
a = int(input("primeiro termo: "))
b = int(input("segundo termo: "))
c = int(input("terceiro termo: "))
y = 0
for x in range (a,b + 1, c):
    y += x
print(y)
