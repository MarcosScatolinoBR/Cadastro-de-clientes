#LOGIN SIMPLES
import time

usr = ''
pwd = ''
Cadastro = {'Marcos':'1234'}
passe = ''
rept = ''


print('SEJA BEM VINDO À MARCOLÂNDIA!')
time.sleep(.5)
print('Se você já possui uma conta, digite 1.')
time.sleep(.5)
print('Se deseja cadastrar uma nova conta, digite 2.')
time.sleep(.5)
print('Se deseja encerrar o programa, digite 3.')
time.sleep(.5)
entrada = input('Escolha uma das opções: ')

if (entrada != 1 or entrada != 2 or entrada != 3):
    print('Favor entrar apenas com números referentes às opções!')
if (entrada == '1'):
    
    usuario = input('Entre com seu nome de usuário: ')
    if(usuario not in Cadastro):
        print('Usuário não cadastrado!')
    else:
        pw = Cadastro[usuario]
        if usuario in Cadastro:
            paswd = input('Entre com sua senha: ')
            if (paswd == pw):
                print('Conectado!')
                import boxmail
            else:
                print('Senha incorreta!')

if (entrada == '2'):
    novoUser = input('Entre com o nome de usuário: ')
    if(novoUser in Cadastro):
        print('Nome de usuário já existente! Favor escolher outro nome!')
        input('Entre com outro nome de usuário: ')
    else:
        passe = input('Escolha sua senha: ')
        rept = input('Repita sua senha: ')
        if (passe != rept):
            print('As duas senhas devem ser a mesma!')
        else:
            Cadastro[novoUser] = passe
            print(Cadastro)

if (entrada == '3'):
    print('A MARCOLÂNDIA AGRADECE A SUA VISITA!')
    time.sleep(.5)
    print('Esperamos vê-lo novamente em breve')
    time.sleep(.5)
    print('Até logo!')
    time.sleep(.5)
    exit()
