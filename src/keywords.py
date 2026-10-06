from sklearn.feature_extraction.text import TfidfVectorizer


def extract_keywords(text, top_n=8):

    vectorizer = TfidfVectorizer(
        stop_words="english",
        ngram_range=(1, 2)
    )

    matrix = vectorizer.fit_transform([text])

    scores = matrix.toarray()[0]

    terms = vectorizer.get_feature_names_out()

    ranked_indices = scores.argsort()[::-1]

    keywords = []

    for index in ranked_indices:

        if scores[index] > 0:

            keywords.append(
                terms[index]
            )

        if len(keywords) == top_n:
            break

    return keywords