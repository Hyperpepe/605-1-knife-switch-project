'''
*******************************************************************************
函数名称: Devideimg
描    述: yolov5训练，数据集的准备，从voc数据集xml文件，分为预测训练验证
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

import os
import random
trainval_percent = 0.1
train_percent = 0.9

basepath = 'C:/Users/LXH/PycharmProjects/pythonProject2/yolov5-master/datasets/daozha-yolo-multi/'

txtsavepath = basepath + 'ImageSets'
xmlfilepath = basepath + 'Annotations'  #xml文件存放地址，绝对路径

if not os.path.exists('ImageSets/'):
    os.makedirs('ImageSets/')

total_xml = os.listdir(xmlfilepath)
num = len(total_xml)
list = range(num)
tv = int(num * trainval_percent)
tr = int(tv * train_percent)
trainval = random.sample(list, tv)
train = random.sample(trainval, tr)
ftrainval = open('ImageSets/trainval.txt', 'w')
ftest = open('ImageSets/test.txt', 'w')
ftrain = open('ImageSets/train.txt', 'w')
fval = open('ImageSets/val.txt', 'w')


for i in list:
    name = total_xml[i][:-4] + '\n'
    if i in trainval:
        ftrainval.write(name)
        if i in train:
            ftest.write(name)
        else:
            fval.write(name)
    else:
        ftrain.write(name)
ftrainval.close()
ftrain.close()
fval.close()
ftest.close()