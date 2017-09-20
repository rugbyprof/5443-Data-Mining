import os
import sys
import pprint as pp
import json

segdir = "/code/PKLot/PKLotSegmented/UFPR04"
regdir = "/code/PKLot/PKLot/UFPR04"


def generic_dir_walk(ddir):
    # traverse root directory, and list directories as dirs and files as files
    for root, dirs, files in os.walk(ddir):
        path = root.split(os.sep)
        print((len(path) - 1) * '---', os.path.basename(root))
        for file in files:
            print(len(path) * '---', file)


def create_segmented_image_list(ddir,outfile=None):
    """
        This function reads a directory structure like below and 
        returns a list of objects representing each image. 

        - Cloudy
            - 2012-09-12
                - Empty
                    - 2012-09-12_09_55_29#090.jpg
                    - 2012-09-12_09_55_29#093.jpg
                    - 2012-09-12_10_05_57#090.jpg
                - Occupied
                    - 2012-09-12_09_55_29#090.jpg
                    - 2012-09-12_09_55_29#093.jpg
                    - 2012-09-12_10_05_57#090.jpg
            - 2012-09-16
            - ...
        - Rainy
            - 2012-09-12
            - 2012-09-16
            - ...
        - Sunny
            - 2012-09-12
            - 2012-09-16 

    Returns: 
        [{
            'day': '14',
            'file_name': '2012-12-14_16_35_13#005.jpg',
            'hour': '16',
            'minute': '35',
            'month': '12',
            'path': 'Cloudy/2012-12-14/Occupied',
            'second': '13',
            'spot_id': '005',
            "occupied": 0,
            'weather': 'Cloudy',
            'year': '2012'
        },...,]

    """
    dirlen = len(ddir) + 1
    image_list = []
    for root, dirs, files in os.walk(ddir):
        path = root.split(os.sep)
        sub_path = os.path.join(path[-3],path[-2],path[-1])
        for file in files:
            f = os.path.join(root,file)[dirlen:]
            weather,day,status,image = f.split(os.sep)
            
            print(status)
            if status.lower() == 'occupied':
                status = 1
            else:
                status = 0

            image_data = {}
            image_data['path'] = sub_path
            image_data['file_name'] = image
            image_data['weather'] = weather
            image_data['day'] = day
            image_data['occupied'] = status
            timevals, spot_num = image.split('#')
            ymd = timevals[:10]
            hms = timevals[11:]
            image_data['spot_id'], ext = spot_num.split('.')
            image_data['year'], image_data['month'], image_data['day'] = ymd.split('-')
            image_data['hour'], image_data['minute'], image_data['second'] = hms.split('_')
            image_list.append(image_data)

    if outfile:
        fp = open(outfile,'w')
        fp.write(json.dumps({'spaces':image_list},indent=4, separators=(',', ': ')))
        fp.close()
    return image_list

def create_lot_image_list(ddir,outfile=None):
    dirlen = len(ddir) + 1
    image_list = []
    for root, dirs, files in os.walk(ddir):
        path = root.split(os.sep)
        
        sub_path = os.path.join(path[-2],path[-1])
        for file in files:
            f = os.path.join(root,file)[dirlen:]
            if f[-3:] == 'xml':
                continue
            weather,day,image = f.split(os.sep)
            
            image_data = {}
            image_data['path'] = sub_path
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

    if outfile:
        fp = open(outfile,'w')
        fp.write(json.dumps({'spaces':image_list},indent=4, separators=(',', ': ')))
        fp.close()
    return image_list

#segmented_images = create_segmented_image_list(segdir,'seg_image_list.json')
lot_images = create_lot_image_list(regdir,'lot_image_list.json')
#pp.pprint(lot_images)