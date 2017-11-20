Scraping Data
======

For me to grade this, I will just need to see your repository page to make sure everything is present and instructions were followed.

| :hash:       | Item                                                                                                 | Possible | Earned |
|--------------|------------------------------------------------------------------------------------------------------|----------|--------|
| :one:        | Path and naming requirements followed.                                                               | 15       |        |
| :two:        | Code is commented                                                                                    | 10       |        |
| :three:      | A README.md is included in the assignment with a brief description and group members (if necessary.) | 10       |        |
| :four:       | A csv or json file exists and contains scraped data.                                                 | 20       |        |
| :five:       | There are a minimum of 100 rows of data in the json/csv file.                                        | 20       |        |
| :six:        | The code actually scraped html and not just txt or tabular data on a server.                         | 25       |        |
|              | ***Total:***                                                                                         | 100      |        |

- &#128193; assignments
  - &#x21b3; &#128193;scrape_data
      - &#x21b3; &#128193; run.py
      - &#x21b3; &#128193; data.json or .csv      


Simple Regression
=================

use given csv to create a pyplot
deliverables = code + plot 

Part 1: File Processing

parking lot 1
=============

📁 assignments

📁 process_single_lot
📁 spaces
📁 histograms
↳ process_lot.py
Look at above folder structure

Write a script (process_lot.py) to open a single parking lot image

Open the corresponding xml file

Convert xml to json

Process json to extract image spaes from parking lot image.

save each "sliced" space image to a folder called "spaces"
save each "histogram" to a folder called "histograms" (e.g. np.savetxt('23.csv', hist, delimiter=',')
Your "sliced" spaces will contain extra pixels around the actual space. This is ok, we will fix this error next time.

Your histograms will also be flawed, becuase they will be run on the poorly sliced spaces. We will re-use your code to run histograms on the improved spaces next time.


cats n dogs
===========

no real deliverable only executable code

Create a folder called catsndogs in your assignments folder.

catsndogs should have the following basic folder structure:

📁 assignments

📁 catsndogs
📁 testing_data
📁 cats # don't upload the images
📁 dogs # don't upload the images
📁 training_data
📁 cats # don't upload the images
📁 dogs # don't upload the images
↳ dataset.py
↳ predict.py
↳ train.py
↳ dogs-cats-model.data-00000-of-00001
↳ dogs-cats-model.index
↳ dogs-cats-model.meta

belgian street sign
===================

running code, sign classification 

Based on the sign data available here

And this iPython Notebook

Deliver the following working version of the tutorial:

📁 assignments

📁 belgian_sign_classification
📁 TrafficSigns (empty - don't upload images)
↳ predict_signs.py

single space cnn
================

- replace cats n dogs with single space data provided by me
- replace testing and training data with single space data
- check slack for data link 


wiki contributions
==================

- add keywords dealing with specific papers
- add additional common terms to other parts of wiki
- edit other groups pages and terms to add addtional clarification.
