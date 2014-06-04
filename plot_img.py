"""
File with the methods to show results
"""
import numpy as np
import logging
from PIL import Image, ImageDraw


def plotImage(tree, size, type_img):
    """Method to show the result image

    :param tree: tree obtained after partition
    :type tree: list
    :param size: size of the base image
    :type size: tuple
    :param type_img: type of the base image
    :type type_img: str"""
    logging.info("** in plotImage():")
    try:
        res = np.zeros(size, dtype=np.uint8)
        for t in tree:
            for p in t.pixel_list:
                res[p.x][p.y] = t.val
        img = Image.fromarray(res, type_img)
        img.show()
        logging.info("\t \t Success")
    except:
        logging.error("\t \t Error in function plotImage()")


def showFinalsRegions(tree, size, type_img, mode="standard"):
    """Method to show the finals regions after partition

    :param tree: tree obtained after partition
    :type tree: list
    :param size: size of the base image
    :type size: tuple
    :param type_img: type of the base image
    :type type_img: str
    :param mode: coloring regions (it can be "blue", "red", "yellow", ...)
    :type mode: str"""
    logging.info("** in showFinalsRegions():")
    if mode == "standard":
        for t in tree:
            res = np.zeros(size, dtype=np.uint8)
            for p in t.pixel_list:
                res[p.x][p.y] = t.val
            img = Image.fromarray(res, type_img)
            img.show()
    else:
        for t in tree:
            zone = []
            res = np.zeros(size, dtype=np.uint8)
            for p in t.pixel_list:
                res[p.x][p.y] = t.val
                zone = zone + [(p.y, p.x)]
            img = Image.fromarray(res, type_img)
            img_demo = img.convert('RGB')
            draw = ImageDraw.Draw(img_demo)
            for z in zone:
                try:
                    draw.point(z, mode)
                    test = "pass"
                except:
                    test = "error"
            if test == "pass":
                img_demo.show()
        if test == "error":
            logging.error("\t \t Wrong value assign to mode argument (mode = '" + mode + "')")
            print "Error: wrong value assign to mode argument"
        else:
            logging.info("\t \t Success")
