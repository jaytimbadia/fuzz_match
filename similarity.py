import numpy as np
from scipy.sparse import csr_matrix
import sparse_dot_topn.sparse_dot_topn as ct
from processing import process
from data import source,  target
from sparse_dot_topn import awesome_cossim_topn
import time

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


def get_match(source, target):

    try:
        if len(source) < len(target):
            return [], 'Source data length canot be less than target data.', 404
        df, X, length = process(source, target)
        X_target = X[length:]

        source_rt, target_rt, confidence_rt = [], [], []
        append1, append2, append3 = source_rt.append, target_rt.append, confidence_rt.append

        for ind, test in enumerate(X_target):

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
                append1(max_word_value)
                append2(target[ind])
                append3(confidence)
                print('Source: {}, target: {}, confidence: {}'.format(max_word_value, target[ind], confidence))
            else:
                append1('Not Found!!!!')
                append2(target[ind])
                append3(0.0)
                print('Source: {}, target: {}, confidence: {}'.format('Not found', target[ind], 0.0))
            print()


        return source_rt, target_rt, confidence_rt
    except Exception as error:
        return [], str(error), 404




# start = time.time()
# print(get_match(source, target))
# print(time.time() - start)