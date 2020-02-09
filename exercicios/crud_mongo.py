#  Criar CRUD de usuário no mongoDB com os compos: nome, cpf e estado
#  Faça um menu a baixo:

from pymongo import MongoClient


def main(action):
    if action == '1':
        insert()

    elif action == '2':
        delete()

    elif action == '3':
        update()

    elif action == '4':
        search()

    elif action == '5':
        exit()


def insert():
    connection = MongoClient()
    db = connection['gotham']

    name = input('Digite o nome do usuário: ')
    cpf = input('Digite o cpf do usuário: ')
    state = input('Digite o estado do usuário: ')
    city = input('Digite a cidade do usuario: ')

    try:
        db.herois.insert_one({
            'nome': name,
            'cpf': cpf,
            'moradia': {
                'estado': state,
                'cidade': city,
            }
        })

        print('Cadastrado com sucesso!')

    except Exception as Erro:

        print('Erro ao inserir no banco !: {}'.format(Erro))


def delete():
    connection = MongoClient()
    db = connection['gotham']

    cpf = input('Digite o cpf do usuario que quer deletar: ')

    try:
        db.herois.delete_one({
            'cpf': cpf
        })
        print('Deletado com sucesso!')

    except Exception as Erro:
        print('Erro deletar usuário do banco !: {}'.format(Erro))


def update():
    connection = MongoClient()
    db = connection['gotham']

    cpf = input('Digite o cpf do usuário que quer atualizar: ')

    try:
        userOption = input('O que quer atualizar?: ')

        if userOption == 'nome':
            newName = input('Digite o novo nome do usuário: ')

            db.herois.update_one({
                "cpf": cpf},
                {"$set": {"nome": newName}})

        if userOption == 'cpf':
            newCPF = input('Digite o novo CPF do usuário: ')

            db.herois.update_one({
                "cpf": cpf},
                {"$set": {"cpf": newCPF}})

        if userOption == 'estado':
            newState = input('Digite o novo estado do usuário: ')

            db.herois.update_one({
                "cpf": cpf},
                {"$set": {"moradia.estado": newState}})

        if userOption == 'cidade':
            newCity = input('Digite a nova cidade do usuário: ')

            db.herois.update_one({
                "cpf": cpf},
                {"$set": {"moradia.cidade": newCity}})

    except Exception as Erro:
        print('Erro ao inserir no banco!: {}'.format(Erro))


def search():
    connetion = MongoClient()
    db = connetion['gotham']

    cpf = input('Digite o CPF de quem quer buscar: ')

    try:
        results = db.herois.find({
            'cpf': cpf
        })
        print([result for result in results])

    except Exception as Erro:
        print('Erro ao buscar no banco!: {}'.format(Erro))


main(input('Digite uma opção:\n'
           '1 - Cadastrar no banco\n'
           '2 - Excluir do banco\n'
           '3 - Atualizar dados no banco\n'
           '4 - Procurar dados no banco\n'
           '5 - Sair\n'
           'Opção: '))
