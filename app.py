from flask import Flask,request,render_template
import numpy as np
import pandas
import sklearn
import pickle

model = pickle.load(open('model.pkl','rb'))
sc = pickle.load(open('standscaler.pkl','rb'))
mx = pickle.load(open('minmaxscaler.pkl','rb'))


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/predict",methods=['POST'])
def predict():
    #SO2,NO,NO2,NOX,CO,O3,PM2.5,PM10,Temperature,RH,Solar_Rad,AQI,AQI_severity,Location
    SO2 = request.form['SO2']
    NO = request.form['NO']
    NO2 = request.form['NO2']
    NOX = request.form['NOX']
    CO = request.form['CO']
    O3 = request.form['O3']
    PM2_5 = request.form['PM2_5']
    PM10 = request.form['PM10']
    Temperature = request.form['Temperature']
    RH = request.form['RH']
    Solar_Rad = request.form['Solar_Rad']
    Location = request.form['Location']

    feature_list = [SO2,NO,NO2,NOX,CO,O3,PM2_5,PM10,Temperature,RH,Solar_Rad,Location]
    #feature_list = [N, P, K, temp, humidity, ph, rainfall]
    single_pred = np.array(feature_list).reshape(1, -1)

    mx_features = mx.transform(single_pred)
    sc_mx_features = sc.transform(mx_features)
    prediction = model.predict(sc_mx_features)

    
    AQI_dict={1:"Good", 2:"Moderate", 3:"Unhealthy for Sensitive Groups", 
              4:"Unhealthy",5:"Very Unhealthy", 6:"Hazardous"}

    if prediction[0] in AQI_dict:
        AQI_Index = AQI_dict[prediction[0]]
        result = "{} is on this location.".format(AQI_Index)
    else:
        result = "Sorry, we could not determine the AQI Severity on provided location data."
    return render_template('index.html',result = result)


if __name__ == "__main__":
    app.run(debug=True)