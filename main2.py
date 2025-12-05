from typing import Union
from fastapi import FastAPI
from fastapi.responses import FileResponse

from src.factorys.datas.createobject import ProjectFactory
from src.factorys.datas.documentbuilder import ObjetosCalculados
from src.config import INPUTS_DIR
import json 


file = INPUTS_DIR / "input_solar.json"
inputs = json.loads(file.read_text(encoding="utf-8"))

projeto = ProjectFactory.factory(inputs)
retorno = ObjetosCalculados(projeto).construtor_dados_memorial()



app = FastAPI()

@app.get("/")
def read_root():
    recebe = retorno
    return recebe

@app.get("/pdf")
def get_pdf():
    pdf_path = "output/diagrama.pdf"
    return FileResponse(
        pdf_path,
        media_type="application/pdf",
        filename="resultado.pdf"
    )

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}