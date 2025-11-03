from src.factorys.factorydatas.factoryobject import projeto
from datetime import datetime
from dateutil.relativedelta import relativedelta
import locale
import pprint

class objetos_calculados:
    def __init__(self):
        self.quantidade_final_placas = 0
        self.potencia_total_paineis_final = 0
        self.potencia_total_inversores_final = 0
    
    @property
    def data_de_hoje(self):
        data_de_hoje = datetime.now()
        # data_futura = data_de_hoje+relativedelta(months=1)
        # locale.setlocale(locale.LC_TIME, 'pt_BR.utf8')
        # plt.rcParams['text.usetex'] = True # Ativar o uso do LaTeX real (MikTeX)
        return data_de_hoje
    
    @property
    def data_futura(data_de_hoje):
        data_futura = data_de_hoje+relativedelta(months=1)
        return data_futura
    
    @property
    def equacao_demanda(self):
        resultado = projeto.energia_media_mensal_kwh / 720
        equacao = fr"$D_{{\mathrm{{media}}}} = \frac{{\mathrm{{Energia\ media}}}}{{N^{{\circ}}\,\mathrm{{de\ horas}}}} = \frac{{{projeto.energia_media_mensal_kwh}}}{{720}} = {resultado:.2f}\ kW$"
        return equacao
    
    @property
    def calculo_fator_de_carga(self):
        fatordecarga = (projeto.energia_media_mensal_kwh / 720) / projeto.carga_instalada_kw
        equacao2 = fr"$FC = \frac{{\mathrm{{Energia}}}}{{\mathrm{{Potencia \ instalada \ x \ 720h}}}} = \frac{{{projeto.energia_media_mensal_kwh}}}{{{projeto.carga_instalada_kw} \ x  \ 720}} = {fatordecarga:.2f}\ kW$"
        return equacao2
    
    #conta a quantidade de placas de um sistema considerando que um sistema só vai ter no máximo dois tipos de placa.
    def conta_placa_do_sistema(self,i):
        sistemas_instalados = projeto.sistema_instalado[i]
        quantidade_final = []
        #debug
        quantidade_placas_lista = list(sistemas_instalados.quantidade_total_placas_do_sistema.values())

        quantidade_placa1 = quantidade_placas_lista[0] 
        modelo = sistemas_instalados.placa.modelo_placa
        marca = sistemas_instalados.placa.marca_placa
        potencia = sistemas_instalados.placa.potencia_placa
        quantidade_ = [modelo, marca, potencia,quantidade_placa1]
        quantidade_final.append(quantidade_)
        self.quantidade_final_placas += quantidade_placa1 
        
        #monta a lista
        #  
        if quantidade_placas_lista[1] not in [None, 0]:
            quantidade_placa2 = quantidade_placas_lista[1]
            modelo2 =  sistemas_instalados.placa2.modelo_placa
            marca2 = sistemas_instalados.placa2.marca_placa
            potencia2 = sistemas_instalados.placa2.potencia_placa
            quantidade_2 = [modelo2, marca2, potencia2,quantidade_placa2]
            quantidade_final.append(quantidade_2) 
            self.quantidade_final_placas += quantidade_placa2
        
        
        return quantidade_final
        
    #calcula a distribuição das placas no inversor, como nesse projeto cada sistema só tem um inversor, fica mais simples o calculo
    #vamos deixar a resposta crua sem identificar quais placas vão ser arranjadas;
    def distribui_placa_por_inversor(self,quantidade_sistemas):
        numero_strings = projeto.sistema_instalado[quantidade_sistemas].inversor.numero_mppt
        numero_de_inversores = projeto.sistema_instalado[quantidade_sistemas].quantidade_inversor
        
        placas_sistema = self.conta_placa_do_sistema(quantidade_sistemas)
        numero_painel1 = placas_sistema[0][3]
        self.potencia_total_paineis_final += placas_sistema[0][3] * placas_sistema[0][2]
        numero_de_paineis = numero_painel1
        if placas_sistema[1][3]:
            numero_painel2 = placas_sistema[1][3]
            self.potencia_total_paineis_final += placas_sistema[1][3] * placas_sistema[1][2]
            numero_de_paineis += numero_painel2

        lista_string = []

        resto_placas_por_string = numero_de_paineis % numero_strings
        placas_por_string = numero_de_paineis // numero_strings
        for numero_mppt in range(numero_strings):
            lista_string.append(placas_por_string)
        if resto_placas_por_string != 0:
            lista_string[-1] += resto_placas_por_string
        return lista_string

    #aqui iteramos sobre cada sistema instalado
    @property
    def calculo_disposicao_placas(self):
        quantidade_final_de_placas_por_inversor = []
        
        for quantidade_sistemas in range(projeto.quantidade_sistemas_instalados):
            quantidade_de_placas_por_inversor = self.distribui_placa_por_inversor(quantidade_sistemas)
            quantidade_final_de_placas_por_inversor.append(quantidade_de_placas_por_inversor)
        #retornamos a quantidade final de placas caso tenha mais de um sistema instalado.
        return quantidade_final_de_placas_por_inversor

    @property
    def calculo_potencia_efetiva(self):        
        return self.potencia_total_paineis_final * 0.745 / 1000
    
    @property
    def energia_gerada(self):
        return self.calculo_potencia_efetiva * 5.84 * 30 

    @property
    def equacao_protecao_inversor(self):
        # equacao3 = fr"$I_{{\mathrm{{AG}}}} = 
        # \frac{{\mathrm{{potencia\ nominal }}}}{{\mathrm{{Tensao\ nominal * {projeto.sistema_instalado.inversor.multiplicador}}}}} = 
        # \frac{{{projeto.sistema_instalado.inversor.potencia_inversor}}}{{{projeto.sistema_instalado.inversor.inversor_tensao * projeto.sistema_instalado.inversor.multiplicador}}} 
        # = {projeto.sistema_instalado.inversor.corrente_saida:.2f}\ A$" 
        equacao = (
            fr"$I_{{\mathrm{{AG}}}} = "
            fr"\frac{{\mathrm{{potência\ nominal}}}}"
            fr"{{\mathrm{{Tensão\ nominal * {projeto.sistema_instalado.inversor.multiplicador}}}}}"
            fr" \\[6pt] = "
            fr"\frac{{{projeto.sistema_instalado.inversor.potencia_inversor}}}"
            fr"{{{projeto.sistema_instalado.inversor.inversor_tensao * projeto.sistema_instalado.inversor.multiplicador}}}"
            fr" \\[6pt] = {projeto.sistema_instalado.inversor.corrente_saida:.2f}\ A$"
        )
        return equacao
    
    @property
    def equacao_queda_tensao(self):
        equacao4 = fr"$\Delta V \% = \frac{{200*\rho*L_c*I_c*cos\varphi}}{{S_c*V_f}}$"
        return equacao4

    @property
    def calculo_queda_tensao(self):
        tensao_queda = (200 * 0.0173 * 10 * projeto.sistema_instalado.inversor.corrente_saida) / (projeto.sistema_instalado.inversor.inversor_tensao * cprojeto.sistema_instalado.inversor.cabo_energia_inversor)
        return tensao_queda
    
    @property
    def get_classe_codigo(self):
        classe_cliente = projeto.classe_consumo
        if classe_cliente == "residencial":
            classe_codigo = "B1"
        elif classe_cliente == "rural":
            classe_codigo = "B2"
        elif classe_cliente == "comercial":
            classe_codigo = "B3"

        return classe_codigo
