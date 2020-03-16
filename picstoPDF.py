#! python3
# -*- coding: utf-8 -*-

"""

-------------------------------------------------

File Name： picstoPDF

Description :

Author : MingDee

date： 2019/11/9

-------------------------------------------------

Change Activity:

2019/11/9:

-------------------------------------------------

"""

import os
import string
from PIL import Image
from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfgen import canvas
import sys


#f_pdf pdf file path ,include filename
#filedir pic file path
#suffix pic file suffix examples: .jpg
def conpdf(f_pdf , filedir, suffix='.jpg'):
    (w, h) = landscape(A4)
    c = canvas.Canvas(f_pdf, pagesize = landscape(A4))
    fileList = os.listdir(filedir)
    fileList.sort(key=lambda x: int(x.split('.')[0]))

    for f in fileList:
        (xsize, ysize) = Image.open(filedir + '/' + f).size

        ratx = xsize / w
        raty = ysize / h
        ratxy = xsize / (1.0 * ysize)
        if ratx > 1:
            ratx = 0.99
        if raty > 1:
            raty = 0.99

        rat = ratx

        if ratx < raty:
            rat = raty
        widthx = w * rat
        widthy = h * rat
        widthx = widthy * ratxy
        posx = (w - widthx) / 2
        if posx < 0:
            posx = 0
        posy = (h - widthy) / 2
        if posy < 0:
            pos = 0

        c.drawImage(filedir + '/' + f, posx, posy, widthx, widthy)
        c.showPage()
    c.save()
    print("Image to pdf success!")


if __name__ == '__main__':
    path = 'D:/Comics/新建文件夹/'
    for name in os.listdir(path):
        try:
            conpdf(path + name + ".pdf", path + name)
        except:
            pass