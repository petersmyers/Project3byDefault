import pandas as pd
import numpy as numpy
from tensorflow.keras.models import load_model

def predict_outcome(loan_info_list):
    # Load model ***
    ml_model = load_model("")
    pred_data = np.array(loan_info_list).reshape(1, "NUMBER OF INPUTS")
    prediction = ml_model.predict(pred_data)


from flask import ( 
    Flask, 
    render_template,
    request
)

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = ""

db = SQLAlchemy(app)

class Loan_Data(db.Model):
    # Add table name ***
    __tablename__ = ""
    #Add column names as variables


    def __repr__(self):
        return '<Loan_Data %r>' % (self.name)

@app.before_first_request
def setup():
    #recreate database each time 
    df.create_all()

@app.route("/")
def home():
    """Render Home Page"""
    return render_template("index.hmtl")

@app.route("/loan_prediction", methods = ['POST', 'GET'])
def generate_prediction():
    if request.method() == "POST":
        # Store loan record ID in variable

        # Query database to retrieve loan data matching record ID
        
        # Format results to match model input requirements

        # Make prediction

        # Render result html template and pass prediction value
