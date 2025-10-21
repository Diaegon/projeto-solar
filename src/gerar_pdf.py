from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Image
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from utils.estilos import styles
from utils.helpers import linha_sumario, add_page_number, data_de_hoje
from utils.equacoes import (equacao, equacao2, equacao3, equacao4, insert_equation, render_equation_to_image)
from textos.textos import (texto_introducao, texto_procuracao, texto_dimensionamento_protecao2, texto_dimensionamento_protecao3, texto_loc, texto_loc2, texto_carginst, texto_calculo_demanda, texto_calculo_demanda2,
    texto_calculo_fc, texto_geradorfv, texto_potenciafv, texto_calculo_enegiagerada, texto_diagramas, texto_parametrizacao, texto_instalacao, texto_dimensionamento_protecao, texto_disjuntores, texto_sinalizacao, texto_diagramauni)
from utils.imagens import img1, img2, img3
from utils.tabelas import (tabeladedados, tabela_assinatura, tabela_localizacao, tabelapainel, tabela_parametros_tensao_inversor, tabela_parametros_frequencia_inversor, tabela_parametros_fp_inversor, tabela_queda_tensao)


def gerar_memorial(inputs):
    doc = SimpleDocTemplate(r"C:\Users\DIEGO\Desktop\code\projetosolar\output\memorial_geracao_distribuida.pdf", pagesize=A4, leftMargin=2*cm, rightMargin=2*cm, topMargin=2*cm, bottomMargin=2*cm)

    story = []
    # CAPA @@ NÃO MUDA NADA
    story.append(Paragraph("MEMORIAL DESCRITIVO", styles['Title']))
    story.append(Spacer(1, 2*cm))
    story.append(Paragraph("PROJETO DE GERAÇÃO DISTRIBUÍDA", styles['Heading1']))
    story.append(Spacer(1, 3*cm))
    story.append(Paragraph(f" PROJETO PARA IMPLANTAÇÃO DE GERADOR FOTOVOLTAICO NA ÁREA {inputs['dados_cliente']['classeconsumo']} DO(A) Cliente: {inputs['dados_cliente']['nome']}", styles['Heading3']))
    story.append(Paragraph(f"Local: {inputs['endereco']['municipio']}", styles['Heading3']))
    story.append(Paragraph(f"{data_de_hoje.strftime("%d/%m/%Y")}", styles['Heading4']))
    story.append(PageBreak())

    #SUMARIO @@NÂO MUDA NADA

    story.append(Paragraph('SUMÁRIO', styles['TituloSecao']))
    story.append(Spacer(1, 2*cm))
    topicos = [
        ('1 - INTRODUÇÃO', 3),
        ('1.1 - Identificação do cliente', 3),
        ('2 - LOCALIZAÇÃO DO GERADOR FOTOVOLTAICO', 3),
        ('2.1 - Planta de situação do gerador', 3),
        ('3 -CARGA INSTALADA ',4),
        ('3.1 - Cálculo da Demanda Média',4),
        ('3.2 - Cálculo do Fator de Carga Médio',4),
        ('4 - GERADOR FOTOVOLTAICO',4),
        ('4.1 - Cálculo da Energia Média Gerad5',5),
        ('5 - DIAGRAMAS BÁSICOS',5),
        ('5.1 - Parametrização do inverso',5),
        ('5.1.x - tabelas de parametrização do inversor',6),
        ('6 - INSTALAÇÃO ELÉTRICA',6),
        ('6.1 – Diagrama unifilar Geral',6),
        ('6.2 – Dimensionamento da Proteção',6),
        ('6.3 – Coordenação entre os Disjuntores',7),
        ('7 – SINALIZAÇÃO',8),
        ('8 – RESPONSÁVEL TÉCNICO',9),
    ]
    for titulo, pagina in topicos:
        linha = linha_sumario(titulo, pagina)
        story.append(Paragraph(linha, styles['SubSecao']))

    story.append(PageBreak())
    #DOC
    story.append(Paragraph("1 - INTRODUÇÃO", styles['TituloSecao']))
    story.append(Spacer(1, 1*cm))
    story.append(Paragraph(texto_introducao(), styles['CorpoTexto']))
    story.append(Spacer(1, 1*cm))
    story.append(Paragraph("1.1 - Identificação do cliente", styles['SubSecao']))
    story.append(tabeladedados)
    story.append(Spacer(1, 2*cm))
    story.append(Paragraph("2 - LOCALIZAÇÃO DO GERADOR FOTOVOLTAICO", styles['TituloSecao']))
    story.append(Spacer(1, 1*cm))
    story.append(Paragraph("2.1 -Planta de situação do gerador", styles['SubSecao']))
    story.append(Paragraph(texto_loc(), styles['CorpoTexto']))
    story.append(tabela_localizacao)
    story.append(Spacer(1, 0.5*cm))
    story.append(Paragraph(texto_loc2(), styles['CorpoTexto']))
    story.append(PageBreak())
    story.append(Paragraph("3 - CARGA INSTALADA", styles['TituloSecao']))
    story.append(Spacer(1, 1*cm))
    story.append(Paragraph(texto_carginst(), styles['CorpoTexto']))
    story.append(Spacer(1, 1*cm))
    story.append(Paragraph("3.1 - Cálculo da Demanda Média", styles['SubSecao']))
    story.append(Paragraph(texto_calculo_demanda(), styles['CorpoTexto']))
    insert_equation(equacao,story,'eqdemanda.png')
    story.append(Paragraph(texto_calculo_demanda2(), styles['CorpoTexto']))
    story.append(Spacer(1, 1*cm))
    story.append(Paragraph("3.2 - Cálculo do Fator de Carga Médio", styles['SubSecao']))
    story.append(Paragraph(texto_calculo_fc(), styles['CorpoTexto']))
    insert_equation(equacao2,story,'eqfc.png')
    story.append(Spacer(1, 1*cm))
    story.append(Paragraph("4 - GERADOR FOTOVOLTAICO", styles['TituloSecao']))
    story.append(Spacer(1, 1*cm))
    story.append(Paragraph(texto_geradorfv(), styles['CorpoTexto']))
    story.append(tabelapainel)
    story.append(Paragraph(texto_potenciafv(), styles['CorpoTexto']))
    story.append(Spacer(1, 1*cm))
    story.append(Paragraph("4.1 - Cálculo da Energia Média Gerada ", styles['SubSecao']))
    story.append(Paragraph(texto_calculo_enegiagerada(), styles['CorpoTexto']))
    story.append(Spacer(1, 2*cm))
    story.append(Paragraph("5 - DIAGRAMAS BÁSICOS", styles['TituloSecao']))
    story.append(Spacer(1, 1*cm))
    story.append(Paragraph(texto_diagramas(), styles["CorpoTexto"]))             
    story.append(img1)
    story.append(Spacer(1, 1*cm))
    story.append(Paragraph("5.1 - Parametrização do inversor ", styles['SubSecao']))
    story.append(Spacer(1, 1*cm))
    story.append(Paragraph(texto_parametrizacao(), styles["CorpoTexto"]))
    story.append(Spacer(1, 2*cm))
    story.append(Paragraph("5.1.1 - Ajuste de sobre e Subtensão ", styles['SubSecao']))
    story.append(tabela_parametros_tensao_inversor)
    story.append(Spacer(1, 1*cm))
    story.append(Paragraph("5.1.2 - Ajustes dos Limites de Freqüência (sobre e subfreqüência) ", styles['SubSecao']))
    story.append(tabela_parametros_frequencia_inversor)
    story.append(Spacer(1, 1*cm))
    story.append(Paragraph(" 5.1.3 - Ajustes do Limite do Fator de Potência", styles['SubSecao']))
    story.append(tabela_parametros_fp_inversor)
    story.append(Spacer(1, 2*cm))
    story.append(Paragraph("6 - INSTALAÇÃO ELÉTRICA", styles['TituloSecao']))
    story.append(Paragraph(texto_instalacao(), styles['CorpoTexto']))
    story.append(Spacer(1, 1*cm))
    story.append(Paragraph(" 6.1 – Diagrama unifilar Geral", styles['SubSecao']))
    story.append(Paragraph(texto_diagramauni(), styles["CorpoTexto"]))
    story.append(Spacer(1, 1*cm))
    story.append(Paragraph(" 6.2 – Dimensionamento da Proteção e Alimentação do Gerador Fotovoltaico", styles['SubSecao']))
    story.append(Paragraph(texto_dimensionamento_protecao(), styles['CorpoTexto']))
    story.append(PageBreak())
    insert_equation(equacao3,story,'corrente.png')
    if inputs['dados_cliente']['quantidade_inversor2'] not in [None, 0]:
        from utils.equacoes import equacao3_2
        insert_equation(equacao3_2,story,'corrente2.png')
    if inputs['dados_cliente']['quantidade_inversor3'] not in [None, 0]:
        from utils.equacoes import equacao3_3
        insert_equation(equacao3_3,story,'corrente3.png')    
    #AJEITAR ESSA LÓGICA PARA NÃO PRECISAR DO IF NO MEIO DO GERADOR DE TEXTO.    
    story.append(Spacer(1, 1*cm))
    story.append(Paragraph(texto_dimensionamento_protecao2(), styles['CorpoTexto']))
    insert_equation(equacao4,story,'quedatensao.png')
    story.append(Spacer(1, 1*cm))
    story.append(tabela_queda_tensao)
    story.append(Spacer(1, 1*cm))
    story.append(Paragraph(texto_dimensionamento_protecao3(), styles['CorpoTexto']))
    story.append(Paragraph(" 6.3 – Coordenação entre o Disjuntor do Gerador Fotovoltaico e da Proteção Geral", styles['SubSecao']))
    story.append(Spacer(1, 1*cm))
    story.append(Paragraph(texto_disjuntores(), styles["CorpoTexto"]))
    story.append(PageBreak())
    story.append(Paragraph("7 – SINALIZAÇÃO", styles['TituloSecao']))
    story.append(Paragraph(texto_sinalizacao(), styles["CorpoTexto"]))
    story.append(img2)
    story.append(Spacer(1, 2*cm))
    story.append(PageBreak())
    story.append(Paragraph("8 – RESPONSÁVEL TÉCNICO", styles['TituloSecao']))
    story.append(Spacer(1, 3*cm))
    story.append(img3)

    doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)

def gerar_procuracao(inputs):
    proc = SimpleDocTemplate(r"C:\Users\DIEGO\Desktop\code\projetosolar\output\procuracao.pdf", pagesize=A4, leftMargin=2*cm, rightMargin=2*cm, topMargin=2*cm, bottomMargin=2*cm)
    procuracao = []
    procuracao.append(Paragraph("PROCURAÇÃO PARTICULAR", styles['Title']))
    procuracao.append(Spacer(1, 4*cm))
    procuracao.append(Paragraph(texto_procuracao(), styles['CorpoTexto']))
    procuracao.append(Spacer(1, 12*cm))
    procuracao.append(tabela_assinatura)
    proc.build(procuracao)
