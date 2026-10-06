from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


analyzer = SentimentIntensityAnalyzer()


NEGATIVE_COMPLAINT_WORDS = [
    "delayed",
    "delay",
    "not arrived",
    "not received",
    "not working",
    "failed",
    "failure",
    "charged twice",
    "wrong charge",
    "unauthorized",
    "fraud",
    "disappointed",
    "frustrated",
    "angry",
    "terrible",
    "bad",
    "problem",
    "issue",
    "complaint",
    "not responded",
    "not updated",
    "cannot access",
    "unable to access"
]


def analyze_sentiment(text):

    text_lower = text.lower()

    scores = analyzer.polarity_scores(text)

    compound = scores["compound"]

    # Detect complaint-specific negative language
    complaint_matches = [
        word
        for word in NEGATIVE_COMPLAINT_WORDS
        if word in text_lower
    ]

    # Strong negative complaint signals
    if complaint_matches:
        sentiment = "Negative"

        # Ensure the score reflects the negative nature
        if compound > -0.05:
            compound = -0.50

    elif compound >= 0.05:
        sentiment = "Positive"

    elif compound <= -0.05:
        sentiment = "Negative"

    else:
        sentiment = "Neutral"

    return {
        "sentiment": sentiment,
        "score": compound
    }