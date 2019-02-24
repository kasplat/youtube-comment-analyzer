from textblob import TextBlob

def get_sentiment_dict(comments):
    """
    creates the sentiment dict. Key is the comment, value is the sentiment polarity.
    """
    s_dict = {}
    for comment in comments:
        blob = TextBlob(comment)
        s_dict[comment] = blob.sentiment.polarity
    s = [(k, s_dict[k]) for k in sorted(s_dict, key=s_dict.get, reverse=True)]
    most_positive = [x[0] for x in s[:9]]
    most_negative = [x[0] for x in s[-10:]]
    return s_dict, most_positive, most_negative


def demo():
    text = '''
    The titular threat of The Blob has always struck me as the ultimate movie
    monster: an insatiably hungry, amoeba-like mass able to penetrate
    virtually any safeguard, capable of--as a doomed doctor chillingly
    describes it--"assimilating flesh on contact.
    Snide comparisons to gelatin be damned, it's a concept with the most
    devastating of potential consequences, not unlike the grey goo scenario
    proposed by technological theorists fearful of
    artificial intelligence run rampant.
    '''

    blob = TextBlob(text)
    blob.tags           # [('The', 'DT'), ('titular', 'JJ'),
                        #  ('threat', 'NN'), ('of', 'IN'), ...]

    blob.noun_phrases   # WordList(['titular threat', 'blob',
                        #            'ultimate movie monster',
                        #            'amoeba-like mass', ...])

    for sentence in blob.sentences:
        print(sentence.sentiment.polarity)
    # 0.060
    # -0.341

    blob.translate(to="es")  # 'La amenaza titular de The Blob...'
    print('my stuff!')
    print(blob.sentiment.polarity)
