class Data:
    def __init__(self, data):
        self.data = data
    
    def dataFormatada(self):
        print("{}".format(self.data).replace(',', '/'))
