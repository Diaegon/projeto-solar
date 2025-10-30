from pydantic import BaseModel, EmailStr

from src.utils.models import tensao_fase, classe_consumo, ramal_energia, tipo_inversor


class Cliente(BaseModel):
    id_cliente: int | None
    nome_cliente: str
    cpf: str 
    data_nascimento: str 
    razao_social: str | None
    nome_fantasia: str | None
    cnpj: str | None
    rg: str
    telefone_cliente: str
    email_cliente: EmailStr

class EnderecoCliente(BaseModel):
    logradouro_cliente: str
    numero_casa_cliente: str
    complemento_casa_cliente: str | None
    cep_cliente: str
    bairro_cliente: str
    cidade_cliente: str
    estado_cliente: str

class EnderecoObra(BaseModel):
    logradouro_obra: str
    numero_obra: str
    complemento_obra: str | None
    cep_obra: str
    bairro_obra: str
    cidade_obra: str
    estado_obra: str
    latitude_obra: float
    longitude_obra: float

class Inversor(BaseModel):
    id_inversor: int | None
    marca_inversor: str
    modelo_inversor: str
    potencia_inversor: float
    numero_fases: tensao_fase
    tipo_inversor: tipo_inversor
    numero_mppt: int | None #reservado para atualizações futuras

    @property
    def multiplicador(self) -> float:
        """Retorna o multiplicador baseado no número de fases."""
        if self.numero_fases == 'monofasico':
            return 1.0
        elif self.numero_fases == 'trifasico':
            return 1.732
        else:
            raise ValueError("Número de fases inválido")
    
    @property
    def inversor_tensao(self) -> int:
        """Retorna a tensão baseada no número de fases."""
        if self.numero_fases == 'monofasico':
            return 220
        elif self.numero_fases == 'trifasico':
            return 380
        else:
            raise ValueError("Número de fases inválido")

    @property
    def corrente_saida(self) -> float:
        """Calcula a corrente de saída do inversor."""
        return self.potencia_inversor / (self.multiplicador * self.inversor_tensao)        

    @property
    def disjuntor_protecao(self) -> int:
        """Calcula o disjuntor de proteção do inversor."""
        corrente = self.corrente_saida
        if corrente <= 10:
            return 10
        elif corrente <= 16:
            return 16
        elif corrente <= 20:
            return 20
        elif corrente <= 25:
            return 25
        elif corrente <= 32:
            return 32
        elif corrente <= 40:
            return 40
        elif corrente <= 50:
            return 50
        elif corrente <= 63:
            return 63
        elif corrente <= 80:
            return 80
        else:
            raise ValueError("Corrente de saída muito alta para disjuntor padrão")

    @property
    def cabo_energia_inversor(self) -> str:
        """Determina o cabo de energia baseado na corrente de saída."""
        corrente = self.corrente_saida
        if corrente <= 27:
            return "4 mm²"
        elif corrente <= 35:
            return "6 mm²"
        elif corrente <= 49:
            return "10 mm²"
        elif corrente <= 67:
            return "16 mm²"
        elif corrente <= 88:
            return "25 mm²"
        elif corrente <= 110:
            return "35 mm²"
        else:
            raise ValueError("Corrente de saída muito alta para cabo padrão")

    @property
    def corrente_max_cabo(self) -> str:
        """Determina a corrente máxima do cabo baseado na corrente de saída."""
        corrente = self.corrente_saida
        if corrente <= 28:
            return "28 A"
        elif corrente <= 36:
            return "36 A"
        elif corrente <= 50:
            return "50 A"
        elif corrente <= 68:
            return "68 A"
        elif corrente <= 89:
            return "89 A"
        elif corrente <= 111:
            return "111 A"
        else:
            raise ValueError("Corrente de saída muito alta para cabo padrão")

    @property
    def quantidade_string(self) -> int:
        if self.potencia_inversor <= 7000:
            return 2
        elif self.potencia_inversor <= 10000:
            return 3
        elif self.potencia_inversor <= 15000:
            return 4
        elif self.potencia_inversor <= 20000:
            return 6
        elif self.potencia_inversor <= 40000:
            return 8

class Placa(BaseModel):
    id_placa: int | None
    marca_placa: str
    modelo_placa: str
    potencia_placa: float
    tipo_celula: str
    tensao_pico: float
    corrente_curtocircuito: float
    tensao_maxima_potencia: float
    corrente_maxima_potencia: float
    eficiencia_placa: float | None #reservado para atualizações futuras

class Projetista(BaseModel):
    id_projetista: int | None
    nome_projetista: str
    creci_projetista: str
    rubrica_projetista: str
    telefone_projetista: str
    email_projetista: EmailStr

class Procurador(BaseModel):
    id_procurador: int | None
    nome_procurador: str
    cpf_procurador: str 
    rg_procurador: str
    telefone_procurador: str
    email_procurador: EmailStr
    logradouro_procurador: str
    numero_casa_procurador: str
    complemento_procurador: str | None
    cep_procurador: str
    bairro_procurador: str
    cidade_procurador: str
    estado_procurador: str

class ConfiguracaoSistema(BaseModel):
    inversor: Inversor
    quantidade_inversor: int
    
    placa: Placa
    quantidade_total_placas_do_sistema: dict

    placa2: Placa | None = None
    placa3: Placa | None = None
    placa4: Placa | None = None
   
    
    @property
    def texto_final_inversor(self):
        textos = []
        textos.append(f"{self.quantidade_inversores} inversor(es) {self.inversor.marca_inversor} {self.inversor.modelo_inversor}")
        if self.quantidade_inversores2 and self.quantidade_inversores2 > 0:
            textos.append(f"{self.quantidade_inversores2} inversor(es) {self.inversor2.marca_inversor} {self.inversor2.modelo_inversor}")
        if self.quantidade_inversores3 and self.quantidade_inversores3 > 0:
            textos.append(f"{self.quantidade_inversores3} inversor(es) {self.inversor3.marca_inversor} {self.inversor3.modelo_inversor}")
        return ' e '.join(textos)

class Projeto(BaseModel):
    id_projeto: int | None
    
    numero_unidade_consumidora: str
    carga_instalada_kw: float
    disjuntor_geral_amperes: float
    energia_media_mensal_kwh: float
    classe_consumo:  classe_consumo #residencial, comercial, industrial, rural
    tipo_fornecimento: tensao_fase #monofasico, bifasico, trifasico
    ramal_energia: ramal_energia #aéreo, subterrâneo
    data_projeto: str
    quantidade_sistemas_instalados: int
    cliente: Cliente
    endereco_cliente: EnderecoCliente
    endereco_obra: EnderecoObra
    projetista: Projetista
    procurador: Procurador
    sistema_instalado: list[ConfiguracaoSistema]
    #quantidades de placas e inversores, por enquanto definidas pelo json de entrada.


    def definicao_arranjo_sistema():
        ...
