from datetime import datetime
import numpy as np
import cv2


def center(x, y, w, h):
    x1 = int(w / 2)
    y1 = int(h / 2)
    cx = x + x1
    cy = y + y1
    return cx, cy


fig = "video720p.mkv"

cap = cv2.VideoCapture("resource/" + fig )

fgbg = cv2.createBackgroundSubtractorMOG2()

detects = []

posL = 150
offset = 30

xy1 = (20, posL)
xy2 = (300, posL)

total = 0

up = 0
down = 0

maior = 0

while 1:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # cv2.imshow("gray", gray)

    fgmask = fgbg.apply(gray)
    # cv2.imshow("fgmask", fgmask)

    retval, th = cv2.threshold(fgmask, 200, 255, cv2.THRESH_BINARY)
    # cv2.imshow("th", th)

    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))

    opening = cv2.morphologyEx(th, cv2.MORPH_OPEN, kernel, iterations=2)
    # cv2.imshow("opening", opening)

    dilation = cv2.dilate(opening, kernel, iterations=8)
    # cv2.imshow("dilation", dilation)

    closing = cv2.morphologyEx(dilation, cv2.MORPH_CLOSE, kernel, iterations=8)
    # cv2.imshow("closing", closing)

    contours, hierarchy = cv2.findContours(closing, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    i = 0
    for cnt in contours:
        (x, y, w, h) = cv2.boundingRect(cnt)

        area = cv2.contourArea(cnt)

        if int(area) > 60000:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            roi = frame[y:y + w, x:x + h]
            mic = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
            cv2.imwrite("res2/" + fig + " " + mic + ".jpg", roi)

    cv2.imshow("frame", frame)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
