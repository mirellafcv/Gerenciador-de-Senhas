import random
import time
# A lista de senhas
randoms = ['123456789', '987654321', '1029384756']
escolhaale = random.choice(randoms)
senhas = {}
print("Olá! Criei um projeto onde você pode salvar todas as suas senhas em um só lugar! Além disso, você também poderá adicionar, editar ou remover senhas.")
time.sleep(3)
print("Abaixo está a sua lista atual de senhas")
print(senhas)


def adicionar(nome, senha):
    senhas[nome] = senha
def remover(nome):
    del senhas[nome]

while True:

    time.sleep(1)
    add = input("Você quer adicionar uma senha?").lower()
    if add == "sim":
        nome = input("Qual nome você quer dar a sua senha?")
        senha = input("Qual é a sua senha?")
        adicionar(nome, senha)
    else:
        print("ok")
    time.sleep(1)
    print("Abaixo está a sua lista atual de senhas")
    print(senhas)

    ale = input("Você deseja que uma senha aleatória seja criada?")
    if ale == "sim":
        nome = input("Qual o nome você quer dar a sua senha?")
        adicionar(nome,escolhaale)
        print(senhas)
    else:
        print("ok")

    rem = input("Você quer remover alguma senha?").lower()
    if rem == "sim":
        nome = input("Qual senha você quer remover? (Digite o nome dela)")
        remover(nome)
    else:
        print("ok")
    time.sleep(1)
    print("Abaixo está a sua lista atual de senhas")
    print(senhas)

    edit = input("Você quer editar alguma senha?").lower()
    if edit == "sim":
        nome = input("Qual senha você quer editar? (Digite o nome dela)")
        senha = input("Para o que quer mudar a senha?")
        adicionar(nome, senha)
    else:
        print("ok")
    time.sleep(1)
    print("Abaixo está a sua lista atual de senhas")
    print(senhas)

    acabar = input("Você deseja encerrar?").lower()
    if acabar == "sim":
        break
    else:
        print("ok")
