#!/bin/bash 
# after running the MapReduce successfully
# type this into the terminal: $bash commands_2.sh
# replace 'sclau' with your aws id
#
cd data/counts/
rm *
s3cmd get s3://stat157-uq85def/home/sclau/project/output/base_counts/part*
cat $(ls -t) > avazu_train.txt
cd ../../
#
#***model_name: base_1 ***
python bayes_prob_base_1.py > data/base_1/bprob_avazu_train.txt
sort data/base_1/bprob_avazu_train.txt -k2,2 -k3,3 -o data/base_1/bprob_avazu_train.txt
python bayes_prob_creator.py < data/base_1/bprob_avazu_train.txt > data/base_1/bayes_probs_base_1.txt
#
chmod +x data/base_1/bayes_probs_base_1.txt
chmod +x bayes_prob_mapper_base_1.py
#
#***model_name: base_2 ***
python bayes_prob_base_2.py > data/base_2/bprob_avazu_train.txt
sort data/base_2/bprob_avazu_train.txt -k2,2 -k3,3 -o data/base_2/bprob_avazu_train.txt
python bayes_prob_creator.py < data/base_2/bprob_avazu_train.txt > data/base_2/bayes_probs_base_2.txt
#
chmod +x data/base_2/bayes_probs_base_2.txt
chmod +x bayes_prob_mapper_base_2.py
#
#***model_name: base_3 ***
python bayes_prob_base_3.py > data/base_3/bprob_avazu_train.txt
sort data/base_3/bprob_avazu_train.txt -k2,2 -k3,3 -o data/base_3/bprob_avazu_train.txt
python bayes_prob_creator.py < data/base_3/bprob_avazu_train.txt > data/base_3/bayes_probs_base_3.txt
#
chmod +x data/base_3/bayes_probs_base_3.txt
chmod +x bayes_prob_mapper_base_3.py
#
# upload files to AWS S3
s3cmd put data/base_1/bayes_probs_base_1.txt s3://stat157-uq85def/home/sclau/project/code/
s3cmd put data/base_2/bayes_probs_base_2.txt s3://stat157-uq85def/home/sclau/project/code/
s3cmd put data/base_3/bayes_probs_base_3.txt s3://stat157-uq85def/home/sclau/project/code/
#
s3cmd put bayes_prob_mapper_base_1.py s3://stat157-uq85def/home/sclau/project/code/
s3cmd put bayes_prob_mapper_base_2.py s3://stat157-uq85def/home/sclau/project/code/
s3cmd put bayes_prob_mapper_base_3.py s3://stat157-uq85def/home/sclau/project/code/
#
# run MapReduce Job for **base_1**
# set Mapper: s3://stat157-uq85def/home/sclau/project/code/bayes_prob_mapper_base_1.py
# set Reducer: org.apache.hadoop.mapred.lib.IdentityReducer
# set Input S3 location: s3://stat157-uq85def/shared/avazudata/newdata/train
# set Ouput S3 location: s3://stat157-uq85def/home/sclau/project/output/base_1_results
# set Arguments: -cacheFile s3://stat157-uq85def/home/sclau/project/code/bayes_probs_base_1.txt#bayes_probs_base_1.txt
#
# run MapReduce Job for **base_2**
# set Mapper: s3://stat157-uq85def/home/sclau/project/code/bayes_prob_mapper_base_2.py
# set Reducer: org.apache.hadoop.mapred.lib.IdentityReducer
# set Input S3 location: s3://stat157-uq85def/shared/avazudata/newdata/train
# set Ouput S3 location: s3://stat157-uq85def/home/sclau/project/output/base_2_results
# set Arguments: -cacheFile s3://stat157-uq85def/home/sclau/project/code/bayes_probs_base_2.txt#bayes_probs_base_2.txt
#
# run MapReduce Job for **base_3**
# set Mapper: s3://stat157-uq85def/home/sclau/project/code/bayes_prob_mapper_base_3.py
# set Reducer: org.apache.hadoop.mapred.lib.IdentityReducer
# set Input S3 location: s3://stat157-uq85def/shared/avazudata/newdata/train
# set Ouput S3 location: s3://stat157-uq85def/home/sclau/project/output/base_3_results
# set Arguments: -cacheFile s3://stat157-uq85def/home/sclau/project/code/bayes_probs_base_3.txt#bayes_probs_base_3.txt