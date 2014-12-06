#!/bin/bash 
# type into to the terminal: $bash commands_1.sh
# replace 'sclau' with your aws id 
#
chmod +x counter_map.py
chmod +x counter_red.py
#
# set up a project folder in s3://stat157-uq85def/home/<your_aws_id>
# with the following subfolders: 'code', 'output', 'logs'
#
# upload files to AWS S3 
s3cmd put counter_map.py s3://stat157-uq85def/home/sclau/project/code/
s3cmd put counter_red.py s3://stat157-uq85def/home/sclau/project/code/
#
# run MapReduce job
# Log folder S3 location: s3://stat157-uq85def/home/sclau/project/logs/
# set Mapper: s3://stat157-uq85def/home/sclau/project/code/counter_map.py 
# set Reducer: s3://stat157-uq85def/home/sclau/project/code/counter_red.py
# set Input S3 location: s3://stat157-uq85def/shared/avazudata/newdata/train
# set Ouput S3 location: s3://stat157-uq85def/home/sclau/project/output/base_counts

mkdir data/
cd data
mkdir base_1
mkdir base_2
mkdir base_3
mkdir base_3_full
mkdir counts
mkdir counts_full
cd base_1/
mkdir results
cd ../base_2/
mkdir results
cd ../base_3/
mkdir results
cd ../base_3_full/
mkdir results
cd ../../../