from xmljson import parker, Parker
from xmljson import yahoo
from xml.etree.ElementTree import fromstring
from json import dumps,loads
import pprint as pp

fp = open('/Users/griffin/Desktop/Trunk/2012-09-12_10_11_12.xml','r')

xmldata = fp.read()

jsond = dumps(yahoo.data(fromstring(xmldata)))

pp.pprint(jsond)

print(type(jsond))

jsond = loads(jsond)

spaces = jsond['parking']['space']

for space in spaces:
    print(space['contour'])
    for point in space['contour']['point']:
        print(point)



