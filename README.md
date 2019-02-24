# Youtube Comment Analyzer

Have you ever wondered how Youtube REALLY feels about a video? Are you a content creator who wants to get real feedback about their video, but you don't want to read the comments by trolls? The Youtube Comment Analyzer can help with this problem! Simply put a Youtube URL into the box and the tool will use Natural Language Processing to generate advanced analytics for the provided video, including overall sentiment, a world cloud of repeated key-words, and toxicity level of your comment sections.

## Setup

### Requirements

* Python 3
* Flask
* Textblob

## Use

* Add a private key as an environment variable (`export youtube_key=YOUR_GOOGLE_API_KEY_HERE`).
* Go into the directory and run `FLASK_APP=ysa_backend.py flask run`. This will start a localhost at http://127.0.0.1:5000/ where you can visit the website.

## Upcoming Features
* Return main ideas of comments (and comment threads)
* compare the comment statistics of two different videos
* use the time stamp of comments to visualize the community engagement in the video over time
* Display most active commentators
* Which comments are fake

## Example toxicities
* hbomberguy: 23%
* nigahiga: 6%
* 

## Acknowledgments

* Thanks to HackCU for hosting us!
* Thanks to srcede for this wonderful tool for using Youtube's (broken) API: https://github.com/srcecde/python-youtube-api

### Contributors

* Karthik Venkatram
* Kesavan Kushalnagar
