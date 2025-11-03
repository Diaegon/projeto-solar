
from src.schemas.schemas import (Projeto, Cliente, EnderecoCliente, EnderecoObra,
Inversor, Placa, Projetista, Procurador, ConfiguracaoSistema)
from pprint import pprint
import json

from src.config import INPUTS_DIR

caminho_absoluto = INPUTS_DIR / "input_solar.json"
with open(caminho_absoluto, 'r', encoding='utf-8') as f:
    inputs = json.load(f)

#FACTORY

"""
cada sistema instalado vai responder a um ramo do diagrama unifilar. é basicamente um inversor e as placas instaladas nele
quando eu tiver inversor em séries no final eles funcionam como um unico inversor com potencia somada.

"""

#criação das classes de sistema isntalado
class SistemaInstaladoFactory:
    @staticmethod
    def instanciar_sistema_instalado_do_json(inputs: dict, a) -> ConfiguracaoSistema:
        dados_sistema = inputs[f'sistema_instalado{a}']
        qtd_total_placas = dados_sistema['quantidade_total_placas_do_sistema']
        #o (a) é o número do sistema instalado no json de entrada.
        # Monta o dicionário de dados
        dados = {
            'inversor': Inversor(**dados_sistema['inversor']),
            'quantidade_inversor': dados_sistema['quantidade_inversor'],
            'placa': Placa(**dados_sistema['placa']),
            'quantidade_placas': qtd_total_placas['quantidade_placas'],
            'quantidade_total_placas_do_sistema': qtd_total_placas
        }
        
        # Adiciona placa2 se existir
        if qtd_total_placas.get('quantidade_placas2'):
            dados['placa2'] = Placa(**dados_sistema['placa2'])
            dados['quantidade_placas2'] = qtd_total_placas.get('quantidade_placas2')
        
        # Adiciona placa3 se existir
        if qtd_total_placas.get('quantidade_placas3'):
            dados['placa3'] = Placa(**dados_sistema['placa3'])
            dados['quantidade_placas3'] = qtd_total_placas.get('quantidade_placas3')
        
        # Adiciona placa4 se existir
        if qtd_total_placas.get('quantidade_placas4'):
            dados['placa4'] = Placa(**dados_sistema['placa4'])
            dados['quantidade_placas4'] = qtd_total_placas.get('quantidade_placas4')
        
        return ConfiguracaoSistema(**dados)
    
    @staticmethod
    def build_sistema_instalado_list(inputs: dict) -> list[ConfiguracaoSistema]:
        sistemas = []
        for i in range(1, inputs['projeto']['quantidade_sistemas_instalados'] + 1):
            sistema = SistemaInstaladoFactory.instanciar_sistema_instalado_do_json(inputs, i)
            sistemas.append(sistema)
        return sistemas

#Criação da classe final dos dados iniciais do projeto. 
class factory_project:
    @staticmethod
    def factory():
        sistema_instalado = SistemaInstaladoFactory.build_sistema_instalado_list(inputs)
        cliente = Cliente(**inputs['cliente'])
        endereco_cliente = EnderecoCliente(**inputs['endereco_cliente'])
        endereco_obra = EnderecoObra(**inputs['endereco_obra'])
        projetista = Projetista(**inputs['projetista'])
        procurador = Procurador(**inputs['dados_procurador'])
        projeto = Projeto(**inputs['projeto'], cliente=cliente, 
                    endereco_cliente=endereco_cliente, 
                    endereco_obra=endereco_obra, projetista=projetista, 
                    procurador=procurador, sistema_instalado=sistema_instalado)

        return projeto
projeto = factory_project.factory()




#criação do objeto que carrega os cálculos do projeto

class objetos_textuais:
    def texto_sistema_instalado():
        pass
    def texto_sistema_completo():
        pass
    def texto_endereco_instalacao():
        pass
    def texto_disposicao_placas():
        pass
    def texto_caracteristicas_placas():
        pass
    def texto_dimensionamento_protecao():
        pass
    def texto_protecoes_inversor():
        pass





def linha_sumario(titulo, pagina, largura_pontilhado=80):
    """Retorna uma string formatada com pontilhado entre título e página"""
    max_linha = largura_pontilhado
    texto_base = f'{titulo} '
    dots = '.' * max(3, max_linha - len(texto_base) - len(str(pagina)))
    return f'{texto_base}{dots} {pagina}'
def add_page_number(canvas, doc):
    page_num = canvas.getPageNumber()
    text = f"Página {page_num}"
    canvas.setFont('Helvetica', 9)
    width, height = doc.pagesize
    canvas.drawCentredString(width / 2.0, 1.5 * cm, text)
