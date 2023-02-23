"""
author: Niklaus Parcell
date: 09 February 2023
objective:
	- pull Updated-Train-Data.csv from S3
	- partition in to 20 different datasets 
	- upload that to Mosaics to start seeing monitoring data 
"""

import pandas as pd 
import numpy as np 
from function_library_aws import pull_s3 

bucket_name = "klaus-bucket1" 
dataset_name = "Updated-Train-Data.csv" 

df = pull_s3(
	bucket_name=bucket_name,
	object_name=dataset_name
)

k = 0 
N = 800
k_1 = k + N  
iter = 0 
while k < len(df):

	partitioned = df[k:k_1]
	partitioned = partitioned[["Text", "Sentiment"]]

	save_name = "./datasets_20/nlp_test_" + str(iter) + ".csv"

	partitioned.to_csv(save_name, index = False)

	iter += 1 
	k += N 
	k_1 += N