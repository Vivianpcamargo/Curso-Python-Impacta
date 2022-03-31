class Teste:
    def __init__(self):
        self._nome = ''
        self.cont = 0

    @property
    def nome(self):
        self.cont += 1
        print(f'Executando a propety... {self.cont}')
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        print('Executando o setter...')
        self._nome = novo_nome
