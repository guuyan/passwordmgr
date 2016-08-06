import logging
logging.critical('critical message')
import math


def isSame(startX, startY, posX, poxY, metir):
    return math.sqrt(math.pow(metir[startX, startY][0] - metir[posX, poxY][0], 2)
                     + math.pow(metir[startX, startY][1] - metir[posX, poxY][1], 2)
                     + math.pow(metir[startX, startY][2] - metir[posX, poxY][2], 2)) > 30

def isGraph(point):
    return point[0] + point[1] + point[2] == 0 or point[0] + point[1] + point[2] == 255 * 3

def isApoint(metir, posX, poxY, maxX, maxY):
    if isGraph(metir[posX, poxY]) is True:
        return metir

    frendiy = 0
    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            index_x, index_y = posX + x, poxY + y
            if index_x < 0 or index_x >= maxX:
                metir[posX, poxY] = (255, 255, 255, 255)
                return metir
            if index_y < 0 or index_y >= maxY:
                metir[posX, poxY] = (255, 255, 255, 255)
                return metir
            if not isSame(index_x, index_y, posX, poxY, metir):
                frendiy += 1
    if frendiy > 6:
        metir[posX, poxY] = (255, 255, 255, 255)
    return metir