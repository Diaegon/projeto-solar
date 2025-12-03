import json
from reportlab.platypus import Table, Paragraph, TableStyle
from src.schemas.tableschemas import styles, estilotabela, estilotabelaloc, estilo_tabela_parametros, estilo_assinatura

class TablesBuilder():
    def __init__(self,retorno):
        self.retorno = retorno

    def Tabela_dados(self):
        dados = [[f"UC: {retorno.numero_uc}"], 
         [f"CLASSE: {retorno.classe_consumo} {retorno.tipo_fornecimento}"], 
         [f"Nome do Cliente: {retorno.nome_cliente}"],
         [f"Endereço: {retorno.logradouro_obra}, {retorno.numero_obra}  {retorno.complemento_obra}, {retorno.bairro_obra},{retorno.cidade_obra} {retorno.estado_obra}."],
         [f"CEP:{retorno.cep_obra}"],
         [f"CPF/CNPJ: {retorno.cpf}"]]
        
        tabeladedados = Table(dados)
        tabeladedados.setStyle(estilotabela)

        return tabeladedados#tabela localização da obra

    def Tabela_localizacao(self):
        loc_instalacao = [["COORDENADAS - coordenadas decimais - WGS 84 "],
                  [" Local de implantação do Gerador fotovoltaico",
                      "Lat: ", "Long: "],
                  ["", f"{retorno.latitude_obra}", f"{retorno.longitude_obra}"]]

        tabela_localizacao = Table(loc_instalacao)
        tabela_localizacao.setStyle(estilotabelaloc)
        return tabela_localizacao


    def Tabela_especificacoes_tecnicas(self):
        #tabelas especificações técnicas
        modulo_caracteristicas = [["Potência nominal máx. (Pmax) ", f"({retorno.texto_potencia_placa} )Wp"],
                                ["Tensão operacional opt. (Vmp) ", f"({retorno.texto_tensao_individual_paineis} )V"],
                                ["Corrente operacional opt. (Imp)", f"({retorno.corrente_mp}) A"], 
                                ["Tensão circuito aberto (Voc) ", f"({retorno.tensao_circuito_aberto} )V"], 
                                ["Corrente curto-circuito (Isc)", f"({retorno.corrente_cc}) A"]]
        tabelapainel = Table(modulo_caracteristicas)
        tabelapainel.setStyle(estilotabela)
        return tabelapainel

    def Tabela_parametrizacao_inversor(self):
        #tabela parametrização inversor
        parametros_tensao_inversor = [["Faixa de tensão no ponto de conexão [V]","Tempo de desconexão [s]"],
                                    ["TL > 231","0,2 s"], 
                                    ["189 ≤ TL ≤ 231","Operação Normal"], 
                                    ["TL < 195,5","0,2 s"]]
        tabela_parametros_tensao_inversor = Table(parametros_tensao_inversor)
        tabela_parametros_tensao_inversor.setStyle(estilo_tabela_parametros)

        parametros_frequencia_inversor = [["Faixa de freqüência no ponto de conexão (Hz)","Tempo de desconexão [s]"],
                                        ["f ≤ 57,5","0,2"],
                                        ["59,9 < f ≤ 60,1","Operação normal"],
                                        ["f > 62,5","0,2"] ]
        tabela_parametros_frequencia_inversor = Table(parametros_frequencia_inversor)
        tabela_parametros_frequencia_inversor.setStyle(estilo_tabela_parametros)

        parametros_fp_inversor = [["Potência Nominal (W) - Pn","Faixa de fator de potência","Fator de potência \nconfiguração em fábrica"],
                                [f"{retorno.potencia_inversores}","0,95 indutivo – 0,95 capacitivo","1"]]
        tabela_parametros_fp_inversor = Table(parametros_fp_inversor)
        tabela_parametros_fp_inversor.setStyle(estilo_tabela_parametros)
        return tabela_parametros_fp_inversor

    def Tabela_parametros_queda_tensao(self):
        #parametros de queda de tensão
        queda_tensao = [["ρ  - resistividade do cobre","0,0173"],
                        [Paragraph("L<sub>c</sub> - comprimento do condutor",styles["CorpoTexto"]),"10 m"], 
                        [Paragraph("I<sub>c</sub> - corrente do condutor",styles["CorpoTexto"]),f"({retorno.corrente_saida_por_inversor}) A"],
                        ["Cosφ - fator de potencia","1"],
                        [Paragraph("S<sub>c</sub> - Seção reta do condutor",styles["CorpoTexto"]), f"({retorno.texto_cabos}) mm²"], 
                        [Paragraph("V <sub>f</sub> - tensão ", styles["CorpoTexto"]), f"{retorno.inversor_tensao}"]]
        tabela_queda_tensao = Table(queda_tensao)
        tabela_queda_tensao.setStyle(estilotabela)
        return tabela_queda_tensao

    def Tabela_assinatura_responsavel_tecnico(self):
        #assinatura do responsável técnico
        assinatura = [[""],[f"                  {retorno.nome_cliente}, CPF:{retorno.cft_crea}                    "], [f"{retorno.data_hoje}"]]
        tabela_assinatura = Table(assinatura)
        tabela_assinatura.setStyle(estilo_assinatura)
        return tabela_assinatura

if __name__ == "__main__":
    from src.factorys.datas.createobject import ProjectFactory
    from src.config import INPUTS_DIR
    import json
    from src.factorys.datas.documentbuilder import ObjetosCalculados
    import pprint
    file = INPUTS_DIR / "input_solar.json"
    inputs = json.loads(file.read_text(encoding="utf-8"))
    
    projeto = ProjectFactory.factory(inputs)
    retorno = ObjetosCalculados(projeto).construtor_dados_memorial()
    pprint.pprint(f"retorno:{retorno}")