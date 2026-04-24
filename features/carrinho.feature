Funcionalidade: Carrinho de Compras
  Como um cliente do e-commerce
  Eu quero adicionar produtos ao carrinho
  Para visualizar o valor total da compra

  Cenário: Adicionar um produto com sucesso
    Dado que o carrinho está vazio
    E que o produto "Notebook" possui preço de 3000 reais
    E que há 5 unidades do produto "Notebook" em estoque
    Quando eu adiciono 2 unidades do produto "Notebook" ao carrinho
    Então o carrinho deve ter 2 unidades do produto "Notebook"
    E o valor total do carrinho deve ser 6000 reais

  Cenário: Tentar adicionar produto sem estoque suficiente
    Dado que o carrinho está vazio
    E que o produto "Mouse" possui preço de 100 reais
    E que há 1 unidade do produto "Mouse" em estoque
    Quando eu tento adicionar 3 unidades do produto "Mouse" ao carrinho
    Então deve ocorrer um erro de "Estoque insuficiente"