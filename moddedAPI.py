


import json
import sys
from urllib import *
import argparse
from urllib.parse import urlparse, urlencode, parse_qs
from urllib.request import  urlopen


YOUTUBE_COMMENT_URL = 'https://www.googleapis.com/youtube/v3/commentThreads'
YOUTUBE_SEARCH_URL = 'https://www.googleapis.com/youtube/v3/search'


def load_comments(mat):
    commlist = []
    for item in mat["items"]:
        comment = item["snippet"]["topLevelComment"]
        author = comment["snippet"]["authorDisplayName"]
        text = comment["snippet"]["textDisplay"]
        commlist.append(text)
        #print("Comment by {}: {}".format(author, text))
        if 'replies' in item.keys():
            for reply in item['replies']['comments']:
                rauthor = reply['snippet']['authorDisplayName']
                rtext = reply["snippet"]["textDisplay"]

            #print("\n\tReply by {}: {}".format(rauthor, rtext), "\n")
            commlist.append(rtext)
    return commlist

def openURL(url, parms):
        f = urlopen(url + '?' + urlencode(parms))
        data = f.read()
        f.close()
        matches = data.decode("utf-8")
        return matches


def get_video_comment(url,key):
    parser = argparse.ArgumentParser()
    mxRes = 20
    vid = str()

    try:
        video_id = urlparse(str(url))
        q = parse_qs(video_id.query)
        vid = q["v"][0]

    except:
        print("Invalid YouTube URL")

    parms = {
                'part': 'snippet,replies',
                'maxResults': mxRes,
                'videoId': vid,
                'textFormat': 'plainText',
                'key': key
            }



    matches = openURL(YOUTUBE_COMMENT_URL, parms)
    i = 2
    mat = json.loads(matches)

    nextPageToken = mat.get("nextPageToken")
    commentArr = load_comments(mat)

    while nextPageToken:
        parms.update({'pageToken': nextPageToken})
        matches = openURL(YOUTUBE_COMMENT_URL, parms)
        mat = json.loads(matches)
        nextPageToken = mat.get("nextPageToken")
        commentArr = commentArr + load_comments(mat)


    return commentArr

    """
    nextPageToken = mat.get("nextPageToken")
    print("\nPage : 1")
    print("------------------------------------------------------------------")
    load_comments(mat)

    while nextPageToken:
        parms.update({'pageToken': nextPageToken})
        matches = openURL(YOUTUBE_COMMENT_URL, parms)
        mat = json.loads(matches)
        nextPageToken = mat.get("nextPageToken")
        print("\nPage : ", i)
        print("------------------------------------------------------------------")

        load_comments(mat)

        i += 1

    except KeyboardInterrupt:
        print("User Aborted the Operation")

    except:
        print("Cannot Open URL or Fetch comments at a moment")
    """
