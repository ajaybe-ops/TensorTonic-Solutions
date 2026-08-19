def remove_stopwords(tokens, stopwords):
  """
  Returns: list[str] - tokens without stopwords
  """ 
  return [token for token in tokens if token not in stopwords]