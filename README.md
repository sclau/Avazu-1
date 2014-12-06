## Introduction

For our STAT 157 semester project at Berkeley, we wanted to compete in a [Kaggle competiton](https://www.kaggle.com/c/avazu-ctr-prediction). Using 11 days worth of Avazu data, we built a Naive Bayes model to predict whether a mobile ad will be clicked or not. 

## Installation

The training and test sets from the Avazu competition are in the following directories:
```
s3://stat157-uq85def/shared/avazudata/newdata/train
s3://stat157-uq85def/shared/avazudata/newdata/test
```
The data produced from running all the code is in:
```
s3://stat157-uq85def/home/sclau/data/
```
In AWS create the following folders
```
s3://stat157-uq85def/home/<your_user_id>/project
s3://stat157-uq85def/home/<your_user_id>/project/output
s3://stat157-uq85def/home/<your_user_id>/project/code
s3://stat157-uq85def/home/<your_user_id>/project/logs
s3://stat157-uq85def/home/<your_user_id>/project/data
```
Download the repository
```
$git clone https://github.com/ucb-stat-157/Avazu.git
```
To calculate the Model, change directory to where the model is
```
$cd ./bayes_model/
```
Read the commands_* files to find out which commands do run in the terminal. Do them sequentially, commands_1.sh, commands_2.sh, commands_3.sh, commands_3_full.sh. You want to run each line of the files line by line in the terminal.

#### commands_1.sh and commands_3.sh example code
```
$chmod +x counter_map.py
$chmod +x counter_red.py
$s3cmd put counter_map.py s3://stat157-uq85def/home/sclau/project/code/
$s3cmd put counter_red.py s3://stat157-uq85def/home/sclau/project/code/

$cd data/base_1/results/
$s3cmd get s3://stat157-uq85def/home/sclau/project/output/base_1_results/part*
$cat $(ls -t) > binstance_base_1.txt
```

Before uploading things to AWS S3, make you sure install s3cmd and configure it. Instructions on how to set up s3cmd and use AWS EMR can be found [here](https://github.com/ucb-stat-157/fall-2014-public/tree/master/lec-19-lab).  

In the command_* files, you'll find instructions on how to run each file and MapReduce job in AWS EMR and what to input for the streaming program entries. 

base_1, base_2, and base_3 are the three variations of our naive bayes model, they are tested on the validation set. base_3_full is the model trained on the full training set

The 4 features in the base model are: app_category, site_categoy, banner_position and device_model

## Results

After calculating the model and testing it on the validation sets, here are the results:

| Model  | Features |     Added Features    | Log Loss |
| ------ |:--------:|:---------------------:|:--------:|
| base_1 |     4    |          None         |   0.436  |
| base_2 |     5    |         Ad Size       |   0.432  |
| base_3 |     6    |   Ad Size, Device IP  |   0.430  |

As of 12/5/2014 our submission 'STAT 157' comes out with a Log Loss of 0.493 for it is ranked 518/601. The first place Log Loss score is 0.389

## Contributors

Ian Chin: Responsible for feature engineering and bayes_prob_mapper*

Shangyu Zhao: Responsible for data characteristics

Samuel Lau: Responsible for Naive Bayes Model
