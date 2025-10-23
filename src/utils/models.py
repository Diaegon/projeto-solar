from enum import Enum

#Base Enum para outras classes Enum
class BaseEnum(str, Enum):
    def __repr__(self):
        return self.value

class tensao_fase(BaseEnum):
    MONOFASICO = "monofasico"
    BIFASICO = "bifasico"
    TRIFASICO = "trifasico"

class classe_consumo(BaseEnum):
    RESIDENCIAL = "residencial"
    COMERCIAL = "comercial"
    INDUSTRIAL = "industrial"
    RURAL = "rural"

class ramal_energia(BaseEnum):
    AEREO = "aereo"
    SUBTERRANEO = "subterraneo"

class tipo_inversor(BaseEnum):
    STRING = "string"
    MICRO = "micro"
