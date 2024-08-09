nome_mais_barato = ""
valor_mais_barato = float("inf")
total_dos_preços = 0

for medicamento in range(5):
    nome = input(f"DIgite o nome do medicameto {medicamento + 1}: ")
    valor = float(input(f"Informe o valor do medicamento: {medicamento + 1}:  "))
    
    if valor < valor_mais_barato:
        nome_mais_barato = nome
        valor_mais_barato = valor
        total_dos_preços += valor
media = total_dos_preços / 5
print (f"Medicamento mais barato: {nome_mais_barato} - Preço mais barato {valor_mais_barato:.2f}")
print (f"A media dos preços é: {media:.2f}")
