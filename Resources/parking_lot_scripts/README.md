Processing Parking Lot Images
=============================

There are 3 parking lots that [this](https://web.inf.ufpr.br/vri/databases/parking-lot-database/) paper collected data on. 
They are: `UFPR05` , `UFPR04` , and `PUCPR`. We will concentrate on `UFPR04` since it has the least amount of data. 

There are two zip files located here: [UFPR04.zip](http://cs.mwsu.edu/~griffin/p-lot/pklot_images/PKLot/UFPR04.zip) and here:[UFPR04_segmented.zip](http://cs.mwsu.edu/~griffin/p-lot/pklot_images/PKLot/UFPR04_segmented.zip)

### Directory Structure
- PKLot
    - PUCPR 
        - Cloudy
            - 2012-09-12
                - 2012-09-11_17_02_42.jpg
                - 2012-09-11_17_02_42.xml
                - 2012-09-11_17_07_30.jpg
                - 2012-09-11_17_07_30.xml
                - ...
            - 2012-09-16
            - ...
        - Rainy
            - 2012-09-12
            - 2012-09-16
            - ...
        - Sunny
            - 2012-09-12
            - 2012-09-16
            - ...
    - UFPR04
        - ...
    - UFPR05
        - ...
        
- PKLotSegmented
    - PUC
        - Cloudy
            - 2012-09-12
                - Empty
                    - 2012-09-12_09_55_29#090.jpg
                    - 2012-09-12_09_55_29#093.jpg
                    - 2012-09-12_10_05_57#090.jpg
                    - ...
                - Occupied
                    - 2012-09-12_09_55_29#090.jpg
                    - 2012-09-12_09_55_29#093.jpg
                    - 2012-09-12_10_05_57#090.jpg
                    - ...
            - 2012-09-16
            - ...
        - Rainy
            - 2012-09-12
            - 2012-09-16
            - ...
        - Sunny
            - 2012-09-12
            - 2012-09-16
    - UFPR04
        - ...
    - UFPR05
        - ...

### Traversing Directory


### Image Manipulation

##### Draw Image
```python
import numpy as np
import cv2 as cv
 
img = cv.imread('/Volumes/1TBHDD/code/repos/5443-Data-Mining/Resources/parking_lot_scripts/UFPRO4_example.jpg')

cv.imshow('Draw01',img)
cv.waitKey(0)
```

##### Draw On Image
```python
# Using previously opened image
img = cv.rectangle(img, (250,70), (330,150), (0,255,0), 4)
    
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img, "This is a rectangle", (230, 50), font, 0.8, (0, 255, 0), 2, cv.LINE_AA)
           
plt.imshow(img)
plt.show()
```

##### Image Slicing
```python
# Using previously opened image
img = cv.rectangle(img, (250,70), (330,150), (0,255,0), 4)

crop_img = img[491:599,974:1036]
# Crop from x, y, w, h -> 100, 200, 300, 400
# NOTE: its img[y: y + h, x: x + w] and *not* img[x: x + w, y: y + h]

plt.imshow(img)
plt.show()
plt.imshow(crop_img)
plt.show()
```
#### Histogram

```python
hsv = cv.cvtColor(crop_img,cv.COLOR_BGR2HSV)
hist = cv.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])
print(hist)
plt.imshow(hist,interpolation = 'nearest')
plt.show()
```

### Processing Spaces

http://deeplearning.net/tutorial/logreg.html#logreg
http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_ml/py_svm/py_svm_opencv/py_svm_opencv.html
http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_histograms/py_2d_histogram/py_2d_histogram.html#twod-histogram