# Criar um script, na linguagem de programação de sua escolha, que:
#  Receba/Carregue uma lista com usuários e informações referentes a eles (por exemplo:
# lendo um arquivo de texto)
#  Consiga criar e bloquear os usuários dessa lista em algum sistema (de preferência o
# próprio sistema operacional)
#  Consiga alterar propriedades desse usuário no sistema (por exemplo: adicionar os
#  usuários carregados a um grupo ou alterar o nome do usuário)

import subprocess
import os
import time
import getpass


def main(action):

    if action == '1':
        insert()

    elif action == '2':
        lockUnlockUser()

    elif action == '3':
        changeUser()

    elif action == '4':
        exit()


def findUser(userID):

    findUser = subprocess.getoutput('grep {} /etc/passwd | cut -d":" -f 1'.format(userID))

    if len(findUser) >= 1:
        return True

    elif len(findUser) == 0:
        return False


def insert():

    option = input('Você está prestes a cadastrar usuarios no sistema. Deseja mesmo continuar?\n'
                   'Obs: O arquivo deve estar dentro da mesma pasta que o programa!\n'
                   'Nota: Senha padrao de criação: mudar@123\n'
                   'YES ou NO: ').lower()

    if option == 'yes':

        with open('cadastro_usuarios.csv', 'r') as openFile:

            for line in openFile.readlines():

                userID = line.split(' ')[0]
                userCPF = line.split(' ')[1]
                userPass = 'mudar@123'

                if findUser(userID) == False:

                    os.system('sudo adduser -m -s /bin/bash {} -c {} > /dev/null 2&>1'.format(userID, userCPF))
                    os.system('sudo echo -e "{}\n{}" | passwd {} &> /dev/null'.format(userPass, userPass, userID))
                    os.system('sudo chage -d 0 {}'.format(userID))
                    print('Usuário {} cadastrado no sistema.'.format(userID))
                    time.sleep(1)

                elif findUser(userID) == True:

                    print('Usuário {} já existe no sistema.'.format(userID))
                    time.sleep(3)

    elif option == 'no':

        return


def lockUnlockUser():

    option = input('Digite a opcao:\n'
                   '1 - Desbloquear usuario\n'
                   '2 - Bloquear usuario\n'
                   'opcao: ')

    if option == '1':

        cpf = input('Digite o CPF do usuario para desbloquear: ')

        try:

            getUser = subprocess.getoutput('grep "{}" /etc/passwd | cut -d":" -f 1'.format(cpf))

            if len(getUser) >= 1:

                os.system('passwd -u {}'.format(getUser))

                time.sleep(6)

            else:

                print('Usuário não encontrado no sistema.')

        except Exception as Erro:

            print('Mensgaem de erro: {}'.format(Erro))

    elif option == '2':

        cpf = input('Digite o CPF do usuario para bloquear: ')

        try:

            getUser = subprocess.getoutput('grep "{}" /etc/passwd | cut -d":" -f 1'.format(cpf))

            if len(getUser) >= 1:

                os.system('passwd -l {}'.format(getUser))

                time.sleep(6)

            else:

                print('Usuário não encontrado no sistema')
                time.sleep(6)

        except Exception as Erro:

            print('Mensagem de erro: {}'.format(Erro))


def changeUser():

    option = input('1 Para alterar o username do usuário\n'
                   '2 Para alterar a senha do usuario\n'
                   '3 Para colocar o usuario em algum grupo secundario\n'
                   'Opcao: ')

    if option == '1':

        cpf = input('Digite o CPF do usuário: ')

        try:

            getUser = subprocess.getoutput('grep "{}" /etc/passwd | cut -d":" -f 1'.format(cpf))

            if len(getUser) >= 1:

                newUserName = input('Digite o novo nome para o usuário usuário: ')

                olderUserName = subprocess.getoutput('grep "{}" /etc/passwd | cut -d":" -f 1'.format(cpf))
                print('Antigo nome de usuário: {}'.format(olderUserName))

                os.system('usermod -l {} {}'.format(newUserName, olderUserName))
                print('Novo nome de usuário: {}'.format(newUserName))
                time.sleep(6)

            else:

                print('Usuário não encontrado no sistema.')
                time.sleep(6)

        except Exception as Erro:

            print('Mensagem de Erro: {}'.format(Erro))
            time.sleep(6)

    elif option == '2':

        cpf = input('Digite o CPF do usuário: ')

        try:

            getUser = subprocess.getoutput('grep "{}" /etc/passwd | cut -d":" -f 1'.format(cpf))

            if len(getUser) >= 1:

                valid = False

                while valid == False:

                    newPass = getpass.getpass('Digite a nova senha para o usuário: ')
                    newPass2 = getpass.getpass('Digite novamente a nova senha: ')

                    if newPass != newPass2:

                        print('Senhas não coincidem')

                    else:

                        os.system('sudo echo -e "{}\n{}" | passwd {} > /dev/null 2>&1'.format(newPass, newPass, getUser))

                        print('Senha alterada com sucesso para o usuario {}'.format(getUser))
                        time.sleep(6)
                        valid = True

            else:

                print('Usuário não encontrado no sistema')
                time.sleep(6)

        except Exception as Erro:

            print('Mensagem de erro: {}'.format(Erro))
            time.sleep(6)

    elif option == '3':

        cpf = input('Digite o CPF do usuário: ')

        try:

            getUser = subprocess.getoutput('grep "{}" /etc/passwd | cut -d":" -f 1'.format(cpf))

            if len(getUser) >= 1:

                newGroup = input('Digite o grupo em que quer colocar no usuario: ')

                try:

                    getGroup = subprocess.getoutput('grep "{}" /etc/group | cut -d":" -f 1'.format(newGroup))

                    if len(getGroup) >= 1:

                        os.system('usermod -a -G {} {}'.format(newGroup, getUser))

                        print('Usuário {} inserido no grupo {}'.format(getUser, newGroup))
                        time.sleep(6)

                    else:

                        print('Grupo não existe no sistema')
                        time.sleep(6)

                except Exception as Erro:

                    print('Mensagem de erro: {}'.format(Erro))
                    time.sleep(6)

            else:

                print('Usuario nao encontrado no sistema')
                time.sleep(6)

        except Exception as Erro:

            print('Mensagem de erro: {}'.format(Erro))
            time.sleep(6)


while True:

    os.system('clear')

    main(input('Digite a opção:\n'
               '1 - Adicionar pools de usuarios no sistema\n'
               '2 - Bloquear/Desbloquear usuarios do sistema\n'
               '3 - Alterar Grupo, Username e Senha de usuario\n'
               '4 - Sair\n'
               'Opcao:  '))
