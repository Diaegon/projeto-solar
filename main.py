import json
from src.gerar_pdf import gerar_memorial, gerar_procuracao
from src.unifilar import gerar_diagramaunifilar
from src.formularioENEL import gerar_formulario

caminho_absoluto = r"C:\Users\DIEGO\Desktop\code\projetosolar\inputs\input_solar.json"

with open(caminho_absoluto, 'r') as f:
    inputs = json.load(f)

def gerar_projeto():
    gerar_memorial(inputs)
    gerar_procuracao(inputs)
    gerar_diagramaunifilar()
    gerar_formulario()

gerar_projeto()