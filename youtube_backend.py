import json

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
        # comments = get_video_comment(url)
        comments = ['I hate dogs', 'I love dogs']
        s_dict = get_sentiment_dict(comments)
        average_sentiment = mean(s_dict.values())
        return render_template("Average Sentiment is " + str(average_sentiment))
    else:
        return render_template('index.html')