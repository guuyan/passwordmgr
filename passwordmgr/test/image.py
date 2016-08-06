import os
import math
from PIL import Image
from GraphLine import GraphLineProcess
MAX_X = 105
MAX_Y = 35


def process_handler(array, max_x, max_y, f):
    for index_x in range(max_x):
        for index_y in range(max_y):
            array = f(array, index_x, index_y, max_x, max_y)


def thread_checker(array, x, y, max_x, max_y):
    if array[x, y][0] < 50 or array[x,y][1] < 50  or array[x,y][2] < 50 :
        array[x, y] = (0, 0, 0, 0)
        return array

    if array[x, y][0] > 200 or array[x, y][1] > 200 or array[x, y][2] > 200:
        array[x, y] = (255, 255, 255, 255)
    return array


def to_gray(array, x, y, max_x, max_y):
    gray = array[x, y][0] * 0.299 + array[x, y][1] * 0.587 + array[x, y][2] * 0.114
    array[x, y] = (0, 0, 0, 0) if gray < 121 else (255,255,255, 255)
    return array


def is_a_point_4_gray(metir, posX, poxY, maxX, maxY):
    if metir[posX, poxY] > 200:
        metir[posX, poxY] = 255
        return metir
    frendiy = 0
    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            index_x, index_y = posX + x, poxY + y
            if index_x < 0 or index_x >= maxX:
                metir[posX, poxY] = 255
                return metir
            if index_y < 0:
                metir[posX, poxY] = 255
                return metir
            if index_y >= maxY:
                return metir
            if abs(metir[posX, poxY] - metir[index_x, index_y]) > 100:
                frendiy += 1
    if frendiy > 6:
        metir[posX, poxY] = 255
    return metir


def clear_noise(metrix, x, y, mx, my):
    if x == 0 or x == 104 or y == 0 or y == 34:
        return metrix

    p = list()
    for cx in [-1, 0, 1]:
        for cy in [-1, 0, 1]:
            index_x, index_y = x + cx, y + cy
            p.append(metrix[index_x, index_y])

    p.sort()
    metrix[x,y] = p[4]
    return metrix


base_path = r"C:\Users\guyan\Pictures\base"
mid_path = r"C:\Users\guyan\Pictures\mid"
out_path = r"C:\Users\guyan\Pictures\out"

toImage = Image.new('L', (30*105, 35))
outx = outy = 0
for onefile in os.listdir(base_path):
    print onefile
    im = Image.open(os.path.join(base_path, onefile))
    im_data = im.load()
    process_handler(im_data, im.size[0], im.size[1], thread_checker)
    process_handler(im_data, im.size[0], im.size[1], to_gray)
    im = im.convert("L")
    gray_data = im.load()
    process_handler(gray_data, im.size[0], im.size[1], clear_noise)
    # for x in range(MAX_X):
    #     gray = gray_data[x, 0]
    #     if gray_data[x, 0] != 255:
    #         node_list = GraphLineProcess(gray_data, (x,0), end_condition="X")
    #         points = node_list.get_point_list()
    #         for point in points:
    #             gray_data[point[0], point[1]] = 0
    #         print points
    # im.show()
    # break
    process_handler(gray_data, im.size[0], im.size[1], is_a_point_4_gray)
    im.save(os.path.join(mid_path, onefile))
    #im.save(os.path.join(out_path, onefile+".tif"))
    toImage.paste(im, (outx, outy))
    outx += im.size[0]
    if outx > 30*105:
        break

toImage.save(os.path.join(out_path, "out.tif"))