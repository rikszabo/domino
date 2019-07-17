import cv2
import numpy as np
import os
import sys
from scipy import ndimage
from PyQt5 import QtGui, QtCore, QtWidgets

count = 0


def makeTemplatesAndMasks(templateImage):
    image_basic = cv2.imread(templateImage)
    for deg in range(360):
        print('create template: ' + str(deg))
        tmpl = ndimage.rotate(image_basic, deg)
        cv2.imwrite(os.path.join('tmp' + str(deg) + '.png'), tmpl)

    for deg in range(360):
        tmpl = cv2.imread(os.path.join('tmp' + str(deg) + '.png'), 0)
        ret2, mask = cv2.threshold(tmpl, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        cv2.imwrite(os.path.join('mask' + str(deg) + '.png'), mask)


def match(img_name, template_image, threshold):
    img_rgb = cv2.imread(os.path.join(img_name))
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

    global count
    visualization = 1
    res = 1  # degree-interval
    #threshold - küszöb

    for deg in range(0, 360, res):
        tmpl = cv2.imread(os.path.join('tmp' + str(deg) + '.png'), 0)
        mask = cv2.imread(os.path.join('mask' + str(deg) + '.png'), 0)
        w, h = tmpl.shape[::-1]
        hit = cv2.matchTemplate(img_gray, tmpl, cv2.TM_SQDIFF, mask=mask)

        loc = np.where(hit < threshold)
        for pt in zip(*loc[::-1]):
            cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
            if visualization == 1:  # csak egyszer írunk ki egy detektalast
                picture = cv2.imread(template_image)
                cv2.imshow('basic_picture' + str(count), picture)
                visualization = 0
                count = count+1
                print('Match detected!')
        cv2.imwrite('res.png', img_rgb)


def firstButton():
    makeTemplatesAndMasks('domino_minta01.jpg')
    match('domino-65136_960_720.jpg', 'domino_minta01.jpg', 45)

    makeTemplatesAndMasks('domino_minta02.jpg')
    match('res.png', 'domino_minta02.jpg', 45)

    makeTemplatesAndMasks('domino_minta03.jpg')
    match('res.png', 'domino_minta03.jpg', 45)

    makeTemplatesAndMasks('domino_minta04.jpg')
    match('res.png', 'domino_minta04.jpg', 45)

    # makeTemplatesAndMasks('domino_minta05.jpg')
    # match('res.png', 'domino_minta05.jpg', 45)

    # makeTemplatesAndMasks('domino_minta06.jpg')
    # match('res.png', 'domino_minta06.jpg', 45)

    # makeTemplatesAndMasks('domino_minta07.jpg')
    # match('res.png', 'domino_minta07.jpg', 45)

    # makeTemplatesAndMasks('domino_minta08.jpg')
    # match('res.png', 'domino_minta08.jpg', 45)

    # makeTemplatesAndMasks('domino_minta09.jpg')
    # match('res.png', 'domino_minta09.jpg', 45)

    # makeTemplatesAndMasks('domino_minta10.jpg')
    # match('res.png', 'domino_minta10.jpg', 45)

    makeTemplatesAndMasks('domino_group.jpg')
    match('res.png', 'domino_group.jpg', 45)

    image_basic2 = cv2.imread('res.png')
    cv2.imshow('detected', image_basic2)
    cv2.waitKey()


def secondButton():
    makeTemplatesAndMasks('domino_minta11.jpg')
    match('img_como_jugar_al_domino_1206_600.jpg', 'domino_minta11.jpg', 60)

    makeTemplatesAndMasks('domino_minta12.jpg')
    match('res.png', 'domino_minta12.jpg', 60)

    makeTemplatesAndMasks('domino_minta13.jpg')
    match('res.png', 'domino_minta13.jpg', 60)

    makeTemplatesAndMasks('domino_minta14.jpg')
    match('res.png', 'domino_minta14.jpg', 60)

    makeTemplatesAndMasks('domino_minta15.jpg')
    match('res.png', 'domino_minta15.jpg', 99)

    image_basic2 = cv2.imread('res.png')
    cv2.imshow('detected', image_basic2)
    cv2.waitKey()


def thirdButton():
    makeTemplatesAndMasks('domino_minta16.jpg')
    match('domino_basic_123.jpg', 'domino_minta16.jpg', 35)

    makeTemplatesAndMasks('domino_minta17.jpg')
    match('res.png', 'domino_minta17.jpg', 40)

    makeTemplatesAndMasks('domino_minta18.jpg')
    match('res.png', 'domino_minta18.jpg', 40)

    makeTemplatesAndMasks('domino_minta19.jpg')
    match('res.png', 'domino_minta19.jpg', 40)

    makeTemplatesAndMasks('domino_group2.jpg')
    match('res.png', 'domino_group2.jpg', 80)

    image_basic2 = cv2.imread('res.png')
    cv2.imshow('detected', image_basic2)
    cv2.waitKey()


def fourthButton():
    makeTemplatesAndMasks('domino_minta21.jpg')
    match('domino_basic_234.jpg', 'domino_minta21.jpg', 5)

    makeTemplatesAndMasks('domino_minta22.jpg')
    match('res.png', 'domino_minta22.jpg', 8)

    makeTemplatesAndMasks('domino_minta23.jpg')
    match('res.png', 'domino_minta23.jpg', 5)

    makeTemplatesAndMasks('domino_minta24.jpg')
    match('res.png', 'domino_minta24.jpg', 5)

    makeTemplatesAndMasks('domino_group3.jpg')
    match('res.png', 'domino_group3.jpg', 35)

    image_basic2 = cv2.imread('res.png')
    cv2.imshow('detected', image_basic2)
    cv2.waitKey()


def fifthButton():
    makeTemplatesAndMasks('domino_minta26.jpg')
    match('domino_basic_345.jpg', 'domino_minta26.jpg', 30)

    makeTemplatesAndMasks('domino_minta27.jpg')
    match('res.png', 'domino_minta27.jpg', 60)

    makeTemplatesAndMasks('domino_minta28.jpg')
    match('res.png', 'domino_minta28.jpg', 20)

    makeTemplatesAndMasks('domino_group4.jpg')
    match('res.png', 'domino_group4.jpg', 70)

    image_basic2 = cv2.imread('res.png')
    cv2.imshow('detected', image_basic2)
    cv2.waitKey()


class Window():
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        w = QtWidgets.QWidget()
        b1 = QtWidgets.QPushButton(w)
        b2 = QtWidgets.QPushButton(w)
        b3 = QtWidgets.QPushButton(w)
        b4 = QtWidgets.QPushButton(w)
        b5 = QtWidgets.QPushButton(w)
        l1 = QtWidgets.QLabel(w)
        l2 = QtWidgets.QLabel(w)
        l3 = QtWidgets.QLabel(w)
        l4 = QtWidgets.QLabel(w)
        l1.setText("Dominó detektáló algoritmus")
        l2.setText("Az algoritmus az 1. tesztre lassú, átlagosan 1 dominó detektálásához")
        l3.setText("1 percig futott(360°-os detektálás), ennek okán 5 mintát keresek")
        l4.setText("képenként, alap járaton 10 minta van előállítva, meg is találja ezeket!")
        l1.move(110, 20)
        l2.move(5, 50)
        l3.move(5, 60)
        l4.move(5, 70)
        b1.setText("Első teszt")
        b2.setText("Második teszt")
        b3.setText("Harmadik teszt")
        b4.setText("Negyedik teszt")
        b5.setText("Ötödik teszt")
        w.setWindowTitle('Domino detektalas')
        b1.move(80, 100)
        b2.move(180, 100)
        b3.move(80, 150)
        b4.move(180, 150)
        b5.move(125, 200)
        b1.clicked.connect(self.button1Clicked)
        b2.clicked.connect(self.button2Clicked)
        b3.clicked.connect(self.button3Clicked)
        b4.clicked.connect(self.button4Clicked)
        b5.clicked.connect(self.button5Clicked)
        w.setGeometry(50, 50, 340, 230)
        w.show()
        sys.exit(app.exec_())

    def button1Clicked(self):
        firstButton()

    def button2Clicked(self):
        secondButton()

    def button3Clicked(self):
        thirdButton()

    def button4Clicked(self):
        fourthButton()

    def button5Clicked(self):
        fifthButton()

def run():
    app = QtWidgets.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec())


run()

