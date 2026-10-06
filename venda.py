from item_venda import ItemVenda


class Venda:
    def __init__(self, id, data):
        self.__id = id
        self.__data = data
        self.__itens = []
        self.__valor_total = 0.0

    @property
    def id(self):
        return self.__id

    @property
    def data(self):
        return self.__data

    @property
    def itens(self):
        return self.__itens.copy()

    def adicionar_item(self, produto, quantidade):
        if quantidade <= 0:
            print("A quantidade deve ser maior que zero.")
            return False

        if produto.decrementar_estoque(quantidade):
            item = ItemVenda(quantidade, produto)

            self.__itens.append(item)
            self.calcular_total()

            print(
                f"{quantidade}x {produto.nome} "
                f"adicionado(s) à venda."
            )

            return True

        print(f"Estoque insuficiente para {produto.nome}.")
        return False

    def remover_item(self, produto):
        removeu = False

        for item in self.__itens.copy():
            if item.produto is produto:
                produto.incrementarEstoque(item.quantidade)
                self.__itens.remove(item)
                removeu = True

        self.calcular_total()
        return removeu
    
    @property
    def valor_total(self):
        return self.__valor_total

    def calcular_total(self):
        self.__valor_total = 0.0

        for item in self.__itens:
            self.__valor_total += item.calcular_subtotal()

        return self.__valor_total

    def calcularQtdTotal(self):
        quantidadeTotal = 0

        for item in self.__itens:
            quantidadeTotal += item.quantidade

        return quantidadeTotal

    def exibirComprovante(self):
        print("\n========== COMPROVANTE ==========")
        print(f"Venda: {self.__id}")
        print(f"Data: {self.__data.strftime('%d/%m/%Y')}")
        print("---------------------------------")

        for item in self.__itens:
            print(
                f"{item.produto.nome} | "
                f"{item.quantidade}x | "
                f"R$ {item.valor_item:.2f} | "
                f"Subtotal: R$ {item.calcular_subtotal():.2f}"
            )
        print("---------------------------------")
        print(f"Quantidade total: {self.calcularQtdTotal()}")
        print(f"Valor total: R$ {self.calcular_total():.2f}")
        print("=================================")
