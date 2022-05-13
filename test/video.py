import numpy as np
import cv2


fig = "video720p.mkv"

cap = cv2.VideoCapture("resource/" + fig )

while 1:
    ret, frame = cap.read()

    cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    _, bin = cv2.threshold(cinza, 90, 255, cv2.THRESH_BINARY)

    desfoque = cv2.GaussianBlur(bin , (5, 5), 0)

    contornos, hier = cv2.findContours(desfoque, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    
    for c in contornos:
        perimetro = cv2.arcLength(c, True)
        if perimetro > 170 and perimetro < 380:
            aprox = cv2.approxPolyDP(c, 0.03 * perimetro, True)

            if len(aprox) == 4:
                (x, y, alt, lar) = cv2.boundingRect(c)
                cv2.rectangle(frame, (x, y), (x + alt, y + lar), (0, 255, 0), 2)

    cv2.imshow("frame", frame)

    if cv2.waitKey(30) & 0xFF == ord('0'):
        break

cap.release()
cv2.destroyAllWindows()