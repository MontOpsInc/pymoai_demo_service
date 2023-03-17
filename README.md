# Welcome to youre first run using pymoai!




<br />

## Big effect with small steps taken
<br />

In this example, we have provided 20 example NLP datasets, which is meant to simulate a standard AIOps process over time. The data is for simple sentiment analysis, taking tweets to determine whether a Crypto coin's price will increase/decrease in the next 3 days (Pos, Neg). Input columns are "Text" and "Sentiment".

We've made the AIOps process simple here using pymoai -- simply run the command that uploads the sample data, and we do the heavy lifting. 

Later, use this same structure to push your own data to MontOps!

<br />

## 1) **Make sure you have a MontOps login**
<br />

>> signup at https://www.montops.ai/
    
    
We will have your account approved within 24 hours of signup.
  
<br />

## 2) **Clone the code from this repository & Setup the virtual environment**
<br />

```bash
$ git clone https://github.com/MontOpsInc/pymoai_demo_service.git
$ cd pymoai_demo_service
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install --upgrade pip && pip install -r requirements.txt
```

## 3) **Edit your credentials in "/run_service/creds.json"**
<br />

- email
- password
- token (only used if you've already received a token)

> Note: Either use the combination of a) email, password, or b) token

<br />

## 4) **Execute the run_service command to upload the 20 NLP datasets**
<br />

```bash
$ python run_service/run.py
```

Start seeing `AIOps` insights in the MontOps UI! 
 
We are available on Browser AND Mobile, so see your Language AIOps insights anywhere!

<br />

## 5) **For any questions, please contact:**
<br />

Support: support@montops.ai

Documentation and pymoai install: https://pypi.org/project/pymoai/

# Example Diagram of how the flow works
<br />

![
Flow -- Vertical (1)](https://user-images.githubusercontent.com/79324142/221371115-a5a7e39c-ebcb-4ff1-b003-d7a9484f1923.png)


