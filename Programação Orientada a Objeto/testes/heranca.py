class Mae:
    def __init__(self, p1):
        print('executando o init de Mae')
        self.p1 = p1


class Filha(Mae):
    def __init__(self, p1, p2):
        print('executando o init de Filha')
        self.p2 = p2
        super().__init__()  # Mae.__init__(self, p2)


class Neta(Filha):
    def __init__(self, p1, p2, p3):
        print('executando o init de Neta')
        self.p3 = p3
        super().__init__()  # Filha.__init__(self)
