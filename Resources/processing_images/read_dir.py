import os
import sys
import pprint as pp

segdir = "/code/PKLot/PKLotSegmented/UFPR04"
regdir = "/code/PKLot/PKLot/UFPR04"


def generic_dir_walk(ddir):
    # traverse root directory, and list directories as dirs and files as files
    for root, dirs, files in os.walk(ddir):
        path = root.split(os.sep)
        print((len(path) - 1) * '---', os.path.basename(root))
        for file in files:
            print(len(path) * '---', file)


def create_segmented_image_list(ddir):
    dirlen = len(ddir) + 1
    image_list = []
    for root, dirs, files in os.walk(ddir):
        path = root.split(os.sep)
        for file in files:
            f = os.path.join(root,file)[dirlen:]
            weather,day,status,image = f.split(os.sep)
            
            image_data = {}
            image_data['file_name'] = image
            image_data['weather'] = weather
            image_data['day'] = day
            image_data['status'] = status
            timevals, spot_num = image.split('#')
            ymd = timevals[:10]
            hms = timevals[11:]
            image_data['year'], image_data['month'], image_data['day'] = ymd.split('-')
            image_data['hour'], image_data['minute'], image_data['second'] = hms.split('_')
            image_list.append(image_data)

    return image_list

def create_lot_image_list(ddir):
    dirlen = len(ddir) + 1
    image_list = []
    for root, dirs, files in os.walk(ddir):
        path = root.split(os.sep)
        for file in files:
            f = os.path.join(root,file)[dirlen:]
            if f[-3:] == 'xml':
                continue
            weather,day,image = f.split(os.sep)
            
            image_data = {}

            image_data['weather'] = weather
            image_data['day'] = day
            timevals,ext = image.split('.')

            image_data['image_name'] = timevals+'.jpg'
            image_data['xml_name'] = timevals+'.xml'

            ymd = timevals[:10]
            hms = timevals[11:]
            image_data['year'], image_data['month'], image_data['day'] = ymd.split('-')
            image_data['hour'], image_data['minute'], image_data['second'] = hms.split('_')
            image_list.append(image_data)

    return image_list

#segmented_images = create_segmented_image_list(segdir)
lot_images = create_lot_image_list(regdir)
pp.pprint(lot_images)