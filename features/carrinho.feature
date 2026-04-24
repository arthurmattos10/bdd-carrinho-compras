Feature: Carrinho de Compras

  Scenario: Adicionar produto com sucesso
    Given que o carrinho está vazio
    And que há 5 unidades em estoque
    And que o produto custa 100 reais
    When eu adiciono 2 unidades
    Then o carrinho deve ter 2 itens
    And o valor total deve ser 200 reais

  Scenario: Tentar adicionar sem estoque suficiente
    Given que o carrinho está vazio
    And que há 1 unidades em estoque
    And que o produto custa 100 reais
    When eu tento adicionar 3 unidades
    Then deve ocorrer um erro de "Estoque insuficiente"