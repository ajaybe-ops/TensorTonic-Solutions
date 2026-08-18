import numpy as np
from collections import Counter
import math


def tfidf_vectorizer(documents):
    """
    Build TF-IDF matrix from a list of text documents.
    Returns tuple of (tfidf_matrix, vocabulary).
    """

    # Tokenize documents
    tokenized_docs = [doc.lower().split() for doc in documents]

    # Create vocabulary
    vocabulary = sorted(
        set(word for doc in tokenized_docs for word in doc)
    )

    # Map each word to a column index
    word_to_index = {
        word: i for i, word in enumerate(vocabulary)
    }

    N = len(documents)

    # Calculate document frequency: number of documents containing each word
    document_frequency = Counter()

    for doc in tokenized_docs:
        for word in set(doc):
            document_frequency[word] += 1

    # Initialize TF-IDF matrix
    tfidf_matrix = np.zeros((N, len(vocabulary)))

    # Calculate TF-IDF for every document and word
    for doc_index, doc in enumerate(tokenized_docs):

        # Count word occurrences
        word_counts = Counter(doc)

        # Total terms in this document
        total_terms = len(doc)

        for word, count in word_counts.items():

            # Term Frequency
            tf = count / total_terms

            # Inverse Document Frequency
            idf = math.log(N / document_frequency[word])

            # TF-IDF
            tfidf_matrix[doc_index][word_to_index[word]] = tf * idf

    return tfidf_matrix, vocabulary