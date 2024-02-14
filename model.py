from datetime import datetime
class Produto:
    def __init__(self, nome, preco, categoria):
        self.nome = nome
        self.preco = preco
        self.categoria = categoria


class Categoria:
    def __init__(self, categoria_Nome):
        self.categoria_Nome = categoria_Nome


class Estoque:
    def __init__(self, produto:Produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade


class Venda:
    def __init__(self, ItensVendidos:Produto, comprador, vendedor, quant_vendidas, data = datetime.now().strftime("%d/%m/%Y")):
        self.ItensVendidos = ItensVendidos
        self.comprador = comprador
        self.data = data
        self.vendedor = vendedor
        self.quant_vendidas = quant_vendidas

class Fornecedor:
    def __init__(self, nome_Fornecedor, categoria, email, telefone, cnpj):
        self.nome_Fornecedor = nome_Fornecedor
        self.categoria = categoria
        self.email = email
        self.cnpj = cnpj
        self.telefone = telefone


class Pessoa:
    def __init__(self, nome , cpf, endereco, telefone, email):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.telefone = telefone
        self.email = email

class Cliente(Pessoa):
    def __init__(self, nome, cpf, endereco, telefone, email):
        super().__init__(nome, cpf, endereco, telefone, email)


class Funcionario(Pessoa):
    def __init__(self, nome, cpf, endereco, telefone, email):
        super().__init__(nome, cpf, endereco, telefone, email)
        