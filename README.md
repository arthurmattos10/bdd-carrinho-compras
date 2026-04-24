# 🛒 BDD - Carrinho de Compras

Este projeto foi desenvolvido como atividade prática da disciplina **Automação de Testes de Software**, cursada no **5º semestre da graduação na Faculdade Impacta**.

Projeto prático utilizando **BDD (Behavior Driven Development)** para simular um sistema simples de carrinho de compras em um e-commerce.

---

## 🎯 Objetivo

Transformar um requisito de negócio em:

* Cenários de comportamento (Gherkin)
* Testes automatizados (pytest-bdd)
* Implementação em Python

---

## 🧠 Conceitos aplicados

* BDD (Behavior Driven Development)
* Gherkin
* Testes automatizados com `pytest-bdd`
* Separação de responsabilidades (negócio, teste e código)

---

## 📁 Estrutura do projeto

```
bdd-carrinho-compras/
│
├── features/
│   └── carrinho.feature      # Cenários em Gherkin
│
├── carrinho.py               # Regra de negócio
├── test_carrinho.py          # Testes automatizados
├── requirements.txt          # Dependências
└── README.md
```

---

## 🧪 Cenários implementados

### ✅ Adicionar produto com sucesso

* O usuário adiciona um produto com estoque disponível
* O carrinho atualiza corretamente:

  * quantidade de itens
  * valor total

### ❌ Falha por estoque insuficiente

* O usuário tenta adicionar mais itens do que disponível
* O sistema retorna erro: `"Estoque insuficiente"`

---

## ⚙️ Tecnologias utilizadas

* Python
* pytest
* pytest-bdd
* Gherkin

---

## 🚀 Como executar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/seu-usuario/bdd-carrinho-compras.git
cd bdd-carrinho-compras
```

---

### 2. Instalar dependências

```bash
pip install -r requirements.txt
```

---

### 3. Executar os testes

```bash
python -m pytest -v
```

---

## ✅ Resultado esperado

```
2 passed
```

---

## 🧩 Exemplo de cenário (Gherkin)

```gherkin
Scenario: Adicionar produto com sucesso
  Given que o carrinho está vazio
  And que há 5 unidades em estoque
  And que o produto custa 100 reais
  When eu adiciono 2 unidades
  Then o carrinho deve ter 2 itens
  And o valor total deve ser 200 reais
```

---

## 💡 Aprendizados

Este projeto demonstra como:

* Traduzir requisitos de negócio em cenários testáveis
* Garantir qualidade com testes automatizados
* Trabalhar com BDD em um fluxo real de desenvolvimento

---

## 📌 Autor

Arthur Matos Rocha 👊
www.linkedin.com/in/arthur-matos-rocha-744516300

