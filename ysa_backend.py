import json
import os
import string

from statistics import mean
from textblob import TextBlob
from flask import Flask, render_template, request
from moddedAPI import get_video_comments
from sentiment_analyzer import get_sentiment_dict
from common_words import common_words
app = Flask(__name__)

from string import punctuation
def strip_punctuation(s):
    return ''.join(c for c in s if c not in punctuation)

@app.route("/", methods=['GET', 'POST', 'PUT'])
def index():
    if request.method == 'POST':
        if 'url' not in request.form:
            return "No url provided, please try again"
        url = request.form['url']
        comments = get_video_comments(url, os.environ['youtube_key'], 50)
        s_dict, most_positive, most_negative = get_sentiment_dict(comments)
        average_sentiment = mean(s_dict.values())
        # print(s_dict)
        # print('num comments: ' + str(len(comments)))
        sentiment_data = str(average_sentiment)
        words = get_words(comments)
        # print(words)
        print(most_negative)
        print(most_positive)
        return render_template("index.html", sentiment_data=sentiment_data, words=json.dumps(words), most_positive=most_positive, most_negative=most_negative)
    else:
        return render_template('index.html')

def get_words(comments):
    words_dict = {}
    for comment in comments:
        for word in comment.split():
            word = strip_punctuation(word.lower())
            if word in words_dict:
                words_dict[word] += 1
            else:
                words_dict[word] = 1
    most_words = []
    for word in sorted(words_dict.keys(), key=lambda word: words_dict[word]):
        if len(most_words) > 30:
            break
        if word in common_words:
            continue
        if words_dict[word] > 1:
            most_words.append({'text': word, 'size': words_dict[word]})
    return most_words