import numpy as np
from scipy.sparse import csr_matrix
from sparse_dot_topn import awesome_cossim_topn
import time
import multiprocessing

from sklearn.feature_extraction.text import TfidfVectorizer
from collections import defaultdict
import pandas as pd
from data import source, target


def make_ngrams(text_list, n=3):

    total = [text_list[i:i+n] for i in range(len(text_list)-n+1)]

    return total


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

# print(1234)

def awesome_cossim_top(A, B, ntop, lower_bound=0):

    A = A.tocsr()
    B = B.tocsr()
    M, _ = A.shape
    _, N = B.shape

    idx_dtype = np.int32

    nnz_max = M*ntop

    indptr = np.zeros(M+1, dtype=idx_dtype)
    indices = np.zeros(nnz_max, dtype=idx_dtype)
    data = np.zeros(nnz_max, dtype=A.dtype)

    ct.sparse_dot_topn(
        M, N, np.asarray(A.indptr, dtype=idx_dtype),
        np.asarray(A.indices, dtype=idx_dtype),
        A.data,
        np.asarray(B.indptr, dtype=idx_dtype),
        np.asarray(B.indices, dtype=idx_dtype),
        B.data,
        ntop,
        lower_bound,
        indptr, indices, data)

    return csr_matrix((data,indices,indptr),shape=(M,N))


def calculate(tuple_value):

    ind = tuple_value[0]
    test = tuple_value[1]

    first_char = source[ind][0].lower()

    data_filter = df[df['char'] == first_char]

    index_val = data_filter['indexes'].tolist()[0]
    words_val = data_filter['words'].tolist()[0]

    extracted = X[index_val]

    t = awesome_cossim_topn(extracted, test.T, 5, 0.01)

    percent = t.data.tolist()

    if percent != []:
        r,c = t.nonzero()
        confidence = max(percent)
        max_index = percent.index(confidence)
        max_word_value = words_val[r[max_index]]
        return 'Source: {}, target: {}, confidence: {}'.format(max_word_value, target[ind], confidence)
    else:
        return 'Source: {}, target: {}, confidence: {}'.format('Not found', target[ind] , 0.0)


if __name__ == '__main__':

    start = time.time()
    X_target = X[length:]

    p = multiprocessing.Pool()
    out = p.map(calculate, enumerate(X_target))

    print(out)

    print(time.time() - start)

