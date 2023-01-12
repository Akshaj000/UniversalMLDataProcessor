from flask import request
from api import app

@app.route('/upload', methods = ['POST'])  
def upload():  
    if request.method == 'POST':  
        f = request.files['file']
        f.save(f"uploads/data.csv")
        return True
    return False

@app.route('/process', methods = ['POST', 'GET'])
def process():
    data = request.get_json()
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
    print(fit)
    return fit
