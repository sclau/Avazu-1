## Introduction

For our STAT 157 semester project at Berkeley, we wanted to compete in a [Kaggle competiton](https://www.kaggle.com/c/avazu-ctr-prediction). Using 11 days worth of Avazu data, we built a Naive Bayes model to predict whether a mobile ad will be clicked or not. 

## Installation

The training and test sets from the Avazu competition are in the following directories:

s3://stat157-uq85def/shared/avazudata/newdata/train
s3://stat157-uq85def/shared/avazudata/newdata/test

In AWS create the following folders
```
s3://stat157-uq85def/home/<your_user_id>/project
s3://stat157-uq85def/home/<your_user_id>/project/output
s3://stat157-uq85def/home/<your_user_id>/project/code
s3://stat157-uq85def/home/<your_user_id>/project/logs
```
Download the repository
```
$git clone https://github.com/ucb-stat-157/Avazu.git
```
To calculate the Model, change directory to ./bayes_model

Read the commands_* files to find out which commands do run in the terminal

Before uploading things to AWS S3, make you sure install s3cmd and configure it
```
$s3cmd sudo apt-get s3cmd
$s3cmd --configure
```
In the command_* files, you'll find instructions on how to run each file and MapReduce job in AWS 

base_1, base_2, and base_3 are the three variations of our naive bayes model, they are tested on the validation set. base_3_full is the model trained on the full training set

## Results

After calculating the model and testing it on the validation sets, here are the results:

| Model  | Features |     Added Features    | Log Loss |
| ------ |:--------:|:---------------------:|---------:|
| base_1 |     4    |          None         |   0.436  |
| base_2 |     5    |         Ad Size       |   0.432  |
| base_3 |     6    |   Ad Size, Device IP  |   0.430  |

As of 12/5/2014 our submission, 'STAT 157' comes out with a Log Loss of 0.493 and is ranked 518/601. The first place Log Loss score is 0.389

## Contributors

Ian Chin, UC Berkeley 2015
Shangyu Zhao, UC Berkeley 2015
Samuel Lau, UC Berkeley 2015 
