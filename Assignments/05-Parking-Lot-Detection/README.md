Occupied Parking Space Project
==============================
Due: TBD

### Overview

This project will use a logistical regression technique and your choice of libary to implement a machine learning approach to identifying whether or not a parking space is occupied. The dataset can be found here: [PKLot.tar.gz](http://cs.mwsu.edu/~griffin/p-lot/pklot_images/PKLot.tar.gz). 

>This database contains 12,417 images (1280X720) captured from two different parking lots (parking1 and parking2) in sunny, cloudy and rainy days. The first parking lot has two different capture angles (parking1a and parking 1b).
>
>The images are organised into three directories (parking1a, parking1b and parking2). Each directory contains three subdirectories for different weather conditions (cloudy, rainy and sunny). Inside of each subdirectory the images are organised by acquisition date.
>
>Each image of the database has a XML file associated including the coordinates of all the parking spaces and its label (occupied/vacant). By using the XML files to segment the parking space, you will be able to get around 695,900 images of  parking spaces.

<sup>Source: https://web.inf.ufpr.br/vri/databases/parking-lot-database/ </sup>

#### Complete Parking Lot Images

| Parking1a| Parking1b |Parking 2
|---------|------------|--------------|
|  ![](http://cs.mwsu.edu/~griffin/p-lot/pklot_images/PKLot/PKLot/PUCPR/Sunny/2012-09-13/2012-09-13_08_21_07.jpg)     |  ![](http://cs.mwsu.edu/~griffin/p-lot/pklot_images/PKLot/PKLot/UFPR04/Sunny/2012-12-16/2012-12-16_12_05_07.jpg)     | ![](http://cs.mwsu.edu/~griffin/p-lot/pklot_images/PKLot/PKLot/UFPR05/Sunny/2013-02-28/2013-02-28_18_05_44.jpg) 
| [xml file](http://cs.mwsu.edu/~griffin/p-lot/pklot_images/PKLot/PKLot/UFPR04/Sunny/2012-12-16/2012-12-16_12_05_07.xml) | [xml file](http://cs.mwsu.edu/~griffin/p-lot/pklot_images/PKLot/PKLot/PUCPR/Sunny/2012-09-13/2012-09-13_10_20_17.xml) | [xml file](http://cs.mwsu.edu/~griffin/p-lot/pklot_images/PKLot/PKLot/UFPR05/Sunny/2013-02-28/2013-02-28_18_05_44.xml) |
|         |           |           |  

#### Segmented Parking Lot Images
| Empty | Occupied |
|---------|------------|
| ![](http://cs.mwsu.edu/~griffin/p-lot/pklot_images/PKLot/PKLotSegmented/UFPR05/Sunny/2013-02-28/Empty/2013-02-28_18_00_44%23011.jpg) | ![](http://cs.mwsu.edu/~griffin/p-lot/pklot_images/PKLot/PKLotSegmented/UFPR05/Sunny/2013-02-28/Occupied/2013-02-28_17_55_44%23011.jpg) | 
|![](http://cs.mwsu.edu/~griffin/p-lot/pklot_images/PKLot/PKLotSegmented/UFPR05/Sunny/2013-02-28/Empty/2013-02-28_18_30_45%23024.jpg) |  ![](http://cs.mwsu.edu/~griffin/p-lot/pklot_images/PKLot/PKLotSegmented/UFPR05/Sunny/2013-02-28/Occupied/2013-02-28_17_55_44%23024.jpg) |

### Part 1: File Processing 

#### Folder Structure

- &#128193; assignments 
    - &#128193; `process_single_lot`
        - &#128193; `spaces`
        - &#128193; `histograms`
    - &#x21b3; `process_lot.py`


- Look at above folder structure
- Write a script (process_lot.py) to open a single parking lot image
- Open the corresponding xml file
- Convert xml to json
- Process json to extract image spaes from parking lot image.
    - save each "sliced" space image to a folder called "spaces"
    - save each "histogram" to a folder called "histograms" (e.g. `np.savetxt('23.csv', hist, delimiter=',')`
- Your "sliced" spaces will contain extra pixels around the actual space. This is ok, we will fix this error next time.
- Your histograms will also be flawed, becuase they will be run on the poorly sliced spaces. We will re-use your code to run histograms on the improved spaces next time.

### Part 2: Image Analysis

- TBD

#### Part 3: Machine Learning Model

- TBD



### Groups

| Group # | Names |
|---------|-------|
| 1.      | Shenglin Sun, Olayinka Soyinka |
| 2.      | Muni Bhupathi Reddy Dandu, Karan Madishetty, Sai Avinash Reddy Biradhavolu      |
| 3.      |  Lavanya Mengaraboina,Krishna saka,Keerthi Reddy Gangidi     |
| 4.      |   showrya chakra kollu,thejaswini reddy vootkuri, karthik yallapragada    |
| 5.      |  Prakriti, Jiaxing Liu, Steven     |
| 6.      |  Nikhil Vangeti, Ajay Dinakar Kandavalli     |
| 7.      |       |
| 8.      |       |
| 9.      |       |
