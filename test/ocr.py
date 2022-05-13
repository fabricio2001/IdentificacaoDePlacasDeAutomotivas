# D:\Tesseract-OCR

from pytesseract import pytesseract
from pprint import pprint
caminho_tesseract = r"D:\Tesseract-OCR\tesseract.exe"
pytesseract.tesseract_cmd = caminho_tesseract

texto = pytesseract.image_to_string("resource/2.png")

# pprint(texto)
# print(len(texto))
# print(texto)
# print(texto[0])
# print(texto.split("\n"))
# print(texto[0:texto.index("\n")])

linhas = texto.split("\n")
# print(linhas)

for linha in linhas:
    if not linha.isspace() and len(linha) > 0:
        print(linha)