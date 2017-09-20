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