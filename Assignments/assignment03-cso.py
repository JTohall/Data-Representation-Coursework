# Data Representation - Assignment 3
# Author: Jamie Tohall

# Write a program that retrieves the dataset for the "exchequer account (historical series)" 
# from the CSO, and stores it into a file called "cso.json"

import requests # Import relevant modules
import json

url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en"
# url for the exchequer account (historical series) dataset, JSON format

def getalldata(): 
    response = requests.get(url)
    return response.json()

if __name__ == "__main__":
    
    with open("cso.json", "w") as fp:
        print(json.dumps(getalldata()),file=fp)