from flask import request
from api import app
import csv
import os

@app.route('/health', methods = ['POST', 'GET'])
def health():
    d = {
        "isHealthy" : False,
        "errors" : None
    }
    try:
        file = open("uploads/data.csv", "rb")
    except FileNotFoundError:
        d["errors"] = "File not found. Please upload the file."
        return d
    d["isHealthy"] = True
    return d

@app.route('/upload', methods = ['POST'])  
def upload():  
    if request.method == 'POST': 
        try:
            f = request.files['file']
            f.save("uploads/data.csv")
            return {"success": True}
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
    else:
        return {
            "success": False,
            "errors": "Can only except post method."
        }

@app.route('/process', methods = ['POST', 'GET'])
def process():
    data = request.get_json()
    try:
        import pandas as pd
        data_pre_object = pd.read_csv("uploads/data.csv")
        from machine import preprocessor, fit
        data_pre_object = preprocessor(
            target = data['target'],
            fill_null = data['fill_null'],
            split_percent = data['split_percent'],
            can_apply_smote= data['can_apply_smote'],
            scaler = data['scaler'],
            data=data_pre_object
        )
        fit = fit(
            data_pre_object = data_pre_object,
            type = data['type']
        )
        return fit
    except Exception as e:
        return {
            "success": False, 
            "errors" : str(e)
        }
