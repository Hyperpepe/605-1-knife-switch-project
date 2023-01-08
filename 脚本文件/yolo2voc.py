import cv2
import os

xml_head = '''<annotation>
    <folder>VOC2007</folder>
    <filename>{}</filename>
    <source>
        <database>The VOC2007 Database</database>
        <annotation>PASCAL VOC2007</annotation>
        <image>flickr</image>
        <flickrid>325991873</flickrid>
    </source>
    <owner>
        <flickrid>null</flickrid>
        <name>null</name>
    </owner>    
    <size>
        <width>{}</width>
        <height>{}</height>
        <depth>{}</depth>
    </size>
    <segmented>0</segmented>
    '''
xml_obj = '''
    <object>        
        <name>{}</name>
        <pose>Rear</pose>
        <truncated>0</truncated>
        <difficult>0</difficult>
        <bndbox>
            <xmin>{}</xmin>
            <ymin>{}</ymin>
            <xmax>{}</xmax>
            <ymax>{}</ymax>
        </bndbox>
    </object>
    '''
xml_end = '''
</annotation>'''

labels = ['hat','person']  # label for datasets

cnt = 0
txt_path = os.path.join('/home/lxh/work/datasets/WHKongTou4/1/')  # yolo存放txt的文件目录
image_path = os.path.join('/home/lxh/work/datasets/WHKongTou4/1')  # 存放图片的文件目录
path = os.path.join('/home/lxh/work/datasets/WHKongTou4/1')  # 存放生成xml的文件目录

for (root, dirname, files) in os.walk(image_path):  # 遍历图片文件夹
    for ft in files:
        ftxt = ft.replace('jpg', 'txt')  # ft是图片名字+扩展名，将jpg和txt替换
        fxxx = ft.replace('jpg', 'jpg' )
        fxml = ft.replace('jpg', 'xml' )
        xml_path = path + fxml
        obj = ''

        img = cv2.imread(root + ft)
        img_h, img_w = img.shape[0], img.shape[1]
        head = xml_head.format(str(fxxx), str(img_w), str(img_h), 3)

        with open(txt_path + ftxt, 'r') as f:  # 读取对应txt文件内容
            for line in f.readlines():
                yolo_datas = line.strip().split(' ')
                label = int(float(yolo_datas[0].strip()))
                center_x = round(float(str(yolo_datas[1]).strip()) * img_w)
                center_y = round(float(str(yolo_datas[2]).strip()) * img_h)
                bbox_width = round(float(str(yolo_datas[3]).strip()) * img_w)
                bbox_height = round(float(str(yolo_datas[4]).strip()) * img_h)

                xmin = str(int(center_x - bbox_width / 2))
                ymin = str(int(center_y - bbox_height / 2))
                xmax = str(int(center_x + bbox_width / 2))
                ymax = str(int(center_y + bbox_height / 2))

                obj += xml_obj.format(labels[label], xmin, ymin, xmax, ymax)
        with open(xml_path, 'w') as f_xml:
            f_xml.write(head + obj + xml_end)
        cnt += 1
        print(cnt)
