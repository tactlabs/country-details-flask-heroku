from flask import Flask, render_template
import os
import sys
from flask import request
from random import randint
import tact_util as t_util

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    
    name  = request.form.get('name')

    name = name.lower()
    
    country_details = t_util.get_country_details(name)

    result = {
        'apiresult' : 0,    
        'apimessage' : 'OK',    

        'name' : name,
        'country_details' : country_details        
    }
    
    return render_template('index.html', result=result)

if __name__ == "__main__":
    app.run()
