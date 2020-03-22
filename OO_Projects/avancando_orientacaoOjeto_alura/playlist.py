class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self.programas = programas
    
    # Duck Typing
    def __getitem__(self, item):
        return self.programas[item]
    
    # Duck Typing
    def __len__(self):
        return len(self.programas)

    @property
    def programa(self):
        return self.programas
