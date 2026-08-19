def word_count_dict(sentences):
    word_count = {}

    for sentence in sentences:
        for word in sentence:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

    return word_count