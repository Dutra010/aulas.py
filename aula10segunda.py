senha_correta = 123456 
tentativasmaximas= 3

for tentativa in range (3):
    senha = int(input(f"Digite a sua senha: "))

    if senha == senha_correta:
        print("Senha correta")
        exit()
    else:
        tentativasrestantes = tentativasmaximas - (tentativa+1)
        if tentativasrestantes > 0:
            print(f"Senha incorreta! Voce ainda tem {tentativasrestantes} tentativas")
        else:
            print("Conta bloqueada!")
