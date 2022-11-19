# Importing essential libraries
from flask import Flask, render_template, request
import pickle
import numpy as np
# Load the Random Forest CLassifier model
filename = 'Heart_disease_model.pkl'
classifier = pickle.load(open(filename, 'rb'))
classifier1 = pickle.load(open('model1.pkl', 'rb'))
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index1.html');
@app.route('/predict2',methods=['POST'])
def predict2():
        return render_template('index.html')
@app.route('/predict3',methods=['POST'])
def predict3():
        return render_template('index2.html')
        

@app.route('/predict', methods=['POST'])
def predict():
    print(request.form)
    if request.method == 'POST':
        age = request.form.get('age',None)
        sex = request.form.get("sex", None)
        cp = request.form.get('cp',None)
        trestbps = request.form.get('trestbps',None)
        chol = request.form.get('chol',None)
        fbs = request.form.get('fbs',None)
        restecg = request.form.get('restecg',None)
        thalach = request.form.get('thalach',None)
        exang = request.form.get('exang',None)
        oldpeak = request.form.get('oldpeak',None)
        slope = request.form.get('slope',None)
        ca = request.form.get('ca',None)
        thal = request.form.get('thal',None)
        data = np.array([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
        print(data)
        my_prediction = classifier.predict(data)
        
        return render_template('result1.html', prediction=my_prediction)

@app.route('/predict1', methods=['POST'])
def predict1():
    if request.method == 'POST':
        Age = request.form['Age']
        Gender = request.form['Gender']
        Polyuria= request.form['Polyuria']
        Polydipsia = request.form['Polydipsia']
        suddenweightloss = request.form['sudden weight loss']
        weakness = request.form['weakness']
        Polyphagia = request.form['Polyphagia']
        Genitalthrush = request.form['Genital thrush']
        visualblurring = request.form['visual blurring']
        Itching = request.form['Itching']
        Irritability = request.form['Irritability']
        delayedhealing = request.form['delayed healing']
        partialparesis = request.form['partial paresis']
        musclestiffness= request.form['muscle stiffness']
        Alopecia= request.form['Alopecia']
        Obesity= request.form['muscle stiffness']
        data = np.array([[Age, Gender,Polyuria,Polydipsia,suddenweightloss,weakness,Polyphagia, Genitalthrush,visualblurring,Itching,Irritability,delayedhealing,partialparesis, musclestiffness,Alopecia,Obesity]])
        my_prediction1 = classifier1.predict(data)
        
        return render_template('result.html', prediction=my_prediction1)




if __name__ == '__main__':
	app.run(debug=True)