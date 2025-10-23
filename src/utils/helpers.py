from datetime import datetime
from dateutil.relativedelta import relativedelta
import locale
import matplotlib.pyplot as plt
from reportlab.lib.units import cm
from src.utils.schemas import Projeto, Cliente, EnderecoCliente, EnderecoObra, Inversor, Placa, Projetista, Procurador
import json

from src.config import INPUTS_DIR


caminho_absoluto = INPUTS_DIR / "input_solar.json"

with open(caminho_absoluto, 'r', encoding='utf-8') as f:
    inputs = json.load(f)

cliente = Cliente(**inputs['cliente'])
endereco_cliente = EnderecoCliente(**inputs['endereco_cliente'])
endereco_obra = EnderecoObra(**inputs['endereco_obra'])
projetista = Projetista(**inputs['projetista'])
procurador = Procurador(**inputs['dados_procurador'])
inversor = Inversor(**inputs['inversor'])
placa = Placa(**inputs['placa'])
projeto = Projeto(**inputs['projeto'], cliente=cliente, 
                  endereco_cliente=endereco_cliente, 
                  endereco_obra=endereco_obra, projetista=projetista, 
                  procurador=procurador, inversor=inversor, placa=placa)

#tudo sendo instanciado corretamente. 


data_de_hoje = datetime.now()
data_futura = data_de_hoje+relativedelta(months=1)
locale.setlocale(locale.LC_TIME, 'pt_BR.utf8')
plt.rcParams['text.usetex'] = True # Ativar o uso do LaTeX real (MikTeX)


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



