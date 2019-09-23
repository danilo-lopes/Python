# Criar um Shell script que consiga:
# Conectar em um banco de dados de sua escolha e realizar operações nele
# Alterar permissões (GRANT/REVOKE) no banco de dados (por exemplo: UPDATE TABLE)
# para um usuário ou uma lista de usuários

import mysql.connector
import os
import time


def main(action):

    if action == '1':
        setPrivileges()

    elif action == '2':
        exit()


def setPrivileges():

    # Conexão com o banco
    db_connector = mysql.connector.connect(host='localhost', db='autoseg_production',
                                           user='admin_autoseg', password='Dan15331923@.')
    # Responsavel por manter a conexão aberta e nos da o shell do banco
    cursor = db_connector.cursor()

    UserOption = input('1 - Para Setar permissão\n'
                       '2 - Para Remover permissão\n'
                       'Opcao: ')

    if UserOption == '1':

        optionToSet = input('Selecione o tipo de permissão\n'
                            '1 - Nível 1 (Select)\n'
                            '2 - Nível 2 (Insert, Delete e Update)\n'
                            '3 - Nível 3 (Todas)\n'
                            'Opcao: ')

        if optionToSet == '1':

            user = input('Digite o nome do usuário: ')

            try:

                cursor.execute('grant select on autoseg_production.* to "{}"@"%";'.format(user))
                db_connector.commit()
                cursor.close()
                db_connector.close()

                print('Privilegios de SELECT atribuidos para o usuário {}'.format(user))
                time.sleep(6)

            except Exception as Erro:

                print('Mensagem de erro: {}'.format(Erro))
                time.sleep(6)

        if optionToSet == '2':

            user = input('Digite o nome do usuário: ')

            try:

                cursor.execute('grant select, insert, delete, update on autoseg_production.* to "{}"@"%";'.format(user))
                db_connector.commit()
                cursor.close()
                db_connector.close()

                print('Privilegios de select, insert, delete e update atribuidos para o usuário {}'.format(user))
                time.sleep(6)

            except Exception as Erro:

                print('Mensagem de erro: {}'.format(Erro))
                time.sleep(6)

        if optionToSet == '3':

            user = input('Digite o nome do usuário: ')

            try:

                cursor.execute('grant all privileges on autoseg_production.* to "{}"@"%";'.format(user))
                db_connector.commit()
                cursor.close()
                db_connector.close()

                print('Todos os privilegios atribuidos para o usuário {}'.format(user))
                time.sleep(6)

            except Exception as Erro:

                print('Mensagem de erro: {}'.format(Erro))
                time.sleep(6)

    if UserOption == '2':

        db_connector = mysql.connector.connect(host='localhost', db='autoseg_production',
                                               user='admin_autoseg', password='Dan15331923@.')
        cursor = db_connector.cursor()

        optionToSet = input('Remover quais tipos de permissão\n'
                            '1 - Nível 1 (Select)\n'
                            '2 - Nível 2 (Insert, Delete e Update)\n'
                            '3 - Nível 3 (Todas)\n'
                            'Opcao: ')

        if optionToSet == '1':

            user = input('Digite o nome do usuário: ')

            try:

                cursor.execute('revoke select on autoseg_production.* from "{}"@"%";'.format(user))
                db_connector.commit()
                cursor.close()
                db_connector.close()

                print('Privilegios de SELECT removidos do usuário {}'.format(user))
                time.sleep(6)

            except Exception as Erro:

                print('Mensagem de erro: {}'.format(Erro))
                time.sleep(6)

        if optionToSet == '2':

            user = input('Digite o nome do usuário: ')

            try:

                cursor.execute('revoke insert, delete, update on autoseg_production.* from "{}"@"%";'.format(user))
                db_connector.commit()
                cursor.close()
                db_connector.close()

                print('Privilegios de insert, delete e update removidos do usuário {}'.format(user))
                time.sleep(6)

            except Exception as Erro:

                print('Mensagem de erro: {}'.format(Erro))
                time.sleep(6)

        if optionToSet == '3':

            user = input('Digite o nome do usuário: ')

            try:

                cursor.execute('revoke all privileges on autoseg_production.* from "{}"@"%";'.format(user))
                db_connector.commit()
                cursor.close()
                db_connector.close()

                print('Todos os privilegios removidos do usuário {}'.format(user))
                time.sleep(6)

            except Exception as Erro:

                print('Mensagem de erro: {}'.format(Erro))
                time.sleep(6)


while True:

    os.system('clear')

    main(input('Digite a opção:\n1 - Gerenciamento de Privilegios a Usuarios do banco\n'
               '2 - Sair\n'
               'Opcao: '))
