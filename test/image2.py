import os
from time import sleep
import cv2
from datetime import datetime

pasta = './res2'
for diretorio, subpastas, arquivos in os.walk(pasta):
    for arquivo in arquivos:

        fig = "res2/" + arquivo

        img = cv2.imread(fig)
        # cv2.imshow("img", img)

        cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # cv2.imshow("cinza", cinza)

        _, bin = cv2.threshold(cinza, 90, 255, cv2.THRESH_BINARY)
        # cv2.imshow("bin", bin)

        desfoque = cv2.GaussianBlur(bin , (5, 5), 0)
        # cv2.imshow("desfoque", desfoque)

        contornos, hier = cv2.findContours(desfoque, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

        # cv2.drawContours(img, contornos, -1, (0, 255, 0), 2)
        # cv2.imshow("contornos", img)

        for c in contornos:
            perimetro = cv2.arcLength(c, True)
            if perimetro > 170:
                aprox = cv2.approxPolyDP(c, 0.03 * perimetro, True)

                if len(aprox) == 4:
                    (x, y, w, h) = cv2.boundingRect(c)
                    if w > h:
                        if w > 90:
                            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

                            roi = img[y:y + h, x:x + w]
                            sleep(0.4)
                            mic = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
                            cv2.imwrite("res3/" + mic + ".jpg", roi)
                            
