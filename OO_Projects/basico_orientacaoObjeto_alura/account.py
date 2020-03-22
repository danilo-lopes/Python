
class Account:
    def __init__(self, number, holder, balance, limit):
        self.__number = number
        self.__holder = holder
        self.__balance = balance
        self.__limit = limit
    
    @staticmethod
    def bank_code():
        return "001"
    
    @staticmethod
    def all_bank_code():
        return {'BB': '001', 'Caixa': '104', 'Bradesco':'237', 'Itau': '341'}

    def bankStatement(self):
        print(f"Holder {self.__holder}. Account Balance: ${self.__balance}.")

    def deposit(self, value):
        self.__balance += value
    
    def __can_withDrow(self, value_withDrow):
        available_value = self.balance + self.limit
        
        return value_withDrow <= available_value

    def withDrow(self, value):
        if self.__can_withDrow(value):
            self.__balance -= value
        
        else:
            print("Operation denied. Your amount exceed the permited limit")

    def transfer(self, value, destination):
        self.withDrow(value)
        destination.deposit(value)

    @property
    def balance(self):
        return self.__balance
    
    @property
    def limit(self):
        return self.__limit
    
    @property
    def holder(self):
        return self.__holder

    @limit.setter
    def limit(self, limit):
        self.__limit = limit
