from datetime import datetime
from dateutil.relativedelta import relativedelta
import locale
import matplotlib.pyplot as plt
from reportlab.lib.units import cm
import json
from src.config import INPUTS_DIR


caminho_absoluto = INPUTS_DIR / "input_solar.json"

with open(caminho_absoluto, 'r', encoding='utf-8') as f:
    inputs = json.load(f)

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


###
### vamos criar classes para os dados
class Entradas:
    
    pass
###

#Endereço da obra

logradouro_obra = inputs['endereco']['logradouro']
numero_obra = inputs['endereco']['numero_casa']
complemento_obra = inputs['endereco']['complemento']    
municipio_obra = inputs['endereco']['municipio']
bairro_obra = inputs['endereco']['bairro']
estado_obra = inputs['endereco']['estado']  
cep_obra = inputs['endereco']['cep']
latitude_obra = inputs['endereco']['latitude']
longitude_obra = inputs['endereco']['longitude']

#endereço do cliente e dados do cliente

nome_cliente = inputs['dados_cliente']['nome']
cpf_cliente = inputs['dados_cliente']['cpf']
uc_cliente = inputs['dados_cliente']['uc']
classe_cliente = inputs['dados_cliente']['classeconsumo'].lower()
fornecimento_cliente = inputs['dados_cliente']['fornecimento'].lower()
ramal_cliente = inputs['dados_cliente']['ramal']
classe_codigo = ""
if classe_cliente == "residencial":
    classe_codigo = "B1"
elif classe_cliente == "rural":
    classe_codigo = "B2"
elif classe_cliente == "comercial":
    classe_codigo = "B3"


logradouro_cliente = inputs['residencia_cliente']['logradouro']
numero_cliente = inputs['residencia_cliente']['numero_casa']
complemento_cliente = inputs['residencia_cliente']['complemento']
municipio_cliente = inputs['residencia_cliente']['municipio']    
estado_cliente = inputs['residencia_cliente']['estado']
cep_cliente = inputs['residencia_cliente']['cep']
email_cliente = inputs['dados_cliente']['email']
telefone_cliente = inputs['dados_cliente']['telefone']

#dados procurador

nome_procurador = inputs['dados_procurador']['nome']
cpf_procurador = inputs['dados_procurador']['cpf']
rg_procurador = inputs['dados_procurador']['rg']
logradouro_procurador = inputs['dados_procurador']['logradouro_procurador']
numero_casa_procurador = inputs['dados_procurador']['numero_casa_procurador']
complemento_procurador = inputs['dados_procurador']['complemento_procurador']
municipio_procurador = inputs['dados_procurador']['municipio_procurador']
estado_procurador = inputs['dados_procurador']['estado_procurador']
cep_procurador = inputs['dados_procurador']['cep_procurador']
telefone_procurador = inputs['dados_procurador']['telefone']
email_procurador = inputs['dados_procurador']['email']
#DADOS PROJETISTA

projetista = inputs['projeto']['projetista']
projeto = inputs['projeto']['rubrica']
cft_crea = inputs['projeto']['cft_crea']
