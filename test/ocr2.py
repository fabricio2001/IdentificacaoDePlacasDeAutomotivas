from time import sleep
import os
import cv2
import numpy as np
from pytesseract import pytesseract
from datetime import datetime

caminho_tesseract = r"D:\Tesseract-OCR\tesseract.exe"
pytesseract.tesseract_cmd = caminho_tesseract

pasta = './res3'
for diretorio, subpastas, arquivos in os.walk(pasta):
    for arquivo in arquivos:
        fig = "res3/" + arquivo
        img_roi = cv2.imread(fig)

        resize_img_roi = cv2.resize(img_roi, None, fx=4, fy=4, interpolation=cv2.INTER_CUBIC)

        # Converte para escala de cinza
        img_cinza = cv2.cvtColor(resize_img_roi, cv2.COLOR_BGR2GRAY)

        # Binariza imagem
        _, img_binary = cv2.threshold(img_cinza, 70, 255, cv2.THRESH_BINARY)

        # Desfoque na Imagem
        img_desfoque = cv2.GaussianBlur(img_binary, (5, 5), 0)

        kernel = np.ones((1,1),np.uint8)
        erosion = cv2.erode(img_desfoque,kernel,iterations = 1)

        # mic = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        # cv2.imwrite("res4/erosion " + mic + ".jpg", erosion)

        # sleep(1)

        texto = pytesseract.image_to_string(erosion)
        linhas = texto.split("\n")
        print("_____________________________")
        for linha in linhas:
            if not linha.isspace() and len(linha) > 0:
                print(linha)
