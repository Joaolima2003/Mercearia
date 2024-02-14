from model import Produto, Categoria, Estoque, Venda , Fornecedor, Pessoa
from dal import DalCategoria, DalEstoque, DalFornecedor, DalFuncionario, DalPessoa, DalVenda
from datetime import datetime

class ControllerCategoria:
    def cadastrarCategoria(self, NovaCategoria):
        existe = False
        x = DalCategoria.ler()
        for i in x:
            if i.categoria_Nome == NovaCategoria:
                existe = True
                

        if not existe:
            DalCategoria.salvar(NovaCategoria)
            print(f'A nova categoria {NovaCategoria} foi cadastrada com sucesso!')        

        else:
            print('Categoria que deseja cadastrar já existe!')

