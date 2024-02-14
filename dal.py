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
    def salvar(cls, produto: Produto, quantidade):
        with open('estoque.txt', 'a') as arq:
            arq.writelines(produto.produto.nome + '|' + produto.produto.preco + '|' + produto.produto.categoria + '|' + str(quantidade))
            arq.writelines('\n')
            


x = Produto('maça', '2', 'fruta')

y = Estoque(x, 10)

DalEstoque.salvar(y)












          
     
