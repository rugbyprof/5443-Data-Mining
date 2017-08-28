import random
import json
import pprint as pp

# print("hello world")

# mylist = []

# mylist.append(3)

# mylist.append("hello")

# mylist.append([4,5,6,7])

# print(mylist)

# for item in mylist:
#     if type(item) is list:
#         for i in item:
#             print(i)

# rnums = []

# while len(rnums) < 100:
#     r = random.randint(0,500)
#     if not r in rnums:
#         rnums.append(r)

# print(rnums)


# myset = (34,56,78,98)
# print(myset)
# print(myset[1])

# mynewset = list(myset)

# print(mynewset)

class colors(object):
    def __init__(self,filename):

        f = open(filename,'r')
        data = f.read()
        self.json_data = json.loads(data)
    
    def get_color_by_rgb(self,rgb):
        for color in self.json_data:
            r,g,b = color['rgb']
            if r == rgb[0] and g == rgb[1] and b == rgb[2]:
                return color 
        return None 
    
    def get_color_by_hex(self,hex):
        for color in self.json_data:
            if color['html'] == hex:
                return color 
        return None

    def get_color_by_name(self,name):
        pass

    def get_color(self,key,value):
        pass


mydict = {}

mydict['name'] = 'molly'
mydict['age'] = 56
mydict['school'] = 'msu'
mydict['grades'] = [88,99,88,99,88,99]


print(mydict)

def convert_colors(file_name):
    new_dict = {}
    f = open(file_name,'r')
    data = f.read()
    json_data = json.loads(data)

    for color in json_data:
        key = color['name']
        del color['name']
        new_dict[key] = color
    return new_dict

def find_color(in_color):
    f = open('colors.json','r')
    data = f.read()
    json_data = json.loads(data)

    for color in json_data:
        if color['name'] == in_color:
            return color


pp.pprint(convert_colors('colors.json'))

c = colors('colors.json')
print(c.get_color_by_hex('#f4a460'))
print(c.get_color_by_rgb([255,0,0]))
#print(find_color('palegoldenrod'))


