import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

df = pd.read_csv('../data/cleaned_articles.csv')

# Define a TF-IDF Vectorizer Object, while removing all english stop words such as 'the', 'a', ...
tfidf = TfidfVectorizer(stop_words='english')

# Construct the required TF-IDF matrix by fitting and transforming the data
tfidf_matrix = tfidf.fit_transform(df['text'])
tfidf_matrix.shape
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

def get_similars(text, cosine_sim=cosine_sim):
    text = text.lower()

    idx = []

    # iterate over articles, and add their index if content contains substring
    for i in range(len(df)):
        if text in df['text'][i].lower():
            idx.append(i)

    # Get the pairwsie similarity scores of all articles with that text
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the articles based on the similarity scores
    sim_scores = sorted(sim_scores, reverse=True)

    # Get the scores of the 3 most similar articles
    sim_scores = sim_scores[1:4]

    # Get the article indices
    article_indices = [i[0] for i in sim_scores]
    print(article_indices)

    if article_indices == []:
        return None
    # Return the top 3 most similar articles
    return df.iloc[article_indices]