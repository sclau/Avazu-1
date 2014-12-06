#!/bin/bash 
# after running the MapReduce successfully
# type this into the terminal: $bash commands_3.sh
# replace 'sclau' with your aws id

cd data/base_1/results/
rm *
s3cmd get s3://stat157-uq85def/home/sclau/project/output/base_1_results/part*
cat $(ls -t) > binstance_base_1.txt
sort binstance_base_1.txt -k1,1 -o binstance_base_1.txt
cd ../../../
# this is the log loss score for base_1 model
python bayes_logLoss.py < data/base_1/results/binstance_base_1.txt > data/base_1/logloss.txt

cd data/base_2/results/
rm *
s3cmd get s3://stat157-uq85def/home/sclau/project/output/base_2_results/part*
cat $(ls -t) > binstance_base_2.txt
sort binstance_base_2.txt -k1,1 -o binstance_base_2.txt
cd ../../../
# this is the log loss score for the base_2 model
python bayes_logLoss.py < data/base_2/results/binstance_base_2.txt > data/base_2/logloss.txt

cd data/base_3/results/
rm *
s3cmd get s3://stat157-uq85def/home/sclau/project/output/base_3_results/part*
cat $(ls -t) > binstance_base_3.txt
sort binstance_base_3.txt -k1,1 -o binstance_base_3.txt
cd ../../../
# this is the log loss score for the base_3 model
python bayes_logLoss.py < data/base_3/results/binstance_base_3.txt > data/base_3/logloss.txt
