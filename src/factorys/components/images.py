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


def render_equation_to_image(equation, filename):
    fig = plt.figure(figsize=(3, 1))
    plt.text(0.5, 0.5, f"${equation}$", fontsize=20, ha='center', va='center')
    plt.axis('off')
    plt.savefig(filename, bbox_inches='tight', pad_inches=0.1, dpi=200)
    plt.close()

def insert_equation(equation, story, img_filename):
    render_equation_to_image(equation, img_filename)
    img = Image(img_filename)
    img.drawHeight = 50
    img.drawWidth = 250
    story.append(img)