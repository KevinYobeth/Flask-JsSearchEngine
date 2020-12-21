from flask import Flask, render_template, jsonify
import numpy as np
import pandas as pd
import json

app = Flask(__name__)

data = pd.read_csv('data.csv', encoding='ISO-8859-1')
data = data.dropna()


@app.route('/')
def index():
    return 'Index Page'


@app.route('/search')
def search():
    pass


@app.route('/code')
@app.route('/code/<codeID>')
def code(codeID=None):
    if codeID == None:
        pass
    else:
        dataDict = data.loc[int(codeID)].to_dict()
        return jsonify(dataDict)
