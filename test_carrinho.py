import pytest
from pytest_bdd import scenarios, given, when, then, parsers

from carrinho import criar_carrinho, adicionar_produto

scenarios('features/carrinho.feature')


@pytest.fixture
def contexto():
    return {}


@given("que o carrinho está vazio")
def carrinho_vazio(contexto):
    contexto["carrinho"] = criar_carrinho()


@given(parsers.parse('que há {estoque:d} unidades em estoque'))
def definir_estoque(contexto, estoque):
    contexto["estoque"] = estoque


@given(parsers.parse('que o produto custa {preco:d} reais'))
def definir_preco(contexto, preco):
    contexto["preco"] = preco


@when(parsers.parse('eu adiciono {quantidade:d} unidades'))
def adicionar(contexto, quantidade):
    carrinho = contexto["carrinho"]

    adicionar_produto(
        carrinho,
        quantidade,
        contexto["estoque"],
        contexto["preco"]
    )


@when(parsers.parse('eu tento adicionar {quantidade:d} unidades'))
def tentar_adicionar(contexto, quantidade):
    carrinho = contexto["carrinho"]

    try:
        adicionar_produto(
            carrinho,
            quantidade,
            contexto["estoque"],
            contexto["preco"]
        )
    except Exception as e:
        contexto["erro"] = str(e)


@then(parsers.parse('o carrinho deve ter {itens:d} itens'))
def validar_itens(contexto, itens):
    assert contexto["carrinho"]["itens"] == itens


@then(parsers.parse('o valor total deve ser {total:d} reais'))
def validar_total(contexto, total):
    assert contexto["carrinho"]["total"] == total


@then(parsers.parse('deve ocorrer um erro de "{mensagem}"'))
def validar_erro(contexto, mensagem):
    assert contexto["erro"] == mensagem