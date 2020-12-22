from flask import Flask, render_template, jsonify, request
import numpy as np
import pandas as pd
import json
import random
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

data = pd.read_csv('data.csv', encoding='ISO-8859-1')
data = data.dropna()


def preprocessData(datas):
    datas = datas.str.lower()
    datas = datas.str.replace('[^\w\s]', '')
    datas = datas.str.replace('\d+', '')
    return datas


def preprocessSearch(query):
    query = query.lower()
    query = re.sub(r'[^\w\s]', '', query)
    query = re.sub(r'\d+', '', query)

    return query


def tf_idf(key, desc):
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_weight = tfidf.fit_transform(desc)
    search = tfidf.transform([key])
    return search, tfidf_weight


def similarity(search, tfidf_weight):
    cosine_sim = cosine_similarity(search, tfidf_weight)
    sim = cosine_sim[0]
    most = []
    min = 10
    while min > 1:
        ind = np.argmax(sim)
        most.append(ind)
        sim[ind] = 0
        min -= 1

    most = list(dict.fromkeys(most))
    return most


title = data['title']
desc = data['description']
code = data['code']

cleanDesc = preprocessData(desc)


@app.route('/')
def index():

    title = data['title']
    length = str(len(title))

    rand = {}
    for i in range(5):
        randomNumber = random.randint(0, len(title))

        rand[str(randomNumber)] = {"id": int(
            randomNumber), "title": title[randomNumber]}

    return jsonify(rand)


@app.route('/search', methods=['POST'])
def search():
    query = request.args['query']
    query = preprocessSearch(query)

    key, weight = tf_idf(query, cleanDesc)
    most = similarity(key, weight)

    jsonTemplate = {}

    for item in most:
        ret = {"id": int(item), "title": title[item]}
        jsonTemplate[str(item)] = ret

    return jsonify(jsonTemplate)


@app.route('/code')
@app.route('/code/<codeID>')
def code(codeID=None):
    if codeID == None:
        pass
    else:
        dataDict = data.loc[int(codeID)].to_dict()
        return jsonify(dataDict)


if __name__ == "__main__":
    app.run(debug=True)
