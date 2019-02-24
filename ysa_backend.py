import json
import os

from statistics import mean
from textblob import TextBlob
from flask import Flask, render_template, request
from moddedAPI import get_video_comment
from sentiment_analyzer import get_sentiment_dict
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST', 'PUT'])
def index():
    if request.method == 'POST':
        if 'url' not in request.form:
            return "No url provided, please try again"
        url = request.form['url']
        comments = get_video_comment(url, os.environ['youtube_key'], 50)
        s_dict = get_sentiment_dict(comments)
        average_sentiment = mean(s_dict.values())
        print(s_dict)
        print('num comments: ' + str(len(comments)))
        sentiment_data = "Average Sentiment is " + str(average_sentiment)
        data = {"sentiment_data": sentiment_data}
        return render_template("index.html", data=data)
    else:
        return render_template('index.html')