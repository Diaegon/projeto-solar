from reportlab.platypus import Image
from reportlab.lib.units import cm
import matplotlib.pyplot as plt

#IMAGENS
imagem1_caminho = 'diagramasolar.png'
img1 = Image(imagem1_caminho, width=10*cm, height=7*cm)

imagem2_caminho ='aviso.png'
img2 = Image(imagem2_caminho, width=18*cm, height=15*cm)

imagem3_caminho = 'ASSINATURA.png'
img3 = Image(imagem3_caminho, width=15*cm, height=4*cm)
