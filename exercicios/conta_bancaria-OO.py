# Dado o cenario abaixo abstraia uma conta bancaria utilizando programacao orientada a objeto
# crie metodos para transferencia, saque, deposito e utilize herança se necessario

# Joao possuia 30K em sua CC e uma poupança com saldo zerado, entao ele transferiu 3k para CC
# de Maria que já possuia 2k em sua CC e depois disso joao transferiu 5k para a sua poupanca
# Apos um mẽs a poupança de Joao rendeu 0.6% do valor de seu saldo


class Account:

    def __init__(self, name, saldo, type):
        self.name = name
        self.saldo = saldo
        self.type = type

    def cash_out(self, value_out):
        self.saldo -= value_out

    def cash_in(self, value_in):
        self.saldo += value_in

    def extract(self):
        print('{} possui {}R$ na sua conta {}'.format(self.name.title(), self.saldo, self.type))

    def transfer(self, value, account_receiver):
        self.cash_out(value)
        account_receiver.cash_in(value)


class AccountCurrency(Account):
    def __init__(self, name, saldo):
        super().__init__(name, saldo, 'corrente')


class AccountPoup(Account):
    def __init__(self, name, saldo):
        super().__init__(name, saldo, 'poupança')

    def rend(self, days):
        if days == 30:
            self.saldo += (self.saldo * 0.06)


joao_account_currency = AccountCurrency('Joao', 30000)
joao_account_poup = AccountPoup('Joao', 0)

maria_account_currency = AccountCurrency('Maria', 2000)
maria_account_poup = AccountPoup('Maria', 0)


joao_account_currency.extract()
maria_account_currency.extract()

print('\n')

joao_account_poup.extract()
maria_account_poup.extract()

print('\n')

print('Transferencia:')
joao_account_currency.transfer(float(input('Digite o valor que quer transferir para maria: ')), maria_account_currency)
joao_account_currency.extract()
maria_account_currency.extract()

print('\n')

print('Poupança - Faça uma transferencia para a conta poupança de Joao')
joao_account_currency.transfer(float(input(
    'Digite o valor que quer transferir para conta poupança de Joao: ')), joao_account_poup)
joao_account_poup.rend(30)
joao_account_poup.extract()

print('Valor que Joao possui na sua conta poupança depois do rendimento de 30 dias')
