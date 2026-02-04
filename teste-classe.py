class vendedor():
    def __init__(self, nome):
        self.nome = nome
        self.vendas = 0

    def vendeu(self, vendas):
        self.vendas = vendas

    def bateu_meta(self, meta):
        if self.vendas >= meta:
            print(self.nome, "Meta batida com sucesso!")

        else:
            print(self.nome, "Infelizmente a meta não foi alcançada!")

vendedor1 = vendedor("João")
vendedor1.vendeu(600)
vendedor1.bateu_meta(400)

vendedor2 = vendedor("Yago")
vendedor2.vendeu(800)
vendedor2.bateu_meta(900)
        


        