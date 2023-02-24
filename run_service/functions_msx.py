"""
author: Niklaus Parcell
date: 19 Feb 2023 
objective: 
	function for pymsx 
"""
import json
import os
from pymsx.client import MsxClient
from pymsx.exceptions import ApiResponseError

# If no credentials are supplied, then environment variables are required.
config = os.path.join(os.path.dirname(__file__), "creds.json")
creds = json.load(open(config))

email = creds['email']
password = creds['password']

# ...or try using an active token.
# This may fail, see exception handling below.
token = "your token"

def msx_sync(name, df, target = "defualt"):
    # First create client with active token or credentials
    msx = MsxClient(
        # ...using email/password
        email=email,
        password=password,

        # ...or instead, use token
        # token=token
    )

    # Check the health of your server
    health = msx.health().dict()

    print("Health: ", health)

    assert health is not None and health['status'] == 'live'

    # Add a dataset to your msx system -- From a DataFrame
    result = msx.datasets.add(
        name,
        df=df,
        target=target,
    )

    return result
