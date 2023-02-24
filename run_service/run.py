"""
author: Niklaus Parcell
date: 22 Feb 2023 
objective:
	- demonstrate usage of pymsx to sync/upload datasets to MSX UI programmatically
"""
import os 
import json
import pandas as pd 
import time 

from functions_msx import msx_sync
 
# Data files will be working with 
data_files = [file for file in os.listdir("./run_service/nlp-test-data/datasets_20") if "nlp_test" in file] 

# Set the name for the version (1..20) that will be added
model_name = "DemoModel"

# Sync data frame to Mosaics 
k = 0
for file in data_files: 
    csv = pd.read_csv("./run_service/nlp-test-data/datasets_20/%s"%file)
    df = pd.DataFrame(csv)

    response = msx_sync(
        model_name,
        df,
        target="Sentiment"
    )

    print("----")
    print("Received response from server: ")
    print(json.dumps(response, indent=2))
    print("run %d and %s synced to msx"%(k, file))
    print("----")

    k += 1
    time.sleep(60)  # Waits 1 minute

print("Syncing concluded")