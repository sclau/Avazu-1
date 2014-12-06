# run each of these lines individually by copying them into the terminal

chmod +x counter_map_full.py

s3cmd put counter_map_full.py s3://stat157-uq85def/home/sclau/project/code/

# run MapReduce job
# Log folder S3 location: s3://stat157-uq85def/home/sclau/project/logs/
# set Mapper: s3://stat157-uq85def/home/sclau/project/code/counter_map_full.py 
# set Reducer: s3://stat157-uq85def/home/sclau/project/code/counter_red.py
# set Input S3 location: s3://stat157-uq85def/shared/avazudata/newdata/train
# set Ouput S3 location: s3://stat157-uq85def/home/sclau/project/output/base_counts_full

cd data/counts_full/
rm *
s3cmd get s3://stat157-uq85def/home/sclau/project/output/base_counts_full/part*
cat $(ls -t) > avazu_train.txt
cd ../../

python bayes_prob_base_3_full.py > data/base_3_full/bprob_avazu_train.txt
sort data/base_3_full/bprob_avazu_train.txt -k2,2 -k3,3 -o data/base_3_full/bprob_avazu_train.txt
python bayes_prob_creator.py < data/base_3_full/bprob_avazu_train.txt > data/base_3_full/bayes_probs_base_3_full.txt

chmod +x data/base_3_full/bayes_probs_base_3_full.txt
chmod +x bayes_prob_mapper_base_3_full.py

s3cmd put data/base_3_full/bayes_probs_base_3_full.txt s3://stat157-uq85def/home/sclau/project/code/
s3cmd put bayes_prob_mapper_base_3_full.py s3://stat157-uq85def/home/sclau/project/code/

# run MapReduce Job for **base_3**
# set Mapper: s3://stat157-uq85def/home/sclau/project/code/bayes_prob_mapper_base_3_full.py
# set Reducer: org.apache.hadoop.mapred.lib.IdentityReducer
# set Input S3 location: s3://stat157-uq85def/shared/avazudata/newdata/test
# set Ouput S3 location: s3://stat157-uq85def/home/sclau/project/output/base_3_results_full
# set Arguments: -cacheFile s3://stat157-uq85def/home/sclau/project/code/bayes_probs_base_3_full.txt#bayes_probs_base_3_full.txt

cd data/base_3_full/results/
s3cmd get s3://stat157-uq85def/home/sclau/project/output/base_3_results_full/part*
cat $(ls -t) > kaggle_submission.txt
cd ../../../