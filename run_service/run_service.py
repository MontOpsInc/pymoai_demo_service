"""
author: Niklaus Parcell
date: 22 Feb 2023 
objective:
	- demonstrate usage of pymsx to sync/upload datasets to MSX UI programmatically
"""

import time 
import os 
import pandas as pd 
from functions_msx import msx_sync 

# Data files will be working with 
data_files = [file for file in os.listdir("./run_service/nlp-test-data/datasets_20") if "nlp_test" in file] 

# Sync data frame to Mosaics 
k = 0
for file in data_files: 
	csv = pd.read_csv("./run_service/nlp-test-data/datasets_20/%s"%file)
	df = pd.DataFrame(csv)
	
	msx_sync(
		df=df,
		model_name="FirstRun",
		target="Sentiment"
	)
	print("run %d and %s synced to msx"%(k, file))
	k += 1
	time.sleep(60)  # Waits 1 minute

print("Syncing concluded")