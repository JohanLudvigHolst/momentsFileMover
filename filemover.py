#!/usr/bin/env python3

# Moves Moments/Classifieds exports into folders based on publication days
# Usage: run from parent folder, and name subfolder . Orignal files are deleted

import xml.etree.ElementTree as ET
from datetime import datetime
from shutil import copy2
import logging

import os

logging.basicConfig(filename='moves.log',level=logging.DEBUG)
rootdir = ("Oyeblikk", "Torg")
sort_dir = 'Dates'
extensions = ('.xml')

def parseXML(filename, product):
    tree = ET.parse(filename)
    root = tree.getroot()
    dates = []

    for rundates in root.iter('rundates'):
        for date in rundates.iter('date'):
            dates.append(date.text)

    # Convert to datetime
    name, ext = os.path.splitext(filename)
    pdfFile = (name + ".pdf")

    for item in dates:
        temp = datetime.strptime(str(item), '%m%d%Y')

        try:
            moveFile(filename, temp.date(), product)
        except Exception as e:
            print("Error moving xml file.\n")
            logging.error("Error moving xml file: %s", filename)
        try:
            moveFile(pdfFile, temp.date(), product)
        except Exception as e:
            print("Error moving pdf file.\n")
            logging.error("Error moving pdf file: %s", filename)

    # Delete original file after copy
    try:
        os.remove(filename)
        logging.info("Deleted: %s", filename)
    except Exception as e:
        logging.error("Could not delete: %s \n %s", filename, e)
    try:
        os.remove(pdfFile)
        logging.info("Deleted: %s", pdfFile)
    except Exception as e:
        logging.error("Could not delete: %s \n %s", pdfFile, e)


def moveFile(filename, date, product):
    print(filename)
    path = product + "_" + str(date)
    if not os.path.exists(path):
        try:
            os.mkdir(path)
        except Exception as e:
            logging.error("Could not create path: %s", path)
    copy2(filename, path)


for i in range(len(rootdir)):
    for subdir, dirs, files in os.walk(rootdir[i]):
        for file in files:
            ext = os.path.splitext(file)[-1].lower()
            if extensions in ext:
                fname = (os.path.join(subdir, file))
                parseXML(fname, rootdir[i])
