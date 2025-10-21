from reportlab.platypus import Image
from reportlab.lib.units import cm
import matplotlib.pyplot as plt
from src.config import IMAGES_DIR

#IMAGENS
imagem1_caminho = f'{IMAGES_DIR}/diagramasolar.png'
img1 = Image(imagem1_caminho, width=10*cm, height=7*cm)

imagem2_caminho =f'{IMAGES_DIR}/aviso.png'
img2 = Image(imagem2_caminho, width=18*cm, height=15*cm)

imagem3_caminho = f'{IMAGES_DIR}/ASSINATURA.png'
img3 = Image(imagem3_caminho, width=15*cm, height=4*cm)
