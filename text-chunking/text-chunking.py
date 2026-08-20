def text_chunking(tokens, chunk_size, overlap):
    step = chunk_size - overlap
    chunks = []

    for start in range(0, len(tokens), step):
        chunk = tokens[start:start + chunk_size]
        if chunk:
            chunks.append(chunk)

        if start + chunk_size >= len(tokens):
            break

    return chunks