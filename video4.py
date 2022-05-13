import re
import cv2
from pytesseract import pytesseract
import numpy as np

caminho_tesseract = r"D:\Tesseract-OCR\tesseract.exe"
pytesseract.tesseract_cmd = caminho_tesseract

fig = "video720p.mkv"

cap = cv2.VideoCapture("resource/" + fig )

while 1:
    _, frame = cap.read()

    (x, y, w, h) = (360, 565, 400, 140)
    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

    roi = frame[y:y + h, x:x + w]

    cinza = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
            
    _, bin = cv2.threshold(cinza, 90, 255, cv2.THRESH_BINARY)
    
    desfoque = cv2.GaussianBlur(bin , (5, 5), 0)

    contornos, hier = cv2.findContours(desfoque, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    for c in contornos:
        perimetro = cv2.arcLength(c, True)
        if perimetro > 170:
            aprox = cv2.approxPolyDP(c, 0.02 * perimetro, True)

            if len(aprox) == 4:
                (x, y, w, h) = cv2.boundingRect(c)

                cv2.rectangle(roi, (x, y), (x + w, y + h), (0, 255, 0), 2)

                roi2 = desfoque[y:y + h, x:x + w]

                # cv2.imwrite("res4/roi.jpg", roi2)
                resize_img_roi = cv2.resize(roi2, None, fx=4, fy=4, interpolation=cv2.INTER_CUBIC)

                kernel = np.ones((1,1),np.uint8)
                erosion = cv2.erode(resize_img_roi,kernel,iterations = 1)

                texto = pytesseract.image_to_string(erosion)

                linhas = texto.split("\n")
                for linha in linhas:
                    if not linha.isspace() and len(linha) > 0:
                        if re.search("[A-Z/a-z/0-9]{3}-[0-9/A-Z/a-z]{4}", linha):
                            print(linha)


    cv2.imshow("frame", frame)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()