import joblib

from src.preprocessing import clean_text
from src.classifier import predict_category
from src.sentiment import analyze_sentiment
from src.urgency import detect_urgency
from src.keywords import extract_keywords
from src.llm_service import analyze_with_llm


MODEL_PATH = "models/complaint_classifier.pkl"

model = joblib.load(MODEL_PATH)


def analyze_complaint(text):

    # Text preprocessing
    cleaned_text = clean_text(text)

    # Complaint category
    category = predict_category(model, text)

    # Sentiment
    sentiment_result = analyze_sentiment(text)

    # Urgency
    urgency_result = detect_urgency(text)

    # Keywords
    keywords = extract_keywords(text)

    # Gemini analysis
    llm_result = analyze_with_llm(
        complaint=text,
        category=category,
        sentiment=sentiment_result["sentiment"],
        priority=urgency_result["priority"],
        keywords=keywords
    )

    return {
        "category": category,
        "sentiment": sentiment_result,
        "urgency": urgency_result,
        "keywords": keywords,
        "llm_analysis": llm_result
    }