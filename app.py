import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('C:/Users/mahsa/OneDrive/Desktop/Machine_learning_API/Heroku-Demo-master/Heroku-Demo-master/heart1.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    def heartattack(output):
        if output == 0:
            return 'You have high chance of heart attack'
        else:
            return 'You do not have heart disease!'

    return render_template('index.html', prediction_text=heartattack(str(output)))


if __name__ == "__main__":
    app.run(debug=True)