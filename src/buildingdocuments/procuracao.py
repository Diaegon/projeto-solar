

def gerar_procuracao(inputs):
    proc = SimpleDocTemplate(r"C:\Users\DIEGO\Desktop\code\projetosolar\output\procuracao.pdf", pagesize=A4, leftMargin=2*cm, rightMargin=2*cm, topMargin=2*cm, bottomMargin=2*cm)
    procuracao = []
    procuracao.append(Paragraph("PROCURAÇÃO PARTICULAR", styles['Title']))
    procuracao.append(Spacer(1, 4*cm))
    procuracao.append(Paragraph(texto_procuracao(), styles['CorpoTexto']))
    procuracao.append(Spacer(1, 12*cm))
    procuracao.append(tabela_assinatura)
    proc.build(procuracao)
