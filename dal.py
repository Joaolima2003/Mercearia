from model import *

class DalVenda:
    @classmethod
    def salvar(cls, venda: Venda):
        with open('venda.txt', 'a') as arq:
            arq.writelines(venda.ItensVendidos.nome + "|" + venda.ItensVendidos.preco + "|" + venda.ItensVendidos.categoria + "|" +  venda.vendedor + "|" + venda.comprador + "|" + venda.data + "|" + venda.quant_vendidas )
            arq.writelines('\n')
    @classmethod
    def ler(cls):
        with open('venda.txt', 'r') as arq:
            cls.venda = arq.readlines()
        cls.venda = list(map(lambda x: x.replace('\n', ' '), cls.venda))
        cls.venda = list(map(lambda x: x.split('|'), cls.venda))
        vend = []
        for i in cls.venda:
            vend.append(Venda(Produto(i[0],i[1],i[2]), i[3], i[4], i[5]))
        return vend
class DalCategoria:
    @classmethod
    def salvar(cls, categoria_Nome):
        with open('categoria.txt', 'a') as arq:
            arq.writelines(categoria_Nome)
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('categoria.txt', 'r') as arq:
            cls.categoria_Nome = arq.readlines()

            cls.categoria_Nome = list(map(lambda x: x.replace('\n',''), cls.categoria_Nome))
           
        cat = []
        for i in cls.categoria_Nome:
            cat.append(Categoria(i))

        return cat
        
class DalEstoque:
    @classmethod
    def salvar(cls, produto: Produto, quantidade):
        with open('estoque.txt', 'a') as arq:
            arq.writelines(produto.produto.nome + '|' + produto.produto.preco + '|' + produto.produto.categoria + '|' + str(quantidade))
            arq.writelines('\n')
    @classmethod        
    def ler(cls):
        with open('estoque.txt', 'r') as arq:
            cls.estoque = arq.readlines()
        
            cls.estoque = list(map(lambda x: x.replace('\n',''), cls.estoque))
            cls.estoque = list(map(lambda x: x.split('|'), cls.estoque))

        est = []
        if (cls.estoque) > 0:
            for i in cls.estoque:
                est.append(Estoque(Produto(i[0], i[1], i[2]), i[3]))
        
        return est

class DalFornecedor:
    @classmethod
    def salvar(cls, fornecedor: Fornecedor):
        with open('fornecedor.txt', 'a') as arq:
            arq.writelines(fornecedor.nome_Fornecedor + '|' + fornecedor.categoria + '|' + fornecedor.email + '|' + fornecedor.telefone + '|' + fornecedor.cnpj)
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('fornecedor.txt', 'r') as arq:
            cls.fornecedor = arq.readlines()

            cls.fornecedor = list(map(lambda x: x.replace('\n', ''), cls.fornecedor))
            cls.fornecedor = list(map(lambda x: x.split('|'), cls.fornecedor))
        forn = []
        for i in cls.fornecedor:
            forn.append(Fornecedor(i[0], i[1], i[2], i[3], i[4]))
        return forn                         

class DalPessoa:
    @classmethod
    def salvar(cls, pessoa: Pessoa):
        with open('pessoa.txt', 'a') as arq:
            arq.writelines(pessoa.nome + '|' + pessoa.cpf + '|' + pessoa.endereco + '|' + pessoa.telefone + '|' + pessoa.email)
            arq.writelines('\n')


    @classmethod
    def ler(cls):
        with open('pessoa.txt', 'r') as arq:
            cls.pessoa = arq.readlines()

            cls.pessoa = list(map(lambda x: x.replace('\n', ''), cls.pessoa))
            cls.pessoa = list(map(lambda x: x.split('|'), cls.pessoa))

        pes = []
        for i in cls.pessoa:
            pes.append(Pessoa(i[0], i[1], i[2], i[3], i[4]))          

        return pes



class DalFuncionario:
    @classmethod
    def salvar(cls, funcionario: Funcionario):
        with open('funcionario.txt', 'a') as arq:
            arq.writelines(funcionario.nome + '|' + funcionario.cpf + '|' + funcionario.endereco + '|' + funcionario.telefone + '|' + funcionario.email)
            arq.writelines('\n')


    @classmethod
    def ler(cls):
        with open('pessoa.txt', 'r') as arq:
            cls.funcionario = arq.readlines()

            cls.funcionario = list(map(lambda x: x.replace('\n', ''), cls.funcionario))
            cls.funcionario = list(map(lambda x: x.split('|'), cls.funcionario))

        fun = []
        for i in cls.funcionario:
            fun.append(Funcionario(i[0], i[1], i[2], i[3], i[4]))          

        return fun   









          
     
