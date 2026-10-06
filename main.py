from produto import Produto
from venda import Venda
from datetime import datetime


# OS PRODUTOS

produto1 = Produto(
    1,
    "Mouse",
    80.00,
    "Mouse Gamer",
    10
)

produto2 = Produto(
    2,
    "Teclado",
    150.00,
    "Teclado Mecânico",
    5
)

produto3 = Produto(
    3,
    "Monitor",
    900.00,
    "Monitor 24 polegadas",
    3
)


# A VENDA

venda1 = Venda(
    1,
    datetime(2026, 10, 4)
)


# ADD PRODUTOS

venda1.adicionar_item(produto1, 2)
venda1.adicionar_item(produto2, 1)
venda1.adicionar_item(produto3, 1)


# REMOVENDO O TECLADO

if venda1.remover_item(produto2):
    print("Teclado removido da venda!")
else:
    print("Produto não encontrado na venda.")


# EXIBIR O COMPROVANTE

venda1.exibirComprovante()


# VISUALIZAR O ESTOQUE

print("\n========== ESTOQUE ==========")

print(
    f"{produto1.nome}: "
    f"{produto1.verificarEstoque()}"
)

print(
    f"{produto2.nome}: "
    f"{produto2.verificarEstoque()}"
)

print(
    f"{produto3.nome}: "
    f"{produto3.verificarEstoque()}"
)
