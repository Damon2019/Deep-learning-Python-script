# -*- coding: utf-8 -*-
import os
import xml.etree.ElementTree as ET


def compute_iou(rec1, rec2):
    """
    computing IoU
    :param rec1: (y0, x0, y1, x1), which reflects
            (top, left, bottom, right)
    :param rec2: (y0, x0, y1, x1)
    :return: scala value of IoU
    """
    # computing area of each rectangles
    S_rec1 = (rec1[2] - rec1[0]) * (rec1[3] - rec1[1])
    S_rec2 = (rec2[2] - rec2[0]) * (rec2[3] - rec2[1])

    # computing the sum_area
    sum_area = S_rec1 + S_rec2

    # find the each edge of intersect rectangle
    left_line = max(rec1[1], rec2[1])
    right_line = min(rec1[3], rec2[3])
    top_line = max(rec1[0], rec2[0])
    bottom_line = min(rec1[2], rec2[2])

    # judge if there is an intersect
    if left_line >= right_line or top_line >= bottom_line:
        return 0
    else:
        intersect = (right_line - left_line) * (bottom_line - top_line)
        #return (intersect / (sum_area - intersect)) * 1.0
        return (intersect / S_rec2) * 1.0


def changelabelname(inputpath):
    listdir = os.listdir(inputpath)
    for file in listdir:
        if file.endswith('xml'):
            file = os.path.join(inputpath,file)
            tree = ET.parse(file)
            root = tree.getroot()
            for obj in root.findall('object'):
                for car in obj.findall('name'):
                    if (car.text == 'car' or car.text == 'watcher'):
                        #get xmin ymin xmax ymax
                        for bndbox in obj.findall('bndbox'):
                            #print('bndbox' ,bndbox[0].text, bndbox[1].text, bndbox[2].text, bndbox[3].text)
                            car_name = car.text
                            red_flag = 0
                            blue_flag = 0
                            unknow_flag = 0
                            rec1 = (int(bndbox[1].text), int(bndbox[0].text), int(bndbox[3].text), int(bndbox[2].text))

                            for obje in root.findall('object'):
                                for armor in obje.findall('name'):
                                    if (armor.text == 'armor_red' or armor.text == 'armor_blue' or armor.text == 'armor_grey'):
                                        #print('111111111111111111111111')
                                        for bndbox_armor in obje.findall('bndbox'):
                                            rec2 = (int(bndbox_armor[1].text), int(bndbox_armor[0].text), int(bndbox_armor[3].text), int(bndbox_armor[2].text))
                                            #print('rec2------',rec2)
                                            iou = compute_iou(rec1,rec2)
                                            #print(type(iou))
                                            if iou>0 and iou<1:
                                                print('iou------',iou)
                                            if iou > 0.8:
                                                if armor.text == 'armor_red':
                                                    red_flag = 1
                                                if armor.text == 'armor_blue':
                                                    blue_flag = 1
                                                if armor.text == 'armor_grey':
                                                    unknow_flag = 1

                            if unknow_flag == 1:
                                car.text = car_name + '_unknow'
                            elif red_flag == 1 and blue_flag == 1:
                                car.text = car_name + '_unknow'
                            elif red_flag == 1:
                                car.text = car_name + '_red'
                            elif blue_flag == 1:
                                car.text = car_name + '_blue'
                            else:
                                car.text = car_name + '_unknow'


                            tree.write(file,encoding='utf-8')

                    ''' 
                    if (sku.text == 'red'):
                        sku.text = 'armor_red'
                        tree.write(file,encoding='utf-8')
                    else:
                        pass
                    '''
        else:
            pass

if __name__ == '__main__':
    inputpath = './xml/'
    changelabelname(inputpath)

