#LOGIN SIMPLES
from cmath import log
from json.tool import main
import time
from pprint import pprint

usr = ''
pwd = ''
lista_cadastro = {'Marcos':'1234'}
passe = ''
rept = ''

def print_slow(text,time_slow= 0.5):
    print(text)
    time.sleep(time_slow)

def menu_entrada(): 
    print_slow('\n\n\nSEJA BEM VINDO À MARCOLÂNDIA!')
    print_slow('Se você já possui uma conta, digite 1.')
    print_slow('Se deseja cadastrar uma nova conta, digite 2.')
    print_slow('Se deseja encerrar o programa, digite qualquer outro número.')
    return input('Escolha uma das opções: ')

def cadastro():
    novoUser = input('\n\n\nEntre com o nome de usuário: ')
    counter = 0
    while(novoUser in lista_cadastro):
        counter +=1
        print_slow('\n\tNome de usuário já existente! Favor escolher outro nome!')
        novoUser = input('Entre com outro nome de usuário: ')
        if counter == 3:
            print_slow('\n\n\tNumero de tentativas excedido')
    passwd = input('Escolha sua senha: ')
    rept = input('Repita sua senha: ')
    if (passwd != rept):
        print_slow('\n\tAs duas senhas devem ser a mesma!\n\n')
        return
    lista_cadastro[novoUser] = passwd
    print_slow(lista_cadastro)

def login():
    usuario = input('\n\n\nEntre com seu nome de usuário: ')
    if(usuario not in lista_cadastro):
        print('\n\tUsuário não cadastrado!')
        return
    
    if usuario not in lista_cadastro:
        print('\n\n\t\tNão encontrado')
        return
    passwd = input('Entre com sua senha: ')
    if (passwd == lista_cadastro[usuario]):
        print('\n\tConectado!')
        return
    print('\n\tSenha incorreta!')



while True:
    entrada = menu_entrada()

    if (entrada == '1'):
        login()

    elif (entrada == '2'):
        cadastro()
        

    else:
        print_slow('\n\n\nA MARCOLÂNDIA AGRADECE A SUA VISITA!')
        print_slow('Esperamos vê-lo novamente em breve')
        print_slow('Até logo!\n\n\n')
        break
    time.sleep(2)

