from sklearn.feature_extraction.text import TfidfVectorizer
from collections import defaultdict
import pandas as pd


def make_ngrams(text_list, n=3):

    total = [text_list[i:i+n] for i in range(len(text_list)-n+1)]

    return total


def process(source, target):

    vectorizer = TfidfVectorizer(analyzer=make_ngrams)

    total_source = list(map(lambda x: x.lower(), source + target))
    X = vectorizer.fit_transform(total_source)

    processor = defaultdict(list)
    words = defaultdict(list)
    for index, word in enumerate(source):
        processor[word[0].lower()].append(index)
        words[word[0].lower()].append(word)

    df = pd.DataFrame({'char': list(processor.keys()), 'indexes': list(processor.values()), 'words': list(words.values())})

    length = len(source)

    return df, X, length


