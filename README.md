O sistema foi feito com três classes em arquivos separados:
Produto, que guarda os dados e controla o estoque; 
ItemVenda, que guarda o produto, a quantidade e o preço, calculando o subtotal; 
e Venda, que organiza os itens e calcula o total. Ao adicionar um produto, o estoque diminui; ao remover, a quantidade volta ao estoque e o total é atualizado. Os atributos foram encapsulados com __, e as propriedades permitem consultar seus valores. No main.py, criamos os produtos e uma venda com data do tipo datetime, testamos a inclusão e a remoção e exibimos o comprovante e o estoque.
Claro, tudo dentro da pasta sisvenda
