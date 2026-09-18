produtos = []

def adicionar_produto(nome):
    produtos.append(nome)

def listar_produtos():
    for produto in produtos:
        print(produto)