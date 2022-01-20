import pickle
from flask import Flask, render_template, request

# OOPs
# Class, Objects, Methods, Inheritence, Polymorphism, Abstraction, Encapsulation
# Decorators, Generastors, Dunder Methods, Abstract methods, Static methods

# Create an object of the class Flask

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))

# url/
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['GET', 'POST'])
def predict():
    prediction = model.predict([[request.form.get('area')]])
    output = round(prediction[0],2)
    return render_template('index.html', prediction_text=f'Total price is : {output}/-')

if __name__=='__main__':
    app.run(debug=True)