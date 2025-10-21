import json
from reportlab.platypus import Table, Paragraph, TableStyle
from utils.helpers import data_de_hoje, nome_cliente, cpf_cliente
from utils.estilos import styles, estilotabela, estilotabelaloc, estilo_tabela_parametros, estilo_assinatura
from utils.equacoes import corrente_saida, tensao_queda, potenciaefetiva, energia_gerada,texto_corrente_saida, inversores_tensao, texto_cabos, vmp_modulos_tabela, potencia_modulos_tabela, imp_modulos_tabela, voc_modulos_tabela, isc_modulos_tabela, inversores_potencia, cabo_inversor1, inversor_tensao
caminho_absoluto = r"C:\Users\DIEGO\Desktop\code\projetosolar\inputs\input_solar.json"
with open(caminho_absoluto, 'r') as f:
    inputs = json.load(f)


dados = [[f"UC:{inputs['dados_cliente']['uc']}"], [f"Classe:{inputs['dados_cliente']['classeconsumo']}  {inputs['dados_cliente']['fornecimento']} "], [f"Nome do Cliente: {inputs['dados_cliente']['nome']}"],
         [f"Endereço: {inputs['endereco']['logradouro']}, {inputs['endereco']['numero_casa']}  {inputs['endereco']['complemento']}, {inputs['endereco']['municipio']}, {inputs['endereco']['estado']}."],
         [f"CEP:{inputs['endereco']['cep']}"],
         [f"CPF/CNPJ: {inputs['dados_cliente']['cpf']}"]]
tabeladedados = Table(dados)
tabeladedados.setStyle(estilotabela)

loc_instalacao = [["COORDENADAS - coordenadas decimais - WGS 84 "],
                  [" Local de implantação do Gerador fotovoltaico",
                      "Lat: ", "Long: "],
                  ["", f"{inputs['endereco']['latitude']}", f"{inputs['endereco']['longitude']}"]]
tabela_localizacao = Table(loc_instalacao)
tabela_localizacao.setStyle(estilotabelaloc)

modulo_caracteristicas = [["Potência nominal máx. (Pmax) ", f"({potencia_modulos_tabela} )Wp"],
                          ["Tensão operacional opt. (Vmp) ", f"({vmp_modulos_tabela} )V"],
                            ["Corrente operacional opt. (Imp)", f"({imp_modulos_tabela}) A"], 
                            ["Tensão circuito aberto (Voc) ", f"({voc_modulos_tabela} )V"], 
                            ["Corrente curto-circuito (Isc)", f"({isc_modulos_tabela}) A"]]
tabelapainel = Table(modulo_caracteristicas)
tabelapainel.setStyle(estilotabela)

parametros_tensao_inversor = [["Faixa de tensão no ponto de conexão [V]","Tempo de desconexão [s]"], ["TL > 231","0,2 s"], ["189 ≤ TL ≤ 231","Operação Normal"], ["TL < 195,5","0,2 s"]]
tabela_parametros_tensao_inversor = Table(parametros_tensao_inversor)
tabela_parametros_tensao_inversor.setStyle(estilo_tabela_parametros)

parametros_frequencia_inversor = [["Faixa de freqüência no ponto de conexão (Hz)","Tempo de desconexão [s]"], ["f ≤ 57,5","0,2"],["59,9 < f ≤ 60,1","Operação normal"],["f > 62,5","0,2"] ]
tabela_parametros_frequencia_inversor = Table(parametros_frequencia_inversor)
tabela_parametros_frequencia_inversor.setStyle(estilo_tabela_parametros)

parametros_fp_inversor = [["Potência Nominal (W) - Pn","Faixa de fator de potência","Fator de potência \nconfiguração em fábrica"], [f"{inversores_potencia}","0,95 indutivo – 0,95 capacitivo","1"]]
tabela_parametros_fp_inversor = Table(parametros_fp_inversor)
tabela_parametros_fp_inversor.setStyle(estilo_tabela_parametros)

queda_tensao = [["ρ  - resistividade do cobre","0,0173"], [Paragraph("L<sub>c</sub> - comprimento do condutor",styles["CorpoTexto"]),"10 m"], 
                [Paragraph("I<sub>c</sub> - corrente do condutor",styles["CorpoTexto"]),f"({texto_corrente_saida}) A"], ["Cosφ - fator de potencia","1"], [Paragraph("S<sub>c</sub> - Seção reta do condutor",styles["CorpoTexto"]), f"({texto_cabos}) mm²"], 
                [Paragraph("V <sub>f</sub> - tensão ", styles["CorpoTexto"]), f"{inversores_tensao}"]]
tabela_queda_tensao = Table(queda_tensao)
tabela_queda_tensao.setStyle(estilotabela)

assinatura = [[""],[f"                  {nome_cliente}, CPF:{cpf_cliente}                    "], [f"{data_de_hoje.strftime("%d de %B de %Y")}"]]
tabela_assinatura = Table(assinatura)
tabela_assinatura.setStyle(estilo_assinatura)