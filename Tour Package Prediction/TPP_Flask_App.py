import numpy as np
import pandas as pd
from flask import Flask, redirect, url_for, render_template, request
app = Flask(__name__)

model = pd.read_pickle('models/TourPackagePredictor')

def find_prediction(data):
    
    template = pd.read_csv('data_template/TPP_template.csv')
    columns = []
    for i in data.columns:
        try:            
            if int(data.loc[0,i]):
                template.loc[0,i]=data.loc[0,i]

        except:
            template.loc[0,i+'_'+data[i]]=1
    return model.predict(template)[0]

@app.route('/')
def homepage():
    return '''
    <html>
        <head>
            <title>Tour Package Predictor</title>
        </head>
        <body>
            <a href = "/predict"><button>Tour Package Predictor</button></a>
            
        </body>
    <html>
    '''

@app.route('/predict', methods=['GET','POST'])
def register_page():
    pred = 'None'
    if request.method == 'GET':
        print(request.args)
        
        
    elif request.method == 'POST':
        
        input_ = request.form

        col = ['Age', 'TypeofContact', 'CityTier', 'DurationOfPitch',
       'Occupation', 'Gender', 'NumberOfPersonVisiting', 'NumberOfFollowups',
       'ProductPitched', 'PreferredPropertyStar', 'MaritalStatus',
       'NumberOfTrips', 'Passport', 'PitchSatisfactionScore', 'OwnCar',
       'NumberOfChildrenVisiting', 'Designation', 'MonthlyIncome']
        data = pd.DataFrame(columns= col)
        data.loc[0,:] = 0
        for i in col:
           if input_[i] == "": 
               return render_template('weekend.html', result = "None")
           else:
               data[i] = input_[i]
        pred = find_prediction(data)
    return render_template('weekend.html', result = pred)



if __name__=='__main__':
    app.run(debug=True)