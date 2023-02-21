# -*- coding: utf-8 -*-
'''
*******************************************************************************
函数名称: Generatelabels
描    述: yolov5训练，数据集的准备，生成路径文件
作    者：lxh
编写时间：2022.11.29
数据集总体结构。
 basepath
 ├── images
     └── img_num.jpg ....
 ├── ImageSets
     └── train.txt #图片名称的txt文件
     ....
 ├── dataSet_path
     └── train.txt #存放绝对路径的txt文件
     ....
 ├──labels
     └── img_num.txt #存放标注信息的txt文件
     ....
 └── Annotations
     └── img_num.xml #存放标注信息的xml文件
*******************************************************************************/
'''


import xml.etree.ElementTree as ET
import os
from os import getcwd

sets = ['train', 'val', 'video']
classes = ["Opened","Closed","Running"]  # 改成自己的类别
abs_path = os.getcwd()
print(abs_path)
basepath = 'C:/Users/LXH/PycharmProjects/pythonProject2/yolov5-master/datasets/daozha-yolo-multi/'

def convert(size, box):
    dw = 1. / (size[0])
    dh = 1. / (size[1])
    x = (box[0] + box[1]) / 2.0 - 1
    y = (box[2] + box[3]) / 2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return x, y, w, h


def convert_annotation(image_id):
    in_file = open(basepath + 'Annotations/%s.xml' % (image_id), encoding='UTF-8')
    out_file = open(basepath +'labels/%s.txt' % (image_id), 'w')
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)
    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        # difficult = obj.find('Difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult) == 1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text),
             float(xmlbox.find('ymax').text))
        b1, b2, b3, b4 = b
        # 标注越界修正
        if b2 > w:
            b2 = w
        if b4 > h:
            b4 = h
        b = (b1, b2, b3, b4)
        bb = convert((w, h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')


wd = getcwd()
for image_set in sets:
    if not os.path.exists(basepath +'labels/'):
        os.makedirs(basepath +'labels/')
    image_ids = open(basepath +'ImageSets/%s.txt' % (image_set)).read().strip().split()

    if not os.path.exists(basepath +'dataSet_path/'):
        os.makedirs(basepath +'dataSet_path/')

    list_file = open(basepath +'dataSet_path/%s.txt' % (image_set), 'w')
    # 这行路径不需更改，这是相对路径
    for image_id in image_ids:
        list_file.write(basepath +'images/%s.jpg\n' % (image_id))
        convert_annotation(image_id)
    list_file.close()

