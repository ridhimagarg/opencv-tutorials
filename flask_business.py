from flask import Flask, render_template, url_for, request, flash, redirect
from flask_bootstrap import Bootstrap
import pandas as pd
import requests, json

app = Flask(__name__,)
app.secret_key = 'some_secret'
Bootstrap(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():


        myprediction =[]

        if request.method == 'POST':
                search = request.form['search']


                api_key = 'AIzaSyC3OPP9VW51lFFQdH-DB3dEdV8e_5362d0'


                url = 'https://maps.googleapis.com/maps/api/place/findplacefromtext/json?'

                
                url1 = 'https://maps.googleapis.com/maps/api/place/details/json?'

                r = requests.get(url+'input='+search +'&inputtype=textquery&fields=formatted_address,name,place_id&key='+api_key)

                results = r.json()


                if results['candidates'] != []:

                    for k in ['name', 'formatted_address']:
                        myprediction.append("{0} : {1}".format(k.capitalize(),results['candidates'][0][k]))


                    place_id  = results['candidates'][0]['place_id']


                    r1 = requests.get(url1+'placeid='+place_id+'&fields=formatted_phone_number,website&key='+api_key)

                    results1 = r1.json()

                    for k in results1['result']:
                        myprediction.append("{0} : {1}".format(k.capitalize(),results1['result'][k]))
    



                else:
                    myprediction.append("No information found")

                return render_template('results.html', len= len(myprediction), prediction = myprediction)
                        
                   

if __name__ == '__main__':
    app.run(debug= True)
