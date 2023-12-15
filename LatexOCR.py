from PIL import Image
from pix2tex.cli import LatexOCR
import pyclip
# https://github.com/lukas-blecher/LaTeX-OCR


imgPath = pyclip.paste()
# imgPath = "/Users/lyk/Documents/cache/Snipaste_2023-11-03_10-51-24.png"
img = Image.open(imgPath)
model = LatexOCR()
print(model(img))